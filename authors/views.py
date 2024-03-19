from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from authors.models import Author
from authors.forms import AuthorModelForm
from django.contrib.auth.decorators import login_required

def home(request):
     return render(request,'authors/home.html')

def list(request):
    authors = Author.get_all_authors()
    return render(request, "authors/list.html",context={"authors": authors})

def profile(request, id):
    author = Author.get_sepcific_author(id)
    return render(request, 'authors/show.html',context={"author":author})

@login_required(login_url='/users/login')
def create_author(request):
    form = AuthorModelForm()

    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save() 
            return redirect(author.show_url)
        
    return render(request, 'authors/add_author.html',context={"form":form})

@login_required(login_url='/users/login')
def edit_author(request, id):
    author = Author.get_sepcific_author(id)
    form = AuthorModelForm(instance=author) 
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect(author.show_url)

    return render(request, 'authors/edit.html',context={"form":form})

@login_required(login_url='/users/login')
def delete_author(request, id):
    author = Author.get_sepcific_author(id)
    author.delete()
    url = reverse("listauthors")
    return redirect(url)





