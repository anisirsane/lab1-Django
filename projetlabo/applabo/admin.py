# auteur: anis irsane
# titre : laboratoire 1
# description:un projet qui relie le drf avec le frontend de react on se connectant les endponts
# version: 2.0
from django.contrib import admin
from applabo.models import Etudiant, Module, Session
# user pour le admin dashboard: anisi

# password pour le admin dashboard: anisi
admin.site.register(Etudiant)
admin.site.register(Module)
admin.site.register(Session)