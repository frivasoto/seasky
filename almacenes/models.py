from django.db import models

# Create your models here.

class Cambio(models.Model):
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    cambio_cup = models.IntegerField()
    
    class Meta:
        verbose_name = 'Cambio'
        verbose_name_plural = 'Cambios'
        ordering = ['-fecha_cambio']
        
class Cliente(models.Model):
    ci = models.CharField(max_length=11, unique=True)
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    direccion_cliente = models.CharField(max_length=300)
    telefono_cliente = models.CharField(max_length=8)
    correo_cliente = models.EmailField()
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Cliente'
        ordering = ['ci']
        
    def __str__(self):
        return self.nombre_cliente + self.apellido_cliente 
        
class Empresa(models.Model):
    nit = models.CharField(max_length=20, unique=True)
    nombre_empresa = models.CharField(max_length=100)
    direccion_empresa = models.CharField(max_length=300)
    telefono_empresa = models.CharField(max_length=8)
    correo_empresa = models.EmailField()
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nit']
        
    def __str__(self):
        return self.nombre_empresa 

class Producto(models.Model):
    id_producto = models.CharField(max_length=20)
    nombre_producto = models.CharField(max_length=50)
    imagen_producto = models.ImageField(upload_to='imagen_producto/,blank=True,null=True')
    cantidad_inicio = models.IntegerField()
    precio_usd = models.DecimalField(default=0,max_digits=7,decimal_places=2)
    impuesto_cup = models.IntegerField(default=0)
    empaquetado = models.IntegerField()
    cantidad_congelada = models.IntegerField()
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id_producto']
        
    def __str__(self):
        return self.nombre_producto