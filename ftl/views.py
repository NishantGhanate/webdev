from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 

# Create your views here.
@api_view(['GET'])
def api_overview(request):
    urls = {
        'List'   : 'user_list',
        'Detail' : 'user_detail?user_id=1A',
    }
    return Response(urls)