from rest_framework.viewsets import ModelViewSet

from garagem.models import Autor
from garagem.serializers import AutorSerializer 

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer