from django.http import HttpResponse
from django.shortcuts import render
from meetups.models import Meetup


# Create your views here.

def meetup_list_view(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
    })

def meetup_detail_view(request, meetup_slug):
    meetup = None
    error = False
    try:
        meetup = Meetup.objects.get(slug=meetup_slug)
    except Exception as e:
        error = True

    return render(request, 'meetups/details.html', {
        'meetup': meetup,
        'error' : error
    })


###### DUMMY

def meetup_list_view_dummy(request):
    meetups = [
        {'title': 'First Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
        {'title': 'Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })
