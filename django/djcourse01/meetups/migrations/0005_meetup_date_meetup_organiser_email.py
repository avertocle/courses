# Generated by Django 4.2.3 on 2023-07-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0004_participant_meetup_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='meetup',
            name='organiser_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
