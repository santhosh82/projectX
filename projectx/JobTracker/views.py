from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.cache import cache_control
from .models import TJob,User,JobShareTable,FriendsTable
from django.views.generic import View
from datetime import datetime
import json


from .forms import UserForm, TJobForm
from .models import TJob


# Create your views here.

@login_required
def index(request):
    print("JobTracker: views.py in index()")
    #return render(request, "JobTracker/index.html")
    return HttpResponseRedirect(reverse('welcome'))


@login_required
def addJob(request):

    if request.method == "GET":
        print("I am here in the get method")
    if request.method == 'POST':

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
            print("job id is ", temp.id)
            return index(request)
        else:
            print(form.errors)
    else:
        form = TJobForm()
    return render(request, 'JobTracker/_create_job.html', {'form': form})

@login_required
def editJob(request, myId):
    print("view edit job")
    myJob = TJob.objects.get(id=myId)
    print("job is ",myJob)
    print("id is ",myId)
    if request.method == "POST":
        print("view edit job post ")
        form = TJobForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.id  = myId
            temp.user = request.user
            temp.save()
            return index(request)
    else:
        form = TJobForm(instance=myJob)

    return render(request,'JobTracker/_edit_job.html',{'form':form,'myId':myId})




@login_required
def deleteJob(request, id):
    print("In the delete job view")
    TJob.objects.get(id=id).delete()
    return jobs_list(request)

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
        return render(request, 'JobTracker/login.html', {})

def about(request):
    return render(request, 'JobTracker/_about.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def welcome(request):
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

def dummy(request):
    pass

def san_portfolio(request):
    return  render(request,'JobTracker/san_portfolio.html')


def add_friends(request):
    return  render(request,'JobTracker/add_friends.html')



def share_job(request,myId):
    print("In the share view with id ",myId)

    return render(request,"JobTracker/share.html",{"id":myId})

def add_job_share(request):
    print("In the add job share view")

    friendName = request.GET['name']
    jobId = request.GET['id']

    # add a row into job share table

    temp =  JobShareTable()

    temp.fromUserId  = request.user
    temp.toUserId = User.objects.all().get(username=friendName)
    temp.jobId = TJob.objects.all().get(id = jobId)

    temp.save()

    results = {"result": "success"}
    data  = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
    #return HttpResponseRedirect(reverse("index"))




def get_users(request,partialName):
    allUsers = User.objects.all()
    results = []

    for u in allUsers:
        data_json = {}
        if partialName in u.username and u.username != request.user.username:
            data_json['name'] = u.username
            results.append(data_json)
    data = json.dumps(results)
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

@login_required
def make_friends(request):
    print("In the make friends")
    print ("one of the parameter is ",request.GET)

    friendName = request.GET['name']
    reltype = request.GET['type']


    # Now create an row in FriendsTable
    user1 = request.user
    user2 = User.objects.all().get(username=friendName)

    f = FriendsTable()
    if user1.id  < user2 .id :
        f.user_first_id = user1
        f.user_second_id = user2
        f.reltype = reltype +"2"
    else:
        f.user_first_id = user2
        f.user_second_id = user1
        f.reltype = reltype + "1"
    f.save()



    data = {"name" : "santhosh"}
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def get_shared_list(request):
    # from the job shared table return all the jobId he is shared with

    sharedJobs = []

    temp = JobShareTable.objects.filter(toUserId = request.user).values('jobId')

    for k in temp:
        sharedJobs.append(TJob.objects.get(id = k['jobId']))

    return render(request, 'JobTracker/jobs_shared_list.html',{"jobs":sharedJobs})