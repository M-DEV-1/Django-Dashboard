from django.shortcuts import render, redirect

# Create your views here.
from .forms import RegisterUser, LoginUser, CreateRecord, UpdateRecord

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from .models import studentrecord

from django.contrib import messages

# - HomePage
def home(request):
    
    # return HttpResponse('hello world')
    return render(request, 'dashboard/index.html')

# - Register new user
 
def register(request):
    
    form = RegisterUser()
    
    if request.method == "POST":
        
        form = RegisterUser(request.POST)
        
        if form.is_valid():
            
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('login')
    
    context = {'form':form}
    
    return render(request, 'dashboard/register.html', context=context)

# - Login User

def login(request):
    form = LoginUser()
    
    if request.method=="POST":
        
        form = LoginUser(request, data=request.POST)
        
        if form.is_valid():
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request,user)
                return redirect('dashboard')
                
    context = {'form2':form}
    return render(request, 'dashboard/login.html', context=context)

# - Dashboard
@login_required(login_url='login')
def dashboard(request):
    
    therecords = studentrecord.objects.all()
    
    context = {'records': therecords}
    
    return render(request, 'dashboard/dashboard.html', context=context)
    
# - Create a record
@login_required(login_url='login')
def create_record(request):
    
    form = CreateRecord()
    
    if request.method == "POST":
         
         form = CreateRecord(request.POST)
         
         if form.is_valid():
             
             form.save()
             messages.success(request, "Record Created")
             return redirect('dashboard')
    
    context = {'form':form}
    return render(request, 'dashboard/create-record.html', context=context)
    
# - Update Record

@login_required(login_url='login')
def update_record(request, pk):
    record = studentrecord.objects.get(id=pk)
    
    form = UpdateRecord(request.POST, instance=record)
    if form.is_valid():
        form.save()  
        messages.success(request, "Update Sucessful")
        return redirect('dashboard')
    
    context = {'form':form}
    return render(request, 'dashboard/update-record.html', context=context)

# - View a particular record
@login_required(login_url='login')
def view_record(request,pk):
    
    all_records = studentrecord.objects.get(id=pk)
    
    context={'record':all_records}
    return render(request, 'dashboard/view-record.html', context=context)
    
# - Delete Record

@login_required(login_url='login')
def delete_record(request,pk):
    record = studentrecord.objects.get(id=pk)
    
    record.delete()
    
    return redirect('dashboard')

# - Logout User

def logout(request):
    auth.logout(request)
    return redirect("login")
    