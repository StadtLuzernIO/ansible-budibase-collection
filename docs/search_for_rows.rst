.. _stadtluzernio.budibase.search_for_rows_module:


*****************************
StadtLuzernIO.budibase.search_for_rows
*****************************

**Can select table which have been created in a Budibase app**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
Can select table which have been created in a Budibase app.


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
                    <b>table</b>
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
                        The name of the table which this request is targeting
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
                        Use table conditions
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>query</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Table query
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>string</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        A map of field name to the string to search for, this will look for rows that have a value starting with the string value
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>fuzzy</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        A fuzzy search, only supported by internal tables.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>range</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Searches within a range, the format of this must be columnName -> [low, high].
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>equal</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Searches for rows that have a column value that is exactly the value set.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>notEqual</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Searches for any row which does not contain the specified column value.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>empty</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Searches for rows which do not contain the specified column. The object should simply contain keys of the column names, these can map to any value.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>notEmpty</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Searches for rows which have the specified column.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>oneOf</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Searches for rows which have a column value that is any of the specified values. The format of this must be columnName -> [value1, value2].
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>paginate</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">boolean</span>
                    </div>
                </td>
                <td>
                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                        <li>yes</li>
                        <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                    </ul>
                </td>
                <td>
                    <div>
                        Enables pagination, by default this is disabled.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>bookmark</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        If retrieving another page, the bookmark from the previous request must be supplied.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td colspan="3">
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
                        The maximum number of rows to return, useful when paginating, for internal tables this will be limited to 1000, for SQL tables it will be 5000.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td colspan="3">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>sort</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        A set of parameters describing the sort behaviour of the search.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>order</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                    <ul style="margin: 0; padding: 0"><b>Choices:</b>
                        <li>ascending</li>
                        <li>descending</li>
                    </ul>
                </td>
                <td>
                    <div>
                        The order of the sort, by default this is ascending.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>column</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        The name of the column by which the rows will be sorted.
                    </div>
                </td>
            </tr>
            <tr>
                <td class="elbow-placeholder"></td>
                <td class="elbow-placeholder"></td>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>type</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                    <div>
                        Defines whether the column should be treated as a string or as numbers when sorting.
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

    - name: "SELECT * FROM inventory WHERE os_family_name == window"
      stadtluzernio.budibase.search_for_rows:
        hostname: https://fibac.budibase.app
        token: 93213c631817d5127b943417b8b6fe65-3906db218002c32a5712fab9327db0e9355626875be3d907e607b95c3e1a4b814f5d67c0a422
        app: stadtluzernio
        table: inventory
        status: published
        validate_certs: false
        conditions:
          query:
            equal:
              os_family_name: windows
              hostname: vm-demo-006


Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
        <tr>
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
            <td colspan="1">
                <div class="ansibleOptionAnchor" id="return-"></div>
                <b>table_info</b>
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
                    &nbsp;&nbsp;"_id": "ta_144efa057b6443c8be51552f9952b6be",<br/>
                    &nbsp;&nbsp;"name": "inventory",<br/>
                    &nbsp;&nbsp;"primaryDisplay": "Auto ID",<br/>
                    &nbsp;&nbsp;"schema": {<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"Auto ID": {<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"autocolumn": true,<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"constraints": {<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"numericality": {<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"greaterThanOrEqualTo": "",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"lessThanOrEqualTo": ""<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"presence": false,<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"type": "number"<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;},<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"icon": "ri-magic-line",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"lastID": 6,<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"name": "Auto ID",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"subtype": "autoID",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"type": "number"<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;},<br/>
                    &nbsp;&nbsp;...<br/>
                    }
                </div>
            </td>
        </tr>
                <tr>
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
                    &nbsp;&nbsp;&nbsp;&nbsp;"Auto ID": 6,<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"Created At": "2023-04-19T13:30:52.464Z",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"Created By": [<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"_id": "ro_ta_users_us_feca9e7375e24c7887cf1f8f548cc003",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"primaryDisplay": "demo_name@domain.ch"<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;],<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"Updated At": "2023-04-19T13:30:52.464Z",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"Updated By": [<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"_id": "ro_ta_users_us_feca9e7375e24c7887cf1f8f548cc003",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"primaryDisplay": "demo_name@domain.ch"<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;],<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"_id": "ro_ta_144efa057b6443c8be51552f9952b6be_046243740d734956b751dc29ce25adb6",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"createdAt": "2023-04-19T13:30:52.808Z",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"description": "Demo Host 006",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"domain_name": "domain.ch",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"environment": "develop",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"hostname": "vm-demo-006",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"os_family_name": "windows",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"state": "destroyed",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"tableId": "ta_144efa057b6443c8be51552f9952b6be",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"type": "row",<br/>
                    &nbsp;&nbsp;&nbsp;&nbsp;"updatedAt": "2023-04-19T13:30:52.808Z"<br/>
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