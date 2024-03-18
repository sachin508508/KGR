from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'core/index.html')
def about(request):
    return render(request,'core/about.html')
def contact(request):
    return render(request,'core/contact.html')
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)