from django.urls import path
from silly_auth.apiviews.jwt_auth import CustomToken

urlpatterns = [
    path(
        'custom-token',
        CustomToken.as_view(),
        name='custom-token'
    ),
]
