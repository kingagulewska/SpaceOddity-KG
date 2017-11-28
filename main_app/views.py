from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from main_app import models
from main_app.forms import SearchForm
from paypal.standard.forms import PayPalPaymentsForm
from django.core.urlresolvers import reverse


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
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('search_results', form.cleaned_data['query'])
    else:
        form = SearchForm()
    user = User.objects.first()


    properties = user.houses.all()
    total_value = sum([house.price for house in properties])

    planets = models.Planet.objects.all()
    context = {
        'planets': planets,
        'user': User.objects.first(),
        'total_value': total_value,
        'form': form
    }
    return render(request, 'index.html', context)

def get_search_results(keyword):
    houses_by_name = models.House.objects.filter(name__contains=keyword)
    planets = models.Planet.objects.filter(name__contains=keyword)
    context = {
        'houses_by_name': houses_by_name,
        'planets': planets
    }

    return context


def search_results(request, keyword):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('search_results', form.cleaned_data['query'])
    else:
        form = SearchForm()

    context = get_search_results(keyword)

    return render(request, 'results.html', context)


def planet(request, planet_id):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect('search_results', form.cleaned_data['query'])
    else:
        form = SearchForm()
    params = generate_params()
    planet = get_object_or_404(models.Planet, id=planet_id)
    params['planet'] = planet
    params['form'] = form
    return render(request, 'planet.html', params)

def house(request, house_id):
    house = get_object_or_404(models.House, id=house_id)

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return redirect(reverse('ayment:process'))

    else:
        form = SearchForm()
    params = generate_params()
    params['house'] = house
    params['form'] = form
    return render(request, 'house.html', params)


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
