from django.db import models

# Create your models here.

class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    participants = models.ManyToManyField(Participant, through='EventParticipant')

    def __str__(self):
        return self.name

class EventParticipant(models.Model):
    PRESENT = 'present'
    ABSENT = 'absent'
    STATUS_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=ABSENT)

    def __str__(self):
        return f"{self.participant} - {self.event} - {self.status}"