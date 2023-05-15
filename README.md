#Ansible Collection: StadtLuzernIO.Budibase

## Overview
This repository contains Budibase Ansible Modules, which one can use with Ansible to work with the [Budibase][budibase].

[budibase]: https://www.budibase.com

For general information about Ansible, visit the [GitHub project page][an-github].

[an-github]: https://github.com/ansible/ansible

## What is Budibase
Budibase is an all-in-one open-source low-code platform for building, designing, and automating business apps, such as; admin panels, forms, internal tools, client portals, and more. Before Budibase, it could take developers weeks to build simple CRUD apps; with Budibase, building CRUD apps takes minutes.


### Get started with Budibase
When getting started with Budibase, you have two options:

1. Use Budibase Cloud - Budibase host your apps. This is the easier, faster option. No docs are required to get started.
2. Self-host Budibase - you host your apps. You can find further instructions below.

#### Cloud
The onboarding process is simple, minimal, and takes seconds. No docs are required.

* [Get started with Budibase Cloud](https://account.budibase.app/register?_gl=1*le1tx5*_ga*NDYzMDAyNTA5LjE2NzE0NDc0NDU.*_ga_2JVG0FWDDG*MTY4MzgwNTkxMi42NC4xLjE2ODM4MDc5NjcuNjAuMC4w)

#### Self-Hosting
Deploy Budibase self-hosted in your existing infrastructure, using Docker, Kubernetes, and Digital Ocean.
* [Docker - single ARM compatible image](https://docs.budibase.com/docs/docker)
* [Docker Compose](https://docs.budibase.com/docs/docker-compose)
* [Kubernetes](https://docs.budibase.com/docs/kubernetes-k8s)
* [Digital Ocean](https://docs.budibase.com/docs/digitalocean)
* [Portainer](https://docs.budibase.com/docs/portainer)

## Prerequisites
The below prerequisites are needed on the local Ansible controller node that executes this ansible collection.

* Budibase [Budibase Documentation](https://docs.budibase.com/docs)
* Ansible >= 2.10.x [Ansible Installation Documentation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
* Python3 >= 3.6.x [Python Documentation](https://www.python.org/downloads/)


## Installation and Usage

### Installing the Collection from Ansible Galaxy
Before using the StadtLuzernIO budibase collection, you need to install the collection with the ansible-galaxy cli:
```sh
ansible-galaxy collection install slu.budibase
```

You can also include it in a requirements.yml file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:
```sh
# requirements.yml
collections:
  - name: stadtluzernio.budibase
```

### Use this Collection in a AWX Project

#### Project Folder
```sh
.
└── project_name
    ├── collections
    │   └──  requirements.yml
    ├── PLAYBOOK_NAME_01.yml
    ├── PLAYBOOK_NAME_02.yml
    └── PLAYBOOK_NAME_...yml
```

#### Credential Type
Credential type to add the Budibase authentication information as AWX credential.
```yaml
awx_credential_type_settings:
  - name: Budibase API
    description: Credential Type for Budibase API
    state: present
    kind: cloud
    inputs:
      fields:
        - id: budibase_host
          type: string
          label: Host
          help_text: Budibase FQDN
        - id: budibase_token
          type: string
          label: API Token
          secret: true
          help_text: budibase token to use
      required:
        - budibase_host
        - budibase_token
    injectors:   
      env:
        BUDIBASE_HOST: '{{ budibase_host }}'
        BUDIBASE_TOKEN: '{{ budibase_token }}'
```
<p>
  <img alt="Budibase" src="https://github.com/StadtLuzernIO/ansible-budibase-collection-private/blob/main/docs/assets/awx_credential_type_settings.png" width="1000" />
</p>

#### Credential
```yaml
awx_credentials_settings:
  - name: Budibase Credential
    credential_type: Budibase API
    organization: My Organisation
    inputs:
      budibase_host: my-budibase-host.my-domain.ch
      budibase_token: afjajsfjsacvksd89rjdd32d02dk20dk2d
```
<p>
  <img alt="Budibase" src="https://github.com/StadtLuzernIO/ansible-budibase-collection-private/blob/main/docs/assets/awx_credentials_settings.png" width="1000" />
</p>

#### Job Template
Add the credentials to the jop template, in which you use this collection.

<p>
  <img alt="Budibase" src="https://github.com/StadtLuzernIO/ansible-budibase-collection-private/blob/main/docs/assets/awx_job_template_settings.png" width="1000" />
</p>


## Module Variables

All modules support the following variable definitions. You may either explicitly define the value on the task or let Ansible fallback to an environment variable to use the same value across all tasks.

Environment variables are ignored if the module variable is defined for a task.

| Module Variable | Environment Variable | Description                                                                                           |
|----------------:|----------------------|-------------------------------------------------------------------------------------------------------|
|      `hostname` | `BUDIBASE_HOST`      | FQDN of a Budibase host.                                                                              |
|         `token` | `BUDIBASE_TOKEN`     | Your individual API key, this will provide access based on the configured RBAC settings of your user. |


## Included content

### Modules

Name | Description
--- | ---
[slu.budibase.execute_a_query](https://github.com/StadtLuzernIO/ansible-budibase-collection-private/blob/main/docs/execute_a_query.rst)|Can executed queries which have been created in a Budibase app                                                |
[slu.budibase.search_for_rows](https://github.com/StadtLuzernIO/ansible-budibase-collection-private/blob/main/docs/search_for_rows.rst)|Get rows from a table in a Budibase app                                                                       |


## Demo Example

https://fibac.budibase.app/app/stadtluzernio#/INVENTORY

<p>
  <img alt="Budibase" src="https://github.com/StadtLuzernIO/ansible-budibase-collection-private/blob/main/docs/assets/budibase_demo_inventory.png" width="1000" />
</p>

```yaml
  - name: "SELECT * FROM inventory WHERE os_family_name == window"
    stadtluzernio.budibase.search_for_rows:
      hostname: fibac.budibase.app
      token: 93213c631817d5127b943417b8b6fe65-3906db218002c32a5712fab9327db0e9355626875be3d907e607b95c3e1a4b814f5d67c0a422
      app: stadtluzernio
      table: inventory
      status: published
      validate_certs: false
      conditions:
        query:
          equal:
            os_family_name: windows
```