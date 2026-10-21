from rest_framework import serializers
from .models import Event, Registration, User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "title", "location", "capacity",
                  "created_at", "date", "description", "organizer"]
        read_only_fields = ["created_at", "id"]


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
      
        model=Registration
        fields=["id","user","event","created_at","updated_at"]
        read_only_fields=["id","created_at","updated_at","user"]


class MyTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):


        data = super().validate(attrs)
        data["user"] = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,


        }

        return data
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]
        extra_kwargs={"password":{"write_only":True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
