from django.urls import path
from .views import (
    EventListCreateview,
    EventDetailView,
    RegistrationListCreateView,
    RegistrationDetailView,
    MyLogin,
    UserListCreateView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("events/", EventListCreateview.as_view(), name="event-list"),
    path("events/<int:pk>/", EventDetailView.as_view(), name="event-detail"),
    path("registrations/", RegistrationListCreateView.as_view(),
         name="registration-list-create"),
    path("registrations/<int:pk>/", RegistrationDetailView.as_view(),
         name="registration-detail"),
    path('token/', MyLogin.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
]
