Section 2.4. Basis of the command line (new introductory version)

You're not alone

Many often miss or mix command or command parameters and options, but it is not your fault.

Many middle school staff also needed to learn how to use computers and mobile phones in the years. How do you explain how this group knows how to operate short video? Does this mean that short video is a better design?

Because many orders are either based on historical constraints or on the ability of developers to maintain them, they are not so uniform or easy to remember or use.

Query [man page] (https://man.freebsd.org/cgi/man.cgi) will know that there is a specific entry called “BUGS”, which is used to describe the deficiencies of the current software.

In terms of personal use experience, if a single software could not find 10 bugs that seriously affected or impeded its use, it would never be open-source software. And most defenders are powerless because Bug is too many, or reality is too confusing, and they have no economic incentive to repair it. The vast majority of open-source businesses have millions or millions of open-source software, and their defenders have mostly never received any financial compensation or reputation.

Trust me, you're not the one who thinks these things are hard to use or even wants to break the keyboard. This is also one of the reasons why people continue to “crew” (resulting in a tool). If you think the GCC is hard to use, then you can go with Clang+LLVM. You're not the first person to find the GCC difficult, and you're not the last.

Many have stressed the importance of command lines, and users of GUI software such as IDE with arrogance and contempt are not necessary. Many will deliberately resonate on the so-called advantages of these tools, a group that is pure Sdergor syndrome patients and advocates of the philosophy of suffering. The essence of Unix ' s philosophy is not to adhere to the ancient laws of ancestral law, but to emphasize the human being. That's today, a quarter of the twenty-first century, still emphasizing the meaning of Unix philosophy. Most people have been blinded by the philosophy of suffering, with an emphasis on the roots, and hate begins with 0 and 1 of computers, while those who seem to be soberer are more confused.

What's so bad if people feel happy and happy? It has always been stressed that these are knowledge and should be reversed. The real question is, what is knowledge? Is knowledge and degree linked? How do you explain that most undergraduates don't know the difference between the monitor and the mainframe?

The American philosopher B. F. Skinner said, "Education is the rest when one forgets everything he learned at school." Unlike traditional Western perceptions (e.g. Plato's memoirs, Augustine's light and God's memory, Locke's whiteboards) and Confucius doctrine (e.g., “learning and learning” in Theory of Essays) and even the emphasis on memory in traditional folklore (e.g., the loss of memory when drinking Bombay's soup) — and the greater emphasis on “forgetting” — this is the further development of the old man's “actless religion” (the second chapter of the Code of Ethics). In Free Travel, M.J. emphasized that “the knowledge is not the knowledge”, and that what we learn on a daily basis is not “the knowledge”. In his view, both old and modern learning is fundamentally alien to human beings, who are taught by modern society and are the culture of the industrial revolution, not knowledge.

>** Thinking issues**
>
>This paper lists the orders and options that are required on a daily basis.
>
> A command may have several hundred options or parameters, and a dictionary or document (man also info) is used to check not back.
>
What do you think, "I've got a career and no career. You've lost your career?

Again, if you've forgotten everything after reading this, only if you use AI to see how orders work, or if you just go from "FreeBSD" to running, then congratulations! You have successfully mastered the most important elements of this paper.

References

- [Reporting] HYDRA: A “rich” harvest with “accumulation” (https://www.cas.cn/xw/cmsm/2014/04/t20140402_4084616.shtml), and, like young people, 71-year-old Ho is now using smartphones.
- [New methods and new names in teaching] (https://www.bfskinner.org/wp-content/uploads/2014/02/New-Methods-aims-in-Teach.pdf), which is not what Einstein said. Is it true that the knowledge we have acquired is so right and true that we are blackmailed now?
- Shiyonlong. Zhuoko's “forgotten” educational picture explains [J]. University education science, 2022 (01): 105-112.

# Login to FreeBSD

When you install FreeBSD, if everything is normal, you should see the following on the screen:

```sh '
FreeBSD/amd64 (ykla) (ttyv0)

I don't know.
````

We call the interface on this screen the TTY or the physical terminal.

Explanation:

- `FreeBSD ' is the name of the operating system;
- `amd64 ' is the structure of the system, which normally is amd64, or x86-64, for Intel and AMD processors;
- `ykla ' is the host name that you set up when the system was installed;
- `ttyv0 ' refers to the first TTY, and you will find that most of the computer's sequences are on zero;
- `login: `Indicating user login.

We enter user names and passwords to log in to the system:

```sh '
FreeBSD/amd64 (ykla) (ttyv0)

login: root # Enter the user name here, then press Back
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
I'm sorry, I'm sorry.
For other languages, place "en" with a language code like de or f.

Show the version of FreeBSD accepted: freebsd-version; uname-a
Please include that output and any emergency messages when posing questions.
Introduce to human pages: man man
FreeBSD directory playout:

To change this logic, see motd (5).
Root@ykla:

````

Congratulations! You've successfully logged into the FreeBSD operating system.

Note**
>
>The password will not be re-printed onto the screen: normally when we enter the password, `****** ' will be displayed on the screen. However, in FreeBSD, where passwords are involved, there will be no display, even if they are empty on the password screen, and no input is a state, nothing, nothing, just enter it back.

- 1: root is the highest authority in UNIX. We used to say Andre root, apple escape, Kindle escape, and so on, to get this root access.

References

- [What is TTY in Linux?] (https://itsfoss.com/what-is-tty-in-linux/), translated in [Linux] Blackword explains: TTY. (https://linuxtory.org/linux-blackmail-explained-what-is-tty/).


# # troubleshooting and unfinished business

- If the user name is correct, but the password is incorrect:

```sh '
I'm sorry.
Password:
Login: incorp
I don't know.
````

- If the username and password are incorrect:

```sh '
login: test # The user does not exist on the current system
Password:
Login: incorp
I don't know.
````

If you don't even know the user name, you can find the root password and see what user accounts or reloading systems are faster.

Who am I?

- View the username of the current login system:

```sh '
Whomi
Ykla
````

- View current login user group related

```sh '
id
uid = 1001 (ykla) gid = 1001 (ykla) groups = 1001 (ykla), 0 (wheel)
````

- View the interruption of current user login and the current login time

```sh '
Who?
root pts/0Mar 19 1500 (3413e8b6b43f)
````

- Show us which users are login and what they're doing.

```sh '
W... w...
3:02PM up 21:52, 1 user, load averages: 0.01, 0.01, 0.00
USER TTY FROM LOGIN@IDLE WHAT
Root pts/ 0,3413e8b6b43f 3 PM-w
````

- View current path

`pwd 'is `print work directory ', printing job directories

```sh '
$pwd
/usr/ports/editos/vscode
````


# Account toggle and exit login

```sh '
root@ykla: / #su ykla 1
ykla@ykla:/ $2
ykla@ykla:/ $su 3
Password: 4
Root@ykla: /#
Root@ykla:/ #exit 5
ykla@ykla:/ $ exit 6
Root@ykla:/ #exit 7

FreeBSD/amd64 (ykla) (ttyv0)

I don't know.
````

-1 Use `suspace username 'to switch to user ykla, switch from root and not need to enter ykla password:
- `root@ykla:/:
- `root ' : Current user is root
- `@`Who' `on `xx' host
- `ykla ' : This is the host name and has nothing to do with ykla. You can name a different host.
- `:/ `: on behalf of the current `/ ` path
Did you notice the change in the hint? root is `# ' and common user is `$ ' (csh is %)
- 3 If it is simply a `su ' return, the command is to switch from the current user to the root account (if it is already root, there will be no reaction). But you have to be a member of the wheel group to do this, otherwise you will miss ' sorry ' .
-4 Switch from normal user to root, the password to enter is the login password for the root account.
-5 Enter `exit ' to exit the current user, and if only login user, exit login to TTY

>** Thinking issues**
>
> 6 and 7, respectively, which users were replaced or which operations were performed?

Command line format

Most command line orders should be meaningful, such as `ls ' or `list ' (listed), `wget ' or `get ' or `get ' (download) through web (network); and few unknown orders, such as `fuck ' (orders that automatically correct spelling errors).

```sh '
# Command Options Parameter 1 Parameter 2
#ls-l/home/ykla/tmp
/home/ykla:
Total 317
...with some omission...
Downloads 2 ykla ykla 2 Mar 9 20:45
Drewxr-x-x 2 ykla ykla 2 Mar 9 20:45
Desktop

/tmp:
Total 6
3 Mar 18 17:23. ICE-unix
-r-r-r-r-- 1 root wheel 11 Mar 18 17:10. X0-lock
````


Where `ls ' (L lower case) means the list of documents in the current or specified directory; option `-l ' (L lower case) means the printing of detailed information and the output format (*long*).

Most of the orders are now subject to the above (abbreviated). This is provided for in [POSIX.1-2024] (https://pubs.opengroup.org/onlinepubs/97997919799).

We need to note that English and Chinese are different, that there are no spaces to divide between Chinese, and that English words must be separated by using spaces. Therefore, there should be room in the middle of each part of the order line, i.e. ' . The number of spaces is generally not limited, but should be at least one, i.e. ' .

>** Thinking issues**
>
> How does the software understand the entire sentence if the command line is not separated by space or some way (e.g. other symbols)?
>
> What kind of experience does it have from a human perspective, without space, from a natural language perspective? >
>
> Replace: `ls-l/home/ykla/tmp ' , `ls/ ' .
>
> ```sh '
>root@ykla:~ #ls-l/home/ykla/tmp
>-sh: ls-l/home/ykla/tmp: not found
>root@ykla: ~ #ls/
>-sh: lls/: not found
> ````
>
As you can see, shell will use the whole sentence as an enforceable order.

We also need to know that an order does not have an automatic error correction function, even if it is just a wrong letter, missing a number, and the order is never successful:

```sh '
# LS # Try full capital
LS: not found
♪ Ls ♪
Ls: not found
Root@ykla: ~ #ls/hom1 /home
No such file or direction
root@ykla: ~ #ls-z/ home # does not exist -z
Is: invalid option-z
Usage: lls [-ABCFGHILPRSTUWZabcdfghiklnoptrstuvwxy1,] [--color=whon] [-D format] [-group-directors=]
````

>** Skills**
>
>Windows is not only not sensitive to file sizes, but also to command sizes.
>
> ``powershell '
>PS C:\Users\ykla> cd C: # Here cd is lowercase
>PS C: > CD D: # Here CD is uppercase
>PS D: > CD c: # Here the C disc is lowercase
>PS C: > dir # lowercase dir, list the directory, equals ls
>
> Directory: C:\
>
> ... part of the omission ...
>
>PSC:\Users\ykla>TREE # Uppercase tree, show path relationships
> Folder PATH List
> Volume Series 2A90-E989
>C: .
I'm sorry.
I miss-- .cache
I'm sorry.
> ... omitted part of...
> ````

> ** Skills**
>
> What does `# ' mean after the command? `# `in shell is generally a note (set out by [POSIX.1-2024] (https://pubs.opengroup.org/onlinepubs/9799799/utilities/V3_chap02.html)), which is equivalent to `/ ' in the C language. This means that the text at the back is only illustrative and not practical.



# thefuck: Automatically correct the misspelled command

# # install the fuck #

Use pkg

```sh '
♪ pkg in the fuck
````

Or ports.

```sh '
# cd/usr/ports/misc/thefuck/
# Make install clean
````

# # Configure the fuck

View installation configuration information

```sh '
# Fuck #
Seems like fuck Libya isn't compromised!
More data - https://github.com/nvbn/thefuck#manual-information
````

We'll open the web browsing. `eval $ (thefuck-lias) ' was found to be added to ~/.bash_profile` (bash shell), ~.bashrc` (bash shell) or ~.zshrc ' (zsh shell).

We FreeBSD by default use sh, so will:

```sh '
eval (thefuck-lias)
````

Write ~/.shrc ', do not use > > redirection, add manually.

Refresh environment variables:

```sh '
Root@ykla: ~ /.shrc
# Fuck #
No fucks give
````

>** Skills**
>
>On the basis of the author ' s information, other aliases can be used if you do not like input `fuck ' : if changed to `eval $ (thefuck-lias abc) ' , all `fuck ' orders below will be replaced with `abc ' .
>
> ```sh '
>root@ykla: #abc
Nothing found
>root@ykla: #plg install gimp
>-sh: plg: not found
>root@ykla: #abc
> pkg install gimp [enter/↑/↓/ctrl+c]
> ... omitted part of...
> ````


# # test with thefuck

```sh '
Root@ykla:~ #ls-l/home/ykla
I don't knowfound
# Fuck #
# Up and down arrows for possible commands, car confirmation, ctrl c interrupted
Total 317
. . . . . . . . . . .
Downloads 2 ykla ykla 2 Mar 9 20:45
Drwxr-xr-x 2 ykla ykla 2 Mar 9 20:45 Desktop
````

Try again:

```sh '
Root@ykla:
plg: not found
# Fuck #
pkg install gimp [enter/↑/ctrl+c]
Updating FreeBSD repository catalogue...
FreeBSD report is up to date.
. . . . . . . . . . .
````

Command execution and interruption

Unlike the Windows and graphical interface software, most command line programs do not have any progress tips in their execution. There are usually only two outcomes:

- Successful implementation of:

```sh '
@ykla: #cptest/root/mydir
Root@ykla:

````

- Implementation interruption:

```sh '
Root@ykla: #cptest9/root/mydir/
No such file or direction
````

There are many possible circumstances in which the interruption of execution is possible, but only one (no specified document or directory exists).

It can be seen that only when the execution is interrupted does the command line have a hint; if the execution is completed, there will be no hint. This Unix design philosophy is designed to ensure the simplicity of terminal output.

Shell

Our orders are to run in the shell, interact with the system through the shell.

FreeBSD default shell is sh (Bourne shell, originally named Stephen R. Bourne). It has now been rewritten and is in general conformity with the regulation of shell in [POSIX.1-2024] (https://pubs.opengroup.org/onlinepubs/9799799/utilities/V3_chap02.html).

The usual shell in Linux is bash. The default shell in MacOS is usually a zsh (Z shell).

Note**
>
There are sshs in >Linux, but it's usually softly linked to bash or other shells, which are not real sshs.
>
>-Ubuntu 24.04 LTS default shell:
>
> ```bash '
>$ls-l/bin/sh
>lrwxrwx 1 root root 4 February 25:19 /bin/sh-> Dash
> ````

Shortcut

Note**
>
> The following shortcut key does not have to be in lower case to be executed, as in upper case.

# # Turns pages and/or lines on the TTY interface

## # Use the Scroll Lock key to flip/ flip pages over and down the TTY interface

Use **Scroll Lock** (rolling): When you press **Scroll Lock**, you can operate the screen using the upper/ lower ↓ orientation key,**Page Up**/**Page Down**.

Different:

- Up/ down
-**Page Up**/**Page Down** Key: Scroll one page on the TTY interface

Press **Scroll Lock** again to exit this mode.

>** Skills**
>
>SL key above **HOME** key, PS screenshot key **Print Screen** right, PB key ** Pause break** left.

In fact, historically, **Scroll Lock** this key was designed for this.

### # use Shift to flip/ flip pages on the TTY interface

Use **Shift** shortcut:

-**Shift** + Up/ Down Direction Key - Scroll a line up/ down in the TTY interface
-**Shift** + **Page Up**/**Page Down** Key - Scroll one page on the TTY interface

## # Complete command or directory

Usually complete commands or directories by **Tab**. Up arrow ** ** is looking at the last command, down arrow ** ** is looking at the next command.

- Completing orders.

```sh '
Root@ykla: ~ #lo # If you press TAB at this time, the output is as follows. You can lose another letter and press TAB again.
I don't know what you're talking about.
The local-unbound local logins
The local-unbound-anchor lock logname
I can't believe it.
Local-unbound-controllockstat Lorder
Local-unbund-setup locktest downtfs-3g
I'm sorry, locale.
````

- Complete file directory or filename

```sh '
$cp / home/ ykla/ # Press TAB here and then press TAB again to see the effect
$cp /home/ykla/test/1.txt
.cache/.login bin/test2
...config/.profile HW_PROBE/test3
I don't know.
.getconfig.sh_histoory.Y8RqIDIDIV mydir/
.k5login.shrc
````

# # Abort the command #

**ctrl** **c**:

```sh '
# Ping163com
PING163.com (59.11160.244), 56 data bytes
64 bytes from 59.111.160.244: icmp_seq=0tl=52 time=27.672 ms
64 bytes from 59.111.160.244: icmp_seq=1 ttl=52 time=27.580 ms
^C # Here, ^C means you pressed the ctrl+c key here and then the command was terminated.
--163..
2 packets trained, 2 packets received, 0% packet lost
= 27.580/27.626/27.672 0.046 ms.
````

Command backstage

**ctrl**+**z**: Place the current process backstage and return to the front desk with a `fg ' command:

```sh '
# Ping163com
PING163.com (59.11160.244), 56 data bytes
64 bytes from 59.111.160.244: icmp_seq=0tl=52 time=27.611 ms
64 bytes from 59.111.160.244: icmp_seq=1 ttl=52 time=27.691 ms
^[1] + Suspended ping 163com #
Root@ykla: ~ fg
Ping 163.com
64 bytes from 59.111.160.244: icmp_seq=3 ttl=52 time=27.465 ms
64 bytes from 59.111.160.244: icmp_seq=4tl=52 time=27.586 ms
64 bytes from 59.111.160.244: icmp_seq=5 ttl=52 time=27.522 ms
^C #Crtl +c to close the command
--163..
6 packets trained, 6 packets received, 0% packet lost
= 27.465/27.596/27.701/0.085 ms
````

Other

-**ctrl**+**l** (L): Empty screen
-**ctrl**+**a**: Move cursor to command line beginning
-**ctrl**+**a**: Move cursor to end of command line

# The source of the command

# Linux

In Linux, all commands are basically from the GNU package, and the Linux kernel does not have any commands. Let's check this out:

```bash
Dpkg-S/bin/mv
/bin/mv
Dpkg-S/bin/cp
/bin/cp
Dpkg-S/bin/ls
/bin/ls
US$dpkg-S/bin/pwd
/bin/pwd
Dpkg-S/bin/cat
/bin/cat
US$dpkg-S/usr/sbin/chroot
/usr/sbin/chroot
Dpkg-S/bin/kill
/bin/kill
Dpkg-S/usr/bin/free
Procps: /usr/bin/free
Dpkg-S/bin/su
util-linux: /bin/su
````

See, in Linux, these common commands are generally derived from GNU software coreutils, util-linux or procps. These software have historically been the re-realization of UNIX by GNU plans.

At the same time, shell itself has some orders:

```bash
$ type cd
cd is shell built-in
````

List all shell built-in commands:

```bash
That's what I want.
I don't know.
:
[ Chuckles ]
Oh, my God.
bg
I'm sorry.
Break
I'm sorry.
Caller
cd
I'm sorry.
Compgen
. . . . . . . . . . .
I don't know.
I'm sorry.
@unalia
I don't know.
Wait
````

FreeBSD

```sh '
$ type cd
Well, cd is a shell buildin.
````

In FreeBSD, except for the above-mentioned shell built-in commands (see [sh(1)] (https://man.freebsd.org/cgi/man.cgi?sh(1))), common commands are self-contained in the basic system and do not belong to any package. For example, the `ls ' command, whose source code is located in [freebsd-src/bin/ls/] (https://github.com/freebsd/freebsd-src/tree/main/bin/ls). The FreeBSD system is an organic whole. It is not a package package that is maintained by different people or teams.

If you configure pkgbase, output is similar:

```sh '
# pkg which/bin/ls
/bin/ls was incorporated by package FreeBSD-runtime-15.snap202500313173555

````


If any command is missing, it can generally be obtained by installing the corresponding package, such as the `lspci ' command, from the package `sysutils/pciutil ' . But there are also a number of commands that have Linuxist problems and are not compatible with other operating systems, such as the ip command, from the GNU package iproute2.

# `ee ' editor basic usage

`ee ' is the editor in the FreeBSD basic system.

The use of `ee ' is much simpler than [nano] (https://www.redhat.com/zh/blog/getting-stard-nano) (a GNU editor), as you can see from its name, “easy editor”.

Like what?

```sh '
# eee a.txt
````

It can be edited directly, just like `nano ' or Windows notebooks.

Press **ESC** to display a reminder box and press ** Return key** to save it.

# `vi ' Editor Basic Use

FreeBSD also has a built-in editor, `vi ' , which is more sophisticated. Unlike most categories of UNIX operating systems, which link `vi ' to `vim ' , the BSD system is the real `vi ' (actually `nvi ' , i.e. new vi, 4.4 BSD is then realized).

- `vi ' under MacOS

```sh '
US$ls-al/usr/bin/vi
lrwxr-xr-x 1 root wheel 3 4 12 13:16/usr/bin/vi-> vim
````

The default after `vi ' open BSD is in "command mode" when `i ' enters into " text mode" and can be easily edited. It should be noted that ** Delete key (reverted key)** does not work, or is the same as **Insert key**. To delete text, press **Delete**.

```sh '
bc123
~ That's it
~ That's it
~ That's it
````

>** Skills**
>
>The empty line will be shown as ~.

After editing, press **ESC** to return from text mode to command mode.

In command mode, enter an order `: ' , i.e. `: q ' is exit from non-storage, `:wq ' is preservation and exit, `:wq! ' is compulsory preservation, `:q! ' is compulsory exit.


```sh '
ABC
~ That's it
~ That's it
:wq
````

Common commands

## `cd ' Command

`cd ' (change working directory, change job directory)

Switch to '/home '

````
$cd/home
Look where it is.
/home
````

### `ls ' Command

The basic use of the `ls` (list, list) command has been described above. The following is an attempt to allow the `ls ' to be listed in a human-readable way:

Option `-h ' , i.e. `human ' (human) shall be used in conjunction with `-l ' (`long ' long output).

```sh '
#ls-hl/home/ykla
Total 326 KB
-rw -- -- 1 ykla ykla 50B Mar 18 17:23. Xauthority
Drwx -- - 6 ykla ykla 6B Mar 10 16:21.cache
Drwx -- --9 ykla ykla 12B Mar 19 15:01.config
-rw-r-r-- 1 ykla ykla 1.0K Feb 24 12:18.shrc
Drwxr-x-x 2 ykla ykla 2B Mar 9 23:48.themes
-rw-r-r-r- 1 root ykla 0B Mar 1915:13 abc. TXT
Drewxr-X3 root ykla 7B Mar 19 15:17 vscode
-rw -- -- 1 ykla ykla 17M Mar 18:09 xrdp-chansrv.core
Drwxr-xx 2 ykla ykla 2B Mar 9 20:45 Download
. . . . . . . . . . .
````

In UNIX, documents or directories starting with `. ' (e.g. `.XIM-unix ' above) are hidden. Your Android phone is the same -- you can look at it yourself.

And option `-a ' can show hidden directories or files:

```sh '
Ykla
.cshrc.login.profile public video
....dbus.login_conf.sh_history
. Xauthority.face.mail_aliass.shrc
.cache .icons .mailrc .themes desktop
.config .local .mozilla Download Template
````

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
>Think on the output above: `. ' , ' . . . . . . . . . . . . . . . . . . . . . . . . . .

What about `-a ' ?

```sh '
Ykla
Download public pictures, documents, desktop templates, videos, music
````

Do not show hidden files.

>**Technology**,
>
> Please test as a normal user because the root shell of FreeBSD always shows hidden files.

## # # `touch ' Create file command

`touch ' means touch, meaning slight change.

Create a file called `test ':

```sh '
That's too much.
````

>** Skills**
>
> You can see that I created `test ' , not `test.txt ' , `test.word ' , `test.pdf ' , etc. FactsOn top, this part of `.txt ' , which we call suffix, is primarily visible, not machine. Is it true that many things we think are as clear as we think?
>
>Even if we remove the corresponding suffix name, the type of file can be identified in the UNIX class, as determined by the file numbers:
>
> ```sh '
>$filebook
>book: PDF document, version 1.7
> ````

One-time multiple files can be created using multiple parameters (similar usage is almost universal and not repeated):

````
Touch test 1 test 2 test 3
````

## # `mkdir' Create directory

`mkdir ' means `make directories ' , create directory

Create a directory called ykla

```sh '
$ mkdir-v ykla#-v options can help us to see changes in the document, which is the abbreviation of the verbose, which means "shut" for the output of detailed information
Ykla
````

If File Exists

```sh '
$ mkdir ykla
mkdir: ykla: File examples # hint already have the directory!
````

I don't...

What if the directory `ykla/ ykla1/ ykla2/ ykla3 '?

```sh '
$ mkdir ykla/ykla1/ ykla2/ykla3
mkdir: ykla/ykla1/ykla2: No such file or direction
````

As above, the parameter `-p ' , `p ' , is meant by the English `parents ' (father), i.e. created in the absence of a parent catalogue.

```sh '
$ mkdir-vp ykla/ykla1/ykla2/ykla3
Ykla/ykla1
Ykla/ykla1/ykla2
Ykla/ykla1/ykla2/ykla3
````

## `rm ' Delete Command

>** Warning**
>
The >FreeBSD command line interface does not have a wastebin, and all orders are irrevocable once executed. The command line operation `rm ' is more dangerous.

`rm ' , the acronym `remove ' in English, is deleted.

I don't...

Delete File `test '

```sh '
$rm test
````

If there is no `test ' file:

```sh '
$rm test
rm: test: No such file or directory # error specified does not exist
````

I don't...

Remove Path `/home/ykla/test '

- If the directory is empty (without any documents, only empty directories)

```sh '
$ rm/home/ykla/test
It's okay.
````

Command `rmdir ' (remove directory, delete directory only empty):

```sh '
$ rmdir/home/ykla/test
It's okay.
````

- If the directory is not empty

```sh '
$ rm / home/ykla/test/
rm: /home/ykla/test/: is a directory / home/ ykla/ test/ is a directory
````

Use parameters `-r` (recursively) and parameters `-f` (force) to forcibly delete:

>** Skills**
>
> What's Recursive?
>
> > Once there was a mountain, there was a temple in which an old monk was telling stories to a small monk. The old monk said, “There used to be a mountain, there was a temple...” and this is the case of return.
>
>In this operation, it is meant to go first to the deepest subdirectories under `/home/ykla/test/ ' , if any, and delete their files and subdirectories themselves; then repeat them up. Until `/home/ykla/test/ ' is deleted. is the Depth-First-Search, DFS.

```sh '
$rm-ref/home/ykla/test/
````

>** Warning**
>
>Use `rm-ref ' is a rather dangerous operation and is irrevocable. Imagine what would happen if the order `/home/ykla/test/` were misspelled as `/home/ykla/test/` (in more spaces)?
>
> ```sh '
>root@ykla: ~ #rm-ref/home/ykla/test
>root@ykla: ~ #ls/home/ykla
>ls: /home/ykla: No such file or directory # finds that ykla is no longer available
> ````

>** Warning**
>
>Online, it is often said that the use of `subdo rm-ref/* `is an order that can xx and mislead others to cause irreparable and catastrophic damage to the system. In essence, the command was based on root privileges (~ okay FreeBSD defaults no sudo~), deleting `/ ' and all that exists under its subdirectories. Let me show you:
>
> ```sh '
>root@ykla: / #rm-ref /*
>rm: /boot/efi:
> rm: /boot: Directory not empty
>rm: /dev/reroot: Operation not supported
>rm: /dev/input: Operation not supported
>rm: /dev/fd: Operation not supported
> ... omitted part of...
>root@ykla:/#
> ````
>
>![ ] (.. .gitbook/assets/noefi.png)
>
When you restart, you'll find no guidance.
>
>** Thinking issues**
>
Do you have a deeper understanding of the phrase "root is the top of UNIX"? Does this indicate consistency of authority and responsibility? Abuse of power not only harms others, but ultimately deprives itself of the reality of existence.

### `mv 'move/rename command

`mv ' is the acronym `move ' in English and is moved.

I don't...

Move file `test ' to `/home/ykla ':

```sh '
$ mv-v test/home/ykla#-v options can help us to see changes in the document, which is the abbreviation of the verbose, which is "beep" and means output details
test - /home/ykla/test
````

Move directory and subdirectories to `/home/ykla '

I don't...

- Rename

Rename 'test5.pdf 'to 'test5.txt '

```sh '
$ mv-v test5.pdf test5.txt
test5.pdf ->test5.txt
````

Rename `test2 'to `test2.pdf '

```sh '
$ mv-v test2 test2.pdf
test2 - test2.pdf
````

### `cp ' Copy Command

The acronym `cp ' , which is English `copy ' , is meant to be reproduced.

I don't...

Copy file `test ' to `/home/ykla '

```sh '
$cp test/home/ykla/
````

The end of `/ ' is important, and `test ' will be renamed `ykla ' (ykla is supposed to be a directory) if the end of `/ ' is missing and the subdirectories do not exist:

```sh '
$cp test/home/ykla/
cp: directory / home/ ykla does not exist # If added / suggests that the directory does not exist
````

If the end `/ ' is missing:

```sh '
$cp -v test/home/ykla# -v options can help us to see changes in the document, which is the abbreviation of the Verbose, which is "beep" and means output of detailed information
test - /home/ykla
````

>** Thinking issues**
>
Is there a similar problem with other orders? Please try.

I don't...

Modify file name and suffix while copying:

```sh '
$cp-v test/home/ykla/abc.TXT
test - /home/ykla/abc.TXT
````

This command is usually used to back up the configuration file.

I don't...

Copy directory and subdirectories:

```sh '
$cp-v/usr/ports/editos/vscode/home/ykla
cp: /usr/ports/editos/vscode is a directory.
````

It is not possible to see a direct copy; the hint is that the directory is not a file.

We need option `-r'. `r ' means `recursively ' (referral):

```sh '
$cp-vr/usr/ports/editos/vscode/home/ykla
/usr/ports/editos/vscode - /home/ykla/vscode
/usr/ports/editos/vscode/distinfo->/home/ykla/vscode/distinfo
. . . . . . . . . . .
````

## Regular expression ##

Sometimes the operation requires a full selection and can use the regular rule `* ' .

- Delete all files with `test ' headers:

```sh '
What's wrong?
Rm: test: is a directory
rm: test4: is a directory
````

See, do not process the directory.

- Delete all files headed by `test ' and ** Catalogue**:

```sh '
$ls test*
What's wrong?
````

- Delete all files and ** Catalogue**:

```sh '
♪ And I'm like, ♪Confirm matching files
♪ I can't believe it ♪
````

# # Logical operator # ##

`& (Logical and, AND): Only if the order before & has been executed, the order behind will be executed; otherwise, if the order before & has failed, the subsequent order will not be executed.

Simple understanding: You have to cook before you eat, and then you can brush the pot - > Cook the cooker `& `Eat the meal ` & ` If you don't cook, then you can't eat.

Use of scenes: execute a series of dependencies. For example, you have to refresh the software to update the system before you can restart it. Take Ubuntu, for example: `subdo apt update-y & subaapt upgrade-y & subo reboot'. Only if the order in front is successful will the order in the back.

# The logical operator #

`Logical ' (or `OR): Only if the order prior to ' || is wrong will the order later be executed; otherwise, if the order prior to ' || has been successful, the subsequent order will not be executed.

Simple understanding: either you cook, or you order, or you eat, or you cook, or you eat, or you eat, or you eat, or you eat, or you eat, or you eat, or you eat, or you eat. If you can't cook, you'll have to order the takeout. If there's no takeout, you'll have to eat.

Use scene: If an order fails, but you want him to. You can write a lot of ' || ' to prevent repeated manual implementation of the order after a failure, such as:

```sh '
♪ Make BATCH ♪
````

The next `make BATCH=yes install ' will still be implemented after a failure. In other words, the previous order failed to be executed, and then the subsequent order was executed.

>** Skills**
>
> & and `|| have the same priority and execute from left to right.

>** Thinking issues**
>
What does >touch a.txt & & touch b.txt || touch c.txt || reboot ' ?
>
> If `touch a.txt ' fails, which of the following operations will be performed?

# BSD style make/grep/ sed/awk

[make] of FreeBSD (https://www.freebsd.org/cgi/man.cgi.cgi?query=make&apropos=0&sektion=0 &manpath=FreeBSD+13.1-RELEASE+and+Ports&arch=default&format=html)/[grep] (https://www.freebsd.org/cgi/cgi?query=gep&sektion=&n=1)//[sed] (https://www.freebsd.org/cgi/man.cgi?quer=0&manpath=FreeBS+13-RELES+and & Ports=default&html=html)//[sed] (https://www.freebs.org/cgi/man.cgi?Qry=0&manpath=FreBreBS +eg=Ewg=Em=E.html=E.org/mregägägägägägägägägägägä See the man manual for more details.

Example:

```sh '
Sed-i's/quarterly/latest/g'/etc/pkg/FreeBSD.conf
````

Must add an empty parameter', can't be omitted.



Turn off and restart

FreeBSD and Linux shutdown commands differ significantly in grammar and behavior, and if you have experience with Linux, you cannot copy it.

FreeBSD design is closer to traditional UNIX behavior.

Shutdown:

- The use of `shutdown now ' will not shut down, but instead switch to a "single user mode" and will prompt: `Enter full pathname of shell or RETURN for /bin/sh: `Enter full pathname for /bin/sh after return;
- The use of `shutdown-h now ' will not be completely out of power, but will only stop the system and will be prompted: `The opening system has held. Please press any key to reboot. ' ;
- The correct shut-off and blackout order is `poweroff ' , which is equivalent to an order `shutdown-p now ' .

Restart:

- The restart order is consistent with Linux and is `reboot ' , but the parameters are not universal.
- `roboot ' under FreeBSD equals `shutdown-r now '

Note**
>
>Close and restart require root permissions to execute.

。