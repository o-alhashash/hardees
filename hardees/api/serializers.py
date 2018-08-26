from rest_framework.serializers import ModelSerializer

from hardees.models import Item


class ListSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'pic',
        ]


class DetailSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
