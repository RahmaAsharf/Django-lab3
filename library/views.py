from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from library.models import Book
from django.contrib.auth.decorators import login_required
from authors.models import Author

def home(request):
     return render(request,'home.html')
def base(request):
     return render(request,'layouts/base.html')


def list(request):
    books = Book.objects.all()
    return render(request,'allbooks.html',context={"books":books})

def profile(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book.html',context={"book":book})

@login_required(login_url='/users/login')
def create_book(request):
    if request.method == 'POST':
        name = request.POST["name"]
        price = request.POST["price"]
        author_id = request.POST["author"]  
        author = Author.get_sepcific_author(id=author_id)  
        image = request.FILES['image']
        no_ofpages = request.POST["no_ofpages"]

        book = Book.objects.create(
            name=name,
            price=price,
            author=author,
            image=image,
            no_ofpages=no_ofpages
        )
        
        return redirect(reverse("list"))

    authors = Author.get_all_authors()
    return render(request, 'create.html', {'authors': authors})
@login_required(login_url='/users/login')
def update_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        author_id = request.POST.get("author") 
        author = Author.objects.get(id=author_id)
        pages = request.POST.get("no_ofpages")

        book.name = name
        book.price = price
        book.author = author
        book.no_ofpages = pages

        if 'image' in request.FILES:
            book.image = request.FILES['image']

        book.save()

        return redirect(reverse('list'))

    else:
        authors = Author.objects.all()
        return render(request, 'update.html', {'book': book, 'authors': authors})

@login_required(login_url='/users/login')
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    url = reverse("list")
    return redirect(url)






