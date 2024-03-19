
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from users.forms import  UserModelForm


def profile(request):
    url = reverse('home')
    return redirect(url)


def register(request):
    form = UserModelForm()
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect(reverse("home"))
    return render(request, 'users/register.html', {'form': form})
