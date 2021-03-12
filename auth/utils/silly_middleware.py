from rest_framework.response import Response
from rest_framework import status

# from django.conf import settings
# https://docs.djangoproject.com/en/3.1/topics/http/middleware/#writing-your-own-middleware

class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
        

class MemeMiddleware(BaseMiddleware):
               
    def process_view(self, request, view_func, view_args, view_kwargs):
        # print('----- Middleware view %s ----------' % view_func.__name__)
        authorization_header = request.headers.get('Authorization')
        if authorization_header:
            if authorization_header.split(' ')[1] == 42069
                return None
            else:
                return Response({
                'success': False,
                'status_code': status.HTTP_401_UNAUTHORIZED,
                'message': 'Do a bruteforce attack baby , Rainbow table may be?',
            }, 
            status = status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'God damn hackekrman123 is here',
            }, 
            status = status.HTTP_401_UNAUTHORIZED)
