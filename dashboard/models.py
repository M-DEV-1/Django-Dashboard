from django.db import models

# Create your models here.

class studentrecord(models.Model):
    
    date_creation = models.DateTimeField(auto_now_add=True)
    
    firstname = models.CharField(max_length=200)
    
    lastname = models.CharField(max_length=200)
    
    parentnumber = models.CharField(max_length=10)
    
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return self.firstname+"  "+self.lastname
        #this is a lazy method

    
    
    
    