from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from garagem.models import Editora

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"
