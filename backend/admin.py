from django.contrib import admin


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    
    list_display = ('nome', 'email', 'telefone', 'data_cadastro')
    search_fields = ('nome', 'email')
    ordering = ('nome')