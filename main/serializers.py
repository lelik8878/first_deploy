from rest_framework import serializers

class PropertiesSerializer(serializers.Serializer):
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255)
    image = serializers.ImageField()
    price = serializers.IntegerField()
    unit = serializers.CharField(max_length=255)
    productproperties_set = PropertiesSerializer(many=True)


