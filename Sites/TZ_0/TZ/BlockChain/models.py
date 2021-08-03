from django.db import models

# Create your models here.

class Task(models.Model):
    Code = models.CharField('Code')
    text =  models.TextField('Comment')

    def __str__(self):
        return self.Code
    
    class Meta:
        verbose_name='Transaction'
        verbose_name_plural="Transactions"