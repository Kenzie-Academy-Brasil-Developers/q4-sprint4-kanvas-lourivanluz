from courses.views import Courses_view,CursesViewPutStudents
from rest_framework.urls import path


urlpatterns = [
    path('courses/',Courses_view.as_view()),
    path('courses/<course_id>/registrations/instructor/',Courses_view.as_view()),
    path('courses/<course_id>/registrations/students/',CursesViewPutStudents.as_view()),
    path('courses/<course_id>/',CursesViewPutStudents.as_view()),
]