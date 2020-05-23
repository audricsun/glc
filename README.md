# gli - Simple GitLab Command line interface(Draft)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=evinoca_MyCli&metric=alert_status)](https://sonarcloud.io/dashboard?id=evinoca_MyCli) [![Coverage Status](https://coveralls.io/repos/github/evinoca/gli/badge.svg?branch=master)](https://coveralls.io/github/evinoca/gli?branch=master)

I am running administrator role for my teams, and it's time wasting to browse and click for create/update roles/projects or setup webhooks/intetgrations for Gitlab projects. Though there are few choices but none of them seems handy enough for me. Let's see if I can make a better one on my own.

> This whole project is built based on the Gitlab administration practice from my work. Not sure if this is a good practice, but it works for my place.

# Roadmap
1. [ ] Multi-level commands/sub-commands design
2. [ ] Configuration management
3. [ ] API wrapper for Gitlab
4. [ ] First Demo for create conf from remote over `gli fetch`
5. [ ] When all above are done. Then i will think about it.


# Ideas
## Quick-Start
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
## Profiles
```
gli profile ls
gli profile update
gli profile desc
gli config ls
gli config desc
```
## Templates
```
gli template ls
gli template new
gli template desc
gli template update
gli template rm
```

## Repository
```
gli repo ls project_name
gli repo clone project_name --workspace=~/workspace/company
gli repo fork project_name
gli repo desc project_name
gli repo update project_name key=value

gli repo regs project_name
gli repo imgs project_name
gli repo img-rm project_name
gli repo imgs-purge project_name --before 2M --no-prompt


gli repo archive project_name
gli repo rm project_name
gli repo rename project_name
gli repo create project_name --namespace company_ns
```

## Group/User
```
gli user ls user_name
gli user desc user_name
gli user create --name="new guy" --mail=new_guy@company.coms
gli group ls developer
gli user update --id 123 --group=group1,group2,group3
```

## Bulk Update
```
gli status
gli diff
gli fetch
gli pull
gli push

```
