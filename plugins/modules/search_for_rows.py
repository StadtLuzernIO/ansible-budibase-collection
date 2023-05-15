#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author:  Stadt Luzern, Zentrale Informatikdienste
# Contact: https://github.com/StadtLuzernIO
# License: The Unlicense, see LICENSE file.

from __future__ import absolute_import, division, print_function
__metaclass__ = type


DOCUMENTATION = r'''
module: search_for_rows
author:
  - Stadt Luzern, Zentrale Informatikdienste
requirements: []
notes:
version_added: 1.0.1
short_description: Returns the value of a table in Budibase.
description:
  - Get the value a single table given its name.
  - You may provide a section label to limit the search to that table section.

extends_documentation_fragment:
  - stadtluzernio.budibase.budibase_api_connect
  - stadtluzernio.budibase.budibase_app_info
options:
    table:
        description: The name of the table which this request is targeting.
        type: str
        required: true
    conditions:
        description: Use table conditions
        type: dict 
        suboptions:
            query:
                description:  Table query
                type: dict
                suboptions:
                    string:
                        description:  A map of field name to the string to search 
                                      for, this will look for rows that have a value 
                                      starting with the string value.
                        type: dict
                    fuzzy:
                        description:  A fuzzy search, only supported by internal 
                                      tables.         
                        type: dict
                    range:
                        description:  Searches within a range, the format of this 
                                      must be columnName -> [low, high].
                        type: dict
                    equal:
                        description:  Searches for rows that have a column value 
                                      that is exactly the value set.
                        type: dict
                    notEqual:
                        description:  Searches for any row which does not contain 
                                      the specified column value.
                        type: dict            
                    empty:
                        description:  Searches for rows which do not contain the 
                                      specified column. The object should simply 
                                      contain keys of the column names, these can 
                                      map to any value.
                        type: dict    
                    notEmpty:
                        description:  Searches for rows which have the specified 
                                      column.
                        type: dict    
                    oneOf:
                        description:  Searches for rows which have a column value 
                                      that is any of the specified values. The format 
                                      of this must be columnName -> [value1, value2].
                        type: dict                
            paginate:
                description:  Enables pagination, by default this is disabled.
                type: bool
                default: false
            bookmark:
                description:  If retrieving another page, the bookmark from the 
                              previous request must be supplied.
                type: str
            limit:
                description:  The maximum number of rows to return, useful when 
                              paginating, for internal tables this will be limited 
                              to 1000, for SQL tables it will be 5000.
                type: int
            sort:
                description:  A set of parameters describing the sort behaviour 
                              of the search.
                type: dict
                suboptions:
                    order:
                        description:  The order of the sort, by default this is 
                                      ascending.
                        type: str
                        choices:
                          - ascending
                          - descending
                    column:
                        description:  The name of the column by which the rows 
                                      will be sorted.
                        type: str
                    type:
                        description:  Defines whether the column should be treated 
                                      as a string or as numbers when sorting.
                        type: str
'''

EXAMPLES = '''
---
- name: Get all rows from table inventory in stadtluzernio app with status published
  stadtluzernio.budibase.search_for_rows:
    hostname: BUDIBASE_HOST
    token: BUDIBASE_TOKEN
    app: BUDIBASE_APP
    query: BUDIBASE_QUERY
    status: published

- name: Get all rows with colume os_famoly_name value equal windows from table inventory in stadtluzernio app with status published
  stadtluzernio.budibase.search_for_rows:
    hostname: BUDIBASE_HOST
    token: BUDIBASE_TOKEN
    app: BUDIBASE_APP
    query: BUDIBASE_QUERY

    status: published
    conditions:
      query:
        equal:
          os_family_name: windows
'''

RETURN = '''
json:
  description: App info, table info and content from selectet row
  type: dict
  returned: always
  contains::
    app_info:
      description: App info (_id, name, status, ...)
      type: dict
      returned: success
    table_info:
      description: Table info (_id, name, schema, ...)
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
      argument_spec=bb_specs.bb_search_for_rows(),
      supports_check_mode=False
  )

  api_client = bb_api.create_client(module)

  bb_app        = module.params.get("app")
  bb_status     = module.params.get("status")
  bb_table      = module.params.get("table")
  bb_conditions = module.params.get("conditions")

  try:
    api_response                = {}
    api_response['app_info']    = api_client.get_app_info_by_name(bb_app, bb_status)
    api_response['table_info']  = api_client.get_table_info_by_name(bb_table, api_response['app_info']['_id'], api_response['app_info']['name'])
    api_response['content']     = api_client.get_table_rows(api_response['app_info']['_id'], api_response['table_info']['_id'] , bb_conditions)
    
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