from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Book
from .forms import BookForm


# Create your views here.

# List view
def home(request):
    context = {}
    books = Book.objects.all()
    context['books'] = books

    return render(request, 'core/home.html', context)


# Create view
def create_book(request):
    context = {}
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'core/create_book.html', context)


# Update view
def update_book(request, id):
    context = {}
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')

    context['form'] = form
    return render(request, 'core/update_book.html', context)


def delete_book(request, id):
    context = {}
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return HttpResponseRedirect('/')

    return render(request, 'core/delete_book.html', context)
