from rest_framework.viewsets import ModelViewSet

from garagem.models import Editora
from garagem.serializers import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

