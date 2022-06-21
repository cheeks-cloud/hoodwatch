from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from neighborhood.forms import *
from users.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from neighborhood.models import *
from django.contrib.auth.models import User

# Create your views here.

@login_required
def home(request):
    b_form = CreateBusinessForm()
    h_form = HoodCreationForm()
    post_form = PostCreationForm()
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    current_user = User.objects.get(username=request.user.username)
    user_hood = current_user.profile.hood
    all_hoods = Neighborhood.objects.all()
    if user_hood:
        hood = Neighborhood.objects.get(hood_name=current_user.profile.hood.hood_name)
    else:
        hood = None
    posts = Post.objects.filter(hood=hood)
    businesses = Business.objects.filter(hood=hood)
    context = {
        'b_form': b_form,
        'h_form': h_form,
        'post_form': post_form,
        'u_form': u_form,
        'p_form': p_form,
        'current_user': current_user,
        'hood': hood,
        'posts': posts,
        'businesses': businesses,
        'all_hoods': all_hoods
    }
    return render(request, 'neighborhood/index.html', context)


@login_required
def single_post(request, post_id):
    b_form = CreateBusinessForm()
    h_form = HoodCreationForm()
    post_form = PostCreationForm()
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    current_user = User.objects.get(username=request.user.username)
    user_hood = current_user.profile.hood
    all_hoods = Neighborhood.objects.all()
    post = Post.objects.get(id=post_id)
    if user_hood:
        hood = Neighborhood.objects.get(hood_name=current_user.profile.hood.hood_name)
    else:
        hood = None
    businesses = Business.objects.filter(hood=hood)
    context = {
        'b_form': b_form,
        'h_form': h_form,
        'post_form': post_form,
        'u_form': u_form,
        'p_form': p_form,
        'current_user': current_user,
        'hood': hood,
        'businesses': businesses,
        'all_hoods': all_hoods,
        'post': post
    }
    return render(request, 'neighborhood/post.html', context)



@login_required
def search(request):
    post_form = PostCreationForm()
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
    current_user = User.objects.get(username=request.user.username)
    user_hood = current_user.profile.hood
    if user_hood:
        hood = Neighborhood.objects.get(hood_name=current_user.profile.hood.hood_name)
    else:
        hood = None
    posts = Post.objects.filter(hood=hood)
    context = {
        'post_form': post_form,
        'u_form': u_form,
        'p_form': p_form,
        'current_user': current_user,
        'hood': hood,
        'posts': posts
    }
    if request.method == 'POST':
        results = Business.objects.filter(business_name__icontains = request.POST.get('search'))
        if results:
            all_results = {'search_results': results}
        else:
            all_results = {'search_results': None}
        context.update(all_results)
        return render(request, 'neighborhood/search.html', context)



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
            current_user.profile.hood = new_hood
            new_hood.save()
            current_user.save()
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


@login_required
def join_hood(request):
    current_user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        if request.POST.get('hood-pick'):
            hood = Neighborhood.objects.get(hood_name=request.POST.get('hood-pick'))
            if current_user.profile.hood == hood:
                messages.success(request, f'You are already a part of this Neighborhood')
                return redirect('neighborhood-home')
            else:
                current_user.profile.hood = hood
                hood.occupants += 1
                hood.save()
                current_user.save()
                messages.success(request, f'Success! You have joined the {hood.hood_name} Neighborhood')
                return redirect('neighborhood-home')
        else:
            messages.warning(request, 'Something went wrong! Retry')
            return redirect('neighborhood-home')
    else:
        return redirect('neighborhood-home')