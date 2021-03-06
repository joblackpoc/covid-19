from django.shortcuts import render

def Home(request):
    return render(request,'covid/home.html')

def DashBoard(request):
    return render(request, 'covid/dashboard.html')

def Icons(request):
    return render(request, 'covid/icons.html')

def Tables(request):
    return render(request, 'covid/tables.html')

def User(request):
    return render(request, 'covid/user.html')

def Typography(request):
    return render(request, 'covid/typography.html')

def Notifications(request):
    return render(request, 'covid/notifications.html')

def Upgrade(request):
    return  render(request, 'covid/upgrade.html')

def Maps(request):
    return render(request, 'covid/maps.html')

def Rtl(request):
    return render(request, 'covid/rtl.html')