from django.shortcuts import render

def News(request):
    return render(request, 'main/News.html')

def Mems(request):
    return render(request, 'main/Mems.html')

def HistoryCharacter(request):
    return render(request, 'main/HistoryCharacter.html')

