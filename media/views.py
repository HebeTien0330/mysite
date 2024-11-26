from django.shortcuts import render
from common.utlis import getContext

# Create your views here.
def media(request):
    context = getContext()
    return render(request, "media.html", context)
