# Concept
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
