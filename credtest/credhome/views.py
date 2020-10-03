from django.shortcuts import render

def Homeview(request):
    return render(request,"home.html")

# class Homeview(request):
#     template_name = 'home.html'
