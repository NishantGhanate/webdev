import re
import datetime
from cerberus import Validator

from webdev.common import (
    messages as glob_messages
)

class CustomValidator(Validator):
    
    #validate user_id
    def _validate_isalphanumeric(self,isalphanumeric,field,value):
        """
        {'type':'boolean'}
        """
        if isalphanumeric:
            zeroes = re.match('^0+$',value)
            if zeroes:
                self._error(
                    field,glob_messages.INVALID_USER_ID)

            alphanumeric_id = re.match('^[a-zA-Z0-9_]+$',value)

            if not alphanumeric_id:
                self._error(
                    field,glob_messages.SPECIAL_CHARS_NOT_ALLOWED)

   