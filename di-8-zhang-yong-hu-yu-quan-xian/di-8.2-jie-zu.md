# Section 8.2 Users and groups


#__CODESPAN_0_ CREATE USER

- CREATE A COMMON USER (KNOWN AS ___CODESPAN_0_) AND ADD IT TO __CODESPAN_1_GROUP:

```sh
# adduser -g video -s sh -w yes
# Username: ykla
```

example: create a user named test and add it to the wheel group setting its default shell is sh:

```sh
root@ykla:/ #  adduser
Username: test # 用户名
Full name:  # 全名，可留空
Uid (Leave empty for default): # UID 设置，可留空
Login group [test]: # 登录组
Login group is test. Invite test into other groups? []: wheel # 设置要加入的组，多个用空格隔开，可留空
Login class [default]: # 登录分类，可留空
Shell (sh csh tcsh git-shell bash rbash nologin) [sh]: sh  # 除非手动设置默认 shell，否则 shell 为 sh
Home directory [/home/test]: #指定家目录
Home directory permissions (Leave empty for default): # 指定家目录权限
Enable ZFS encryption? (yes/no) [no]: # 是否使用 zfs 加密
Use password-based authentication? [yes]:  # 是否使用密码
Use an empty password? (yes/no) [no]:   # 是否空密码
Use a random password? (yes/no) [no]:   # 是否随机密码
Enter password: # 输入密码
Enter password again: # 重复输入密码
Lock out the account after creation? [no]: # 锁定账号？
Username   : test
Password   : *****
Full Name  :
Uid        : 1002
ZFS dataset : zroot/home/test
Class      :
Groups     : test wheel
Home       : /home/test
Home Mode  :
Shell      : /bin/sh
Locked     : no
OK? (yes/no): yes # 检查有错误否
adduser: INFO: Successfully created ZFS dataset (zroot/home/test).
adduser: INFO: Successfully added (test) to the user database.
Add another user? (yes/no): no # 还需要创建另一个账号吗？
Goodbye!
```


#__CODESPAN_0_ DELETE USER AND __CODESPAN_1_ PASSWORD CHANGE

- TO REMOVE THE USER. LIKE THE ___CODESPAN_0_ COMMAND, IT IS ALSO INTERACTIVE. THIS COMMAND HAS PARAMETERS __CODESPAN_1 AND LISTS USERS

Example:

```sh
# rmuser -y test1 test2 # 同时删除用户 test1 和 test2
Removing user (test1): mailspool home passwd.
Removing user (test2): home passwd.

```

PARAMETER __CODESPAN_0_ IS USED TO SKIP THE CONFIRMATION STEP。

- THE __CODESPAN_0_ COMMAND OPENS AND CHANGES THE SPECIFIED USER INFORMATION IN THE __CODESPAN_1 EDITOR, AND DEFAULTS ON THE CURRENT USER IF THE USER IS NOT SPECIFIED。

>** Skills**
>
>__CODESPAN_0_ REPLACES THE EDITOR WITH A SIMPLER __CODESPAN_1_。

COMMON PARAMETER: __CODESPAN_0_ FOR LOGIN ENVIRONMENT

Example:

```sh
# chpass -s sh test1 # 修改用户 test1 的登录环境为 /bin/sh
chpass: user information updated
# export EDITOR=/usr/bin/ee 
# chpass # 以 ee 方式打开当前用户信息进行修改
# passwd # 修改用户密码，如不指定用户则默认为当前用户。
```

the root user can change the password for all users。

#__CODESPAN_0_COMMAND

In FreeBSD, the user and group can be managed by __CODESPAN_0_ command:

- CREATE __CODESPAN_0_GROUP AND ADD __CODESPAN_1_ TO __CODESPAN_2_ AND __CODESPAN_3_GROUP:

```sh
# pw groupadd admin
# pw usermod ykla -G admin,wheel
```

Check it out:

```
root@ykla:~ # id ykla
uid=1001(ykla) gid=1001(ykla) groups=1001(ykla),0(wheel),1002(admin)
```

- CREATE __CODESPAN_0_GROUP WITH ONLY __CODESPAN_1_ USER:

```sh
# pw groupadd wheel
# pw groupmod wheel -m root
```

- REMOVE USER_CODESPAN_1_:

```sh
# pw groupmod admin -d ykla
```

- DELETE GROUP __CODESPAN_0_:

```sh
# pw groupdel admin
```

---|---

DISTINCTION BETWEEN THE COMPETENCE OF CODESPAN_0_ AND CODESPAN_1_:

- __CODESPAN_0, with the permission of the management system (as is the default configuration for sudo), can use __CODESPAN_1_。
- ___ CODESPAN_0, Super Administrator Permission (the name is derived from the slang big wiel, the big man)。


## __CODESPAN_0_COMMAND

For new users

Example:

```sh
# pw useradd test1 # 创建用户 test1，uid 系统默认，test1 组，登录环境 /bin/sh，未创建主目录
# pw groupadd test2 # 创建主组 test2
# pw useradd test2 -u 1200 -m -d /tmp/test -g test2 -G wheel -s sh -c test2 # 创建用户 test2，uid 为 1200，创建主目录，主目录为 /tmp/test，主组为 test2，有管理员权限（Wheel），登录环境 /bin/sh，全名 test2
# echo password | pw useradd test3 -h 0 # 创建用户 test3，同时设置密码为 password
```

## __CODESPAN_0_COMMAND

To modify user information, common parameters:

__CODESPAN_0_, rename the user with reference to the userad sub-command for other parameters。

Example:

```sh
# pw usermod test1 -l test2 # 把用户 test1 重命名为 test2
```

## __CODESPAN_0_COMMAND

to remove users, common parameters:

`-r`, DELETE THE USER WHILE DELETING THE USER'S HOME DIRECTORY AND ALL RELATED INFORMATION; IF THIS PARAMETER IS NOT USED, THE INFORMATION IS KEPT AND ONLY THE USER IS DELETED

Example:

```sh
# pw userdel test2 -r
```

## __CODESPAN_0_COMMAND

to display user information, for example:

```sh
# pw usershow test2
test2:$6$FkxPcs2y.Y8cxyuj$kVDoV1LC.IWKGlSitll3oLArF18aHQYID0JYE.TUuD0YFgba.c7MbGs3xLnmpCZyu1nVKHhNqW2X7a57qN0xg/:1201:1201::0:0:User &:/home/test1:/bin/sh
```

## __CODESPAN_0_COMMAND

RETURNS THE NEXT UID AND GID AVAILABLE, FOR EXAMPLE:

```sh
# pw usernext
1202:1202
```

## __CODESPAN_0_COMMAND

Locked account number. Locked account number is not available

Example:

```sh
# pw lock test2
```

## __CODESPAN_0_COMMAND

Unlock the account. Unlock the account

Example:

```sh
# pw unlock test2
```

## __CODESPAN_0_COMMAND

to create a new group。

Example:

```sh
# pw groupadd test -g 1200 # 创建组 test。gid 为 1200；gid 与 uid 有所不同
# pw groupadd test5 -M test1,test2 # 创建组 test5。成员有 test1 和 test2
```

## __CODESPAN_0_COMMAND

To modify group information, common parameters:

__CODESPAN_0, SPECIFY A NEW __CODESPAN_1_

__CODESPAN_0_, RENAME GROUP NAME

`-M`, REPLACE THE LIST OF EXISTING GROUP MEMBERS, MULTIPLE COMMAS SEPARATED

__CODESPAN_0_, ADDING NEW MEMBERS TO THE LIST OF EXISTING GROUP MEMBERS

OTHER PARAMETERS REFER TO THE __CODESPAN_0_ COMMAND。

Example:

```sh
# pw groupmod test -g 1300 # 修改 test 组的 gid 为 1300
# pw groupmod test -l test2 # test 组重命名为 test2
# pw groupmod test5 -M test1 # 设置组 test5 的成员为 test1，原有成员会被删除！
# pw groupmod test5 -m test3 # 为组 test5 新增成员 test3
```

## __CODESPAN_0_COMMAND

To remove groups

Example:

```sh
# pw groupdel test5
```

## __CODESPAN_0_COMMAND

To display group information

Example:

```sh
# pw groupshow test5
test5:*:1202:test1
```

## __CODESPAN_0_COMMAND

CAN RETURN THE NEXT AVAILABLE __CODESPAN_0_

Example:

```sh
# pw groupnext
1301
```

# References

- [FreeBSD introductory notes] (https://lvvv.me/posts/221/04/19_freebsd_101/), by lvv.me
