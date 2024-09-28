from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    adress = models.TextField()
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    adress = models.TextField()
    cnpj = models.CharField(max_length=30)

    def __str__(self):
        return self.name
