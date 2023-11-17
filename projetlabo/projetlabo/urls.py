from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from applabo.views import ModuleViewset,EtudiantViewset, SessionViewset

# Ici nous créons notre routeur
router = routers.SimpleRouter()
# on enregistre nos routes pour les endpoints
router.register('Module', ModuleViewset, basename='Module')
router.register('Etudiant', EtudiantViewset, basename='Etudiant')
router.register('Session', SessionViewset, basename='Session')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)), 
]