from django.shortcuts import render
from .forms import UserForm, TJobForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    print("JobTracker: views.py in index()")
    return render(request, "JobTracker/index.html")


def addJob(request):
    if request.method == 'POST':
        form = TJobForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print(form.errors)
    else:
        form = TJobForm()

    return render(request, 'JobTracker/_create_job.html', {'form': form})


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # save the user's form to database
            user = user_form.save()

            # we hash the password with the set_password method
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request, 'JobTracker/register.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == "POST":
        print("user login post")
        # get the usernames and passwords
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        print("username is ",username)
        print("pass is ",password)

        user  = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                print("just before the redirecting")
                login(request,user)
                print("The user got login but not redirected")
                return  HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("your account is not active")

        else:
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request,'JobTracker/login.html',{})

def welcome(request):
    user_form = UserForm()

    return render(request, 'JobTracker/welcome.html', {'user_form': user_form})
@login_required
def user_logout(request):
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('welcome'))



