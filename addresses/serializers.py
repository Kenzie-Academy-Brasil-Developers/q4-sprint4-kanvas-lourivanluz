from rest_framework import serializers


class Adresses_serializers(serializers.Serializer):

    address_uui     = serializers.CharField(read_only=True)
    street          = serializers.CharField()
    house_number    = serializers.IntegerField()
    city            = serializers.CharField()
    state           = serializers.CharField()
    zip_code        = serializers.CharField()
    country         = serializers.CharField()