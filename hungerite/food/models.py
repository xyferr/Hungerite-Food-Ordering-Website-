from django.db import models

# Create your models here.
class order(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    food=models.CharField(max_length=100)
    address=models.TextField()
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name
    
    