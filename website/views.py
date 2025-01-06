from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import User
from .forms import add_record_form


# Create your views here.
def home(request):
    records = User.objects.all()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')  # Replace 'home' with the name of the view you'd like to redirect to.
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return render(request, 'home.html', {})  # Render the form again with the error message.

    # For GET requests or any other method, render the form.
    return render(request, 'home.html', {'records' : records})



def logout_user(request):
    logout(request)
    messages.success(request, "Succefully logout")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully registered")
                return redirect('home')
            else:
                messages.error(request, "Authentication failed after registration.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def User_Record(request, pk):
    if request.user.is_authenticated:
        # Get the record
        UserRecord = User.objects.get(pk=pk)
        return render(request, 'User.html', {'UserRecord': UserRecord})
    else:
        messages.error(request, "You must be logged in to view this page.")
        return redirect('home')
    
def delete_user(request, pk):
    if request.user.is_authenticated:
        # Get the record
        UserRecord = User.objects.get(pk=pk)
        UserRecord.delete()
        messages.success(request, "User deleted.")
        return redirect('home')
    else:
        messages.error(request, "You must be logged in to delete a user.")
        return redirect('home')
    
def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = add_record_form(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                username = form.cleaned_data.get('username')
                city = form.cleaned_data.get('city')
                state = form.cleaned_data.get('state')
                email = form.cleaned_data.get('email')
                phone = form.cleaned_data.get('phone')
                address = form.cleaned_data.get('address')
                zip_code = form.cleaned_data.get('zip_code')
                country = form.cleaned_data.get('country')
                User.objects.create(username = username, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code, country=country)
                messages.success(request, "Record added.")
                return redirect('home')
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = add_record_form()
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, "You must be logged in to add a record.")
        return redirect('home')

def edit_record(request, pk):  
    if request.user.is_authenticated:
        # Get the record
        UserRecord = User.objects.get(pk=pk)
        if request.method == 'POST':
            form = add_record_form(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                username = form.cleaned_data.get('username')
                city = form.cleaned_data.get('city')
                state = form.cleaned_data.get('state')
                email = form.cleaned_data.get('email')
                phone = form.cleaned_data.get('phone')
                address = form.cleaned_data.get('address')
                zip_code = form.cleaned_data.get('zip_code')
                country = form.cleaned_data.get('country')
                UserRecord.first_name = first_name
                UserRecord.last_name = last_name
                UserRecord.username = username
                UserRecord.city = city
                UserRecord.state = state
                UserRecord.email = email
                UserRecord.phone = phone
                UserRecord.address = address
                UserRecord.zip_code = zip_code
                UserRecord.country = country
                UserRecord.save()
                messages.success(request, "Record updated.")
                return redirect('home')
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = add_record_form()
        return render(request, 'edit_record.html', {'form': form, 'UserRecord': UserRecord})
    else:
        messages.error(request, "You must be logged in to edit a record.")
        return redirect('home')