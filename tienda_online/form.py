from django import forms
from .models import *

class PartidaArancelariaForm(forms.ModelForm):
    class Meta:
        model = PartidaArancelaria
        fields = ['partida', 'descripcion']
        widgets = {'partida': forms.TextInput(attrs={'class': 'form-control'}), 
                   'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de los productos contenidos en la partida arancelaria...'})
                   }

class UnidadDeMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadDeMedida
        fields = ['nombre']
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'})}

class UnidadMedidaContenedorForm(forms.ModelForm):
    class Meta:
        model = UnidadMedidaContenedor
        fields = ['nombre', 'sigla']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    unidad_medida = forms.ModelChoiceField(queryset=UnidadDeMedida.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    partida_arancelaria = forms.ModelChoiceField(queryset=PartidaArancelaria.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Producto
        fields = ['partida_arancelaria', 'descripcion', 'peso_neto', 'peso_bruto', 'unidad_medida']
        widgets = {
            
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del producto'}),
            'peso_neto': forms.NumberInput(attrs={'class': 'form-control float-left mr-1', 'step': 'any'}),
            'peso_bruto': forms.NumberInput(attrs={'class': 'form-control float-left', 'step': 'any'}),
}
    def clean_peso_neto(self):
        peso_neto = self.cleaned_data.get('peso_neto')
        if peso_neto <= 0:
            raise forms.ValidationError("El peso neto debe ser mayor que cero.")
        return peso_neto

    def clean_peso_bruto(self):
        peso_bruto = self.cleaned_data.get('peso_bruto')
        if peso_bruto <= 0:
            raise forms.ValidationError("El peso bruto debe ser mayor que cero.")
        return peso_bruto
        
class PuertoForm(forms.ModelForm):
    pais_puerto = forms.ModelChoiceField(queryset=Pais.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Puerto
        fields = ['nombre_puerto', 'sigla', 'pais_puerto']
        widgets = {
            'nombre_puerto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del puerto..'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Siglas del puerto..'}),
}
        
class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre_pais', 'sigla']
        widgets = {
            'nombre_pais': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del pais..'}),
            'sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Siglas del pais..'}),
}

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_proveedor', 'direccion_proveedor','pin']
        widgets = {
            'nombre_proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor..'}),
            'direccion_proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del proveedor..'}),
            'pin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'pin..'}),
}
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'direccion_cliente']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente..'}),
            'direccion_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del cliente..'}),
}
        
class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre_empresa', 'logo_empresa', 'firma_empresa', 'direccion_empresa', 'forma_pago', 'cod_camara', 'nombre_encargado', 'cargo_encargado', 'activo']
        widgets = {
            'nombre_empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la empresa..'}),
            'direccion_empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección de la empresa..'}), 
            'forma_pago': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Forma de pago'}), 
            'cod_camara': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Codigo de camara de comercio'}), 
            'nombre_encargado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del encargado..'}), 
            'cargo_encargado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo del encargado..'}),
            'activo': forms.CheckboxInput()
        }
        
class ImportadoraForm(forms.ModelForm):
    class Meta:
        model = Importadora
        fields = ['nombre_importadora', 'direccion_importadora', 'contrato']
        widgets = {
            'nombre_importadora': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la imoportadora..'}),
            'direccion_importadora': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección de la importadora..'}),
            'contrato': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de contrato'})
        }
        
class ContenedorForm(forms.ModelForm):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    importadora = forms.ModelChoiceField(queryset=Importadora.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    transporte = forms.ModelChoiceField(queryset=Transporte.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    puerto_origen = forms.ModelChoiceField(queryset=Puerto.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    puerto_destino = forms.ModelChoiceField(queryset=Puerto.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    unidad = forms.ModelChoiceField(queryset=UnidadMedidaContenedor.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Contenedor
        fields = ['identificador', 'sello','hbl', 'empresa', 'importadora', 'proveedor', 'cliente','transporte', 'puerto_origen', 'puerto_destino', 'unidad', 'cubicaje', 'flete', 'seguro','estado' ]
        widgets = {
            'identificador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'id de contenedor..'}), 
            'sello': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '# de sellos..'}),
            'hbl': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '# de HBL..'}),
            'cubicaje': forms.NumberInput(attrs={'class': 'form-control'}), 
            'flete': forms.NumberInput(attrs={'class': 'form-control'}), 
            'seguro': forms.NumberInput(attrs={'class': 'form-control'}), 
            
            
        }


class LLenarContenedorForm(forms.ModelForm):
    productos = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = LLenarContenedor
        fields = ['productos', 'cantidad', 'precio', 'bruto_kg', 'neto_kg', 'bultos',]
        widgets = {
            
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'bruto_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'neto_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'bultos': forms.NumberInput(attrs={'class': 'form-control'}),
            
        }
        
class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ['orden','nombre_estado', 'color']
        widgets = {
            'orden': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre_estado': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'type': 'color'}),   
        }
        
class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = ['nombre_transporte', 'descripcion_transporte']
        widgets = {
            
            'nombre_transporte': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_transporte': forms.TextInput(attrs={'class': 'form-control'}),   
        }