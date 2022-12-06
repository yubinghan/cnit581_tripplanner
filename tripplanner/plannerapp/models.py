from django.db import models

# Create your models here.
class tripRecm(models.Model):
    title = models.CharField(max_length=150, null=True)
    days = models.IntegerField(null=True)
    fee = models.IntegerField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

