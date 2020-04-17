from rest_framework import serializers

from .models import *


class MaintainToolsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintainCommand
        fields = '__all__'

class ExecCommandSerializer(serializers.ModelSerializer):

    class Meta:
        model = SshExecCommand
        fields = '__all__'

