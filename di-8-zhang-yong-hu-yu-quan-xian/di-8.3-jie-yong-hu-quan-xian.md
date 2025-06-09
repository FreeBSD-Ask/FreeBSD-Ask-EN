Section 8.3 User privileges

Permissions

First, the following command output is observed:

```sh '
#ls-al/home/ykla
Total 74
Drewxr-x17 ykla 27 Mar 19 17:57.
Drewxr-x-x 3 root sheel 4 Mar 19 16:05...
Drwx -- - 4 ykla ykla 4 Mar 10 16:21 .mozilla
.profile
-rw -- -- 1 ykla ykla 200 Mar 19 17:57.sh_history
-rw-r-r-- 1 ykla ykla 1003 Feb 24 12:18.shrc
Drwxr-x-x 2 ykla 2 Mar 9 23:48.
Drwxr-xr-x 2 ykla ykla 2 Mar 9 20:45 Desktop
````

Reobservation:

```sh '
---- 1 root wheel 0 Mar 19 22:26 test
````

FreeBSD file access can be explained by 10 markers (or not 10 in the first row of the count), which are made up of 4 parts:

Split with slash: `-/-/--/----- '

The first part is the 1st digit, which is the `d ' for the directory, `- ' for the normal file, `l ' for the link file, `b ' for the block device file, `p ' for the conduit file, `c ' for the character device file and `s ' for the socket file;

The second part, in points 2, 3 and 4, is used to identify access to the document by the user to whom the document belongs, and to use `rwx ' to indicate the permission to read, write, execute (for the catalogue, i.e. access to the `ls ' and `cd ' directory) and write without permission to `- ';

Part III, Nos. 5, 6 and 7, is used to identify access to documents by members of the group to which the document belongs.

Part IV, which is the eighth, ninth and tenth places, is used to identify access to documents by other users.

Read, write and execute, in addition to being expressed in `rwx ', can also be read as numbers 4, 2, 1, without permission 0. After each three-digit number is added, the combination is the expression of three-digit numbers. (Memory machine: read 4 write 2 execute 1)

For example:

| character identification privileges | digital identification privileges | description |
|: -: |: | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | : | | | | | | | | | | | | | | | | | | : | | | | : | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| -rwxrwxrwx | 777 | Normal file readable, written and executed by all
| -rwxr-xr-xx |755 | This is a normal file whose users have read, write and execute privileges; the same group of users and other users can only read or execute and cannot write |

>** Thinking issues**
>
> `drew - - `, i.e. `600 ' , is a catalogue that can be read and written only by the user to whom it belongs.
>
Is that right? Does it make sense? Why?

# `chmod ' Command

# # Operator Method

````
That's right.
````

In `a+x ' :

The first indicates that the operator, `u ' is the user to which the user belongs, `g ' is the group to which the `o ' is the other user, and `a ' is the user to whom the system defaults;

The second is the operator, `+ ' is the addition and `- ' is the removal;

The third is the permission mode, `rwx ' means reading, writing and executing, respectively, and `s ' means that the process is or is organized in a manner consistent with the document ' s owner or group at the time the document is executed.

Number method

```sh '
750 bucks.
````

Of these, 7 indicates that the users to whom they belong have the right to read, write and execute, and the same group of users have the right to read and execute, while the other users do not have the right to read and execute, which is more convenient to use.

Option `-R ' , Recursive Empowerment

Example:

```sh '
#chmod-R777/tmp # allows any user to read, write, execute all files under /tmp directory
#chmod -Ra+rwx /tmp # allows any user to read, write, execute all files under /tmp directory
````

# 'down 'command

Changes have been made to the main body of the document, including the user and group to which it belongs.


Option `-R ' , Recursive Empowerment

Example:

```sh '
# chown test1 t.sh
# Downtest1: best t.sh
#down-R test1: best/tmp # modify/tmp the owner of all files in the directory
````
