from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    text =  models.TextField('Comment')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Taskovich'
        verbose_name_plural="Taskovichane"