
from django.contrib import admin
from .models import CriancaEspecial, Missao, ValorImage, Contato, Membro, Evento, Noticia, Servico,Historia,CarouselImage
admin.site.register(CriancaEspecial)
admin.site.register(Missao)
admin.site.register(ValorImage)
admin.site.register(Contato)
admin.site.register(Membro)
admin.site.register(Evento)
admin.site.register(Noticia)
admin.site.register(Servico)


class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'imagem')
    search_fields = ('titulo', 'descricao')
    list_filter = ('titulo',)

admin.site.register(Historia, HistoriaAdmin)


class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)

admin.site.register(CarouselImage)








