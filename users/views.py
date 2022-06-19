from django.shortcuts import render, redirect
from .forms import UserSignupForm
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
            return render(request, 'users/signup.html', context)
    else:
        return render(request, 'users/signup.html', context)



@login_required
def update(request, user_id):
    pass