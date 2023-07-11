from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def meetup_list_view(request):
    meetups = [
        {'title': 'First Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
        {'title': 'Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })
