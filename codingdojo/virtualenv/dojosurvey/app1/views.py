from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')


def survey(request):
    request.session['user_name'] = request.POST['user_name'] 
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, 'result.html')