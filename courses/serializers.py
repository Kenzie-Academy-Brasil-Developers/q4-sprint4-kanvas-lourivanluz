from rest_framework import serializers

from users.serializers import Users_serializers


class Courses_serializers(serializers.Serializer):
    
    uuid            = serializers.UUIDField(read_only=True)
    name            = serializers.CharField()
    demo_time       = serializers.TimeField()
    created_at      = serializers.DateTimeField(required=False)
    link_repo       = serializers.CharField()
    instructor      = Users_serializers(required=False)

    students        = Users_serializers(required=False,many=True)

class CoursesSerializersForPath(serializers.Serializer):
    name            = serializers.CharField(required=False)
    demo_time       = serializers.TimeField(required=False)
    link_repo       = serializers.CharField(required=False)


class CoursesSerializersPutInstructor(serializers.Serializer):
    
    instructor_id   = serializers.UUIDField()



class CoursesSerializerPutStudents(serializers.Serializer):
    
    students_id = serializers.ListField(child=serializers.UUIDField())
    