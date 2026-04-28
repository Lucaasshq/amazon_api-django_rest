from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cliente
        fields = '__all__' # Para expor todas Colunas da entidade
        

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor 
        fields = '__all__'
        
        
class ProdutoSerializer(serializers.ModelSerializer):
    categoria_display = serializers.CharField(
        source='get_categoria_display',
        read_only=True
    )
    
    
    class Meta:
        model = Produto
        fields = '__all__'
        extra_fields = ['categoria_display']


