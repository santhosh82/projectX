from django.shortcuts import render
from .forms import UserForm, TJobForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from .models import TJob,User,JobShareTable
from django.views.generic import View



# Create your views here.

@login_required
def index(request):
    print("JobTracker: views.py in index()")
    return render(request, "JobTracker/index.html")



@login_required
def addJob(request):
    print("in the add job")
    try:
        profile = request.user

    except User.DoesNotExist:

        profile = User(user=request.user)


    if request.method == 'POST':
        print("In the form condition")

        # creating partial author form
        form = TJobForm(request.POST)

        if form.is_valid():
            print("form is valid")

            # Now commit to False
            temp = form.save(commit=False)

            # add user value to the object
            # if not working, set using queires
            temp.user = request.user
            temp.save()
            return index(request)
        else:
            print(form.username)
    else:
        form = TJobForm()
        #form.user = request.user

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username is ", username)
        print("pass is ", password)

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                print("just before the redirecting")
                login(request, user)
                print("The user got login but not redirected")
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("your account is not active")

        else:
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request,'JobTracker/login.html',{})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def welcome(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    user_form = UserForm()
    return render(request, 'JobTracker/welcome.html', {'user_form': user_form})


@login_required
def user_logout(request):
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('welcome'))




@login_required
def jobs_list(request):
    jobs = TJob.objects.filter(user_id=request.user)
    return render(request, 'JobTracker/_jobs_list.html', {'jobs': jobs})

#views which displays the list of jobs you have
    # def jobs_shared_list(request):
    #     jobs = JobShareTable.objects.all().filter(jobId = request.user.id)
    #     return render(request, 'JobTracker/_jobs_shared_list.html', {'jobs': jobs})