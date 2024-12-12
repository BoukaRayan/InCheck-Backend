from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event, Participant, EventParticipant
from .serializers import EventSerializer, ParticipantSerializer, EventParticipantSerializer
from django.shortcuts import get_object_or_404

# Vue pour lister et créer des événements
class EventListCreateView(APIView):
    permission_classes = []
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.save()
            return Response(EventSerializer(event).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Vue pour récupérer les détails d'un événement spécifique
class EventDetailView(APIView):
    permission_classes = []
    def get(self, request, id):
        event = get_object_or_404(Event, id=id)
        serializer = EventSerializer(event)
        return Response(serializer.data)

# Vue pour récupérer les participants d'un événement spécifique
class EventParticipantsView(APIView):
    permission_classes = []
    def get(self, request, id):
        event = get_object_or_404(Event, id=id)
        event_participants = EventParticipant.objects.filter(event=event)
        serializer = EventParticipantSerializer(event_participants, many=True)
        return Response(serializer.data)

# Vue pour ajouter des participants à un événement spécifique
class EventAddParticipantsView(APIView):
    permission_classes = []
    def post(self, request, id):
        event = get_object_or_404(Event, id=id)
        participant_ids = request.data.get('participant_ids', [])
        
        # Récupérer les participants à ajouter
        participants = Participant.objects.filter(id__in=participant_ids)
        
        # Associer les participants à l'événement
        event.participants.add(*participants)
        
        return Response({"message": "Participants added successfully."}, status=status.HTTP_200_OK)
    
class ParticipantListView(APIView):
    permission_classes = []
    def get(self, request):
        participants = Participant.objects.all()
        serializer = ParticipantSerializer(participants, many=True)
        return Response(serializer.data)

       
    

