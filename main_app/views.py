from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Icon, User_Sneaker



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

def index(request):
    icons = Icon.objects.all() #get all icons from DB
    return render(request, 'icons/index.html', {
        'icons': icons
    })

def user_index(request):
    user_sneakers = User_Sneaker.objects.all() #get all icons from DB
    return render(request, 'user_sneakers/user_index.html', {
        'user_sneakers': user_sneakers
    })

# detail pages for each model

def icons_detail(request, icon_id):
  icon = Icon.objects.get(id=icon_id)
  return render(request, 'icons/detail.html', { 'icon': icon })

def user_detail(request, user_sneaker_id):
  user_sneaker = User_Sneaker.objects.get(id=user_sneaker_id)
  return render(request, 'user_sneakers/user_detail.html', { 'user_sneaker': user_sneaker })

#User CRUD for their sneaker collection

class UserCreate(CreateView):
  model = User_Sneaker
  fields = '__all__'
# redirect after form is completed
#   success_url = '/user_sneakers/{user_sneaker_id}'

class UserUpdate(UpdateView):
  model = User_Sneaker
  fields = '__all__'

class UserDelete(DeleteView):
  model = User_Sneaker
  success_url = '/user_sneakers'