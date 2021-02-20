import json
import logging
import argparse

from models import ( 
   User , UserActivity
)
from django.conf import settings

# logger = logging.getLogger('ftl')

# # create a session for sql alchemy
# session = settings.DB_SESSION

# def create_user(user_data):
#     user_detail = User(
#         id = user_data.get('id'),
#         real_name = user_data.get('real_name'),
#         time_zone = user_data.get('time_zone'),
#     )
#     session.add(user_detail)
#     session.commit()

#     except Exception as e:
#         logger.error('QUERY HELPER - CREATE USER: {}'.format(e))
#         session.rollback()
#         user_detail = None

#     return user_detail.id
    
# def add_user_activity(id,activity_data):
#     user_activity = UserActivity(
#         user_id = id,
#         start_time = activity_data.get('start_time'),
#         end_time = activity_data.get('end_time')
#     )

#     session.add(user_activity)
#     session.commit()

#     except Exception as e:
#         logger.error('QUERY HELPER - ADD uSER ACTIVITY: {}'.format(e))
#         session.rollback()
#         user_activity = None

#     return user_activity


parser = argparse.ArgumentParser()
parser.add_argument("-f","--file",type=argparse.FileType('r'), help="Takes json file as input")
args = parser.parse_args()
if args.file:
    print("File name is given {}".format(args.file))

    data_list = json.load(args.file)
    user_data_list = data_list.get('members')
    if user_data_list:
        for user_data in user_data_list:
            activity_data = user_data.pop('activity_periods')
            user_detail = user_data
            # print(user_detail)
            # print(activity_data)


