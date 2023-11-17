from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Module, Etudiant, Session
from .serializers import ModuleSerializer, EtudiantSerializer, SessionSerializer

class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ModuleViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = ModuleSerializer

    def get_queryset(self):
        return Module.objects.all()
class EtudiantViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = EtudiantSerializer

    def get_queryset(self):
        return Etudiant.objects.all()

class SessionViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = SessionSerializer

    def get_queryset(self):
        queryset = Session.objects.all()
        session_id = self.request.GET.get('session-id')
        if session_id:
            queryset = queryset.filter(session_id=session_id)
        return queryset





