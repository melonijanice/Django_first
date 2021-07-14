from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("List of all my Blogs")

def new(request):
    return HttpResponse("New form to create new blog")

def create(request):
    return redirect("/new")
    
def show(request, num):
    return HttpResponse(f"placeholder to display blog number {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog number {num}")

def delete(request,num):
    return redirect("/")

