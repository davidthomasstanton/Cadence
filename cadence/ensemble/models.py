import uuid
from django.db import models

class User(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='user-images/', blank=True, null=True)
    ensembles = models.ManyToManyField('Ensemble', related_name='user_ensembles', blank=True)
    song_likes = models.ManyToManyField('Song', related_name='user_song_likes', blank=True)
    voice_part = models.CharField(max_length=30, blank=True, null=True)
    instrument = models.CharField(max_length=30, blank=True, null=True)
    # Meta Data
    date_created = models.DateTimeField(auto_now_add=True)
    login_count = models.IntegerField(default=0)
    sets_viewed = models.ManyToManyField('Set', related_name='user_sets_viewed', blank=True)
    tracks_played = models.ManyToManyField('Track', related_name='user_tracks_played', blank=True)
    charts_viewed = models.ManyToManyField('Chart', related_name='user_charts_viewed', blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}, @{self.username}"
    
    def serialize(self):
        return {
            'id': self.uid,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'image': self.image.url,
            'ensembles': [ensemble.serialize() for ensemble in self.ensembles.all()],
            'song_likes': [song.serialize() for song in self.song_likes.all()],
            'voice_part': self.voice_part,
            'instrument': self.instrument,
        }

class Ensemble(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=60, unique=True)
    admins = models.ManyToManyField(User, related_name='ensembles_administered', blank=True)
    organization = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='ensemble-images/', blank=True, null=True)
    members = models.ManyToManyField(User, related_name='ensembles_joined', blank=True)
    songs = models.ManyToManyField('Song', related_name='ensemble_songs', blank=True)    
    sets = models.ManyToManyField('Set', related_name='ensemble_sets', blank=True)
    # Meta Data
    date_created = models.DateTimeField(auto_now_add=True)
    login_count = models.IntegerField(default=0)
    number_of_sets_viewed = models.IntegerField(default=0)
    number_of_songs_viewed = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}, part of {self.organization}"
    
    def serialize(self):
        return {
            'id': self.uid,
            'name': self.name,
            'admins': [admin.serialize() for admin in self.admins.all()],
            'organization': self.organization,
            'description': self.description,
            'image': self.image.url,
            'members': [member.serialize() for member in self.members.all()],
            'songs': [song.serialize() for song in self.songs.all()],
            'sets': [set.serialize() for set in self.sets.all()],
        }

class Song(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=60)
    composer = models.CharField(max_length=60, blank=True, null=True)
    lyricist = models.CharField(max_length=60, blank=True, null=True)
    arranger = models.CharField(max_length=60, blank=True, null=True)
    key = models.CharField(max_length=30, blank=True, null=True)
    hymn_tune = models.CharField(max_length=30, blank=True, null=True)
    hymn_number = models.CharField(max_length=30, blank=True, null=True)
    compilation = models.CharField(max_length=60, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=60, blank=True, null=True)
    charts = models.ManyToManyField('Chart', related_name='song_charts', blank=True)
    tracks = models.ManyToManyField('Track', related_name='song_tracks', blank=True)
    sets = models.ManyToManyField('Set', related_name='songs_set', blank=True)
    ensembles = models.ManyToManyField(Ensemble, related_name='song_ensembles', blank=True)
    liked_by = models.ManyToManyField(User, related_name='song_liked_by', blank=True)
    # Meta Data
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_times_viewed = models.IntegerField(default=0)
    number_of_times_played = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.composer}"

    def serialize(self):
        return {
            'id': self.uid,
            'title': self.title,
            'composer': self.composer,
            'lyricist': self.lyricist,
            'arranger': self.arranger,
            'key': self.key,
            'hymn_tune': self.hymn_tune,
            'hymn_number': self.hymn_number,
            'compilation': self.compilation,
            'year': self.year,
            'publisher': self.publisher,
            'charts': [chart.serialize() for chart in self.charts.all()],
            'tracks': [track.serialize() for track in self.tracks.all()],
            'sets': [set.serialize() for set in self.sets.all()],
            'ensembles': [ensemble.serialize() for ensemble in self.ensembles.all()],
            'liked_by': [user.serialize() for user in self.liked_by.all()],
        }

class Set(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    songs = models.ManyToManyField(Song, related_name='set_songs', blank=True)
    ensemble = models.ForeignKey(Ensemble, on_delete=models.CASCADE)
    #Meta Data
    date_created = models.DateTimeField(auto_now_add=True)
    number_of_times_viewed = models.IntegerField(default=0)
    

    def __str__(self):
        return f"{self.name} for {self.ensemble.name}, contains {len(self.songs.all())} songs"

    def serialize(self):
        return {
            'id': self.uid,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'songs': [song.serialize() for song in self.songs.all()],
            'ensemble': self.ensemble.serialize(),
        }

class Chart(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} for {self.song.title}"
    
    def serialize(self):
        return {
            'id': self.uid,
            'name': self.name,
            'type': self.type,
            'pdf': self.pdf.url,
        }

class Track(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} for {self.song.title}"
    
    def serialize(self):
        return {
            'id': self.uid,
            'name': self.name,
            'type': self.type,
            'audio': self.audio.url,
        }

