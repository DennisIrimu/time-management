from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    start_date = models.DateTimeField(auto_now_add=True)
    duration = models.DateTimeField(auto_now=False)

    def __str__(self):
        return (self.name)