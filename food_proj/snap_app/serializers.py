from rest_framework.serializers import ModelSerializer
from .models import SnapData, ApplicationInfo, StateSnapProgram

class StateSnapProgramSerializer(ModelSerializer):
    class Meta:
        model = StateSnapProgram
        fields = '__all__'

class ApplicationInfoSerializer(ModelSerializer):
    class Meta:
        model = ApplicationInfo
        fields = '__all__'

class SnapDataSerializer(ModelSerializer):
    class Meta:
        model = SnapData
        fields = '__all__'