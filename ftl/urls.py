from django.urls import path
from ftl.views import api_overview
from ftl.apiviews.user_detail import UerDetail
from ftl.apiviews.users_list import UserList

urlpatterns = [
    path(
        '', 
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
    )

]