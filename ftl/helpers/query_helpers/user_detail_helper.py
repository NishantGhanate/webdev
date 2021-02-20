import json
import logging

from django.conf import settings

from ftl.models import ( 
   User, UserActivity
)

from webdev.utils.data_formatter import (
    result_row_to_dict, result_list_to_dict
)

logger = logging.getLogger('ftl')

# create a session for sql alchemy
session = settings.DB_SESSION

def get_user(user_id):
    try:
        user_detail = session.query(
            User.id,
            User.real_name,
            User.time_zone.label('tz')
        ).filter(
            User.id == user_id
        ).first()

        if user_detail:
            user_detail = result_row_to_dict(user_detail)
            user_detail['activity_periods'] = get_user_activity(user_detail['id'])

        session.commit()

    except Exception as e :
        logger.error('QUERY HELPER - GET USER Activity : {}'.format(e))
        session.rollback()
        user_detail = None

    return user_detail


def get_user_activity(user_id):
    try:
        user_activity = session.query(
            UserActivity.start_time,
            UserActivity.end_time
        ).filter(
            UserActivity.user_id == user_id
        ).all()
        
        if user_activity:
            user_activity  = result_list_to_dict(user_activity)

        session.commit()

    except Exception as e :
        logger.error('QUERY HELPER - GET USER Activity : {}'.format(e))
        session.rollback()
        user_activity = None

    return user_activity
