from django.shortcuts import render

def biriyani(request):
    return render(request,'biriyani.html')

def parota(request):
    return render(request,'parota.html')
