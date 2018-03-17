from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Example.Example2.bookmarks.account.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], passwoed = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authentication succeeded ! :)')
                else:
                    return HttpResponse('Account is blocked! :(')
            else:
                return HttpResponse('Incorrect data! :(')
    else:
        form = LoginForm()
    return render(request,'account/login.html',{'form': form})
