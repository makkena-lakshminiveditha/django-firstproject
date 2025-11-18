from django.db import models

# Create your models here.

class employe_model(models.Model):
    employe_name = models.CharField(max_length=50)
    employe_id = models.IntegerField()
    employe_salary = models.IntegerField()

    def __str__(self):
        return self.employe_name