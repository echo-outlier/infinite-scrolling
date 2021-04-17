from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from lorem_text import lorem

# Create your views here.
def index(request):
    return render(request,'creative/index.html')


def random(request,word):
    text=lorem.words(word)
    return HttpResponse(text)

def loremtext(request):
    return render(request,'creative/lorem.html')

    
