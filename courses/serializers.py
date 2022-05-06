from rest_framework import serializers


class Courses_serializers(serializers.Serializer):
    
    course_uuid     = serializers.CharField(read_only=True)
    name            = serializers.CharField()
    demo_time       = serializers.TimeField()
    created_at      = serializers.DateTimeField()
    link_repo       = serializers.CharField()