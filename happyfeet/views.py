from django.shortcuts import render
from .models import MyShoe
from .forms import ShoeForm, AddMilesForm

# Create your views here.
def get_closet(request):
    return render(request, 'closet.html',
    {'shoes': MyShoe.objects.filter(user=request.user)
    })

def create_shoe(request):
    if request.method == "POST":
        form = ShoeForm(request.POST)
        if form.is_valid():
            Shoe = form.save(commit=False)
            Shoe.user = request.user
            Shoe.save()
            return render(request, 'profile.html')
    else:
        form = ShoeForm()
        return render(request, 'addshoe.html',
        {'shoes': MyShoe.objects.filter(user=request.user),
        'form': form
        })


def add_miles(request, id):
    if request.method == "POST":
            form = AddMilesForm(request.POST)
            if form.is_valid():
                shoe_from_user = form.save(commit=False)
                shoe_to_update = MyShoe.objects.get(pk=id)
                shoe_to_update.miles_run += shoe_from_user.miles_run
                shoe_to_update.save()
                return render(request, 'profile.html',
                {'shoe': shoe_to_update,})
    else:
        form = AddMilesForm()
        shoe_to_update = MyShoe.objects.get(pk=id)
        return render(request, 'addmiles.html',
        {'shoe': shoe_to_update,
        'form': form
        })

def select_shoe(request, id):
    shoe = MyShoe.objects.get(pk=id)
    return render(request, 'selectshoe.html',
    {'shoe': shoe,})
