from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserRegistrationForm, CustomUserLoginForm, CustomUserUpdateForm, CustomProfileUpdateForm
def registration(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    form = CustomUserRegistrationForm()

    return render(request, 'register_page.html', {'form':form})


def CustomLogin(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('main')
            else:
                messages.error(request,'Invalid credentials')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})


def profileView(request):
    if request.method == 'POST':
        u_form = CustomUserUpdateForm(request.POST, instance=request.user)
        p_form = CustomProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        print('Files in request.FILES:', request.FILES)
        print('Image field data:', request.FILES.get('image'))  # Печатает файл из формы
        if u_form.is_valid() and p_form.is_valid():
            print('Image to save:', p_form.instance.image)
            u_form.save()
            p_form.save()
            return redirect('profile')
        else:
            print('Form errors:', p_form.errors)
    else:
        u_form = CustomUserUpdateForm(instance=request.user)
        p_form = CustomProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)
