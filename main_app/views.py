from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from main_app import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def generate_params():
    user = User.objects.first()
    properties = user.houses.all()
    total_value = sum([house.price for house in properties])
    planets = models.Planet.objects.all()

    context = {
        'planets': planets,
        'user': User.objects.first(),
        'total_value': total_value,
    }
    return context

def index(request):
    user = User.objects.first()

    properties = user.houses.all()
    total_value = sum([house.price for house in properties])

    planets = models.Planet.objects.all()
    context = {
        'planets': planets,
        'user': User.objects.first(),
        'total_value': total_value
    }
    return render(request, 'index.html', context)


def planet(request, planet_id):
    params = generate_params()
    planet = get_object_or_404(models.Planet, id=planet_id)
    params['planet'] = planet
    return render(request, 'planet.html', params)


def change_ownership(request, house_id):
    house = get_object_or_404(models.House, id=house_id)
    if house.owner is not None:
        house.owner = None
    else:
        house.owner = User.objects.first()

    house.save()
    
    return redirect('planet', planet_id=house.planet.id)

def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/admin/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login.html', {}, context)

def nav_bar():
    return render()