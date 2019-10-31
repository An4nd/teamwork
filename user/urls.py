from django.urls import path
from .views import PersonalView,TeamView
urlpatterns = [
    path('', PersonalView.as_view(),name='personal_home'),
    path('team', TeamView.as_view(),name='team_home'),
]