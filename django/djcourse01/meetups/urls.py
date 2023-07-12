from django.urls import path
from meetups import views

urlpatterns = [
    path('meetups/', views.meetup_list_view, name='meetup-listing'),
    path('meetups/<slug:meetup_slug>', views.meetup_detail_view, name='meetup-details'),
]
