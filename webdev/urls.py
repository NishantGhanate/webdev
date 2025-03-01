"""webdev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import re_path , include

urlpatterns = [
    re_path(
        r'',
        include(
            ('overview.urls','overview'), 
            namespace = 'overview'
        )
    ),
    re_path(
        r'v1/ftl/',
        include(
            ('ftl.urls','ftl'), 
            namespace = 'ftl:v1'
        )
    ),
    re_path(
        r'v1/silly-auth/',
        include(
            ('silly_auth.urls','silly_auth'), 
            namespace = 'silly_auth:v1'
        )
    ),
]
