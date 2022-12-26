from django.db import models



class Client(models.Model):
    name= models.CharField(max_length=50)
    surname= models.CharField(max_length=50)
    email= models.EmailField()
    role= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.surname} {self.email} {self.role}"
