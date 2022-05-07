from django.db import IntegrityError
from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY
    )


from courses.models import Courses
from courses.serializers import CoursesSerializers, CoursesSerializerPutStudents, CoursesSerializersForPath,CoursesSerializersPutInstructor
from users.models import Users
from kanvas_app.permissions import IsAdmim

class Courses_view(APIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAdmim]

    def get(self,_:Request):
        serializer = CoursesSerializers(Courses.objects.all(),many=True)
        return Response(serializer.data,HTTP_200_OK)

    def post(self,request:Request):
        user:Users = request.user
        if user.is_anonymous:
            return Response({'detail': 'Authentication credentials were not provided.'},HTTP_401_UNAUTHORIZED)
        if not user.is_admin:
            return Response({"detail": "You do not have permission to perform this action."},HTTP_403_FORBIDDEN)
        try:
            serializer = CoursesSerializers(data=request.data)
            serializer.is_valid(raise_exception=True)
            course:Courses = Courses.objects.create(**serializer.validated_data)
            serializer = CoursesSerializers(course)

            return Response(serializer.data,HTTP_201_CREATED)
        except IntegrityError:
            return Response({'message': 'Course already exists'},HTTP_422_UNPROCESSABLE_ENTITY)

    def put(self,request:Request,course_id):
        user:Users = request.user
        if user.is_anonymous:
            return Response({'detail': 'Authentication credentials were not provided.'},HTTP_401_UNAUTHORIZED)
        if not user.is_admin:
            return Response({"detail": "You do not have permission to perform this action."},HTTP_403_FORBIDDEN)
        
        course:Courses = Courses.objects.filter(uuid=course_id).first()
        if not course:
            return Response({'message': 'Course does not exist'},HTTP_404_NOT_FOUND)
    
        serializer = CoursesSerializersPutInstructor(data=request.data)
        serializer.is_valid(raise_exception=True)

        instructor:Users = Users.objects.filter(uuid=serializer.validated_data['instructor_id']).first()
        if not instructor:
            return Response({"message": "Invalid instructor_id"},HTTP_404_NOT_FOUND)
        if not instructor.is_admin:
            return Response({"message": "Instructor id does not belong to an admin"},HTTP_422_UNPROCESSABLE_ENTITY)
        
        old_course:Courses = Courses.objects.filter(instructor_id=instructor.uuid).first()
        if old_course:
            old_course.instructor = None
            old_course.save()
        course.instructor = instructor
        course.save()

        serializer = CoursesSerializers(course)
        return Response(serializer.data,HTTP_200_OK)

    
class CursesViewPutStudents(APIView):
    authentication_classes = [TokenAuthentication]
    permissions_classes = [IsAdmim]

    def get(self,_:Request,course_id):
        try:
            course:Courses = Courses.objects.filter(uuid=course_id).first()   
            if course: 
                serializer = CoursesSerializers(course)
                return Response(serializer.data,HTTP_200_OK)
            return Response({'message': 'Course does not exist'},HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({'message': 'Course does not exist'},HTTP_404_NOT_FOUND)

    def put(self,request:Request,course_id):

        user:Users = request.user
        if user.is_anonymous:
            return Response({'detail': 'Authentication credentials were not provided.'},HTTP_401_UNAUTHORIZED)
        if not user.is_admin:
            return Response({"detail": "You do not have permission to perform this action."},HTTP_403_FORBIDDEN)
        
        course:Courses = Courses.objects.filter(uuid=course_id).first()
        if not course:
            return Response({"message": 'Course does not exist'},HTTP_404_NOT_FOUND)

        serializer = CoursesSerializerPutStudents(data=request.data)
        serializer.is_valid(raise_exception=True)

        for uuid in serializer.validated_data['students_id']:
            
            student:Users = Users.objects.filter(uuid=uuid).first()
            if not student:
                return Response({"message": "Invalid students_id list"},HTTP_404_NOT_FOUND)
            if student.is_admin:
                return Response({"message": "Some student id belongs to an Instructor"},HTTP_422_UNPROCESSABLE_ENTITY)
            else:

                course.students.add(student)
                course.save()
            serializer = CoursesSerializers(course)

        return Response(serializer.data)

    
    def patch(self,request:Request,course_id):
        user:Users = request.user
        if user.is_anonymous:
            return Response({'detail': 'Authentication credentials were not provided.'},HTTP_401_UNAUTHORIZED)
        if not user.is_admin:
            return Response({"detail": "You do not have permission to perform this action."},HTTP_403_FORBIDDEN)
        
        try:
            course = Courses.objects.filter(uuid=course_id)
            if not course.first():
                return Response({"message": 'Course does not exist'},HTTP_404_NOT_FOUND)

            serializer = CoursesSerializersForPath(request.data)
            course.update(**serializer.data)
            serializer = CoursesSerializers(course.first())

            return Response(serializer.data,HTTP_200_OK)
        except IntegrityError:
            return Response({'message': 'This course name already exists'},HTTP_422_UNPROCESSABLE_ENTITY)
            
    def delete(self,request:Request,course_id):
        user:Users = request.user
        if user.is_anonymous:
            return Response({'detail': 'Authentication credentials were not provided.'},HTTP_401_UNAUTHORIZED)
        if not user.is_admin:
            return Response({"detail": "You do not have permission to perform this action."},HTTP_403_FORBIDDEN)
        
        course = Courses.objects.filter(uuid=course_id)
        if not course.first():
            return Response({"message": 'Course does not exist'},HTTP_404_NOT_FOUND)

        course.delete()
        
        return Response('',HTTP_204_NO_CONTENT)

        
