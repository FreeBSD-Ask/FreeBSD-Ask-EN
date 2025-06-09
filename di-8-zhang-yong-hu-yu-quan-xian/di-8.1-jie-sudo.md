# Section 8.1 sudo and doas

Doas

In fact, for most people, only the `sudo su ' line is required, and the rest is superfluous.

OpenBSD has developed its own [doas] (https://man.openbsd.org/doas) because of the complexity of the sudo software configuration, poor code quality and too many loopholes. Naturally, FreeBSD can also be used.

# Install doas #

- Install with pkg:

```sh '
# Pkg install doas
````

- Or install with Ports:

```sh '
# cd/usr/ports/security/doas/
# Make install clean
````

# # See doas installed information

```sh '
root@ykla: #pkginfo-Ddoas
Doas-63p12:
On install:
To use doas,

/usr/local/etc/doas.conf

I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry.
/usr/local/etc/doas.conf.sample as an example.
# To use doas, a profile must be created /usr/local/etc/doas.conf.
# See on-line documents for doas.conf(5), or see the /usr/local/etc/doas.conf.sample profile.

In order to be able to run most desktop (GUI) applications, the user
If keepenv is not treated then
Keeps, like the user's $HOME can, will be reset and cause the GUI
I'm sorry, application to crash.
# Note: If you need to run a GUI (GUI) program, you must add a keyword to the configuration.
# Otherwise environment variables like $HOME will be emptied, leading to the collapse of the GUI program.

Users who only need to run line applications can usually get away
I don't know.
# If only to run the command line program, usually no keepenv.

When in doubt, try to understand us as it is less secure to have
I'm sorry, but I'm sorry.
# If it's not clear whether it's necessary, it's recommended to avoid the use of keepingenv, as it could reduce the system's security,
# The environment variable of the original user is passed to the target user with permission.

On upward from doas<6:1
With the 6.1 transfer of most environmental assets (e.g. USER),
From the original user to the target user has changed.
# Environmental variables (e.g. USER, HOME, PATH) have changed from doas version 6.1.

Please return to doas.conf(5) for further details.

# See doas.conf(5) on-line documentation for more details.
````

# Configure doas

As is known above, the sample example is in `/usr/local/etc/doas.conf.sample ' .

And we need to place the configuration document in `/usr/local/etc/doas.conf ' , which by default does not exist and we need to create it ourselves.

- `/usr/local/etc/doas.conf.sample ' , which is very simple to understand compared to sudo:

Let's just say this:

````
Sample file for doas
Please see doas.
# Up a doas.

♪ Permit members of the world group to perform actions as root. ♪
permit :wheel # Allow the wheel group members doas

# Same without having to enter the password
_Other Organiser

♪ Permit user like to run people as a root user. ♪
# Allow the user alice doas

♪ Permit user Bob to run the programs as root, makin' ♪
# Environables. #
Personal keepenv Bob as root # Allows users to Bob doas and inherits the environment variable of the user Bob, which is required by the GUI but which reduces security (see see post-installation information)

? Permit usr kind to run only the pkg pack as root
# To perform package updates and upwards. #
%1 content as root cmd pkg arms update %1
# Only pkg upgrad

♪ Allow david to run id company as root without reading it ♪
# Allow David to run `id ' commands as root and not log logs

````


`/usr/local/etc/doas.conf '

```sh '
This post is part of our special coverage Syria Protests 2011.
````

It meets daily needs (your users must join the `wheel ' group).

# Sudo #

# Install sudo #

- Install with pkg:

```sh '
♪ Pkg install sudo
````

- Or install with Ports:


```sh '
#cd/usr/ports/security/sudo/
# Make install clean
````

# sudo without password

New files `username ' (user needing password-free) and `wheel ' :

- The document `username ' reads as follows:

```sh '
%admin Alll=(All)All
````

- The document `wheel ' reads as follows:

Add a line to the following:

```sh '
%whoel alll=(ALL)NOPSWD:All
````

# # troubleshooting and unfinished business

- ♪ Is not in the Sudoers File.

A sentence should be added to solve this problem in sudoers:


Edit `/usr/local/etc/sudoers ' , find `root ALL=(ALL:ALL) All ' , usually in line 94. Add the following sentence after the line:

```sh '
Your normal user name All = (All:All) All
````

Then save the exit.
。