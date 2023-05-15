# Author:  Stadt Luzern, Zentrale Informatikdienste
# Contact: https://github.com/StadtLuzernIO
# License: The Unlicense, see LICENSE file.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


class Error(Exception):
  DEFAULT_MSG = "Error while interacting with Budibase"

  def __init__(self, message=None):
    self.message = message or self.DEFAULT_MSG
    super(Error, self).__init__(message)

class APIError(Error):
    DEFAULT_MSG = "Error while communicating with Budibase api"
    STATUS_CODE = 400

    def __init__(self, status_code=None, message=None):
        self.status_code = status_code or self.STATUS_CODE
        super(APIError, self).__init__(message)

class NotFoundError(APIError):
  DEFAULT_MSG = "Content not found"
  STATUS_CODE = 404

class BadRequestError(APIError):
    DEFAULT_MSG = "Invalid request body or parameters"
    STATUS_CODE = 400
    
class ServerError(APIError):
    DEFAULT_MSG = "Budibase Server encountered an error. Please try again"
    STATUS_CODE = 500

class AccessDeniedError(APIError):
    DEFAULT_MSG = "Token invalid or access to Budibase api not granted by token."
    STATUS_CODE = 403




