from django.contrib import admin
from .models import *


# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["id", "referencia", "descripcion", "partida_arancelaria", "peso_neto", "peso_bruto"]
    readonly_fields = ('referencia',)


class ConfiguracionAdmin(admin.ModelAdmin):
    list_display = ["llave", "valor"]


class PuertoAdmin(admin.ModelAdmin):
    list_display = ["nombre_puerto", "sigla"]


class PaisAdmin(admin.ModelAdmin):
    list_display = ["nombre_pais", "sigla"]


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre_proveedor", "direccion_proveedor"]


class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre_cliente", "direccion_cliente"]


class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["nombre_empresa", "direccion_empresa"]


class UnidadDeMedidaAdmin(admin.ModelAdmin):
    list_display = ["nombre"]


class PartidaArancelariaAdmin(admin.ModelAdmin):
    list_display = ["partida", "descripcion"]


class ContenedorAdmin(admin.ModelAdmin):
    list_display = ["factura", 'empresa', 'importadora', 'hbl', 'proveedor', 'cliente', 'puerto_origen', 'puerto_destino',
                    'cubicaje', 'flete', 'seguro', 'identificador', 'sello', 'transporte']


admin.site.register(Producto, ProductoAdmin, )
admin.site.register(Configuracion, ConfiguracionAdmin, )
admin.site.register(Puerto, PuertoAdmin, )
admin.site.register(Pais, PaisAdmin, )
admin.site.register(Proveedor, ProveedorAdmin, )
admin.site.register(Cliente, ClienteAdmin, )
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(UnidadDeMedida, UnidadDeMedidaAdmin)
admin.site.register(PartidaArancelaria, PartidaArancelariaAdmin)
admin.site.register(Contenedor, ContenedorAdmin)
