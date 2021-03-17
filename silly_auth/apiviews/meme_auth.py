from rest_framework.authentication import BasicAuthentication
from rest_framework import exceptions
from webdev.common import messages as glob_messages
import logging
import base64

logger = logging.getLogger('auth')

class MemeAuthentication(BasicAuthentication):
    def authenticate(self, request):
        
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            raise exceptions.AuthenticationFailed(glob_messages.AUTH_FAILED) 

        username, password = self._basic_decode(authorization_header)     
        if not username :
            raise exceptions.AuthenticationFailed(glob_messages.DECODE_ERROR)
        
        try:
            auth_user = (username == '420' ) and (password == '69')
            if not auth_user :
                raise exceptions.AuthenticationFailed(glob_messages.AUTH_FAILED)
        
        except Exception as e :
            logger.error('MEME-AUTH  : {}'.format(e))
            raise exceptions.AuthenticationFailed(glob_messages.AUTH_FAILED)

        return (auth_user,None)

    def _basic_decode(self,authorization_header):
        try :
            auth = authorization_header.split(' ')
            if len(auth) == 2:
                    if auth[0].lower() == "basic":
                        username, password = base64.b64decode(
                            auth[1]).decode(
                            "utf8"
                        ).split(':', 1)
                    return (username,password)
        except Exception as e:
            logger.error('MEME-AUTH  : {}'.format(e))
            raise exceptions.AuthenticationFailed(glob_messages.DECODE_ERROR) 
            
            