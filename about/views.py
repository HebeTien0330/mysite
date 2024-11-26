from django.shortcuts import render
from common.utlis import getContext

# Create your views here.
def about(request):
    context = getContext()
    return render(request, "about.html", context)
