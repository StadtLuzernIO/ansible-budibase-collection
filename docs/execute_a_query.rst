.. _stadtluzernio.budibase.execute_a_query_module:


*****************************
StadtLuzernIO.budibase.execute_a_query
*****************************

**Can executed queries which have been created in a Budibase app**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
Can executed queries which have been created in a Budibase app.


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="4">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>hostname</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                        / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Budibase Hostname (FQDN)
                    </div>
                </td>
            </tr>
            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>token</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                        / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Token to authenticate Budibase
                    </div>
                </td>
            </tr>
            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>validate_certs</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                        <li>no</li>
                        <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                    </ul>
                </td>
                <td>
                    <div>
                        Allows connection when SSL certificates are not valid. Set to <code>false</code> when certificates are not trusted.
                    </div>
                    <div>
                        If the value is not specified in the task, the value of environment variable <code>BUDIBASE_VALIDATE_CERTS</code> will be used instead.
                    </div>
                </td>
            </tr>
            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>app</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                        / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        The name of the app which this request is targeting
                    </div>
                </td>
            </tr>
            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>status</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                        / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                        <li>development</li>
                        <li><div style="color: blue"><b>published</b>&nbsp;&larr;</div></li>
                    </ul>
                </td>
                <td>
                    <div>
                        App status published / development
                    </div>
                </td>
            </tr>
            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>query</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                        / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        The name of the query to execute
                    </div>
                </td>
            </tr>
            <tr>
            <tr>
                <td colspan="4">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>conditions</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Use query conditions
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>parameters</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        This contains the required parameters for the query, this depends on query type, setup and bindings.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>pagination</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        For supported query types (currently on REST) pagination can be performed using these properties.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>page</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        The page which has been returned from a previous query
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>limit</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">integer</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        The number of rows to return per page
                    </div>
                </td>
            </tr>
    </table>

Notes
-----

.. note::
   - All modules requires API access to the Budibase app.


Examples
--------

.. code-block:: yaml

    - name: "SELECT * FROM BUDIBASE_QUERY_NAME WHERE BDUIBASE_BINDING_NAME == VALUE"
      stadtluzernio.budibase.search_for_rows:
        hostname: BUDIBASE_HOSTNAME
        token: BUDIBASE_TOKEN
        app: BUDIBASE_APP
        query: BUDIBASE_QUERY_NAME
        status: published
        conditions:
          parameters:
            BDUIBASE_BINDING_NAME: BDUIBASE_BINDING_VALUE


Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
        <tr>
        <td colspan="2">
                <div class="ansibleOptionAnchor" id="return-"></div>
                <b>json</b>
                <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">dictionary</span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>
                    Return json dictionary
                </div>
            </td>
        </tr>
        <tr>
            <td class="elbow-placeholder"></td>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-"></div>
                <b>app_info</b>
                <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">dictionary</span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>
                    Dictionary with Budibase app infos
                </div><br/>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">
                    {<br/>
                    &nbsp;&nbsp;"_id": "app_fibac_5790b94023c44995ba66df18ce421b2f",<br/>
                    &nbsp;&nbsp;"createdAt": "2023-04-19T10:57:00.144Z",<br/>
                    &nbsp;&nbsp;"name": "stadtluzernio",<br/>
                    &nbsp;&nbsp;"status": "published",<br/>
                    &nbsp;&nbsp;"tenantId": "fibac",<br/>
                    &nbsp;&nbsp;"updatedAt": "2023-04-24T12:07:54.990Z",<br/>
                    &nbsp;&nbsp;"url": "/stadtluzernio",<br/>
                    &nbsp;&nbsp;"version": "2.5.2"<br/>
                    }
                </div>
            </td>
        </tr>
        <tr>
            <td class="elbow-placeholder"></td>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-"></div>
                <b>query_info</b>
                <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">dictionary</span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>
                    Dictionary with Budibase table infos
                </div><br/>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">
                    {<br/>
                    &nbsp;&nbsp;"_id": "query_datasource_plus_83e861649ab940a3b390113352d7307e_808d59c6e42b459884eedae516b379b3",<br/>
                    &nbsp;&nbsp;"datasourceId": "datasource_plus_83e861649ab940a3b390113352d7307e",<br/>
                    &nbsp;&nbsp;"fields": {<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"sql": "WITH \napi_input (\n  BDUIBASE_BINDING_NAME\n) AS (\n  VALUES (\n    ({{BDUIBASE_BINDING_NAME}}::text)\n  )\n)\nSELECT\n\tesy.V,\n\tsad.domain_name\n\nFROM\n\tentry_sys AS esy\nLEFT JOIN shared_sys AS ssy\n\tON ssy.entry_sys_id = esy.entry_sys_id\nINNER JOIN sys_tier AS sti\n\tON sti.sys_tier_id = esy.sys_tier_id\n\tOR sti.sys_tier_id = ssy.sys_tier_id\nINNER JOIN domain AS sad\n\tON sad.domain_id = esy.domain_id\nINNER JOIN deployment AS zde\n\tON zde.deployment_id = sti.deployment_id\nWHERE \n\tzde.BDUIBASE_BINDING_NAME = (SELECT BDUIBASE_BINDING_NAME FROM api_input)"<br/>
                    &nbsp;&nbsp;},<br/>
                    &nbsp;&nbsp;"name": "BUDIBASE_QUERY_NAME",<br/>
                    &nbsp;&nbsp;"parameters": [<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;{<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"default": "test-domain",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "BDUIBASE_BINDING_NAME"<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;}<br/>
                    &nbsp;&nbsp;],<br/>
                    &nbsp;&nbsp;"queryVerb": "read",<br/>
                    &nbsp;&nbsp;"readable": true,<br/>
                    &nbsp;&nbsp;"schema": {<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"name": {<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "name",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"type": "string"<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;},<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"domain_name": {<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "domain_name",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"type": "string"<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;}<br/>
                    &nbsp;&nbsp;},<br/>
                    &nbsp;&nbsp;"transformer": "return data"<br/>
                    &nbsp;&nbsp;}<br/>
                    }
                </div>
            </td>
        </tr>
        <tr>
            <td class="elbow-placeholder"></td>
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-"></div>
                <b>content</b>
                <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                <div style="font-size: small">
                  <span style="color: purple">list</span>
                  / <span style="color: purple">elements=dictionary</span>
                </div>
            </td>
            <td>success</td>
            <td>
                <div>
                    Dictionary with Budibase app infos
                </div><br/>
                <div style="font-size: smaller"><b>Sample:</b></div>
                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">
                    [<br/>
                    &nbsp;&nbsp;{<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"name": "demo",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"domain_name": "domain.ch"<br/>
                    &nbsp;&nbsp;}<br/>
                    ]
                </div>
            </td>
        </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~