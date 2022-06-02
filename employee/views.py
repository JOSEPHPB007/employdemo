from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

# function based views
# class based views

# def index(request):
#     return HttpResponse("<h1> hello world </h1>")
#
# def login(request):
#     print(",,,,,,,,,,,,,,,,,,,",request)
#     return render(request,"login.html")
#
# def registraion(request):
#     return render(request,"reg.html")
#

class LogineView(View):

    def get(self,request):
        return render(request,"login.html")
    def post(self,request):
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd"))
        return render(request,"login.html")

class RegistrationView(View):

    def get(self,request):
        return render(request,"reg.html")
    def post(self,request):
        print(request.POST.get("fn_name"))
        print(request.POST.get("l_name"))
        print(request.POST.get("e_mail"))
        print(request.POST.get("pwd"))
        print(request.POST.get("u_name"))


        return render(request,"reg.html")



