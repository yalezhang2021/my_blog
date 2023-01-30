from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm

def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            #.cleaned_data 清洗出合法数据
            data = user_login_form.cleaned_data
            # check accound, passwort is correct patch some users in database or not
            # if patch, return this user
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                # save user data in session, this is login action
                login(request, user)
                return redirect("article:article_list")
            else:
                return HttpResponse("账号或密码输入有误，请重新输入。")
        else:
            return HttpResponse("账号或密码输入不合法。")
    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form }
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据。")

def user_logout(request):
    logout(request)
    return redirect("article:article_list")
    
