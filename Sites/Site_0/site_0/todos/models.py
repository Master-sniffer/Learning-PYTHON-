# Create your models here.
from django.db import models

class Todo(models.Model): # Table will be called Todo 
    content = models.TextField() # Column will be called content and it accepts text