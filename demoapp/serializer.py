from rest_framework import routers, serializers, viewsets
from demoapp.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','task', 'description')