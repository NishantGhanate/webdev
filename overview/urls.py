from django.urls import path
from overview.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='homeview'),
]