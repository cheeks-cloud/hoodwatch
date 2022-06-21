from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    form = UserSignupForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            form.save()
            messages.success(request, f"Thank you, {username}. Your accout has been successfuly created! Login to continue...")
            return redirect('users-signin')
        else:
            messages.warning(request, 'Something went wrong with the application')
            return render(request, 'users/signup.html', context)
    else:
        return render(request, 'users/signup.html', context)



@login_required
def update(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Success! Your accout has been successfuly updated!')
            return redirect('neighborhood-home')
        else:
            messages.warning(request, 'Failed! Your accout could not be updated!')
            return redirect('neighborhood-home')
    else:
        return redirect('neighborhood-home')