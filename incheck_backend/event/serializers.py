from rest_framework import serializers
from .models import Event, Participant, EventParticipant

# Sérialiseur pour Event
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name', 'location', 'date']

# Sérialiseur pour Participant
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'first_name', 'last_name', 'email']

class EventParticipantSerializer(serializers.ModelSerializer):
    participant = ParticipantSerializer()  # Sérialiser les informations du participant
    status = serializers.CharField()  # Ajouter le champ de statut

    class Meta:
        model = EventParticipant
        fields = ['participant', 'status']  # Inclure le participant et son statut