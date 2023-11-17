from django.db import models

# user pour le admin dashboard: admin
# password pour le admin dashboard: admin

# ce code et develope est customise depuis les quiz et le premier tutorial du django
# source:https://www.mongodb.com/community/forums/t/schema-design-many-to-many-relationships-and-normalization/209349
# dans ces models j'ai base ma conception le database normalisation concept, qui insiste sur eviter les many to many relationships en creeant une table intermidiaire
class Etudiant(models.Model):
    Nom = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.Nom

class Module(models.Model):
    Nom = models.CharField(max_length=255)
    coeff = models.IntegerField()
    description = models.TextField()
    etudiants = models.ManyToManyField(Etudiant, blank=True, related_name='modules', through="Session")

    def __str__(self):
        return self.Nom
class Session(models.Model):
    Num = models.CharField(max_length=255)
    Modules = models.ForeignKey('applabo.Module' , on_delete=models.CASCADE)
    Etudiants = models.ForeignKey('applabo.Etudiant',on_delete=models.CASCADE)
    def __str__(self):
        return self.Num



