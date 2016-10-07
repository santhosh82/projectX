from django.shortcuts import render
from .forms import UserForm, TJobForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse,HttpResponseRedirect

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
        # get the usernames and passwords
        username  = request.POST.get('username')
        password  = request.POST.get('password')

        user  = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return  HttpResponseRedirect('JobTracker/index/')

            else:
                return HttpResponse("your account is not active")

        else:
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request,'JobTracker/login.html',{})
