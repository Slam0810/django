from django.db import models
from django.utils import timezone


class Produit(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True)
    nom = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100, default="")
    caracteristic = models.CharField(max_length=100)
    image = models.FileField(upload_to="photos/", default = None)
    description = models.TextField(null=True)
    etat = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")



    class Meta:
        verbose_name = "produit"
        ordering = ['date']


    def __str__(self):
        return self.nom

class Contact(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True)
    email = models.EmailField(max_length=100)
    nom = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de parution")

    class Meta:
        verbose_name = "contact"
        ordering = ['date']


    def __str__(self):
        return self.nom


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return self.contact.nom

class Presentation(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True)
    nom = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    metier = models.CharField(max_length=100, default="")
    image = models.FileField(upload_to="images/", default = None)

    class Meta:
        verbose_name = "contact"

    def __str__(self):
        return self.nom
