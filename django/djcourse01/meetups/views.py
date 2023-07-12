from django.http import HttpResponse
from django.shortcuts import render

from meetups.forms import RegistrationForm
from meetups.models import Meetup


# Create your views here.

def meetup_list_view(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
    })


def meetup_detail_view(request, meetup_slug):
    meetup = None
    reg_form = None
    try:
        meetup = Meetup.objects.get(slug=meetup_slug)
        if request.Method == 'GET':
            reg_form = RegistrationForm()
            return render(request, 'meetups/details.html', {
                'meetup': meetup,
                'reg_form': reg_form,
                'error': False,
            })
        else:
            reg_form = RegistrationForm(request.POST)
            if reg_form.is_valid():
                participant = reg_form.save()
                meetup.participants.save(participant)
                return render(request, 'meetups/reg_confirm.html', {
                    'meetup': meetup,
                    'participant':participant,
                })
            else:
                return render(request, 'meetups/details.html', {
                    'meetup': meetup,
                    'reg_form': reg_form,
                    'error': True,
                    'error_msg': 'Invalid Details !!'
                })
    except Exception as e:
        return render(request, 'meetups/details.html', {
            'meetup': meetup,
            'reg_form': reg_form,
            'error': True,
        })



# DUMMY

def meetup_list_view_dummy(request):
    meetups = [
        {'title': 'First Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
        {'title': 'Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups,
    })
