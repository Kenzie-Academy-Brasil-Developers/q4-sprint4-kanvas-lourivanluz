from django.urls import path
from users.views import Login_view, Users_View


urlpatterns = [
    path('accounts/',Users_View.as_view()),
    path('login/',Login_view.as_view()),
]