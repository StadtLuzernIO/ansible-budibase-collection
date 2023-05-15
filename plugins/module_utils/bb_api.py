# Author:  Stadt Luzern, Zentrale Informatikdienste
# Contact: https://github.com/StadtLuzernIO
# License: The Unlicense, see LICENSE file.

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import json
import sys

from urllib.error import HTTPError
from ansible.module_utils.urls import fetch_url
from ansible.module_utils.six.moves.urllib.parse import urlencode, quote, urlunparse, urlparse
from ansible_collections.stadtluzernio.budibase.plugins.module_utils import bb_const, bb_errors


def create_client(module):
  if not module.params.get("hostname") or not module.params.get("token"):
    raise bb_errors.AccessDeniedError(message="Hostname or auth token not defined")

  return Budibase(
      hostname=module.params["hostname"],
      token=module.params["token"],
      module=module
  )

class Budibase:
  API_VERSION = "v1"
  API_BASE_PATH = "/api/public"


  def __init__(self, hostname, token, module):
      self.hostname = hostname
      self.token = token
      self._module = module
      self._user_agent = _format_user_agent(
          bb_const.COLLECTION_VERSION,
          python_version=".".join(str(i) for i in sys.version_info[:3]),
          ansible_version=self._module.ansible_version
      )


  def _send_request(self, path, method="GET", data=None, params=None, headers=None):
    fetch_kwargs = {
      "url": build_endpoint(self.hostname, path, params=params, api_base_path=None, api_version=None),
      "method": method,
      "headers": self._build_headers(headers)
    }

    if method.upper() in ["POST", "PUT", "PATCH"] and data != None:
        fetch_kwargs["data"] = self._module.jsonify(data)

    resp, info = fetch_url(self._module, **fetch_kwargs)
    if info.get("status") == 200:
      try:
        resp_body = json.loads(resp.read().decode("utf-8"))
      except (AttributeError, ValueError):
        msg = "Server returned error with invalid JSON: {err}".format(
          err=info.get("msg", "<Undefined error>")
        )
        return self._module.fail_json(msg=msg)
    else:
        raise_for_error(info)

    return resp_body


  def _build_headers(self, headers=None):   
    fetch_kwargs = {
      "accept": "application/json",
      "content-type": "application/json",
      "x-budibase-api-key": self.token,
    }

    if headers != None:
      for enty in headers:
        fetch_kwargs[enty] = headers[enty]

    return fetch_kwargs

  def get_query_rows(self, bb_app_id, bb_query_id, bb_conditions):
    path = "/queries/" + bb_query_id
    resp = []

    headers = {}
    headers['x-budibase-app-id'] = bb_app_id
    
    data = {}

    if type(bb_conditions) == dict:
      for key,value in bb_conditions.items():
        if value != None:
          data[key] = value
    else:
      data = None

    rows = self._send_request(path, method="POST", data=data, headers=headers)

    headers = None
    data = None

    resp = rows['data']

    if not resp:
      raise bb_errors.NotFoundError

    return resp 


  def get_table_rows(self, bb_app_id, bb_table_id, bb_conditions):
    path = "/tables/" + bb_table_id + "/rows/search"
    resp = []

    headers = {}
    headers['x-budibase-app-id'] = bb_app_id
    
    data = {}

    if type(bb_conditions) == dict:
      for key,value in bb_conditions.items():
        if value != None:
          data[key] = value
    else:
      data = None

    rows = self._send_request(path, method="POST", data=data, headers=headers)

    headers = None
    data = None

    resp = rows['data']

    if not resp:
      raise bb_errors.NotFoundError

    return resp 


  def get_app_info_by_name(self, bb_app_name, bb_app_status):
    path = "/applications/search"
    resp = []
    
    data = {}
    data['name'] = bb_app_name

    apps = self._send_request(path, method="POST", data=data)

    data = None

    tmp_resp = apps['data']

    if tmp_resp and any(dict['name'] == bb_app_name for dict in tmp_resp):
      resp = []
      for dict in tmp_resp:
        if dict['name'] == bb_app_name:
          if dict['status'] == bb_app_status:
            resp.append(dict)
    else:
      raise bb_errors.APIError(
        message="No app was found with name " + bb_app_name + " in Budibase app " + bb_app_name
      )  

    if len(resp) > 1:
      raise bb_errors.APIError(
        message="More than 1 match found for an budibase app with that name. Please adjust your app name " + bb_app_name
      )

    return resp[0]


  def get_query_info_by_name(self, bb_query_name, bb_app_id, bb_app_name):
    path = "/queries/search"

    headers = {}
    headers['x-budibase-app-id'] = bb_app_id

    data = {}
    data['name'] = bb_query_name

    query = self._send_request(path, method="POST", data=data, headers=headers)

    headers = None
    data = None

    tmp_resp = query['data']

    if tmp_resp and any(dict['name'] == bb_query_name for dict in tmp_resp):
      resp = []
      for dict in tmp_resp:
        if dict['name'] == bb_query_name:
          resp.append(dict)
    else:
      raise bb_errors.APIError(
        message="No query was found with name " + bb_query_name + " in Budibase app " + bb_app_name
      )  

    if len(resp) > 1:
      raise bb_errors.APIError(
        message="More than 1 match found for an Budibase query with that name. Please adjust your query name " + bb_query_name
      )

    return resp[0]


  def get_table_info_by_name(self, bb_table_name, bb_app_id, bb_app_name):
    path = "/tables/search"

    headers = {}
    headers['x-budibase-app-id'] = bb_app_id

    data = {}
    data['name'] = bb_table_name

    table = self._send_request(path, method="POST", data=data, headers=headers)

    headers = None
    data = None

    tmp_resp = table['data']

    if tmp_resp and any(dict['name'] == bb_table_name for dict in tmp_resp):
      resp = []
      for dict in tmp_resp:
        if dict['name'] == bb_table_name:
          resp.append(dict)
    else:
      raise bb_errors.APIError(
        message="No table was found with name " + bb_table_name + " in Budibase app " + bb_app_name
      )  

    if len(resp) > 1:
      raise bb_errors.APIError(
        message="More than 1 match found for an Budibase table with that name. Please adjust your table name " + bb_table_name
      )

    return resp[0]


def build_endpoint(hostname, path, params=None, api_base_path=None, api_version=None):
  url_parts = list(urlparse('https://' + hostname))

  if not api_base_path:
    api_base_path = Budibase.API_BASE_PATH

  if not api_version:
    api_version = Budibase.API_VERSION

  url_parts[2] = "{api_base_path}/{api_version}/{path}".format(
    api_base_path=quote(api_base_path.strip('/')),
    api_version=api_version,
    path=quote(path.strip('/'))
  )

  if params:
    url_parts[4] = urlencode(params)
  return urlunparse(url_parts)


def raise_for_error(response_info):
  try:
    response_info_body = json.loads(response_info.get("body").decode("utf-8"))
    err_details = {
      "message": response_info_body.get("message"),
      "status_code": response_info_body.get("status")
    }
  except (AttributeError, ValueError):
    # `body` key not present if urllib throws an error ansible doesn't handle
    err_details = {
      "message": response_info.get("msg", "Error not defined"),
      "status_code": response_info.get("status")
    }

  if err_details["status_code"] >= 500:
    raise bb_errors.ServerError(**err_details)
  elif err_details["status_code"] == 404:
    raise bb_errors.NotFoundError(**err_details)
  elif err_details["status_code"] in [401, 403]:
    raise bb_errors.AccessDeniedError(**err_details)
  else:
    raise bb_errors.APIError(**err_details)


def _format_user_agent(collection_version, python_version=None, ansible_version=None):
  return "stadtluzernio.budibase/{version} Python/{py_version} Ansible/{ansible}".format(
    version=collection_version,
    py_version=python_version or "unknown",
    ansible=ansible_version or "unknown"
  )