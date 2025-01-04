from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
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
    return render(request, 'home.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, "Succefully logout")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})




