from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_Login.forms import SignUpForms,  UserProfileChange, ProfileImg
def sign_up(request):
    form = SignUpForms()
    registered = False   # initially it is set to false, once form is filled user is registered
    if request.method == 'POST':
        form = SignUpForms(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form, 'registered':registered}
    return render(request, 'App_Login/signup.html', context=dict)
def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index')) # means if right credentials it will let you to home page
    return render(request, 'App_Login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:signin'))
@login_required
def profile(request):
    return render(request,'App_Login/profile.html', context={})


@login_required
def user_change(request):
    current_user = request.user
    form =  UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form =  UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form =  UserProfileChange(instance=current_user)
    return render(request, 'App_Login/change_profile.html', context={'form':form})

@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form =  PasswordChangeForm(current_user)
    if request.method == 'POST':
        form =  PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    return render(request, 'App_Login/pass_change.html', context={'form':form, 'changed':changed})


@login_required
def add_pro_img(request):
    form = ProfileImg()
    if request.method == 'POST':
        form = ProfileImg(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/pro_img_add.html', context={'form' : form})




@login_required
def change_pro_img(request):
    form = ProfileImg(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfileImg(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/pro_img_add.html', context={'form' : form})
