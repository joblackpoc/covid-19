from django.shortcuts import render

def Home(request):
    return render(request,'covid/home.html')

def DashBoard(request):
    return render(request, 'covid/dashboard.html')
