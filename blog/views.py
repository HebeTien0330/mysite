from django.shortcuts import render
from common.utlis import getContext

# Create your views here.
def blog(request):
    context = getContext()
    return render(request, "blog.html", context)
