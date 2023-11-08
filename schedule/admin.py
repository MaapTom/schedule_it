from django.contrib import admin
from .models import Collaborator, Service
from .forms import CollaboratorForm
from .widgets import CPFFormatWidget, PhoneFormatWidget
from .models import Scheduling


class CollaboratorAdmin(admin.ModelAdmin):
    form = CollaboratorForm

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'phone':
            kwargs['widget'] = PhoneFormatWidget()
        elif db_field.name == 'cpf':
            kwargs['widget'] = CPFFormatWidget()
        return super().formfield_for_dbfield(db_field, request, **kwargs)


# schedule/admin.py

class SchedulingAdmin(admin.ModelAdmin):
    list_display = ['user', 'collaborator', 'day', 'hours']


admin.site.register(Scheduling, SchedulingAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(Service)
