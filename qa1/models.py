from django.db import models

# Create your models here.
def __str__(self):
        return self.title

class task(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    
    def __str__(self):
        return self.title


