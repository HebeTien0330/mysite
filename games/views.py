from django.shortcuts import render
from common.utlis import getContext

# Create your views here.
def games(request):
    context = getContext()
    return render(request, "games.html", context)
