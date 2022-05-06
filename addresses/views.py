from xmlrpc.client import Boolean
from rest_framework. views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from addresses.models import Addresses
from addresses.serializers import Adresses_serializers
from users.models import Users


class AdressView(APIView):
    def put(self,request:Request):
        user:Users = Users.objects.first()
        serializer = Adresses_serializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        adress,_ = Addresses.objects.get_or_create(**serializer.validated_data)
        adress.users.add(user)
        adress.save()
        print(adress)
        serializer = Adresses_serializers(adress)
        return Response(serializer.data,HTTP_201_CREATED)
        
