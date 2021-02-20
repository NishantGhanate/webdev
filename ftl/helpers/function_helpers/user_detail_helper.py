import logging

from rest_framework.response import Response
from rest_framework import status

from ftl.helpers.query_helpers.user_detail_helper import(
    get_user
)

from webdev.utils import custom_exceptions as ce
from webdev.common import messages as glob_messages

# Get an instance of logger
logger = logging.getLogger('ftl')

def fetch_user_v1(user_id):
    """ Given user id fetch all its activies

        Parameters:
        user_id : alphanum field 

        Returns:
        user_activity : list
    """
    try:
        result = get_user(user_id= user_id)
        if result:
            return Response({
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': glob_messages.USER_ACTIVITY_FOUND,
                'data': {
                    'member' : result
                    },
            }, 
            status = status.HTTP_200_OK)

        return Response({
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': glob_messages.DATA_NOT_FOUND,
                'data': None,
            }, status = status.HTTP_200_OK)
        
    except Exception as e:
        logger.error('FUNCTION HELPER - USER ACTIVITY : {}'.format(e))
        raise ce.InternalServerError
