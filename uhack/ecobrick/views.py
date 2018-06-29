from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect,redirect,HttpResponse, reverse, get_object_or_404, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.views import generic
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import datetime
# import timezone
#LOGIN
def login_view(request):
    title = "Login"
    form = login(request.POST or None)
    context = {"form":form, "title": title}

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request,user)

            if request.user.is_authenticated: 
                return redirect("home.html")
            else:
                context['log_error'] = "Cannot find an account with that combination"


    return render(request, "login.html", context)

#HOME
class HomeView(generic.View):
    template_name = 'navbar.html'

    #display blank form
    def get(self, request):
        return render(request, self.template_name)

class RewardsView(generic.View):
    rewards = Reward.objects.all()
    template_name = 'rewards.html'
    context={}
    #display blank form
    def get(self, request):
        return render(request, self.template_name, {"rewards": self.rewards})
#REGISTER
# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         form2 = UserDetailsForm(request.POST)
#         if form.is_valid() and form2.is_valid():
#             user = form.save(commit=False)
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#
#             try:
#                 validate_password(password,email)
#             except ValidationError as e:
#                 form.add_error('password',e)
#                 return render(request, 'leverageapp/register_bs4.html',{'form':form,'form2':form2})
#
#             user.set_password(password)
#             user.save()
#             #user.groups.add(Group.objects.get(name='Client'))
#
#
#             user_details = form2.save(commit=False)
#             user_details.user = user
#             user_details.save()
#
#             return HttpResponse('WELCOME TO LEVERAGE')
#     else:
#         form = UserForm()
#         form2 = UserDetailsForm()
#     return render(request, 'leverageapp/register_bs4.html', {'form': form, 'form2':form2})

#LOGOUT
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def staff_view(request):
    all_users = UserDetail.objects.all()
    title = "Staff page"
    success = ""

    if request.method == "POST":
        if "userId" in request.POST:
            if "numEcobrick" in request.POST:
                uid = request.POST.get("userId")
                num = request.POST.get("numEcobrick")
                weight = request.POST.get("weightEco")

                user = get_object_or_404(User,id=uid)
                user2 = get_object_or_404(UserDetail,user=user)

                user2.brickNum = user2.brickNum + int(num)
                user2.brickWeight = user2.brickWeight + int(weight)
                user2.save()
                    
                return render(request,'admin.html',{'title':title,'success':"Eco brick successfully added"})

    return render(request,'admin.html',{'title':title,'success':success})