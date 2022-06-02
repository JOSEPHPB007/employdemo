from django.urls import path
from employee import views
urlpatterns=[
path("index",views.LogineView.as_view()),
    path("register",views.RegistrationView.as_view())


]

