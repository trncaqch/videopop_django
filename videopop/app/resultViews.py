from django.shortcuts import render
from django.http import HttpResponse
from models import Score

def results(request):
    result = None
    context_dict = {}

    if request.user.is_authenticated():
        result = Score.objects.filter(user = request.user).latest("date")

    context_dict = {"result" : result}
    return render(request, 'app/results.html', context_dict)
