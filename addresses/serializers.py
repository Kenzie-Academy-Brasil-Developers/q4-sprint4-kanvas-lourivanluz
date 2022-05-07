from rest_framework import serializers


from users.serializers import UsersSerializers

class AdressesSerializers(serializers.Serializer):

    uuid             = serializers.UUIDField(read_only=True)
    street          = serializers.CharField()
    house_number    = serializers.IntegerField()
    city            = serializers.CharField()
    state           = serializers.CharField()
    zip_code        = serializers.CharField()
    country         = serializers.CharField()

    users = UsersSerializers(read_only=True,many=True)