# Generated by Django 4.2.3 on 2023-07-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0005_meetup_date_meetup_organiser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
