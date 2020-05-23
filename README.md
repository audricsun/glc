# gli - A Draft GitLab Command line interface
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=evinoca_MyCli&metric=alert_status)](https://sonarcloud.io/dashboard?id=evinoca_MyCli) [![Coverage Status](https://coveralls.io/repos/github/evinoca/gli/badge.svg?branch=master)](https://coveralls.io/github/evinoca/gli?branch=master)

I am running administrator role for my teams, and it's time wasting to browse and click for create/update roles/projects or setup webhooks/intetgrations for Gitlab projects. Though there are few choices but none of them seems handy enough for me. Let's see if I can make a better one on my own.

> This whole project is built based on the Gitlab administration practice from my work. Not sure if this is a good practice, but it works for my place. 

# Roadmap
1. [ ] Cli structure
2. [ ] User profile management
3. [ ] Cli entry for `gli init`


# Quick-Start

```
$ gli init
```
There will be prompt for gitlab `host`, `port`, `admin-token`

Configuration files will be created based on user input.

`ls -al ~/.gli`
```
gli.yaml
credential.yml
${gitlab_host}/
    /projects/
    /groups/
    /users/
```
# Examples
## General
```
gli fetch
gli pull
gli push
gli diff
gli apply -c $path_to_config_files
gli --profile my_other_gitlab fetch
```


## Project
```
gli project ls project_name
gil project desc project_name
gli project update project_name key=value
gli diff
gli push
gli reset
```

## Group/User
```
gli user ls user_name
gli user desc user_name
```
