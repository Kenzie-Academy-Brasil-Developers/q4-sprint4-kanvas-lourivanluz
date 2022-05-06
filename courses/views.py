from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED
from courses.models import Courses

from courses.serializers import Courses_serializers, CoursesSerializerPutStudents, CoursesSerializersForPath,CoursesSerializersPutInstructor
from users.models import Users



class Courses_view(APIView):
    def get(self,_:Request):
        serializer = Courses_serializers(Courses.objects.all(),many=True)
        return Response(serializer.data,HTTP_200_OK)

    def post(self,request:Request):
        serializer = Courses_serializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        course:Courses = Courses.objects.create(**serializer.validated_data)
        serializer = Courses_serializers(course)

        return Response(serializer.data,HTTP_201_CREATED)
    
    def put(self,request:Request,course_id):
        try:
            course:Courses = Courses.objects.filter(uuid=course_id).first()
            if not course:
                raise ValidationError("Course does not exist")
        

            serializer = CoursesSerializersPutInstructor(data=request.data)
            serializer.is_valid(raise_exception=True)

            instructor:Users = Users.objects.filter(uuid=serializer.validated_data['instructor_id']).first()
            if not instructor:
                return Response({"message": "Invalid instructor_id"})
            if not instructor.is_admin:
                return Response({"message": "Instructor id does not belong to an admin"})

            course.instructor = instructor
            course.save()

            serializer = Courses_serializers(course)
            return Response(serializer.data,HTTP_200_OK)

        except ValidationError as err:
            return Response({"message": err})


class CursesViewPutStudents(APIView):

    def get(self,_:Request,course_id):
        try:
            course:Courses = Courses.objects.filter(uuid=course_id).first()    
            serializer = Courses_serializers(course)
            return Response(serializer.data,HTTP_200_OK)
        except ValidationError:
            return Response({"message":"Course does not exist"})

    def put(self,request:Request,course_id):

        try:
            course:Courses = Courses.objects.filter(uuid=course_id).first()
            if not course:
                raise ValidationError("Course does not exist")

            serializer = CoursesSerializerPutStudents(data=request.data)
            
            serializer.is_valid(raise_exception=True)

            for uuid in serializer.validated_data['students_id']:
                
                student:Users = Users.objects.filter(uuid=uuid).first()
                if not student:
                    return Response({"message": "Invalid students_id list"})
                if student.is_admin:
                    return Response({"message": "Some student id belongs to an Instructor"})
                else:

                    course.students.add(student)
                    course.save()
                serializer = Courses_serializers(course)

            return Response(serializer.data)
        except ValidationError as err:
            return Response({"message": err})
    
    def patch(self,request:Request,course_id):
        try:
            course = Courses.objects.filter(uuid=course_id)
            if not course.first():
                raise ValidationError("Course does not exist")

            serializer = CoursesSerializersForPath(request.data)
            course.update(**serializer.data)
            serializer = Courses_serializers(course.first())

            return Response(serializer.data,HTTP_200_OK)
            

        except ValidationError as err:
            return Response({"message": err})

        
