# Author:  Stadt Luzern, Zentrale Informatikdienste
# Contact: https://github.com/StadtLuzernIO
# License: The Unlicense, see LICENSE file.

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.module_utils.basic import env_fallback

"""
Defines common option budibase specs for modules
"""

def common_options():
  """Collects & returns options shared by all module implementations
  :return: dict
  """
  # Just budibase api connect params
  return API_CONFIG


def bb_search_for_rows():
  """Helper that compiles search_for_rows params spec and all common module budibase specs
  :return dict
  """
  search_for_rows_spec = dict(
    table=dict(
      type="str",
      required=True
    ),
    conditions=dict(
      type="dict",
      options=dict(
        query=dict(
          type="dict"
        ),
        paginate=dict(
          type="bool"
        ),
        bookmark=dict(
          type="str"
        ),
        limit=dict(
          type="int"
        ),
        sort=dict(
          type="dict"
        )
      )
    )
  )
  search_for_rows_spec.update(common_options())
  return search_for_rows_spec

def bb_execute_a_query():
  """Helper that compiles execute_a_query params spec and all common module budibase specs
  :return dict
  """
  execute_a_query = dict(
    query=dict(
      type="str",
      required=True
    ),
    conditions=dict(
      type="dict",
      options=dict(
        parameters=dict(
          type="dict"
        ),
        pagination=dict(
          type="dict"
        )
      )
    )
  )
  execute_a_query.update(common_options())
  return execute_a_query


# API config options for all modules
API_CONFIG = dict(
  hostname=dict(
    type="str",
    fallback=(env_fallback, ['BUDIBASE_HOST'])
  ),
  token=dict(
    type="str",
    fallback=(env_fallback, ['BUDIBASE_TOKEN']),
    no_log=True
  ),
  validate_certs=dict(
    type="bool",
    fallback=(env_fallback, ['BUDIBASE_VALIDATE_CERTS']),
    default="true"
  ),
  app=dict(
    type="str",
    required=True
  ),
  status=dict(
    type="str",
    default="published",
    choices=['published', 'development']
  )
)