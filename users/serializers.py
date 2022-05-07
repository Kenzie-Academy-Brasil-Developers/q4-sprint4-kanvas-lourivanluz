from rest_framework import serializers


class UsersSerializers(serializers.Serializer):

    uuid            = serializers.CharField(read_only=True)
    is_admin        = serializers.BooleanField(required=False)
    email           = serializers.EmailField()
    password        = serializers.CharField(write_only=True)
    first_name      = serializers.CharField()
    last_name       = serializers.CharField()


class LoginSerializers(serializers.Serializer):
    email           = serializers.EmailField()
    password        = serializers.CharField()
