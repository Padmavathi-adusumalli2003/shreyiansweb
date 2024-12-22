from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def course(request):
    return render(request,'course.html')
def bootcamp(request):
    return render(request,'bootcamp.html')
def request(request):
    return render(request,'request.html')
def sign(request):
    return render(request,'sign.html')
def email(request):
    return render(request,'email.html')
