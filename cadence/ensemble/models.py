from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='user-images/', blank=True)
    ensembles = models.ManyToManyField('Ensemble', related_name='user_ensembles', blank=True)
    song_likes = models.ManyToManyField('Song', related_name='user_song_likes', blank=True)
    voice_part = models.CharField(max_length=30, blank=True)
    instrument = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, @{self.username}"
    
    def serialize(self):
        return {
            'id': self.id,
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
    name = models.CharField(max_length=30, unique=True)
    admins = models.ManyToManyField(User, related_name='ensembles_administered', blank=True)
    organization = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='ensemble-images/', blank=True)
    members = models.ManyToManyField(User, related_name='ensembles_joined', blank=True)
    songs = models.ManyToManyField('Song', related_name='ensemble_songs', blank=True)    
    sets = models.ManyToManyField('Set', related_name='ensemble_sets', blank=True)

    def __str__(self):
        return f"{self.name}, part of {self.organization}"
    
    def serialize(self):
        return {
            'id': self.id,
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
    title = models.CharField(max_length=30)
    composer = models.CharField(max_length=30, blank=True)
    lyricist = models.CharField(max_length=30, blank=True)
    arranger = models.CharField(max_length=30, blank=True)
    key = models.CharField(max_length=30, blank=True)
    hymn_tune = models.CharField(max_length=30, blank=True)
    hymn_number = models.CharField(max_length=30, blank=True)
    compilation = models.CharField(max_length=30, blank=True)
    year = models.IntegerField(blank=True)
    publisher = models.CharField(max_length=30, blank=True)
    charts = models.ManyToManyField('Chart', related_name='song_charts', blank=True)
    tracks = models.ManyToManyField('Track', related_name='song_tracks', blank=True)
    sets = models.ManyToManyField('Set', related_name='songs_set', blank=True)
    ensembles = models.ManyToManyField(Ensemble, related_name='song_ensembles', blank=True)
    liked_by = models.ManyToManyField(User, related_name='song_liked_by', blank=True)

    def __str__(self):
        return f"{self.title} by {self.composer}"

    def serialize(self):
        return {
            'id': self.id,
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
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True)
    songs = models.ManyToManyField(Song, related_name='set_songs', blank=True)
    ensemble = models.ForeignKey(Ensemble, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} for {self.ensemble.name}, contains {len(self.songs.all())} songs"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'songs': [song.serialize() for song in self.songs.all()],
            'ensemble': self.ensemble.serialize(),
        }

class Chart(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    pdf = models.FileField(upload_to='pdfs/', blank=True)

    def __str__(self):
        return f"{self.name} for {self.song.title}"
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'pdf': self.pdf.url,
        }

class Track(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    audio = models.FileField(upload_to='audio/', blank=True)

    def __str__(self):
        return f"{self.name} for {self.song.title}"
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'audio': self.audio.url,
        }

