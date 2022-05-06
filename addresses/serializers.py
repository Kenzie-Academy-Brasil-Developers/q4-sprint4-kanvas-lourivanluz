from rest_framework import serializers

from users.serializers import Users_serializers



class Adresses_serializers(serializers.Serializer):

    uui     = serializers.CharField(read_only=True)
    street          = serializers.CharField()
    house_number    = serializers.IntegerField()
    city            = serializers.CharField()
    state           = serializers.CharField()
    zip_code        = serializers.CharField()
    country         = serializers.CharField()

    users = Users_serializers(read_only=True,many=True)