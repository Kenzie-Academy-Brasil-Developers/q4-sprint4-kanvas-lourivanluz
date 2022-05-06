from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK,HTTP_409_CONFLICT,HTTP_404_NOT_FOUND,HTTP_201_CREATED
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


from users.models import Users
from users.serializers import Login_serializers, Users_serializers


class Users_View(APIView):

    def post(self,request:Request):

        serializer = Users_serializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        found_user = Users.objects.filter(email=serializer.validated_data['email']).exists()

        if found_user:
            return Response({'message':'User already exists'},HTTP_409_CONFLICT)

        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        
        
        user = Users.objects.create(**serializer.validated_data)
        

        serializer = Users_serializers(user)
        return Response(serializer.data,HTTP_201_CREATED)
    
    def get(self,_:Request):
        serializer = Users_serializers(Users.objects.all(),many=True)
        return Response(serializer.data,HTTP_200_OK)


class Login_view(APIView):
    def post(self,request:Request):

        serializer = Login_serializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        user:Users = authenticate(
            username=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({'msg':"nao achou o usuario"},HTTP_404_NOT_FOUND)

        
        token,_ = Token.objects.get_or_create(user=user)

        return Response({'token':token.key},HTTP_200_OK)