from django.db import models
from datetime import datetime


# Create your models here.


class PartidaArancelaria(models.Model):
    partida = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    
    def __str__(self):
        return self.partida +" "+"("+self.descripcion+")"

class UnidadDeMedida(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    referencia = models.CharField(max_length=10, unique=True, editable=False)  
    partida_arancelaria = models.ForeignKey(PartidaArancelaria, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=100)
    peso_neto = models.FloatField()
    peso_bruto = models.FloatField()
    unidad_medida = models.ForeignKey(UnidadDeMedida, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['referencia']
    
    def save(self, *args, **kwargs):
        
        if not self.pk:
            last_reference = Configuracion.objects.get(llave = "genpro")
            last_number = int(last_reference.valor)  # Extraer el número de la última referencia
            next_number = last_number + 1
            self.referencia = f'SGC{next_number:05}'  # Formatear el próximo número con ceros a la izquierda
            last_reference.valor = next_number 
            last_reference.save()
        super().save(*args, **kwargs)

class Configuracion(models.Model):
    llave = models.CharField(max_length=20, unique=True)
    valor = models.CharField(max_length=20)
        
    class Meta:
        verbose_name = 'Configuracion'
        verbose_name_plural = 'Configuraciones'
        ordering = ['llave']
        
class Pais(models.Model):
    nombre_pais = models.CharField(max_length=50, unique=True)
    sigla = models.CharField(max_length=10)
    
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'
        ordering = ['sigla']
        
    def __str__(self):
        return self.nombre_pais

class Puerto(models.Model):
    nombre_puerto = models.CharField(max_length=50, unique=True)
    sigla = models.CharField(max_length=10)
    pais_puerto = models.ForeignKey(Pais, on_delete=models.CASCADE,default=None, blank=True, null=True) 
    
    class Meta:
        verbose_name = 'Puerto'
        verbose_name_plural = 'Puertos'
        ordering = ['sigla']
    
    def __str__(self):
        return self.nombre_puerto

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=20, unique=True)
    direccion_proveedor = models.CharField(max_length=300)
    pin = models.CharField(max_length=4, unique=True)
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre_proveedor']
        
    def __str__(self):
        return self.nombre_proveedor
        
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=20, unique=True)
    direccion_cliente = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre_cliente']
        
    def __str__(self):
        return self.nombre_cliente
        
class Empresa(models.Model):
    nombre_empresa = models.CharField(max_length=30, unique=True)
    logo_empresa = models.ImageField(upload_to='logo_empresa/',blank=True,null=True, default='defaults/default.png')
    firma_empresa = models.ImageField(upload_to='firma_empresa/',blank=True,null=True,default='defaults/default.png')
    direccion_empresa = models.CharField(max_length=300)
    forma_pago = models.TextField(max_length=150)
    cod_camara = models.CharField(max_length=10)
    nombre_encargado = models.CharField(max_length=30)
    cargo_encargado = models.CharField(max_length=20)
    activo = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nombre_empresa']
        
    def __str__(self):
        return self.nombre_empresa
        
class Importadora(models.Model):
    nombre_importadora = models.CharField(max_length=100, unique=True)
    direccion_importadora = models.CharField(max_length=500)
    contrato = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Importadora'
        verbose_name_plural = 'Importadoras'
        ordering = ['nombre_importadora']
        
    def __str__(self):
        return self.nombre_importadora
    
class Transporte(models.Model):
    nombre_transporte = models.CharField(max_length=10)
    descripcion_transporte = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'
        ordering = ['nombre_transporte']
        
    def __str__(self):
        return self.nombre_transporte
 
class Estado(models.Model):
    nombre_estado = models.CharField(max_length=100)
    orden = models.IntegerField(default=0)
    color = models.CharField(max_length=7, default='#000000')
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['orden']
    
    def __str__(self):
        return self.nombre_estado
        
class Contenedor(models.Model):
    cubicaje = models.DecimalField(max_digits=10, decimal_places=2)
    flete = models.DecimalField(max_digits=10, decimal_places=2)
    seguro = models.DecimalField(max_digits=10, decimal_places=2)
    factura = models.CharField(max_length=15, editable=False, unique=True,default=None, blank=True, null=True)
    identificador = models.CharField(max_length=500)
    sello = models.CharField(max_length=100)
    hbl = models.CharField(max_length=100, default=None, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE,)
    importadora = models.ForeignKey(Importadora, on_delete=models.CASCADE,)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE, default=None, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=None, blank=True, null=True)
    puerto_origen = models.ForeignKey(Puerto, related_name='puerto_origen', on_delete=models.CASCADE,default=None, blank=True, null=True)
    puerto_destino = models.ForeignKey(Puerto, related_name='puerto_destino', on_delete=models.CASCADE,default=None, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Contenedor'
        verbose_name_plural = 'Contenedores'
        ordering = ['-fecha_creacion']
        
    def __str__(self):
        return self.identificador
    
    def save(self, *args, **kwargs):
    
        if not self.pk:
            year = datetime.now().year
            last_factura = Configuracion.objects.get(llave="genfac")
            last_number = int(last_factura.valor)
            next_number = last_number + 1
            self.factura = f'SSK{next_number:03}/{str(year)[-2:]}'
            last_factura.valor = next_number
            last_factura.save()
        super().save(*args, **kwargs)
    
class LLenarContenedor(models.Model):
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    bruto_kg = models.FloatField()
    neto_kg = models.FloatField()
    bultos = models.PositiveIntegerField()
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    contenedor = models.ForeignKey(Contenedor, related_name='items', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'LLenarContenedor'
        verbose_name_plural = 'LLenarContenedores'
        ordering = ['contenedor']
    
    
    