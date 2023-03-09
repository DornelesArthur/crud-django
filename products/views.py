from django.shortcuts import render

def index(request):
    return render(request, 'pages/products/index.html')

def view(request):
    pass