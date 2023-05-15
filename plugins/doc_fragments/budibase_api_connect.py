from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment:

    DOCUMENTATION = r'''
    options:
        hostname:
            type: str
            description:
                - Budibase Hostname (FQDN).
        token:
            type: str
            description:
                - Token to authenticate Budibase.
                - Ansible should never log or display this value.
        validate_certs:
            type: bool
            description: If false, SSL certificates will not be validated
            default: true
    '''