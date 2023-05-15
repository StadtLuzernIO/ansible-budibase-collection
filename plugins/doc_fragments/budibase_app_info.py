from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment:

    DOCUMENTATION = r'''
    options:
        app:
            description: The name of the app which this request is targeting.
            type: str
            required: true
        status:
            description: App status published / development
            type: str
            default: published
            choices:
              - published
              - development
    '''