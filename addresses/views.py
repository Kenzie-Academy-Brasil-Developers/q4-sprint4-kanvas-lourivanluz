from xmlrpc.client import Boolean
from rest_framework. views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_401_UNAUTHORIZED
from rest_framework.authentication import TokenAuthentication


from addresses.models import Addresses
from addresses.serializers import Adresses_serializers
from users.models import Users
from kanvas_app.permissions import IsAdmim


class AdressView(APIView):

    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAdmim]

    def put(self,request:Request):
        
        user:Users = request.user
        if user.is_anonymous:
            return Response({"detail": "Invalid token."},HTTP_401_UNAUTHORIZED)


        serializer = Adresses_serializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        adress,_ = Addresses.objects.get_or_create(**serializer.validated_data)
        adress.users.add(user)
        adress.save()
        serializer = Adresses_serializers(adress)
        return Response(serializer.data,HTTP_200_OK)
        
