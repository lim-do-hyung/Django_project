from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title