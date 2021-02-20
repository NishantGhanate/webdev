import logging

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.versioning import NamespaceVersioning

from ftl.helpers.function_helpers.user_list_helper import (
    fetch_users_list_v1
)

from webdev.utils import custom_exceptions as ce
from webdev.utils.custom_validators import CustomValidator
from webdev.common import messages as glob_messages

# Get an instance of logger
logger = logging.getLogger('ftl')

# Get an instance of custom Validator
c_validator = CustomValidator({}, allow_unknown = True)


class VersioningConfig(NamespaceVersioning):
    default_version = 'v1'
    allowed_versions = ['v1']
    version_param = 'version'

class UserList(APIView):
    permission_classes = [AllowAny]
    versioning_class = VersioningConfig
    
    def get(self, request):
        try :
            if request.version == 'v1':
                result = fetch_users_list_v1()
                return result
            else:
                raise ce.VersionNotSupported

        except ce.ValidationFailed as vf:
            logger.error('ACTIVITY LIST API VIEW : {}'.format(vf))
            raise

        except ce.VersionNotSupported as vns:
            logger.error('ACTIVITY LIST API VIEW : {}'.format(vns))
            raise
        
        except Exception as e:
            logger.error('ACTIVITY LIST API VIEW :  {}'.format(e))
            raise ce.InternalServerError

