from django.urls import *
from tienda_online import views
from tienda_online.views import *

urlpatterns = [
    path('producto/', ProductoListView.as_view(), name="productos_listado"),
    path('producto/nuevo/', ProductoCreateView.as_view(), name='crear_producto'),
    path('producto/actualizar/<int:pk>', ProductoUpdateView.as_view(), name='actualizar_producto'),
    path('producto/eliminar/<int:pk>', ProductoDeleteView.as_view(), name='eliminar_producto'),
    path('home/', Home.as_view(), name='base'),
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    path('puerto/', PuertoListView.as_view(), name='puerto_listado'),
    path('puerto/nuevo/', PuertoCreateView.as_view(), name='crear_puerto'),
    path('puerto/actualizar/<int:pk>', PuertoUpdateView.as_view(), name='actualizar_puerto'),
    path('puerto/eliminar/<int:pk>', PuertoDeleteView.as_view(), name='eliminar_puerto'),
    
    path('pais/', PaisListView.as_view(), name='pais_listado'),
    path('pais/nuevo/', PaisCreateView.as_view(), name='crear_pais'),
    path('pais/actualizar/<int:pk>', PaisUpdateView.as_view(), name='actualizar_pais'),
    path('pais/eliminar/<int:pk>', PaisDeleteView.as_view(), name='eliminar_pais'),
    
    path('proveedor/', ProveedorListView.as_view(), name='proveedor_listado'),
    path('proveedor/nuevo/', ProveedorCreateView.as_view(), name='crear_proveedor'),
    path('proveedor/actualizar/<int:pk>', ProveedorUpdateView.as_view(), name='actualizar_proveedor'),
    path('proveedor/eliminar/<int:pk>', ProveedorDeleteView.as_view(), name='eliminar_proveedor'),
    
    path('cliente/', ClienteListView.as_view(), name='cliente_listado'),
    path('cliente/nuevo/', ClienteCreateView.as_view(), name='crear_cliente'),
    path('cliente/actualizar/<int:pk>', ClienteUpdateView.as_view(), name='actualizar_cliente'),
    path('cliente/eliminar/<int:pk>', ClienteDeleteView.as_view(), name='eliminar_cliente'),
    
    path('empresa/', EmpresaListView.as_view(), name='empresa_listado'),
    path('empresa/nuevo/', EmpresaCreateView.as_view(), name='crear_empresa'),
    path('empresa/actualizar/<int:pk>', EmpresaUpdateView.as_view(), name='actualizar_empresa'),
    path('empresa/eliminar/<int:pk>', EmpresaDeleteView.as_view(), name='eliminar_empresa'),
    
    path('importadora/', ImportadoraListView.as_view(), name='importadora_listado'),
    path('importadora/nuevo/', ImportadoraCreateView.as_view(), name='crear_importadora'),
    path('importadora/actualizar/<int:pk>', ImportadoraUpdateView.as_view(), name='actualizar_importadora'),
    path('importadora/eliminar/<int:pk>', ImportadoraDeleteView.as_view(), name='eliminar_importadora'),
    
    path('unidad/', UnidadDeMedidaListView.as_view(), name='unidad_listado'),
    path('unidad/nuevo/', UnidadDeMedidaCreateView.as_view(), name='crear_unidad'),
    path('unidad/actualizar/<int:pk>', UnidadDeMedidaUpdateView.as_view(), name='actualizar_unidad'),
    path('unidad/eliminar/<int:pk>', UnidadDeMedidaDeleteView.as_view(), name='eliminar_unidad'),
    
    path('partida/', PartidaArancelariaListView.as_view(), name='partida_listado'),
    path('partida/nuevo/', PartidaArancelariaCreateView.as_view(), name='crear_partida'),
    path('partida/actualizar/<int:pk>', PartidaArancelariaUpdateView.as_view(), name='actualizar_partida'),
    path('partida/eliminar/<int:pk>', PartidaArancelariaDeleteView.as_view(), name='eliminar_partida'),
    
    path('contenedor/', ContenedorListView.as_view(), name='contenedor_listado'),
    path('contenedor/nuevo/', ContenedorCreateView.as_view(), name='crear_contenedor'),
    path('contenedor/actualizar/<int:pk>', ContenedorUpdateView.as_view(), name='actualizar_contenedor'),
    path('contenedor/eliminar/<int:pk>', ContenedorDeleteView.as_view(), name='eliminar_contenedor'),
    path('contenedor/llenar/<int:pk>/detalle', LLenarContenedorView.as_view(), name='contenedor_llenar'),
    path('contenedor/llenar/<int:pk>/add', AgregarProductoCreateView.as_view(), name='agregar_producto'),
    path('contenedor/llenar/<int:pk>/remove', EliminarProductoDeleteView.as_view(), name='remove_producto'),
    path('contenedor/llenar/<int:pk>/update', ActualizarProductoDeleteView.as_view(), name='update_producto'),
    
    path('contenedor/llenar/<int:pk>/factura', Factura.as_view(), name='factura'),
    path('contenedor/llenar/<int:pk>/', FacturaView.as_view(), name='factura_view'),
    path('contenedor/llenar/<int:pk>/declaracion', Declaracion.as_view(), name='declaracion'),
    
    path('estado/', EstadoListView.as_view(), name='estado_listado'),
    path('estado/nuevo/', EstadoCreateView.as_view(), name='crear_estado'),
    path('estado/actualizar/<int:pk>', EstadoUpdateView.as_view(), name='actualizar_estado'),
    path('estado/eliminar/<int:pk>', EstadoDeleteView.as_view(), name='eliminar_estado'),
    
    path('transporte/', TransporteListView.as_view(), name='transporte_listado'),
    path('transporte/nuevo/', TransporteCreateView.as_view(), name='crear_transporte'),
    path('transporte/actualizar/<int:pk>', TransporteUpdateView.as_view(), name='actualizar_transporte'),
    path('transporte/eliminar/<int:pk>', TransporteDeleteView.as_view(), name='eliminar_transporte'),

    path('contenedor/llenar/<int:pk>/excel', ExportarContenedorExcelView.as_view(), name='excel'), 
    
    path('proveedor/<str:nombre_proveedor>/pin/', SolicitarPinView.as_view(), name='solicitar_pin'),   
    path('proveedor/<str:nombre_proveedor>/contenedores/', ContenedoresPorProveedorView.as_view(), name='contenedores_por_proveedor'),
    path('proveedor/<str:nombre_proveedor>/contenedores/<int:pk>', ContenedoresPorProveedorDetalleView.as_view(), name='contenedores_por_proveedor_detalle'),
]