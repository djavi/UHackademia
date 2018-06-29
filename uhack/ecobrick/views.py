from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponseRedirect,redirect,HttpResponse, reverse, get_object_or_404, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.views import generic
from .models import *
from .forms import *

import datetime
# import timezone
#LOGIN
def login_view(request):
    title = "Login"
    form = login(request.POST or None)
    context = {}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request,user)

        return redirect(reverse('client-panel', kwargs={'pk':request.user.pk}))

    if User.DoesNotExist:
        context['log_error'] = "Cannot find an account with that combination"


    return render(request, "login.html",{"form":form, "title": title}, context)

#HOME
class HomeView(generic.View):
    template_name = 'navbar.html'

    #display blank form
    def get(self, request):
        return render(request, self.template_name)
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
    title = "Staff page"

    if request.method == "POST":
        if userId in request.POST:
            if numEcobrick in request.POST:
                print("hello")
                return render(request,'admin.html',{'title':title,'success':"Eco brick successfully added"})

    return render(request,'admin.html',{'title':title})