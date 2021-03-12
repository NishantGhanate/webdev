import logging

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.versioning import NamespaceVersioning

from ftl.helpers.function_helpers.user_detail_helper import (
    fetch_user_v1
)

from auth.apiviews.meme_auth import MemeAuthentication
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

class UserAuth(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [MemeAuthentication]
    versioning_class = VersioningConfig
    
    def get(self, request):
        try :
            if request.version == 'v1':
                schema = {
                    'user_id': {
                        'required': True,
                        'isalphanumeric' : True
                    }
                }

                is_valid = c_validator.validate(
                    request.query_params, schema
                )

                if not is_valid:
                    raise ce.ValidationFailed({
                        'message': glob_messages.VALIDATION_FAILED,
                        'data': c_validator.errors
                    })
                
                result = fetch_user_v1(
                    user_id= request.query_params['user_id']
                )
                return result
            else:
                raise ce.VersionNotSupported

        except ce.ValidationFailed as vf:
            logger.error('USER ACTIVITY API VIEW : {}'.format(vf))
            raise

        except ce.VersionNotSupported as vns:
            logger.error('USER ACTIVITY API VIEW : {}'.format(vns))
            raise
        
        except Exception as e:
            logger.error('USER ACTIVITY API VIEW : {}'.format(e))
            raise ce.InternalServerError

