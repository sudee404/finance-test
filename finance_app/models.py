from enum import unique
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Income(models.Model):
    """
    This model holds the user's total income obtained from the instances added
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_instances(self):
        return IncomeInstance.objects.filter(income=self)

    def __str__(self):
        return f"{self.owner.get_username}"


class IncomeInstance(models.Model):
    """This is an income instance"""
    income = models.ForeignKey(Income, on_delete=models.CASCADE)
    description = models.CharField(max_length=200,default = 'Others')
    amount = models.PositiveIntegerField()
    age_start = models.PositiveIntegerField(null=True,default=40)
    age_stop = models.PositiveIntegerField(null=True,default=90)
    growth = models.IntegerField(null=True,blank=True)

    class Meta:
        ordering = ['age_start']
        unique_together = ['income','description']
