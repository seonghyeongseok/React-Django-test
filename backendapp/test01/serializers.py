from rest_framework.serializers import ModelSerializer
from .models import SysConfig

class TestDataSerializer(ModelSerializer):
    class Meta:
        model = SysConfig
        fields = '__all__'