from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class JwtTestHello(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes =()
    
    def get(self, request):
        content = {'message': 'Hello, boi you got some of that JWT token ?'}
        return Response(content)