# auteur: anis irsane
# titre : laboratoire 1
# description:un projet qui relie le drf avec le frontend de react on se connectant les endponts
# version: 2.0
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from applabo.models import Module, Etudiant, Session



class ModuleSerializer(serializers.ModelSerializer):
    #source: https://www.django-rest-framework.org/api-guide/relations/
    # cette ligne est pour faire la relations entre le serializer de chaque modele
    etudiants = serializers.StringRelatedField(many=True)

    class Meta:
        model = Module
        fields = ['id','Nom', 'description','coeff', 'etudiants']
class ModuleEtudiantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ['id','Nom']
class EtudiantSerializer(serializers.ModelSerializer):
    modules = ModuleEtudiantSerializer(many=True, read_only=True)
    class Meta:
        model = Etudiant
        fields = ['id','Nom', 'email','modules']

class SessionSerializer(ModelSerializer):
    # ce code est pour afficher le id de chaque module et le nom de chaque etudiant qui appartient a chaqu esssion
    Modules = ModuleSerializer()
    Etudiants = EtudiantSerializer()
    class Meta:
        model = Session
        fields = ['id','Num', 'Modules','Etudiants']






