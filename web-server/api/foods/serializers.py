from rest_framework import serializers
from api.models import Foods

class FoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Foods
        fields = '__all__'
class RecommendSerializer(serializers.Serializer):
    pagesize=serializers.IntegerField(max_value=20,min_value=1,default=20)
    page=serializers.IntegerField(max_value=10,min_value=1,default=1)
class CollectSerializer(serializers.Serializer):
    id=serializers.CharField()
class ClickSerializer(serializers.Serializer):
    id=serializers.CharField()
    