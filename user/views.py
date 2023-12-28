from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django import forms


class LoginForm(View):
    def get(self,request,*args,**kwargs):
      return render(request,'login.html')
    


    def post(self,request,*args,**kwargs):
     pass       

class RegisterForm(View):
    

    def get(self,request,*args,**kwargs):
      return render(request,'register.html')
    


    def post(self,request,*args,**kwargs):
      pass
def logOut(request):
  logout(request)
  return redirect('homepage')         
