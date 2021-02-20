import json
import logging

from django.conf import settings

from ftl.models import ( 
   User, UserActivity
)

from webdev.utils.data_formatter import (
    result_row_to_dict, result_list_to_dict
)

from ftl.helpers.query_helpers.user_detail_helper import(
    get_user_activity
)

logger = logging.getLogger('ftl')

# create a session for sql alchemy
session = settings.DB_SESSION

def get_user_list():
    try:
        user_list = session.query(
            User.id,
            User.real_name,
            User.time_zone.label('tz')
        ).all()

        if user_list:
            user_list = result_list_to_dict(user_list)

            for user in user_list:
                user['activity_periods'] = get_user_activity(user['id'])

        session.commit()

    except Exception as e :
        logger.error('QUERY HELPER - GET USER LIST : {}'.format(e))
        session.rollback()
        user_list = None

    return user_list


