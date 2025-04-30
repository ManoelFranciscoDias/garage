from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from garagem.models import Autor

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"