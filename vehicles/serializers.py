from rest_framework import serializers
class VehicleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    brand = serializers.CharField()
    color = serializers.CharField()
    fuel_type = serializers.CharField()
    year = serializers.DateField()
    runned_km = serializers.IntegerField()
    price = serializers.IntegerField()
    user=serializers.CharField()
