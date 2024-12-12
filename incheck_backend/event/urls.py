from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListCreateView.as_view(), name='event-list-create'),
    #path('events/<int:id>/', views.EventDetailView.as_view(), name='event-detail'),
    path('events/<int:id>/participants/', views.EventParticipantsView.as_view(), name='event-participants'),
    path('events/<int:id>/add-participants/', views.EventAddParticipantsView.as_view(), name='event-add-participants'),
    path('participants/', views.ParticipantListView.as_view(), name='participant-list'),
]
