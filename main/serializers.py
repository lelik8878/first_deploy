from rest_framework import serializers

class QuantitySerializer(serializers.Serializer):
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)
    unit = serializers.CharField()
    
class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    image = serializers.ImageField()
    price = serializers.IntegerField()
    
    quantity_set = QuantitySerializer(many=True)

