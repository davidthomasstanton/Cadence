# Generated by Django 5.1.3 on 2025-01-16 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0003_alter_chart_name_alter_chart_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chart',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
        migrations.AlterField(
            model_name='ensemble',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ensemble',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ensemble-images/'),
        ),
        migrations.AlterField(
            model_name='ensemble',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='ensembles_joined', to='ensemble.user'),
        ),
        migrations.AlterField(
            model_name='ensemble',
            name='organization',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='ensemble',
            name='sets',
            field=models.ManyToManyField(blank=True, null=True, related_name='ensemble_sets', to='ensemble.set'),
        ),
        migrations.AlterField(
            model_name='ensemble',
            name='songs',
            field=models.ManyToManyField(blank=True, null=True, related_name='ensemble_songs', to='ensemble.song'),
        ),
        migrations.AlterField(
            model_name='set',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='songs',
            field=models.ManyToManyField(blank=True, null=True, related_name='set_songs', to='ensemble.song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='arranger',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='charts',
            field=models.ManyToManyField(blank=True, null=True, related_name='song_charts', to='ensemble.chart'),
        ),
        migrations.AlterField(
            model_name='song',
            name='compilation',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='composer',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='ensembles',
            field=models.ManyToManyField(blank=True, null=True, related_name='song_ensembles', to='ensemble.ensemble'),
        ),
        migrations.AlterField(
            model_name='song',
            name='hymn_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='hymn_tune',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='key',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='song_liked_by', to='ensemble.user'),
        ),
        migrations.AlterField(
            model_name='song',
            name='lyricist',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='publisher',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='sets',
            field=models.ManyToManyField(blank=True, null=True, related_name='songs_set', to='ensemble.set'),
        ),
        migrations.AlterField(
            model_name='song',
            name='tracks',
            field=models.ManyToManyField(blank=True, null=True, related_name='song_tracks', to='ensemble.track'),
        ),
        migrations.AlterField(
            model_name='song',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='charts_viewed',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_charts_viewed', to='ensemble.chart'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ensembles',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_ensembles', to='ensemble.ensemble'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user-images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='instrument',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sets_viewed',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_sets_viewed', to='ensemble.set'),
        ),
        migrations.AlterField(
            model_name='user',
            name='song_likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_song_likes', to='ensemble.song'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tracks_played',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_tracks_played', to='ensemble.track'),
        ),
        migrations.AlterField(
            model_name='user',
            name='voice_part',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
