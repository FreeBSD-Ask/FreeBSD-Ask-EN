Section 2.4. Basis of the command line (new introductory version)

You're not alone

Many often miss or mix command or command parameters and options, but it is not your fault。

Many middle school staff also needed to learn how to use computers and mobile phones in the years. How do you explain how this group knows how to operate short video? Does this mean that short video is a better design

Because many orders are either based on historical constraints or on the ability of developers to maintain them, they are not so uniform or easy to remember or use。

Query [man page] (https://man.freebsd.org/cgi/man.cgi) will know that there is a specific entry called “BUGS”, which is used to describe the deficiencies of the current software。

In terms of personal use experience, if a single software could not find 10 bugs that seriously affected or impeded its use, it would never be open-source software. And most defenders are powerless because Bug is too many, or reality is too confusing, and they have no economic incentive to repair it. The vast majority of open-source businesses have millions or millions of open-source software, and their defenders have mostly never received any financial compensation or reputation。

Trust me, you're not the one who thinks these things are hard to use or even wants to break the keyboard. This is also one of the reasons why people continue to “crew” (resulting in a tool). If you think the GCC is hard to use, then you can go with Clang+LLVM. You're not the first person to find the GCC difficult, and you're not the last。

Many have stressed the importance of command lines, and users of GUI software such as IDE with arrogance and contempt are not necessary. Many will deliberately resonate on the so-called advantages of these tools, a group that is pure Sdergor syndrome patients and advocates of the philosophy of suffering. The essence of Unix ' s philosophy is not to adhere to the ancient laws of ancestral law, but to emphasize the human being. That's today, a quarter of the twenty-first century, still emphasizing the meaning of Unix philosophy. Most people have been blinded by the philosophy of suffering, with an emphasis on the roots, and hate begins with 0 and 1 of computers, while those who seem to be soberer are more confused。

What's so bad if people feel happy and happy? It has always been stressed that these are knowledge and should be reversed. The real question is, what is knowledge? Is knowledge and degree linked? How do you explain that most undergraduates don't know the difference between the monitor and the mainframe

The American philosopher B. F. Skinner said, "Education is the rest when one forgets everything he learned at school." Unlike traditional Western perceptions (e.g. Plato's memoirs, Augustine's light and God's memory, Locke's whiteboards) and Confucius doctrine (e.g., “learning and learning” in Theory of Essays) and even the emphasis on memory in traditional folklore (e.g., the loss of memory when drinking Bombay's soup) — and the greater emphasis on “forgetting” — this is the further development of the old man's “actless religion” (the second chapter of the Code of Ethics). In Free Travel, M.J. emphasized that “the knowledge is not the knowledge”, and that what we learn on a daily basis is not “the knowledge”. In his view, both old and modern learning is fundamentally alien to human beings, who are taught by modern society and are the culture of the industrial revolution, not knowledge。

>** Thinking issues**
>
>This paper lists the orders and options that are required on a daily basis。
>
> a command may have several hundred options or parameters, and a dictionary or document (man also info) is used to check not back。
>
What do you think, "I've got a career and no career. You've lost your career

Again, if you've forgotten everything after reading this, only if you use AI to see how orders work, or if you just go from "FreeBSD" to running, then congratulations! You have successfully mastered the most important elements of this paper。

References

- [♪ I can't believe ♪] (https://www.cas.cn/xw/cmsm/2014/04/t20140402_4084616.shtml)
- [New methods and new ones in teaching] (https://www.bfskinner.org/wp-content/uploads/2014/02/New-Methods-aims-in-Teach.pdf), not Einstein. Is it true that the knowledge we have acquired is so right and true that we are blackmailed now
- SHIYONLONG. ZHUOKO'S “FORGOTTEN” EDUCATIONAL PICTURE EXPLAINS [J]. UNIVERSITY EDUCATION SCIENCE, 2022 (01): 105-112.

# Login to FreeBSD

When you install FreeBSD, if everything is normal, you should see the following on the screen:

```sh
FreeBSD/amd64 (ykla) (ttyv0)

i don't know
````

We call the interface on this screen the TTY or the physical terminal。

Explanation:

__CODESPAN_0 IS THE NAME OF THE OPERATING SYSTEM
- ___ CODESPAN_0_ is the structure of the system, and the general Intel and AMD processors are amd64, or x86-64
- CODESPAN_0 IS THE HOST NAME THAT YOU SET UP WHEN THE SYSTEM WAS INSTALLED
- {\CHFFE7C5} {\CH00FFFF}{\CH00FFFF} {\CHFFFFFF}{\CH00FFFF} {\CHFFFFFF}{\CH00FFFF}{\CH00FF00} {\CHFFFFFF}{\CH00FFFF} {\CHFFFFFF}{\CH00FFFF} {\CHFFFFFF}{\CH00FF00} {\CHFFFFFF}{\CH00FF00} {\CHFFFFFF}{\CH00FF00} {\CHFFFFFF}{\CH00} {\CHFFFFFF}{\CH00FF00}
- __CODESPAN_0_ INDICATES USER LOGIN。

We enter user names and passwords to log in to the system:

```sh
FreeBSD/amd64 (ykla) (ttyv0)

login: root # enter the user name here, then press back
Password: # Enter the password here, then press the Return key
Last login: Tue Mar 18 17:24:48 2025 from 3413e8b6b43f
FreeBSD 15.0-CURRENT (GENERIC)main-n275981-b0375f78e32a

Come to FreeBSD!

Release Notes, Errata: https://www.FreeBSD.org/releases/
Security Industries: https://www.FreeBSD.org/security/
FreeBSD Handbook: https://www.FreeBSD.org/handbook/
FreeBSD FAQ: https://www.FreeBSD.org/faq/
Questions List: https://www.FreeBSD.org/lists/questions/
FreeBSD Forums: https://forums.FreeBSD.org/

Documents incorporated with the system are in the/usr/local/share/doc/freebsd/
i'm sorry, i'm sorry
For other languages, place "en" with a language code like de or f.

Show the version of FreeBSD accepted: freebsd-version; uname-a
Please include that output and any emergency messages when posing questions.
Introduce to human pages: man man
FreeBSD directory playout:

To change this logic, see motd (5).
root@ykla:

```

Congratulations! You've successfully logged into the FreeBSD operating system。

Note**
>
The >cipher is not reproduced on the screen: __CODESPAN_0_ is shown when we enter the password. However, in FreeBSD, where passwords are involved, there will be no display, even if they are empty on the password screen, and no input is a state, nothing, nothing, just enter it back。

- 1: root is the highest authority in UNIX. We used to say Andre root, apple escape, Kindle escape, and so on, to get this root access。

References

- [What is TTY in Linux?] (https://itsfoss.com/what-is-tty-in-linux/), translated in [Linux explains in black: What's TTY] (https://linuxstory.org/linux-blackmail-explained-what-is-tty/)。


# # troubleshooting and unfinished business

- If the user name is correct, but the password is incorrect:

```sh
login: root
Password:
Login: incorrect # 即不正确的意思
login: 
```

- If the username and password are incorrect:

```sh
login: test # 当前系统中不存在该用户
Password:
Login: incorrect
login: 
```

if you don't even know the user name, you can find the root password and see what user accounts or reloading systems are faster。

Who am I

- View the username of the current login system:

```sh
$ whoami
ykla
```

- View current login user group related

```sh
$ id
uid=1001(ykla) gid=1001(ykla) groups=1001(ykla),0(wheel)
```

- View the interruption of current user login and the current login time

```sh
$ who
root             pts/0        Mar 19 15:00 (3413e8b6b43f)
```

- Show us which users are login and what they're doing

```sh
$ w
 3:02PM  up 21:52, 1 user, load averages: 0.01, 0.01, 0.00
USER       TTY      FROM           LOGIN@  IDLE WHAT
root       pts/0    3413e8b6b43f   3:00PM     - w
```

- View current path

__CODESPAN_0_I. __CODESPAN_1_, PRINT WORK DIRECTORY

```sh
$ pwd
/usr/ports/editors/vscode
```


# Account toggle and exit login

```sh
root@ykla:/ # su ykla ①
ykla@ykla:/ $ ②
ykla@ykla:/ $ su ③
Password: ④
root@ykla:/ #
root@ykla:/ # exit ⑤
ykla@ykla:/ $ exit ⑥
root@ykla:/ # exit ⑦

FreeBSD/amd64 (ykla) (ttyv0)

i don't know
````

-1 Use __CODESPAN_0_ to switch to ykla, and not need to enter ykla password:
- CODESPAN_0:
-_CODESPAN_0_: Current user is root
- __CODESPAN_0_ "Who"_CODESPAN_1_ "xx" host
- ___ CODESPAN_0: Here's the host name, not the user ykla. You can name a different host
- __CODESPAN_0: REPRESENTS THE CURRENT PATH UNDER __CODESPAN_1_
Did you notice the change in the hint? root is __CODESPAN_0, and the common user is __CODESPAN_1 (csh is __CODESPAN_2_)
- 3 If it is simply __CODESPAN_0_go back, the command is to switch from the current user to the root account (if it is already root, there will be no reaction). But you have to be a member of the wheel group to do this, or you'll miss it。
-4 switch from normal user to root, the password to enter is the login password for the root account。
-5 ENTER __CODESPAN_0_ TO EXIT THE CURRENT USER, AND IF ONLY LOGIN, EXIT LOGIN TO TTY

>** Thinking issues**
>
> 6 and 7, respectively, which users were replaced or which operations were performed

Command line format

Most of the command line orders should be meaningful, e.g. ___ CODESPAN_0_, i.e. __ CODESPAN_1_ (listed), __ CODESPAN_2_, i.e. __ CODESPAN_3_ (downloaded) through web (network); few commands that are unknown, e.g. __ CODESPAN_4_ (orders that automatically correct spelling errors)。

```sh
# 命令 选项  参数 1       参数 2
# ls   -l   /home/ykla /tmp
/home/ykla:
total 317
  ……有所省略……
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 下载
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 
桌面

/tmp:
total 6
3 Mar 18 17:23. ICE-unix
-r-r-r-r-- 1 root wheel 11 Mar 18 17:10. X0-lock
````


Of these, __CODESPAN_0(L lowercase) means the list of documents under the current or specified directory; option __CODESPAN_1_(L lowercase) means the printing of detailed information and the output format (*long*)。

Most of the orders are now subject to the above (abbreviated). This is provided for in [POSIX.1-2024] (https://pubs.opengroup.org/onlinepubs/97997919799)。

WE NEED TO NOTE THAT ENGLISH AND CHINESE ARE DIFFERENT, THAT THERE ARE NO SPACES TO DIVIDE BETWEEN CHINESE, AND THAT ENGLISH WORDS MUST BE SEPARATED BY USING SPACES. THEREFORE, THERE SHOULD BE SPACES IN THE MIDDLE OF EACH PART OF THE COMMAND LINE, I.E. __CODESPAN_0_. THE NUMBER OF SPACES IS GENERALLY NOT LIMITED, BUT SHOULD BE AT LEAST ONE, I.E. __CODESPAN_1_。

>** Thinking issues**
>
> How does the software understand the entire sentence if the command line is not separated by space or some way (e.g. other symbols)
>
>WHAT WOULD CODESPAN_0__ EXPERIENCE IF IT WAS SEEN FROM A HUMAN PERSPECTIVE FROM A NATURAL LANGUAGE PERSPECTIVE WITHOUT SPACE
>
> REPLACE: __CODESPAN_0, __CODESPAN_1_ __
>
> ```sh '
>root@ykla:~ #ls-l/home/ykla/tmp
>-sh: ls-l/home/ykla/tmp: not found
>root@ykla: ~ #ls/
>-sh: lls/: not found
> ````
>
as you can see, shell will use the whole sentence as an enforceable order。

We also need to know that an order does not have an automatic error correction function, even if it is just a wrong letter, missing a number, and the order is never successful:

```sh
root@ykla:~ # LS # 试试全大写
-sh: LS: not found
root@ykla:~ # Ls # 一大一小呢
-sh: Ls: not found
root@ykla:~ # ls /hom1 # 实为 /home
ls: /hom1: No such file or directory
root@ykla:~ # ls -z /home # 不存在选项 -z
ls: invalid option -- z
usage: ls [-ABCFGHILPRSTUWZabcdfghiklmnopqrstuvwxy1,] [--color=when] [-D format] [--group-directories=] [file ...]
```

>** Skills**
>
>Windows is not only not sensitive to file sizes, but also to command sizes。
>
> ``powershell '
>PS C:\Users\ykla> cd C: # Here cd is lowercase
>PS C: > CD D: # HERE CD IS UPPERCASE
>PS D: > CD c: # Here the C disc is lowercase
>PS C: > dir # lowercase dir, list the directory, equals ls
>
> DIRECTORY: C:\
>
> ... part of the omission ..
>
>PSC:\Users\ykla>TREE # Uppercase tree, show path relationships
> FOLDER PATH LIST
> VOLUME SERIES 2A90-E989
>C: .
i'm sorry
i miss-- .cache
i'm sorry
> ... omitted part of..
> ````

> ** Skills**
>
What does > CODESPAN_0_ mean after the command? ___ CODESPAN_1 _ in shell is generally an annotated function (set out by [POSIX.1-2024] (https://pubs.opengroup.org/onlinepubs/9799799/utilities/V3_chap02.html)), which corresponds to `//`_ in C language. This means that the text at the back is only illustrative and not practical。



# thefuck: automatically correct the misspelled command

# # install the fuck #

use pkg

```sh
# pkg ins thefuck
```

or ports

```sh
# cd /usr/ports/misc/thefuck/
# make install clean
```

# # configure the fuck

View installation configuration information

```sh
root@ykla:~ # fuck
Seems like fuck alias isn't configured!
More details - https://github.com/nvbn/thefuck#manual-installation
```

We'll open the web browsing. It was discovered that `eval $(thefuck --alias)`_ would be added to __CODESPAN_1_(bash shell), __CODESPAN_2_(bash shell) or __CODESPAN_3_(zsh shell)。

We FreeBSD by default use sh, so will:

```sh
eval $(thefuck --alias) 
```

WRITE __CODESPAN_0, DO NOT REDIRECT __CODESPAN_1_, PLEASE EDIT MANUALLY TO JOIN。

Refresh environment variables:

```sh
root@ykla:~ # . ~/.shrc
root@ykla:~ # fuck
No fucks given
```

>** Skills**
>
>ON THE BASIS OF THE AUTHOR ' S INFORMATION, IF YOU DO NOT LIKE ENTERING __CODESPAN_0, YOU CAN ALSO USE OTHER ALIASES: IF CHANGED TO __CODESPAN_1 __, ALL THE __CODESPAN_2 __ COMMANDS BELOW WILL BE REPLACED BY __CODESPAN_3 __。
>
> ```sh '
>root@ykla: #abc
Nothing found
>root@ykla: #plg install gimp
>-sh: plg: not found
>root@ykla: #abc
> pkg install gimp [enter/↑/↓/ctrl+c]
> ... omitted part of..
> ````


# # test with thefuck

```sh
root@ykla:~ # ls-l /home/ykla/ # 先输入一遍错误的试试
-sh: ls-l: not found
root@ykla:~ # fuck
​​​​​​​​​​ls -l /home/ykla/ [enter/↑/↓/ctrl+c] # 上下箭头切换可能的命令，回车确认，ctrl c 中断​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​
total 317
……省略一部分……
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 下载
drwxr-xr-x  2 ykla ykla        2 Mar  9 20:45 桌面
```

Try again:

```sh
root@ykla:~ # plg install gimp
-sh: plg: not found
root@ykla:~ # fuck
​​​​​​​​​​pkg install gimp [enter/↑/↓/ctrl+c]​​​​​​​​​​
Updating FreeBSD repository catalogue...
FreeBSD repository is up to date.
……省略一部分……
```

Command execution and interruption

Unlike the Windows and graphical interface software, most command line programs do not have any progress tips in their execution. There are usually only two outcomes:

- Successful implementation of:

```sh
root@ykla:~ # cp test /root/mydir/
root@ykla:~ #

```

- Implementation interruption:

```sh
root@ykla:~ # cp test9 /root/mydir/
cp: test9: No such file or directory
```

There are many possible circumstances in which the interruption of execution is possible, but only one (no specified document or directory exists)。

It can be seen that only when the execution is interrupted does the command line have a hint; if the execution is completed, there will be no hint. This Unix design philosophy is designed to ensure the simplicity of terminal output。

Shell

our orders are to run in the shell, interact with the system through the shell。

FreeBSD default shell is sh (Bourne shell, originally named Stephen R. Bourne). It has now been rewritten and is in general conformity with the regulation of shell in [POSIX.1-2024] (https://pubs.opengroup.org/onlinepubs/9799799/utilities/V3_chap02.html)。

The usual shell in Linux is bash. The default shell in MacOS is usually a zsh (Z shell)。

Note**
>
There are sshs in >Linux, but it's usually softly linked to bash or other shells, which are not real sshs。
>
>-Ubuntu 24.04 LTS default shell:
>
> ```bash '
>$ls-l/bin/sh
>lrwxrwx 1 root root 4 february 25:19 /bin/sh-> dash
> ````

Shortcut

Note**
>
> The following shortcut key does not have to be in lower case to be executed, as in upper case。

# # TURNS PAGES AND/OR LINES ON THE TTY INTERFACE

## # Use the Scroll Lock key to flip/ flip pages over and down the TTY interface

Use **Scroll Lock** (rolling): When you press **Scroll Lock**, you can operate the screen using the upper/ lower ↓ orientation key,**Page Up**/**Page Down**。

Different:

- UP/ DOWN
-**Page Up**/**Page Down** Key: Scroll one page on the TTY interface

Press **Scroll Lock** again to exit this mode。

>** Skills**
>
>SL key above **HOME** key, PS screenshot key **Print Screen** right, PB key ** Pause break** left。

In fact, historically, **Scroll Lock** this key was designed for this。

### # use Shift to flip/ flip pages on the TTY interface

Use **Shift** shortcut:

-**Shift** + Up/ Down Direction Key - Scroll a line up/ down in the TTY interface
-**Shift** + **Page Up**/**Page Down** Key - Scroll one page on the TTY interface

## # Complete command or directory

Usually complete commands or directories by **Tab**. Up arrow ** ** is looking at the last command, down arrow ** ** is looking at the next command。

- Completing orders

```sh
root@ykla:~ # lo # 若此时按 TAB 键，输出如下。可以再输一个字母再按一次 TAB 键看看
local                    localedef                login
local-unbound            locate                   logins
local-unbound-anchor     lock                     logname
local-unbound-checkconf  lockf                    look
local-unbound-control    lockstat                 lorder
local-unbound-setup      locktest                 lowntfs-3g
locale
```

- Complete file directory or filename

```sh
$ cp /home/ykla/ # 此处按 TAB 键，然后再重复按一次 TAB 键，看看效果
$ cp /home/ykla/test/1.txt
.cache/                 .login                  bin/                    test2
.config/                .profile                HW_PROBE/               test3
.cshrc                  .sh_history             mine
.gitconfig              .sh_history.Y8RqIDNDIv  mydir/
.k5login                .shrc
```

# # Abort the command #

**ctrl** **c**:

```sh
root@ykla:~ # ping 163.com
PING 163.com (59.111.160.244): 56 data bytes
64 bytes from 59.111.160.244: icmp_seq=0 ttl=52 time=27.672 ms
64 bytes from 59.111.160.244: icmp_seq=1 ttl=52 time=27.580 ms
^C # 注意这里，^C 即代表你在此处按下了 ctrl + c 的组合键，随后命令被终止
--- 163.com ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.580/27.626/27.672/0.046 ms
```

Command backstage

**ctrl**+**z**: Place the current process backstage and return to the front desk with __CODESPAN_0_ command:

```sh
root@ykla:~ # ping 163.com
PING 163.com (59.111.160.244): 56 data bytes
64 bytes from 59.111.160.244: icmp_seq=0 ttl=52 time=27.611 ms
64 bytes from 59.111.160.244: icmp_seq=1 ttl=52 time=27.691 ms
^Z[1] + Suspended               ping 163.com # 注意此处，按下了 ctrl + z
root@ykla:~ # fg # 返回前台
ping 163.com
64 bytes from 59.111.160.244: icmp_seq=3 ttl=52 time=27.465 ms
64 bytes from 59.111.160.244: icmp_seq=4 ttl=52 time=27.586 ms
64 bytes from 59.111.160.244: icmp_seq=5 ttl=52 time=27.522 ms
^C # 按 crtl + c 结束命令
--- 163.com ping statistics ---
6 packets transmitted, 6 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.465/27.596/27.701/0.085 ms
```

Other

-**ctrl**+**l** (L): Empty screen
-**ctrl**+**a**: move cursor to command line beginning
-**ctrl**+**a**: move cursor to end of command line

# The source of the command

# Linux

In Linux, all commands are basically from the GNU package, and the Linux kernel does not have any commands. Let's check this out:

```bash
$ dpkg -S /bin/mv 
coreutils: /bin/mv
$ dpkg -S /bin/cp
coreutils: /bin/cp
$ dpkg -S /bin/ls
coreutils: /bin/ls
$ dpkg -S /bin/pwd
coreutils: /bin/pwd
$ dpkg -S /bin/cat
coreutils: /bin/cat
$ dpkg -S /usr/sbin/chroot
coreutils: /usr/sbin/chroot
$ dpkg -S /bin/kill
procps: /bin/kill
$ dpkg -S /usr/bin/free
procps: /usr/bin/free
$ dpkg -S /bin/su
util-linux: /bin/su
```

See, in Linux, these common commands are generally derived from GNU software coreutils, util-linux or procps. These software have historically been the re-realization of UNIX by GNU plans。

at the same time, shell itself has some orders:

```bash
$ type cd
cd 是 shell 内建
```

list all shell built-in commands:

```bash
$ compgen -b
.
:
[
alias
bg
bind
break
builtin
caller
cd
command
compgen
……省略一部分……
ulimit
umask
unalias
unset
wait
```

FreeBSD

```sh
$ type cd
cd is a shell builtin
```

In FreeBSD, except for the above-mentioned shell built-in commands (see [s(1)] (https://man.freebsd.org/cgi/man.cgi?sh(1))), common commands are self-contained in basic systems and do not belong to any of the packages. For example, the __CODESPAN_0_ command, the source code is located in [freebsd-src/bin/ls/] (https://github.com/freebsd/freebsd-src/tree/main/bin/ls). The FreeBSD system is an organic whole. It is not a package package that is maintained by different people or teams。

if you configure pkgbase, output is similar:

```sh
# pkg which /bin/ls
/bin/ls was installed by package FreeBSD-runtime-15.snap20250313173555

```


If one command is missing, it can be obtained by installing the corresponding package, e.g. __CODESPAN_0, from __CODESPAN_1_. But there are also a number of commands that have Linuxist problems and are not compatible with other operating systems, such as the ip command, from the GNU package iproute2。

#__CODESPAN_0_ BASIC USE OF EDITOR

__CODESPAN_0_ is the editor for the FreeBSD basic system。

__CODESPAN_0 is much simpler than [no, nano] (https://www.redhat.com/zh/blog/getting-stard-nano) (a GNU editor), as you can see from its name “easy editor”。

Like what

```sh
# ee a.txt
```

You can edit it directly, just like __CODESPAN_0_ or Windows Notes。

PRESS **ESC** TO DISPLAY A REMINDER BOX AND PRESS ** RETURN KEY** TO SAVE IT。

#__CODESPAN_0_ BASIC USE OF EDITOR

FreeBSD also has a built-in editor -- CODESPAN_0 -- which is more sophisticated. Unlike most categories of UNIX operating systems, which link `vi`_ to __CODESPAN_2_, the BSD system is the real `vi`_ (in fact __CODESPAN_4_, i.e. new vi, 4.4 BSD)。

- CODESPAN_0__ under MacOS

```sh
$ ls -al /usr/bin/vi   
lrwxr-xr-x  1 root  wheel  3  4 12 13:16 /usr/bin/vi -> vim
```

Opens the __CODESPAN_0_, and then enters __CODESPAN_1_, so you can enter the __CODESPAN_1 and edits the text. It should be noted that ** Delete key (reverted key)** does not work, or is the same as **Insert key**. To delete text, press **Delete**。

```sh
bc123
~      
~
~
```

>** Skills**
>
> AN EMPTY LINE WILL BE DISPLAYED AS __CODESPAN_0_。

AFTER EDITING, PRESS **ESC** TO RETURN FROM TEXT MODE TO COMMAND MODE。

IN COMMAND MODE, ENTER ___ CODESPAN_0, I.E. __ CODESPAN_1 IS NOT SAVED, __ CODESPAN_2 IS SAVED AND EXITED, __ CODESPAN_3 IS MANDATORY, __ CODESPAN_4 IS FORCED EXIT。


```sh
ABC
~
~
:wq
```

Common commands

## __CODESPAN_0_COMMAND

__CODESPAN_0_(change working directory, change job directory)

SWITCH TO __CODESPAN_0_

```
$ cd /home
$ pwd # 看看现在在哪
/home
```

## __CODESPAN_0_COMMAND

__CODESPAN_0_(list, list) The basic usage of the command is described above, and the following is an attempt to make the lls list the size of the file in a human-readable way:

OPTION __CODESPAN_0, I.E. __CODESPAN_1_(HUMAN), SHALL BE USED IN CONJUNCTION WITH __CODESPAN_2_(_CODESPAN_3_ LONG OUTPUT)。

```sh
# ls -hl /home/ykla
total 326 KB
-rw-------  1 ykla ykla   50B Mar 18 17:23 .Xauthority
drwx------  6 ykla ykla    6B Mar 10 16:21 .cache
drwx------  9 ykla ykla   12B Mar 19 15:01 .config
-rw-r--r--  1 ykla ykla  1.0K Feb 24 12:18 .shrc
drwxr-xr-x  2 ykla ykla    2B Mar  9 23:48 .themes
-rw-r--r--  1 root ykla    0B Mar 19 15:13 abc.TXT
drwxr-xr-x  3 root ykla    7B Mar 19 15:17 vscode
-rw-------  1 ykla ykla   17M Mar 18 17:09 xrdp-chansrv.core
drwxr-xr-x  2 ykla ykla    2B Mar  9 20:45 下载
……省略一部分……
```

In UNIX, files or directories starting with __CODESPAN_0 (such as __CODESPAN_1 above) are hidden. Your Android phone is the same -- you can look at it yourself。

AND OPTION __CODESPAN_0_ CAN SHOW HIDDEN DIRECTORIES OR FILES:

```sh
ykla@ykla:~ $ ls -a
.		.cshrc		.login		.profile	公共		视频
..		.dbus		.login_conf	.sh_history	图片		音乐
.Xauthority	.face		.mail_aliases	.shrc		文档
.cache		.icons		.mailrc		.themes		桌面
.config		.local		.mozilla	下载		模板
```

>** Thinking issues**
>
> ```sh '
>ykla@ykla: ~$pwd
>/home/ykla
< ykla@ykla: ~ $ cd.
>ykla@ykla: ~$pwd
>/home/ykla
>ykla@ykla: $ cd...
>ykla@ykla:/home $ pwd
>/home
>ykla@ykla:/home $ cd...
>ykla@ykla:/ $pwd
>/
>ykla@ykla:/ $cd/home/ykla
>ykla@ykla: ~$cd../..
>ykla@ykla:/ $pwd
>/
> ````
>
>THROUGH THE OUTPUT ABOVE, THINK: __CODESPAN_0, __CODESPAN_1_, RESPECTIVELY

TRY NOT HAVING AN OPTION

```sh
ykla@ykla:~ $ ls
下载	公共	图片	文档	桌面	模板	视频	音乐
```

Do not show hidden files。

>**Technology**
>
> Please test as a normal user because the root shell of FreeBSD always shows hidden files。

## __CODESPAN_0_CREATION FILE COMMAND

`touch` IS A TOUCH, MEANING A SLIGHT CHANGE。

CREATE A FILE CALLED __CODESPAN_0_:

```sh
$ touch test
```

>** Skills**
>
> YOU CAN SEE I CREATED __CODESPAN_0 INSTEAD OF __CODESPAN_1 , __ CODESPAN_2 , __ CODESPAN_3 > . IN FACT, THIS PART OF CODESPAN, WHICH WE CALL A SUFFIX, IS MAINLY FOR PEOPLE, NOT MACHINES. IS IT TRUE THAT MANY THINGS WE THINK ARE AS CLEAR AS WE THINK
>
>Even if we remove the corresponding suffix name, the type of file can be identified in the UNIX class, as determined by the file numbers:
>
> ```sh '
>$filebook
>book: PDF document, version 1.7
> ````

One-time multiple files can be created using multiple parameters (similar usage is almost universal and not repeated):

```
$ touch test test1 test2 test3
```

CREATE DIRECTORY

__CODESPAN_0_I_CODESPAN_1_, CREATE DIRECTORY

create a directory called ykla

```sh
$ mkdir -v ykla # -v 选项可以帮我们看到文件的变动，是 verbose 的缩写，即“啰嗦”一些，意为输出详细信息
ykla
```

If File Exists

```sh
$ mkdir ykla
mkdir: ykla: File exists # 提示已经有了该目录了！
```

---|---

DO YOU WANT TO CREATE A DIRECTORY __CODESPAN_0

```sh
$ mkdir ykla/ykla1/ykla2/ykla3
mkdir: ykla/ykla1/ykla2: No such file or directory
```

AS ABOVE, THE PARAMETERS __CODESPAN_0, __CODESPAN_1 ARE REQUIRED AT THIS TIME, MEANING THE ENGLISH __CODESPAN_2_(FATHER), I.E. IF THE PARENT DIRECTORY DOES NOT EXIST, IT IS CREATED TOGETHER。

```sh
$ mkdir -vp  ykla/ykla1/ykla2/ykla3
ykla/ykla1
ykla/ykla1/ykla2
ykla/ykla1/ykla2/ykla3
```

## __CODESPAN_0_ DELETING COMMAND

>** Warning**
>
The >FreeBSD command line interface does not have a wastebin, and all orders are irrevocable once executed. The command line operation __CODESPAN_0 is more dangerous。

THE ABBREVIATIONS __CODESPAN_0_, I.E. __CODESPAN_1_, ARE DELETED。

---|---

DELETE FILE __CODESPAN_0_

```sh
$ rm test
```

IF THERE IS NO FILE CALLED __CODESPAN_0_:

```sh
$ rm test
rm: test: No such file or directory # 报错指定的文件或目录不存在
```

---  |---  

REMOVE PATH __CODESPAN_0_

- If the directory is empty (without any documents, only empty directories)

```sh
$ rm /home/ykla/test
$ 
```

It can also be used as a command __CODESPAN_0_(remove directory, delete directory only empty):

```sh
$  rmdir /home/ykla/test
$ 
```

- If the directory is not empty

```sh
$ rm /home/ykla/test/
rm: /home/ykla/test/: is a directory # 提示我们 /home/ykla/test/ 是个目录
```

Forced deletion of __CODESPAN_0(recursively) and __CODESPAN_1(force)

>** Skills**
>
> What's Recursive
>
> > Once there was a mountain, there was a temple in which an old monk was telling stories to a small monk. The old monk said, “There used to be a mountain, there was a temple...” and this is the case of return。
>
>In this operation, meaning to go first to the deepest subdirectories under __CODESPAN_0, if any, to delete their files and subdirectories; then repeat the operation up. Until __CODESPAN_1_ was deleted. is the Depth-First-Search, DFS。

```sh
$ rm -rf /home/ykla/test/
```

>** Warning**
>
>USE __CODESPAN_0_ IS A RATHER DANGEROUS OPERATION AND IS IRREVOCABLE. IMAGINE WHAT WOULD HAPPEN IF THE ORDER __CODESPAN_1 _ __CODESPAN_2 _ (MORE THAN ONE SPACE) WAS WRONGLY STRUCK
>
> ```sh '
>root@ykla: ~ #rm-ref/home/ykla/test
>root@ykla: ~ #ls/home/ykla
>ls: /home/ykla: No such file or directory # finds that ykla is no longer available
> ````

>** Warning**
>
>Online it is often said that the use of __CODESPAN_0 is an order that can xx and mislead others to cause irreversible and catastrophic damage to the system. The command is in essence a root permission (~ okay FreeBSD defaults no sudo~), delete __CODESPAN_1_1_and all that exists under its subdirectories. Let me show you:
>
> ```sh '
>root@ykla: / #rm-ref /*
>rm: /boot/efi:
> rm: /boot: Directory not empty
>rm: /dev/reroot: Operation not supported
>rm: /dev/input: Operation not supported
>rm: /dev/fd: Operation not supported
> ... omitted part of..
>root@ykla:/#
> ````
>
>![ ] (.. .gitbook/assets/noefi.png)
>
When you restart, you'll find no guidance。
>
>** Thinking issues**
>
Do you have a deeper understanding of the phrase "root is the top of UNIX"? Does this indicate consistency of authority and responsibility? Abuse of power not only harms others, but ultimately deprives itself of the reality of existence。

## __CODESPAN_0_MOVE/RENAME COMMAND

THE ACRONYM __CODESPAN_0_, I.E. __CODESPAN_1_, IS MOVED。

---|---

MOVE __CODESPAN_0_TO __CODESPAN_1:

```sh
$ mv -v test /home/ykla # -v 选项可以帮我们看到文件的变动，是 verbose 的缩写，即“啰嗦”一些，意为输出详细信息
test -> /home/ykla/test
```

MOVE DIRECTORY AND SUBDIRECTORIES TO __CODESPAN_0_

---|---

- Rename

RENAME __CODESPAN_0_TO `test5.txt`_

```sh
$ mv -v  test5.pdf test5.txt
test5.pdf -> test5.txt
```

RENAME __CODESPAN_0_TO `test2.pdf`_

```sh
$ mv -v test2 test2.pdf 
test2 -> test2.pdf
```

COPY COMMAND ### __CODESPAN_0_

THE ACRONYM __CODESPAN_0_, I.E. __CODESPAN_1_, IS MEANT TO BE REPRODUCED。

---|---

COPY __CODESPAN_0_TO `/home/ykla`_

```sh
$ cp test /home/ykla/
```

At the end of ___CODESPAN_0 is important, if the end of __CODESPAN_1 is missing and if the subdirectories ykla do not exist, `test` will be renamed __CODESPAN_3_(ykla is supposed to be a directory):

```sh
$ cp test /home/ykla/
cp: directory /home/ykla does not exist # 若加上 /，会提示目录不存在
```

IF THE END OF ___CODESPAN_0 IS MISSING:

```sh
$ cp -v test /home/ykla # -v 选项可以帮我们看到文件的变动，是 verbose 的缩写，即“啰嗦”一些，意为输出详细信息
test -> /home/ykla
```

>** Thinking issues**
>
Is there a similar problem with other orders? Please try。

---|---

Modify file name and suffix while copying:

```sh
$ cp -v test /home/ykla/abc.TXT
test -> /home/ykla/abc.TXT
```

This command is usually used to back up the configuration file。

---|---

Copy directory and subdirectories:

```sh
$ cp -v /usr/ports/editors/vscode /home/ykla
cp: /usr/ports/editors/vscode is a directory (not copied).
```

It is not possible to see a direct copy; the hint is that the directory is not a file。

WE NEED OPTION __CODESPAN_0_. ___ CODESPAN_1__ MEANS __ CODESPAN_2_(RETROGRESSION):

```sh
$ cp -vr /usr/ports/editors/vscode /home/ykla
/usr/ports/editors/vscode -> /home/ykla/vscode
/usr/ports/editors/vscode/distinfo -> /home/ykla/vscode/distinfo
……省略一部分……
```

## REGULAR EXPRESSION_CODESPAN_0_

SOMETIMES THE OPERATION REQUIRES A FULL SELECTION AND CAN USE REGULAR __CODESPAN_0_。

- DELETE ALL FILES WITH THE NAME __CODESPAN_0_:

```sh
$ rm test*
rm: test: is a directory
rm: test4: is a directory
```

See, do not process the directory。

- DELETE ALL FILES WITH __CODESPAN_0 AND ** CATALOGUE**:

```sh
$ ls test*  # 确认匹配的文件
$ rm -rf test*
```

- Delete all files and ** Catalogue**:

```sh
$ ls *  # 确认匹配的文件
$ rm -rf *
```

# # LOGICAL OPERATOR __CODESPAN_0_

___ CODESPAN_0 (LOGICAL AND AND): ONLY IF THE ORDER OF __CODESPAN_1 __ HAS BEEN EXECUTED SUCCESSFULLY WILL THE ORDER OF THE LATTER BE EXECUTED; OTHERWISE, IF THE ORDER OF __CODESPAN_2 __ HAS FAILED, THE SUBSEQUENT ORDER WILL NOT BE EXECUTED。

SIMPLE UNDERSTANDING: YOU HAVE TO COOK BEFORE YOU CAN EAT, AND THEN YOU CAN BRUSH THE POT -- {\CHFFE7C5} {\CHFFE7C5} {\CH3F4F4} IF YOU DON'T COOK, THEN YOU CAN'T EAT。

Use of scenes: execute a series of dependencies. For example, you have to refresh the software to update the system before you can restart it. Take Ubuntu, for example: Only if the order in front is successful will the order in the back

# # LOGICAL OPERATOR __CODESPAN_0_

__CODESPAN_0 (LOGICAL OR OR): ONLY IF THE ORDER BEFORE __CODESPAN_1 IS WRONG WILL THE ORDER LATER BE EXECUTED; OTHERWISE, IF __CODESPAN_2 IS SUCCESSFUL, THE SUBSEQUENT ORDER WILL NOT BE EXECUTED。

SIMPLE UNDERSTANDING: EITHER YOU COOK, OR YOU ORDER TAKEOUT, OR YOU EAT - {\CHFFE7C5} {\CHF7C5} {\CH3F3F4} IF YOU CAN'T COOK, YOU'LL HAVE TO ORDER THE TAKEOUT. IF THERE'S NO TAKEOUT, YOU'LL HAVE TO EAT。

USE SCENE: IF AN ORDER FAILS, BUT YOU WANT HIM TO. YOU CAN WRITE A LOT OF CODESPAN_0 TO PREVENT REPEATED MANUAL IMPLEMENTATION OF THE ORDER AFTER A FAILURE, FOR EXAMPLE:

```sh
make BATCH=yes install || make BATCH=yes install || make BATCH=yes install || make BATCH=yes install
```

WHEN __CODESPAN_0_FAILED, THE NEXT __CODESPAN_1_ WILL STILL BE EXECUTED. IN OTHER WORDS, THE PREVIOUS ORDER FAILED TO BE EXECUTED, AND THEN THE SUBSEQUENT ORDER WAS EXECUTED

>** Skills**
>
> __CODESPAN_0_ AND __CODESPAN_1_ HAVE THE SAME PRIORITY AND EXECUTE FROM LEFT TO RIGHT。

>** Thinking issues**
>
WHAT DOES > CODESPAN_0__ MEAN
>
> IF __CODESPAN_0_ FAILS, WHICH OPERATION WILL BE FOLLOWED

# BSD style make/grep/ sed/awk

[make] of FreeBSSD (https://www.freebsd.org/cgi/man.cgi?query=make &apropos=0&sektion=0&manpath=FreeBSD+13.1-RELEASE+and+Ports&arch=default=html)//[i'mformat=html] (https://www.freebsd.org/cgi/man.cgi?query=grep&sektion=&n=1)///[i'm&apposposs=0&sorry, sed=0&sektion=0&sektion=0&s=0&s=0&s=0&sektion=0&s=0&s=0&s=0&s=0&sepas=FreeB=reeb_((i'm)=RefreeBS+andPorry_s=0&s&s=[.org/[wxxxxxx=Am_(egegegeg_Add=http.html=http.htm= See the man manual for more details。

Example:

```sh
sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
```

Must add an empty parameter', can't be omitted。



Turn off and restart

FreeBSD and Linux shutdown commands differ significantly in grammar and behavior, and if you have experience with Linux, you cannot copy it。

FreeBSD design is closer to traditional UNIX behavior。

Shutdown:

- USING __CODESPAN_0_ WILL NOT SHUT DOWN, BUT WILL SWITCH TO A “SINGLE-USER MODE” AND WILL PROMPT: __CODESPAN_1_TO ENTER A SINGLE-USER MODE UPON RETURN
- THE USE OF __CODESPAN_0 __ WILL NOT BE COMPLETELY OUT OF POWER, WILL ONLY STOP THE SYSTEM FROM RUNNING AND WILL BE PROMPTED TO: __CODESPAN_1 __ HERE BY PRESSING ANY KEY TO RESTART THE SYSTEM
- THE CORRECT SHUTDOWN AND BLACKOUT ORDER IS CODESPAN_0, WHICH IS EQUIVALENT TO CODESPAN_1_。

Restart:

- Resume commands are consistent with Linux, which are ___CODESPAN_0, but the parameters are not universal。
- Under FreeBSD `roboot` equals __CODESPAN_1_..

Note**
>
>close and restart require root permissions to execute。

