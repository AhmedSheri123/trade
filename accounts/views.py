from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect('index')
        
    return render(request, 'accounts/signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        users = User.objects.filter()
        if not users.filter(username=username).exists():
            if password == password2:
                user = users.create(username=username)
                user.set_password(password)
                user.save()
                return redirect('signin')
            else: messages.error(request, 'كلمة المرور غير متطابقة')
        else: messages.error(request, 'اختر اسم مستخدم اخر')

    return render(request, 'accounts/signup.html')