
from django.contrib import admin
from .models import CriancaEspecial, Missao, ValorImage, Contato, Membro, Evento, Noticia, Servico,CarouselImage
admin.site.register(CriancaEspecial)
admin.site.register(Missao)
admin.site.register(ValorImage)
admin.site.register(Contato)
admin.site.register(Membro)
admin.site.register(Evento)
admin.site.register(Noticia)
admin.site.register(Servico)


class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)

admin.site.register(CarouselImage)

class Membro(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')
    list_filter = ('telefone',)  # Exemplo de filtro por telefone

class CriancaEspecial(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')
    search_fields = ('nome', 'email')
    list_filter = ('telefone',)  # Exemplo de filtro por telefone





