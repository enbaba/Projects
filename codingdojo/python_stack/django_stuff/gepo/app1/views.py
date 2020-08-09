from django.shortcuts import render

def index(request):
    return render(request,'form.html')
def process(request):
    if request.method=='post'
       context = {
           "name":"Enbaba"
           "language":["java","python","c#"]
           "location":"San jose"
       }
       return render(request, "index.html",context)