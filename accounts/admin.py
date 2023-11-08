from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User  # Importe o modelo User padrão
from .models import Contact  # Alterando o nome do modelo para "Contact"

# Defina uma classe personalizada para o modelo Contact


class ContactInline(admin.StackedInline):
    model = Contact

# Estenda o UserAdmin com ContactInline


class CustomUserAdmin(UserAdmin):
    inlines = (ContactInline,)


# Registre o modelo User padrão com a classe CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


