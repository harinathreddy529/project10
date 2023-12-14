from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topics(request):
    QLTO=topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)