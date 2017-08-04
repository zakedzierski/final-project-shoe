from django.shortcuts import render
from .models import MyShoe
from .forms import ShoeForm
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
            Shoe.name = form.save()
            Shoe.brand = form.save()
            Shoe.icon = form.save()
            Shoe.miles_run = form.save()
            Shoe.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ShoeForm()
        return render(request, 'addshoe.html',
        {'shoes': MyShoe.objects.filter(user=request.user),
        'form': form
        })
