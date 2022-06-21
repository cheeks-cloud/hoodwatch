from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from neighborhood.forms import *
from django.contrib import messages
from neighborhood.models import *
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    b_form = CreateBusinessForm()
    h_form = HoodCreationForm()
    post_form = PostCreationForm()
    context = {
        'b_form': b_form,
        'h_form': h_form,
        'post_form': post_form
    }
    return render(request, 'neighborhood/index.html', context)


@login_required
def create_business(request):
    b_form = CreateBusinessForm()
    current_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        b_form = CreateBusinessForm(request.POST)
        if b_form.is_valid():
            new_business = Business.objects.create(
                user = current_user, 
                hood = current_user.profile.hood, 
                business_name = b_form.cleaned_data.get('business_name'),
                email = b_form.cleaned_data.get('email')
            )
            new_business.save()
            messages.success(request, 'Success! You new business has been created!')
            return redirect('neighborhood-home')
        else:
            messages.warning(request, 'Failed! Your new business could not be created!')
            return redirect('neighborhood-home')
    else:
        return redirect('neighborhood-home', )



@login_required
def create_hood(request):
    h_form = HoodCreationForm()
    current_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        h_form = HoodCreationForm(request.POST)
        if h_form.is_valid():
            new_hood = Neighborhood.objects.create(
                hood_name = h_form.cleaned_data.get('hood_name'),
                location = h_form.cleaned_data.get('location'),
                admin = current_user
            )
            new_hood.save()
            messages.success(request, 'Success! You have created a new hood!')
            return redirect('neighborhood-home')
        else:
            messages.warning(request, 'Failed! The new hood could not be created')
            return redirect('neighborhood-home')
    else:
        return redirect('neighborhood-home')
        

@login_required
def create_post(request):
    post_form = PostCreationForm()
    current_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        post_form = PostCreationForm(request.POST, request.FILES)
        if post_form.is_valid():
            new_post = Post.objects.create(
                title = post_form.cleaned_data.get('title'),
                image = post_form.cleaned_data.get('image'),
                content = post_form.cleaned_data.get('content'),
                user = current_user,
                hood = current_user.profile.hood
            )
            new_post.save()
            messages.success(request, 'Success! You have created a Post!')
            return redirect('neighborhood-home')
        else:
            messages.warning(request, 'Failed! The new Post could not be created!')
            return redirect('neighborhood-home')
    else:
        return redirect('neighborhood-home')