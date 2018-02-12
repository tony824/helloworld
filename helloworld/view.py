from django.shortcuts import render

def hello(request):
    context          = {}
    context['output'] = 'Congrats!!!'
    return render(request, 'hello.html', context)
