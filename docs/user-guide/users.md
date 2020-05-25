## Group/User
```
gli user ls user_name
gli user desc user_name
gli user create --name="new guy" --mail=new_guy@company.coms
gli group ls developer
gli user update --id 123 --group=group1,group2,group3
```

```
gli user ls --group=".*auth-users.*" --since=20200101 --format "{id username email settings.public_email}"|awk '{print $1}'|gli group `some group`
```
