from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Userregisterform,UserUpdateForm,UpdateProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=='POST':
        form=Userregisterform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username') 
            messages.success(request,f'Account Created for {username} You can now Login Hurray!!')
            return redirect('Login')
    else:
        form=Userregisterform()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        uform=UserUpdateForm(request.POST,instance=request.user)
        p_form=UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
        if uform.is_valid() and p_form.is_valid:
            uform.save()
            p_form.save()
            messages.success(request,f'Your Account has been updated')
            return redirect('profile')
    else:
        uform=UserUpdateForm(instance=request.user)
        p_form=UpdateProfile(instance=request.user.profile)
    context={
        'uform':uform,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)