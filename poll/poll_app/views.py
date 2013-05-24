from django.views.generic.simple import direct_to_template
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from models import *
import datetime
# Create your views here.

def home(request):
    poll_entries = Poll.objects.order_by('poll_pub_date')
    return direct_to_template(request,'poll_app_templates/home.html',{'poll_entries':poll_entries})

def login_view(request):
    if request.method == "GET":
        return direct_to_template(request,'poll_app_templates/login.html',{})
    user = authenticate(username = request.POST['username'], password = request.POST['password'])
    if user is not None:
        login(request,user)
    else:
        return HttpResponse('Invalid login')
    return HttpResponseRedirect(reverse('home'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def add_poll(request):
    if request.method == "GET":
        return direct_to_template(request,'poll_app_templates/add_poll.html',{})
    else:
        poll = Poll()
        poll.poll_question = request.POST['poll_question']
        poll.poll_type = int(request.POST['poll_type'])
        poll.poll_creator = request.user
        poll.poll_pub_date = datetime.datetime.now().date()
        poll.save()
        return direct_to_template(request,'poll_app_templates/add_choice.html',{'poll':poll})

def view_poll(request,poll_id):
    poll = Poll.objects.get(id=poll_id)
    choices = Choice.objects.filter(poll=poll_id)
    return direct_to_template(request,'poll_app_templates/view_poll.html',{'poll':poll,'choices':choices})

@login_required
def add_choice(request,poll_id):
    choices = request.POST.getlist('choice')
    for each_choice in choices:
        choice = Choice()
        choice.poll = Poll.objects.get(id=poll_id)
        choice.poll_choice = str(each_choice)
        choice.save()
    return HttpResponseRedirect(reverse('home'))

@login_required
def vote(request):
   choice_ids = request.POST.getlist('vote')
   for choice_id in choice_ids:
       choice = Choice.objects.get(id=int(choice_id))
       choice.votes +=1
       choice.save()
   choices = Choice.objects.filter(poll=choice.poll)
   return direct_to_template(request,'poll_app_templates/result.html',{'poll':choice.poll,'choices':choices})

def delete_poll(request,poll_id):
    Choice.objects.filter(poll=poll_id).delete()
    Poll.objects.filter(id=poll_id).delete()
    return HttpResponseRedirect(reverse('home'))

