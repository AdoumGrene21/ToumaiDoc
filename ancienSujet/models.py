from django.db import models

# Create your models here.
class Faculte(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.nom

class Departement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    #fk
    faculte = models.ForeignKey(Faculte, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    #fk
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nom

class Niveau(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    #fk
    filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nom

class Type(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.nom


class Document(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    document = models.FileField(upload_to='documents', null=True)
    #fk
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    niveau = models.ForeignKey(Niveau, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom

