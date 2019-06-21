from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    start_date = models.DateTimeField(auto_now_add=True)
    duration = models.DateTimeField(auto_now=False)
    owner = models.ForeignKey('auth.User',related_name='Projects',on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)