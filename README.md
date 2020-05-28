# glc
A command line tool for Gitlab.
Aim to provide a centralized configuration file to archive/backup/restore Gitlab settings/namespace/groups/users/repositories.

[![Actions Status](https://github.com/evinoca/glc/workflows/CI/badge.svg)](https://github.com/evinoca/glc/actions?query=workflow%3ACI) [![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=evinoca_MyCli&metric=alert_status)](https://sonarcloud.io/dashboard?id=evinoca_MyCli) [![Coverage Status](https://coveralls.io/repos/github/evinoca/glc/badge.svg?branch=master)](https://coveralls.io/github/evinoca/glc?branch=master) [![Readthedoc](https://readthedocs.org/projects/glc/badge/?version=latest)](https://glc.readthedocs.io/en/latest/)

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
