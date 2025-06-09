Section 8.3 User privileges

Permissions

First, the following command output is observed:

```sh
root@ykla:~ # ls -al /home/ykla
total 74
drwxr-xr-x  17 ykla ykla    27 Mar 19 17:57 .
drwxr-xr-x   3 root wheel    4 Mar 19 16:05 ..
drwx------   4 ykla ykla     4 Mar 10 16:21 .mozilla
-rw-r--r--   1 ykla ykla   966 Feb 24 12:18 .profile
-rw-------   1 ykla ykla   200 Mar 19 17:57 .sh_history
-rw-r--r--   1 ykla ykla  1003 Feb 24 12:18 .shrc
drwxr-xr-x   2 ykla ykla     2 Mar  9 23:48 .themes
drwxr-xr-x   2 ykla ykla     2 Mar  9 20:45 桌面
```

Reobservation:

```sh
----------   1 root wheel         0 Mar 19 22:26 test
```

FreeBSD file access can be explained by 10 markers (or not 10 in the first row of the count), which are made up of 4 parts:

SPLIT BY SLASH: __CODESPAN_0_

THE FIRST PART IS THE 1ST POSITION, WHICH IS THE DIRECTORY IN __CODESPAN_0, __ CODESPAN_1_ FOR THE GENERAL FILE, __ CODESPAN_2_ FOR THE LINK FILE, __ CODESPAN_3_ FOR THE BLOCK DEVICE FILE, __ CODESPAN_4_ FOR THE CONDUIT FILE, __ CODESPAN_5_ FOR THE CHARACTER DEVICE FILE, __ CODESPAN_6_ FOR THE PACKAGE FILE

THE SECOND PART, NUMBER 2, 3 AND 4, IS USED TO IDENTIFY ACCESS TO THE DOCUMENT BY THE USER TO WHOM THE DOCUMENT BELONGS, AND TO USE `rwx` AS A MEANS OF READING, WRITING, EXECUTING (FOR THE CATALOGUE, I.E. ACCESS TO __CODESPAN_1 AND __CODESPAN_2_) AND, WITHOUT PERMISSION, TO __CODESPAN_3_

Part III, Nos. 5, 6 and 7, is used to identify access to documents by members of the group to which the document belongs。

Part IV, which is the eighth, ninth and tenth places, is used to identify access to documents by other users。

READ, WRITE AND EXECUTE, IN ADDITION TO BEING EXPRESSED IN __CODESPAN_0, CAN ALSO BE EQUAL TO A NUMBER OF 4, 2, 1, WHICH IS 0. AFTER EACH THREE-DIGIT NUMBER IS ADDED, THE COMBINATION IS THE EXPRESSION OF THREE-DIGIT NUMBERS. (MEMORY MACHINE: READ 4 WRITE 2 EXECUTE 1)

For example:

| Character Identification Permissions | Digital Identification Permissions | Annotations |
| :----------: | :----------: | :-----: |
| -rwxrwxrwx | 777 | General documents read, written and executed by all |
| -rwxr-xr-x | 755 | This is a normal file, whose users have read, write, execute permissions; the same group and other users can read or execute only and cannot write |

>** Thinking issues**
>
> CODESPAN_0, OR ___ CODESPAN_1 > THIS IS A DIRECTORY THAT CAN BE READ AND WRITTEN ONLY BY THE USER TO WHOM IT BELONGS。
>
Is that right? Does it make sense? Why

#__CODESPAN_0_COMMAND

# # Operator Method

```
$ chmod a+x test.sh
```

IN __CODESPAN_0:

THE FIRST IS FOR THE OPERATING OBJECT, CODESPAN_0, WHICH IS THE USER, CODESPAN_1, WHICH IS THE GROUP, CODESPAN_2 , WHICH IS THE OTHER USER, AND CODESPAN_3 , WHICH IS FOR ALL USERS AND DOES NOT WRITE BY DEFAULT;

THE SECOND IS THE OPERATOR, CODESPAN_0 IS THE ADDITION, CODESPAN_1 IS THE REMOVAL;

THE THIRD IS THE PERMISSION MODE, WHICH INDICATES READING, WRITING AND EXECUTION, RESPECTIVELY, OF CODESPAN_0, AND OF CODESPAN_1, WHICH MEANS THAT THE PROCESS IS OR IS ORGANIZED IN A MANNER CONSISTENT WITH THAT OF THE DOCUMENT。

Number method

```sh
$ chmod 750 test.sh
```

Of these, 7 indicates that the users to whom they belong have the right to read, write and execute, and the same group of users have the right to read and execute, while the other users do not have the right to read and execute, which is more convenient to use。

OPTION __CODESPAN_0_, RECURSIVE EMPOWERMENT

Example:

```sh
# chmod -R 777 /tmp # 允许任何用户读、写、执行 /tmp 目录下所有文件
# chmod -R a+rwx /tmp # 允许任何用户读、写、执行 /tmp 目录下所有文件
```

#__CODESPAN_0_COMMAND

Changes have been made to the main body of the document, including the user and group to which it belongs。


OPTION __CODESPAN_0_, RECURSIVE EMPOWERMENT

Example:

```sh
# chown test1 t.sh # 修改 t.sh 属主为用户 test1
# chown test1:test t.sh # 修改 t.sh 属主为用户 test1、组 test
# chown -R test1:test /tmp # 修改/tmp 目录下所有文件的属主为用户 test1、组 test
```
