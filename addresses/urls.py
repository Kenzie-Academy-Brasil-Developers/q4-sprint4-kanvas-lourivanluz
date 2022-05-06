from rest_framework.urls import path


from addresses.views import AdressView

urlpatterns = [
    path('address/',AdressView.as_view())
]