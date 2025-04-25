from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from garagem.models import Categoria, Editora, Livro, Autor
from garagem.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer, AutorSerializer, LivroDetailSerializer, LivroListSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]



class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer

class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer