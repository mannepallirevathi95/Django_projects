from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    # req method is post i.e., signup operation
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        # after the form created as per the req, now  it is to be validated
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect ('login')
    else:
       # form = UserCreationForm()
        form = RegisterForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')