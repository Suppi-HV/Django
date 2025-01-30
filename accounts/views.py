# from django.shortcuts import render,redirect
# # from django.contrib.auth.models import user,auth
# from django.contrib.auth.models import User
# from django.contrib import auth
# from django.contrib import messages


# # Create your views here.
# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']

#         user=auth.authenticate(username=username,password=password)

#         if user is not None:
#             auth.login(request,user)
#             return redirect("/")
#         else:
#             messages.info(request,'invalid credentials')
#             return redirect("login")
#     else:
#         return render(request,'login.html')

# def register(request):
#     if request.method=='POST':
#         first_name=request.POST['first_name']
#         last_name=request.POST['first_name']
#         username=request.POST['username']
#         password1=request.POST['password1']
#         password2=request.POST['password2']
#         email=request.POST['email']
    
#         if password1==password2:
#             if User.objects.filter(username=username).exists():
#                # print("Username taken")
#                messages.info(request,'Username Taken')
#                return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'Email Taken')
#                 return redirect('register')
#                 #print('email taken')

#             else:    
#                 user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
#                 user.save();
#                 #print('user created')
#                 return redirect('login')
                
#         else:
#           # print('password not matching')
#           messages.info(request,'password not matching..')
#           return redirect('register')
#         return redirect('/')# going back to home page
#     else:
#          return render(request,'register.html')
    
# def logout(request):
#     auth.logout(request)
#     return redirect('/')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
import re

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid credentials')
            return redirect("login")
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # Allowed email domains
        allowed_domains = ["yahoo.com", "email.com", "mnkgcs.com"]

        # Extract domain from email
        match = re.search(r'@([a-zA-Z0-9.-]+)', email)
        email_domain = match.group(1) if match else None

        if not email_domain or email_domain not in allowed_domains:
            messages.error(request, "Please use an email from Yahoo, Email.com, or Mnkgcs.")
            return redirect('register')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:    
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "Registration successful! You can now log in.")
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')

    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
