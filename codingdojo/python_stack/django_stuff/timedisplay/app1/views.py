from django.shortcuts import render
from time import gmtime, strftime

def index(request):
    context={
       "time": strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    }

    return render(request, 'index.html',context)



