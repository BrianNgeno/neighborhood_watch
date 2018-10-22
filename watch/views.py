from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from .models import Profile,User,Post,Business,NeighborHood,Post
from django.contrib.auth.models import User
import datetime as dt
from .forms import BusinessForm,ProfileForm,HoodForm

# Create your views here.

def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day
    '''
    return render for home page
    '''
def home_page(request):
    date = dt.date.today()
    hoods = NeighborHood.objects.all()
    return render(request,'home.html',locals())

def logout(request):
    return render(request, 'home.html')

'''
    editing user profile fillform & submission
 
    '''
@login_required(login_url='/accounts/login/')
def edit(request):
    profile = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/edit_profile.html', locals())

@login_required(login_url='/accounts/login')
def upload_business(request):
    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            upload = businessform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('home_page')
    else:
        businessform = BusinessForm()
    return render(request,'Business.html',locals())

@login_required(login_url='/accounts/login')
def add_hood(request):
    if request.method == 'POST':
        hoodform = HoodForm(request.POST, request.FILES)
        if hoodform.is_valid():
            upload = hoodform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('home_page')
    else:
        hoodform = HoodForm()
    return render(request,'add-hood.html',locals())

@login_required(login_url = '/accounts/login')
def all_hoods(request):

   if request.user.is_authenticated:
       if Join.objects.filter(user_id=request.user).exists():
           hood = Neighbourhood.objects.get(pk=request.user.join.hood_id.id)
           businesses = Business.objects.filter(hood=request.user.join.hood_id.id)
        #    posts = Post.objects.filter(hood=request.user.join.hood_id.id)
           print(posts)
           return render(request, "hood.html", locals())
       else:
           neighbourhoods = Neighbourhood.objects.all()
           return render(request, 'hood.html', locals())
   else:
       neighbourhoods = Neighbourhood.objects.all()

       return render(request, 'hood.html', locals())
    

@login_required(login_url='/accounts/login')
def join(request,neighborhood_id):
    hood = NeighborHood.objects.get(id=neighborhood_id)
    current_user = request.user
    current_user.profile.neighborhood = hood
    current_user.profile.save()
    return redirect('')

@login_required(login_url='/accounts/login')
def leave(request,neighborhood_id):
    current_user = request.user
    current_user.profile.neighborhood = None
    current_user.profile.save()
    return redirect('home_page')

def single_hoods(request,neighborhood_id):
    hood = NeighborHood.objects.get(pk="neighborhood_id")
    return render(request,'hood.html', locals())