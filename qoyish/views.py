from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def Home(request):
    context=Video.objects.all()
    if request.method =="POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=Video_form()
    return render(request,('qoyish/home.html'),{'context':context,"form":form})
