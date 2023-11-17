from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from applabo.models import Module, Etudiant, Session



class ModuleSerializer(serializers.ModelSerializer):
    #source: https://www.django-rest-framework.org/api-guide/relations/
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
    Modules = ModuleSerializer()
    Etudiants = EtudiantSerializer()
    class Meta:
        model = Session
        fields = ['id','Num', 'Modules','Etudiants']






