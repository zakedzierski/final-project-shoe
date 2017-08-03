from django.shortcuts import render
from .models import MyShoe

# Create your views here.
def get_closet(request):
    return render(request, 'closet.html',
    {'shoes': MyShoe.objects.all()
    })
