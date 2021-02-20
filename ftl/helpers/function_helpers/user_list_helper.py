import logging

from rest_framework import status
from rest_framework.response import Response


from ftl.helpers.query_helpers.user_list_helper import (
    get_user_list
)

from webdev.utils import custom_exceptions as ce
from webdev.common import messages as glob_messages

# Get an instance of logger
logger = logging.getLogger('ftl')


def fetch_users_list_v1():
    """ Fetch users details : 
        id, real_name, tz, activities

        Returns:
        users : list
    """
    try:
        result = get_user_list()
        if result:
            return Response({
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': glob_messages.USER_ACTIVITY_FOUND,
                'data': {
                    'members' : result
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
        logger.error('FUNCTION HELPER - USER LIST : {}'.format(e))
        raise ce.InternalServerError