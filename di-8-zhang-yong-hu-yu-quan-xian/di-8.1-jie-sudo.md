# section 8.1 sudo and doas

doas

IN FACT, FOR MOST PEOPLE, IT'S ONLY CODESPAN_0, AND THE REST IS SUPERFLUOUS。

OpenBSD has developed its own [doas] (https://man.openbsd.org/doas) because of the complexity of the sudo software configuration, poor code quality and too many loopholes. Naturally, FreeBSD can also be used。

# install doas #

- install with pkg:

```sh
# pkg install doas
```

- Or install with Ports:

```sh
# cd /usr/ports/security/doas/
# make install clean
```

# # see doas installed information

```sh
root@ykla:~ # pkg info -D doas
doas-6.3p12:
On install:
To use doas,

/usr/local/etc/doas.conf

i'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry
/usr/local/etc/doas.conf.sample as an example.
# to use doas, a profile must be created /usr/local/etc/doas.conf。
# see on-line documents for doas.conf(5), or see the /usr/local/etc/doas.conf.sample profile。

In order to be able to run most desktop (GUI) applications, the user
if keepenv is not treated then
keeps, like the user's $HOME can, will be reset and cause the GUI
i'm sorry, application to crash.
# Note: If you need to run a GUI (GUI) program, you must add a keyword to the configuration。
# OTHERWISE ENVIRONMENT VARIABLES LIKE $HOME WILL BE EMPTIED, LEADING TO THE COLLAPSE OF THE GUI PROGRAM。

Users who only need to run line applications can usually get away
i don't know.
# if only to run the command line program, usually no keepenv。

When in doubt, try to understand us as it is less secure to have
i'm sorry, but i'm sorry.
# if it's not clear whether it's necessary, it's recommended to avoid the use of keepingenv, as it could reduce the system's security
# The environment variable of the original user is passed to the target user with permission。

On upward from doas<6:1
With the 6.1 transfer of most environmental assets (e.g. USER),
From the original user to the target user has changed.
# Environmental variables (e.g. USER, HOME, PATH) have changed from doas version 6.1。

Please return to doas.conf(5) for further details.

# see doas.conf(5) on-line documentation for more details。
````

# configure doas

IT IS KNOWN ABOVE THAT THE EXAMPLE TEMPLATE IS AT ___CODESPAN_0。

AND WE NEED TO PUT THE PROFILE ON ___CODESPAN_0, AND THE DOCUMENT DOES NOT EXIST BY DEFAULT AND WE NEED TO CREATE IT OURSELVES。

- CODESPAN_0 __ reads as follows:

Let's just say this:

```
# Sample file for doas
# Please see doas.conf manual page for information on setting
# up a doas.conf file.

♪ Permit members of the world group to perform actions as root. ♪.
permit :wheel # allow the wheel group members doas

# Same without having to enter the password
_other organiser

♪ Permit user like to run people as a root user. ♪.
# allow the user alice doas

♪ Permit user Bob to run the programs as root, makin' ♪
# Environables. #.
personal keepenv Bob as root # Allows users to Bob doas and inherits the environment variable of the user Bob, which is required by the GUI but which reduces security (see see post-installation information)

? Permit usr kind to run only the pkg pack as root
# to perform package updates and upwards. #.
%1 content as root cmd pkg arms update %1
# only pkg upgrad

♪ Allow david to run id company as root without reading it ♪
_Other Organiser command as root cmd id

```


FOR THE GENERAL POPULATION, ONLY CREATE __CODESPAN_0_, WRITE

```sh
permit :wheel
```

_OTHER ORGANISER。

# sudo #

# install sudo #

- install with pkg:

```sh
# pkg install sudo
```

- Or install with Ports:


```sh
# cd /usr/ports/security/sudo/ 
# make install clean
```

# sudo without password

NEW TWO FILES UNDER __CODESPAN_0_, __ CODESPAN_1 (USER WITHOUT PASSWORD) AND _CODESPAN_2_:

- DOCUMENT ___CODESPAN_0_ READS AS FOLLOWS:

```sh
%admin ALL=(ALL) ALL
```

- DOCUMENT ___CODESPAN_0_ READS AS FOLLOWS:

ADD ONE MORE LINE AND DO NOT NEED TO ENTER A PASSWORD USING __CODESPAN_0:

```sh
%wheel ALL=(ALL) NOPASSWD:ALL
```

# # troubleshooting and unfinished business

- CODESPAN_0_

a sentence should be added to solve this problem in sudoers:


EDIT __CODESPAN_0, FIND __CODESPAN_1_ IN THIS LINE, USUALLY IN LINE 94. ADD THE FOLLOWING SENTENCE AFTER THE LINE:

```sh
你的普通用户名 ALL=(ALL:ALL) ALL
```

Then save the exit。
