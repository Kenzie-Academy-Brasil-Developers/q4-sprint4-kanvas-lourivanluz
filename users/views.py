from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_201_CREATED,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


from users.models import Users
from users.serializers import LoginSerializers, UsersSerializers
from kanvas_app.permissions import IsAdmim


class UsersView(APIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAdmim]
    
    def post(self,request:Request):

        serializer = UsersSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        found_user = Users.objects.filter(email=serializer.validated_data['email']).exists()

        if found_user:
            return Response({'message':'User already exists'},HTTP_422_UNPROCESSABLE_ENTITY)

        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        
        user = Users.objects.create(**serializer.validated_data)
        
        serializer = UsersSerializers(user)
        return Response(serializer.data,HTTP_201_CREATED)

    def get(self,request:Request):
        user:Users = request.user
        if user.is_anonymous:
            return Response({'detail': 'Authentication credentials were not provided.'},HTTP_401_UNAUTHORIZED)
        if not user.is_admin:
            return Response({"detail": "You do not have permission to perform this action."},HTTP_403_FORBIDDEN)
            
        serializer = UsersSerializers(Users.objects.all(),many=True)
        return Response(serializer.data,HTTP_200_OK)
    

class LoginView(APIView):
    def post(self,request:Request):

        serializer = LoginSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        user:Users = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({"detail": "unauthorized."},HTTP_401_UNAUTHORIZED)

        token,_ = Token.objects.get_or_create(user=user)

        return Response({'token':token.key},HTTP_200_OK)