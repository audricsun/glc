## Group/User
```
glc user ls user_name
glc user desc user_name
glc user create --name="new guy" --mail=new_guy@company.coms
glc group ls developer
glc user update --id 123 --group=group1,group2,group3
```

```
glc user ls --group=".*auth-users.*" --since=20200101 --format "{id username email settings.public_email}"|awk '{print $1}'|glc group `some group`
```
