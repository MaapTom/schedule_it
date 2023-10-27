from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Contact(models.Model):  # Alterando o nome do modelo para "Contact"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)


@receiver(post_save, sender=User)
# Alterando o nome da função para "create_contact"
def create_contact(sender, instance, created, **kwargs):
    if created:
        Contact.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_contact(sender, instance, **kwargs):  # Alterando o nome da função para "save_contact"
#     instance.contact.save()
