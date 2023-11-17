from django.contrib import admin
from applabo.models import Etudiant, Module, Session
# user pour le admin dashboard: admin

# password pour le admin dashboard: admin
admin.site.register(Etudiant)
admin.site.register(Module)
admin.site.register(Session)