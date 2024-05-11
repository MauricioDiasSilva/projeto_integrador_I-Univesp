
from django.contrib import admin
from .models import CriancaEspecial
from django.contrib.auth.models import User

admin.site.register(CriancaEspecial)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')

# Desregistrar o modelo User
admin.site.unregister(User)

# Registrar novamente com a classe ModelAdmin personalizada
admin.site.register(User, UserAdmin)

