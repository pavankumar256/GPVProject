from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def marriage_fun(request):
    age = int(request.POST['txtage'])
    gender = request.POST['ddlgen']
    return render (request,'marriage.html',{"age":age,"gender":gender})


def leap_fun(request):
    year = int(request.POST['txtyear'])
    return render(request,"leap.html",{"year":year})