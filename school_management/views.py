from django.shortcuts import render, redirect, HttpResponse
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser

def Base(request):
    return render(request, 'base.html')

def user_login(request):
    return render(request, 'login.html')

def doLogin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request,
                                         username = request.POST.get('email'),
                                         password = request.POST.get('password'))
        if user!=None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('hod_home')
            elif user_type == '2':
                return redirect('staff_home')
            elif user_type == '3':
                return HttpResponse('This is Student User')
            else:
                messages.error(request, 'Email and Password are invalid!')
                return redirect('login')
            
        else:
            messages.error(request, 'Email and Password are invalid!')
            return redirect('login')
        
def doLogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/')
def Profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        'user' : user,
    }
    return render(request, 'profile.html', context)

@login_required(login_url='/')
def ProfileUpdate(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(profile_pic, first_name, last_name, email, username, password)

        try:
            customuser = CustomUser.objects.get(id = request.user.id)
          
            customuser.first_name = first_name
            customuser.last_name = last_name
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
            customuser.save()
            if password != None and password != "":
                customuser.set_password(password)
            customuser.save()
            messages.success(request, "Profile updated successfully")
            return redirect('profile')
        except:
            messages.error(request, "Failed to update profile")

    return render(request, 'profile.html')

                