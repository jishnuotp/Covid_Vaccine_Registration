from django.contrib import messages, auth
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Vaccine_Center, District, Person


# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Register is invalid')
            return redirect('login')
    return render(request,'Login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This username is already taken")
                return redirect('http://127.0.0.1:8000/Register/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This email is already taken")
                return redirect('http://127.0.0.1:8000/Register/register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                print("User Created")
        else:
            messages.info(request,"Password not matching")
            return redirect('http://127.0.0.1:8000/Register/register')
        return redirect('http://127.0.0.1:8000/Register/login')
    return render(request,'Registration.html')

def User_Details(request):
    User = get_user()
    form = PersonCreationForm(initial={'Created_by':User.id})
    return render(request,'User_Details.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('/')


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("User created")
            return redirect('http://127.0.0.1:8000/Register/user_details')
    return render(request, 'persons/home.html', {'form': form})

def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/home.html', {'form': form})

# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    center = Vaccine_Center.objects.filter(District_id=district_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'cities': center})




