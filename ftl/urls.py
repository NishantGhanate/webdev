from django.urls import path
from ftl.views import api_overview
from ftl.apiviews.user_detail import UerDetail
from ftl.apiviews.users_list import UserList
from ftl.apiviews.user_auth import UserAuth
from ftl.apiviews.jwt_test import JwtTestHello



urlpatterns = [
    path(
        'overview', 
        api_overview, 
        name='over_view'
    ),
    path(
        'user_detail', 
        UerDetail.as_view(), 
        name='user_detail'
    ),
    path(
        'user_list', 
        UserList.as_view(), 
        name='user_list'
    ),
    path(
        'user_auth', 
        UserAuth.as_view(), 
        name='user_auth'
    ),
    path(
        'jwt_hello',
        JwtTestHello.as_view(),
        name='hello'
    ),
    

]