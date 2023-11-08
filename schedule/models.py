from django.db import models
from .widgets import CPFFormatWidget
from .widgets import PhoneFormatWidget
from accounts.models import User
from django.db.models.fields.related import ForeignKey
from django.core.exceptions import ValidationError
from datetime import date


# from .utils import preencher_horarios_disponiveis


class Collaborator(models.Model):

    name = models.CharField(max_length=100)

    address = models.CharField(max_length=200)

    cpf = models.CharField(max_length=14)

    phone = models.CharField(max_length=14)

    SEXY_CHOICES = (


        ('M', 'Masculino'),


        ('F', 'Feminino'),

        ('O', 'Outro'),
    )

    sexy = models.CharField(max_length=1, choices=SEXY_CHOICES)

    DAY_CHOICES = (

        ('monday', 'Monday'),

        ('tuesday', 'Tuesday'),

        ('wednesday', 'Wednesday'),

        ('thursday', 'Thursday'),

        ('friday', 'Friday'),

        ('saturday', 'Saturday'),

        ('sunday', 'Sunday'),
    )

    day = models.CharField(max_length=10, choices=DAY_CHOICES, blank=True,

                           null=True, default='monday')

    HOURS_CHOICES = (

        ('oito', '8:00'),

        ('nove', '9:00'),

        ('dez', '10:00'),

        ('onze', '11:00'),

        ('doze', '12:00'),

        ('treze', '13:00'),

        ('quatorze', '14:00'),

        ('quinze', '15:00'),

        ('dezesseis', '16:00'),

        ('dezessete', '17:00'),

        ('dezoito', '18:00'),

        ('dezenove', '19:00'),

        ('vinte', '20:00'),
    )

    available_hours = models.CharField(max_length=10, choices=HOURS_CHOICES, blank=True,

                                       null=True,)

    OFFICE_CHOICES = (


        ('barber', 'Barbeiro'),

        ('hairdresser', 'Cabeleireiro'),

        ('stylist_barber', 'Barbeiro Estilista'),

        ('receptionist', 'Recepcionista'),

        ('barbershop_manager', 'Gerente da Barbearia'),

        ('barber_assistant', 'Auxiliar de Barbeiro'),

        ('hair_treatment_specialist', 'Especialista em Tratamentos Capilares'),

        ('manicurist_pedicurist', 'Manicure/Pedicure'),

        ('facial_esthetician', 'Esteticista Facial'),

        ('masseuse_massagist', 'Massagista'),
    )

    office = models.CharField(max_length=100, choices=OFFICE_CHOICES)

    code = models.AutoField(primary_key=True)

    def __str__(self):

        return self.name


class Service(models.Model):

    SERVICE_CHOICES = (






        ('haircut', 'Corte de Cabelo'),






        ('beard_trim', 'Barba e Bigode'),






        ('beard_design', 'Design de Barba'),






        ('full_beard', 'Barba Completa'),






        ('hair_treatments', 'Tratamentos Capilares'),






        ('hair_coloring', 'Coloração de Cabelo'),






        ('eyebrow_design', 'Design de Sobrancelha'),






        ('facial_massage', 'Massagens Faciais'),






        ('skin_care', 'Tratamentos de Pele'),






        ('hair_cauterization', 'Cauterização de Fios'),






        ('beard_hydration', 'Hidratação de Barba'),






        ('sideburn_trim', 'Aparar Costeletas'),






        ('beard_cauterization', 'Cauterização da Barba'),






        ('acne_facial_treatment', 'Tratamento de Acne Facial'),






        ('dark_circle_treatment', 'Tratamento de Olheiras'),

    )

    name = models.CharField(max_length=100, choices=SERVICE_CHOICES)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    codigo = models.AutoField(primary_key=True)

    def __str__(self):

        return self.name

# -------------------------------------------------


# schedule/models.py
def validate_day(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('Não é possivel escolher um data atrasada.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Escolha um dia útil da semana.')


class Scheduling(models.Model):

    # Crie um relacionamento ForeignKey com a classe User

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Client')
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE, related_name='schedules')
    day = models.DateField(validators=[validate_day], default=date.today)
    HOURS_CHOICES = (

        ('1', '8:00'),

        ('2', '9:00'),

        ('3', '10:00'),

        ('4', '11:00'),

        ('5', '12:00'),

        ('6', '13:00'),

        ('7', '14:00'),

        ('8', '15:00'),

        ('9', '16:00'),

        ('10', '17:00'),

        ('11', '18:00'),

        ('12', '19:00'),

        ('13', '20:00'),
    )
    hours = models.CharField(max_length=10, choices=HOURS_CHOICES, default=1)
    SERVICE_CHOICES = (
        ('haircut', 'Corte de Cabelo'),
        ('beard_trim', 'Barba e Bigode'),
        ('beard_design', 'Design de Barba'),
        ('full_beard', 'Barba Completa'),
        ('hair_treatments', 'Tratamentos Capilares'),
        ('hair_coloring', 'Coloração de Cabelo'),
        ('eyebrow_design', 'Design de Sobrancelha'),
        ('facial_massage', 'Massagens Faciais'),
        ('skin_care', 'Tratamentos de Pele'),
        ('hair_cauterization', 'Cauterização de Fios'),
        ('beard_hydration', 'Hidratação de Barba'),
        ('sideburn_trim', 'Aparar Costeletas'),
        ('beard_cauterization', 'Cauterização da Barba'),
        ('acne_facial_treatment', 'Tratamento de Acne Facial'),
        ('dark_circle_treatment', 'Tratamento de Olheiras'),
    )
    service = models.CharField(max_length=45,choices=SERVICE_CHOICES, default=1)

    class Meta:
        unique_together = ('collaborator', 'hours', 'day')

    def __str__(self):
        return f'{self.day.strftime("%b %d %Y")} - {self.get_hours_display()} - {self.collaborator}'
