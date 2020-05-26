# Welcome to Document of gli
Gli (Gitlab Cli) is a wrapper based on python-click and Gitlab HTTP API v4.
It's aim to provide a centralized configuration file to archive/backup/restore settings of Gitlab.

[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=evinoca_MyCli&metric=alert_status)](https://sonarcloud.io/dashboard?id=evinoca_MyCli) [![Coverage Status](https://coveralls.io/repos/github/evinoca/gli/badge.svg?branch=master)](https://coveralls.io/github/evinoca/gli?branch=master) [![Readthedoc](https://readthedocs.org/projects/gli/badge/?version=latest)](https://gli.readthedocs.io/en/latest/)

## Background
I am running administrator role for my teams, and it's time wasting to browse and click for create/update roles/projects or setup webhooks/intetgrations for Gitlab projects. Though there are few choices but none of them seems handy enough for me. Let's see if I can make a better one on my own.

> The whole project is built based on the Gitlab administration practice from my work.

## Installation


### Pip/Pipx
```
gli init --host https://git.company.com --token=xxxx
Do you want to create configuration files at /usr/username/.gli/git.company.com Y/n ? Yes
Creating configuration file...
Authentication...
Fetching namespaces...
Fetch project list...
Fetching user list...
Fetching group list...
Done!
```

### Docker
TBD

### Curl(TBD)
TBD

### Homebrew(TBD)
TBD

## Quick-Start

### Initial Configuration
TBD

### Profile/Credentials
TBD

### Sync-Up
TBD
