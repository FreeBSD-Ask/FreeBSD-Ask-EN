# Section 8.2 Users and groups


# `adduser ' Create User

- Create an ordinary user (user name `ykla ' ) and add it to the `video ' group:

```sh '
♪ Adduser-g video-ssh-w yes ♪
Username: ykla
````

Example: Create a user named test and add it to the Wheel group setting its default shell is sh:

```sh '
#adduser
Username: test# username
Full name: # Full name, leave empty
Uid (Leave empty for default): #UID settings, leave empty
Login group [test]: # Login group
Login group is best. Invite test into other groups? [: sheel #] Set groups to be added, multiple separated by spaces and leave empty
Login class [default]: # Login classification, leave empty
Shell (sh csh tcsh git-shell rbash nologin)
Home directory [/home/test]: #Appointer directory
Home directory missions (Leave empty for default): # Specifie home directory privileges
Enable ZFS encryption? (yes/no) [no]: # Whether to use zfs encryption
Use password-based access? [yes]:
Use an empty password? (yes/no)
Use a random password? (yes/no)
Enter password: # Enter password
Enter password again:
Lock out the account after creation?
Usename: test
Password: *****
Full Name:
Uid: 1002
ZFS dataset: zroot/ home/test
Class:
Groups: best news
Home: /home/test
Home Mode:
Shell: /bin/sh
Locked: no
OK? (yes/no): Yes # Check for errors
(Zroot/home/test).
IFO:
Add another user? (yes/no): No.
Goodbye!
````


# `rmuser ' Delete user and `passwd ' password changes

- to remove the user. Like the `adduser ' command, it is also interactive. The command has parameters `-y ' and lists users,

Example:

```sh '
# rmuser-y test1 test2
Removing user (test 1): mailspool home passwd.
Removing user (test 2: home passwd.

````

Parameter `-y ' is used to skip the confirmation step.

- `chpass ' command to open and modify specified user information in `vi ' editor or default to the current user if the user is not specified.

>** Skills**
>
> `export EDITOR=/usr/bin/ee ' may replace the editor with a simpler `ee ' .

Common parameter: `-s ' for login environment

Example:

```sh '
#chpass -sh test1
chapass: user information updating
#export EDITOR=/usr/bin/ee
#chpass
#passwd # Change the user password and default to the current user if the user is not specified.
````

The root user can change the password for all users.

# `pw ' Command

In FreeBSD, `pw ' commands can be used to manage users and groups:

- Create `admin ' groups and add user `ykla ' to both `admin ' and `wheel ' groups:

```sh '
# Pw grouped admin
♪ Pw usermod ykla-g admin, wheel ♪
````

Check it out:

````
# id ykla
uid = 1001 (ykla) gid = 1001 (ykla) groups = 1001 (ykla), 0 (wheel), 1002 (admin)
````

- Create `wheel ' group with only `root ' users:

```sh '
# Pw grouped #
?
````

- Remove user `ykla ' from the `admin ' group:

```sh '
♪ Pw groupmod admin-d ykla
````

- Delete the `admin ' group:

```sh '
# Pw groupdel admin
````

I don't...

Distinction between `admin ' and `wheel ' competence:

- `admin ' , having the competence of a management system (as is the default configuration of sudo), may use the `sudo ' command.
- `wheel ' , Super Administrator Permission (name derived from slang big wheel, i.e. the big man).


# # `pw userad ' command

For new users

Example:

```sh '
# pw userradttest1 # Create user test1,uid default, test1 group, login environment /bin/sh, no home directory created
# pw groupd test2
# pw userradd test2-u 1200-m-d/tmp/test2-g test2-G wheel-sh-c test2 # Create user test2-uid for 1200, create home directory with /tmp/test, main group with test2 with administrator privileges (Weel), login environment/bin/sh, full name test2
# echo password | pw useradd test3-h0 # create user test3 and set password to password
````

# # `pw usermod ' command

To modify user information, common parameters:

`-l`, rename the user with reference to the userad sub-command for other parameters.

Example:

```sh '
# pw usermod test1-l test2
````

# # `pw userdel ' command

to remove users, common parameters:

`-r ' , delete the user while deleting the user ' s home directory and all related information; if this parameter is not used, the information is retained and only the user is deleted

Example:

```sh '
♪ Pw userdel test2-r
````

## `pw usershow' command

to display user information, for example:

```sh '
# Pw usershow test2
test2: $6.FkxPcs2y.Y8cxyuj$kVDoV1LC.IWGlSitll3oLArF18/2011/QYID0JE.TuD0YFgba.c7MbGs3xLnmpCZyu1nVKhNqW2X7a57qN0xg/:1201:01:0:0:User &:/home/test1:/bin/ssh
````

## `pw usrnext' command

Returns the next UID and GID available, for example:

```sh '
# Pw usual
1202:1202
````

## `pw lock ' Command

Locked account number. Locked account number is not available.

Example:

```sh '
# Pw lock test2
````

## `pw unlock ' command

Unlock the account. Unlock the account.

Example:

```sh '
# Pw unlock test2
````

## `pw grouped 'command

to create a new group.

Example:

```sh '
# pw grouped test-g 1200 # create group gid for 1200;gid is different from uid
# pw grouped 5-M test1, test2 # create group 5. Members have test1 and test2
````

## `pw groupmod' command

To modify group information, common parameters:

`-g ' , designate new `gid '

`-l', rename group name

`-M ' , replaces the list of existing group members, multiple commas separated

`-m ' , adding new members to the current list of group members

Other parameters refer to the `groupd ' command.

Example:

```sh '
# Pw groupmod test-g 1300 # Modify the test group gid to 1300
# pw group best-l test2
# pw groupmud test5-M test1 # set group test5 to test1 and the original members will be deleted!
# pw groupmod test5-m test3
````

## `pw groupdel ' command

To remove groups,

Example:

```sh '
# Pw groupdel test5
````

# # `pw grouphow' command

To display group information,

Example:

```sh '
# Pw groupshow test5
test5:* 1202: test1
````

# # `pw grouptext' command

Can return the next available `gid ',

Example:

```sh '
# Pw groupnext
1301
````

# References

- [FreeBSD Introduction Notes] (https://lvv.me/posts/2021/04/19_freebsd_101/), by Ivvv.me
