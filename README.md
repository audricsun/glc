# glc
A command line tool for Gitlab.
Aim to provide a centralized configuration file to archive/backup/restore Gitlab settings/namespace/groups/users/repositories.

[![PyPI version](https://badge.fury.io/py/glc.svg)](https://badge.fury.io/py/glc)
[![PyPI](https://img.shields.io/pypi/pyversions/glc.svg)](https://pypi.org/project/glc/)
[![Actions Status](https://github.com/evinoca/glc/workflows/CI/badge.svg)](https://github.com/evinoca/glc/actions?query=workflow%3ACI)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=glc&metric=alert_status)](https://sonarcloud.io/dashboard?id=glc)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=glc&metric=coverage)](https://sonarcloud.io/dashboard?id=glc)
[![Coverage Status](https://coveralls.io/repos/github/evinoca/glc/badge.svg?branch=master)](https://coveralls.io/github/evinoca/glc?branch=master)
[![Readthedoc](https://readthedocs.org/projects/gli/badge/?version=latest)](https://gli.readthedocs.io/en/latest/)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/evinoca/glc.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/evinoca/glc/alerts/)

## Background
I am running administrator role for my teams, and it's time wasting to browse and click for create/update roles/projects or setup webhooks/intetgrations for Gitlab projects. Though there are few choices but none of them seems handy enough for me. Let's see if I can make a better one on my own.

> **Note: This project is basically only a mix of ideal concepts and still under developing.**


## Installation


### Pip/Pipx
```bash
# Install over pip
pip install --upgrade glc
# It's even better with pipx
pipx install glc
```

## Usage
```
glc config init
```

## Developing
Take a look at [Develop](https://glc.readthedocs.io/en/latest/develop/)

## Contribute
Wherever there is any issue or suggestions, feel free to raise issus [here](https://github.com/evinoca/glc/issues).

## Reference
For more detail, check [Document](https://glc.readthedocs.io/en/latest/).
