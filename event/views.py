from django.shortcuts import render

# Create your views here.
from .models import Event, Registration, User
from .serializers import EventSerializer, RegistrationSerializer, MyTokenObtainSerializer, UserSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .permissions import IsSuperUser


class EventListCreateview(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        else:
            return [IsSuperUser()]

  
class EventDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsSuperUser()]


class RegistrationListCreateView(ListCreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        event = serializer.validated_data["event"]

        if Registration.objects.filter(
            user=self.request.user,
            event=event
        ).exists():
            raise ValidationError("You are already registered for this event.")

        if event.registrations.count() >= event.capacity:
            raise ValidationError("This event is full.")

        serializer.save(user=self.request.user)


class RegistrationDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        if self.request.user.is_superuser:
            return Registration.objects.all()

        return Registration.objects.filter(user=self.request.user)

class MyLogin(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer

class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsSuperUser()]
