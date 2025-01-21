# Generated by Django 5.1.3 on 2025-01-20 21:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0004_alter_chart_pdf_alter_ensemble_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chart',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='ensemble',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='set',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='song',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='track',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='ensemble',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='ensembles_joined', to='ensemble.user'),
        ),
        migrations.AlterField(
            model_name='ensemble',
            name='sets',
            field=models.ManyToManyField(blank=True, related_name='ensemble_sets', to='ensemble.set'),
        ),
        migrations.AlterField(
            model_name='ensemble',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='ensemble_songs', to='ensemble.song'),
        ),
        migrations.AlterField(
            model_name='set',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='set_songs', to='ensemble.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='charts',
            field=models.ManyToManyField(blank=True, related_name='song_charts', to='ensemble.chart'),
        ),
        migrations.AlterField(
            model_name='song',
            name='ensembles',
            field=models.ManyToManyField(blank=True, related_name='song_ensembles', to='ensemble.ensemble'),
        ),
        migrations.AlterField(
            model_name='song',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='song_liked_by', to='ensemble.user'),
        ),
        migrations.AlterField(
            model_name='song',
            name='sets',
            field=models.ManyToManyField(blank=True, related_name='songs_set', to='ensemble.set'),
        ),
        migrations.AlterField(
            model_name='song',
            name='tracks',
            field=models.ManyToManyField(blank=True, related_name='song_tracks', to='ensemble.track'),
        ),
        migrations.AlterField(
            model_name='user',
            name='charts_viewed',
            field=models.ManyToManyField(blank=True, related_name='user_charts_viewed', to='ensemble.chart'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ensembles',
            field=models.ManyToManyField(blank=True, related_name='user_ensembles', to='ensemble.ensemble'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sets_viewed',
            field=models.ManyToManyField(blank=True, related_name='user_sets_viewed', to='ensemble.set'),
        ),
        migrations.AlterField(
            model_name='user',
            name='song_likes',
            field=models.ManyToManyField(blank=True, related_name='user_song_likes', to='ensemble.song'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tracks_played',
            field=models.ManyToManyField(blank=True, related_name='user_tracks_played', to='ensemble.track'),
        ),
    ]
