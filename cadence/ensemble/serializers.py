from rest_framework import serializers
from .models import User, Ensemble, Song, Set, Chart, Track

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class EnsembleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ensemble
    fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
  class Meta:
    model = Song
    fields = '__all__'

class SetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Set
    fields = '__all__'
  
class ChartSerializer(serializers.ModelSerializer):
  class Meta:
    model = Chart
    fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
  class Meta:
    model = Track
    fields = '__all__'

    