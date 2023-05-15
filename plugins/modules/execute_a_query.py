#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author:  Stadt Luzern, Zentrale Informatikdienste
# Contact: https://github.com/StadtLuzernIO
# License: The Unlicense, see LICENSE file.

from __future__ import absolute_import, division, print_function
import json
__metaclass__ = type


DOCUMENTATION = r'''
module: execute_a_query
author:
  - Stadt Luzern, Zentrale Informatikdienste
requirements: []
notes:
version_added: 1.0.1
short_description: Returns the value of a query in Budibase.
description:
  - Get the value a single query given its name.
  - You may provide a section label to limit the search to that query section.

extends_documentation_fragment:
  - stadtluzernio.budibase.budibase_api_connect
  - stadtluzernio.budibase.budibase_app_info
options:
    query:
        description: The name of the query which this request is targeting.
        type: str
        required: true
    conditions:
        description: Use query conditions
        type: dict 
        suboptions:
            parameters:
                description:  This contains the required parameters for the query,
                              this depends on query type, setup and bindings.
                type: dict
            pagination:
                description:  For supported query types (currently on REST) pagination 
                              can be performed using these properties.
                type: dict
                suboptions:
                    page:
                        description:  The page which has been returned from a 
                                      previous query.
                        type: str
                    limit:
                        description:  The number of rows to return per page.
                        type: int
'''

EXAMPLES = '''
---
- name: Get all rows from query inventory in stadtluzernio app with status published
  stadtluzernio.budibase.execute_a_query:
    hostname: BUDIBASE_HOST
    token: BUDIBASE_TOKEN
    app: BUDIBASE_APP
    query: BUDIBASE_QUERY
    status: published
'''

RETURN = '''
json:
  description: App info, query info and content from selectet row
  type: dict
  returned: always
  contains::
    app_info:
      description: App info (_id, name, status, ...)
      type: dict
      returned: success
    query_info:
      description: Query info (_id, name, schema, ...)
      type: dict
    content:
      description: Content from selectet rows
      type: list
      elements: dict
      returned: success
'''


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.stadtluzernio.budibase.plugins.module_utils import bb_specs, bb_api, bb_errors
from ansible.module_utils.common.text.converters import to_native


def main():
  result = {"json": {}, "changed": False}
  changed = False

  # the AnsibleModule object will be our abstraction working with Ansible
  # this includes instantiation, a couple of common attr would be the
  # args/params passed to the execution, as well as if the module
  # supports check mode
  module = AnsibleModule(
      argument_spec=bb_specs.bb_execute_a_query(),
      supports_check_mode=False
  )

  api_client = bb_api.create_client(module)

  bb_app        = module.params.get("app")
  bb_status     = module.params.get("status")
  bb_query      = module.params.get("query")
  bb_conditions = module.params.get("conditions")

  try:
    api_response                = {}
    api_response['app_info']    = api_client.get_app_info_by_name(bb_app, bb_status)
    api_response['query_info']  = api_client.get_query_info_by_name(bb_query, api_response['app_info']['_id'], api_response['app_info']['name'])
    api_response['content']     = api_client.get_query_rows(api_response['app_info']['_id'], api_response['query_info']['_id'] , bb_conditions)

    result.update({"json": api_response, "changed": bool(changed)})

  except bb_errors.NotFoundError as e:
      result.update({"msg": to_native("Row not found: {err}".format(err=e))})
      module.fail_json(**result)
  except bb_errors.Error as e:
    result.update({"msg": to_native(e)})
    module.fail_json(**result)

  module.exit_json(**result)


if __name__ == '__main__':
    main()