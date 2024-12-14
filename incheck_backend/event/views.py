from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event, Participant, EventParticipant
from .serializers import EventSerializer, ParticipantSerializer, EventParticipantSerializer
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import EmailMessage
from io import BytesIO
import qrcode
from django.conf import settings

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
    




  # views for checkin

class QRCodeCheckInView(APIView):
    permission_classes = []
    def post(self, request):
        qr_data = request.data.get('qr_data')  # Exemple de qr_data: "participant_id:1,event_id:2"
        if not qr_data or ',' not in qr_data:
            return Response({'error': 'QR data is invalid'}, status=status.HTTP_400_BAD_REQUEST)
                 
        try:
            participant_id, event_id = qr_data.split(',')
            participant_id = participant_id.split(':')[1]
            event_id = event_id.split(':')[1]
        except Exception as e:
            return Response({'error': 'Invalid QR format'}, status=status.HTTP_400_BAD_REQUEST)

        event = get_object_or_404(Event, id=event_id)
        try:
            participant = get_object_or_404(Participant, id=participant_id)
        except ObjectDoesNotExist:
            return Response({'error': 'Participant not found'}, status=status.HTTP_400_BAD_REQUEST)

        # Marquer le participant comme présent
        event_participant = EventParticipant.objects.filter(participant=participant, event=event).first()
        if not event_participant:
            return Response({'error': 'Participant not registered for this event'}, status=status.HTTP_400_BAD_REQUEST)

        # Modifier le statut du participant
        event_participant.status = 'present'
        event_participant.save()

        # Retourner les informations du participant
        serializer = ParticipantSerializer(participant)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class SendQRCodesView(APIView):
    permission_classes = []
    def post(self, request, id):
        event = Event.objects.filter(id=id).first()
        if not event:
            return Response({"detail": "Event not found."}, status=status.HTTP_404_NOT_FOUND)

        participants = EventParticipant.objects.filter(event=event)
        if not participants:
            return Response({"detail": "No participants found for this event."}, status=status.HTTP_404_NOT_FOUND)

        for event_participant in participants:
            participant = event_participant.participant

            # Générer les données du QR code
            qr_data = f"participant_id:{participant.id},eventid:{event.id}"
            qr_image = qrcode.make(qr_data)

            # Convertir l'image QR en fichier binaire
            qr_image_io = BytesIO()
            qr_image.save(qr_image_io, format='PNG')
            qr_image_io.seek(0)

            # Construire l'email
            subject = f"Your QR Code for Event: {event.name}"
            message = f"Hello {participant.first_name},\n\nPlease find your QR code for the event '{event.name}' attached to this email."
            email = EmailMessage(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [participant.email],
            )

            # Ajouter l'image QR comme pièce jointe
            email.attach("QR_Code.png", qr_image_io.read(), 'image/png')

            # Envoyer l'email
            email.send()

        return Response({"detail": "QR codes sent to all participants."}, status=status.HTTP_200_OK)
        

       
    

