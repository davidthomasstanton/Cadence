# Generated by Django 5.1.3 on 2025-01-20 21:48

from django.db import migrations, models
import uuid

def populate_uid(apps, schema_editor):
    User = apps.get_model('ensemble', 'User')
    Ensemble = apps.get_model('ensemble', 'Ensemble')
    Song = apps.get_model('ensemble', 'Song')
    Set = apps.get_model('ensemble', 'Set')
    Track = apps.get_model('ensemble', 'Track')

    for model in [User, Ensemble, Song, Set, Track]:
        for obj in model.objects.all():
            obj.uid = uuid.uuid4()
            obj.save()
    

class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0005_chart_uid_ensemble_uid_set_uid_song_uid_track_uid_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_uid),
    ]
