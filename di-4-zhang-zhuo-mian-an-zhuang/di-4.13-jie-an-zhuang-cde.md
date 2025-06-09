# Section 4.13 CODE

The CDE is the abbreviation for Common Desktop Environment. It is a long-standing desktop environment that is often used for the Unix commercial release.


# Install software

- Install with pkg:

```sh '
# Pkg install xorg cde wqy-fonts xdg-user-dirs
````

- Or install with Ports:

```sh '
#cd/usr/ports/x11/xorg/ & make install clean
#cd/usr/ports/x11/cde/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````


- Explain:

Name of package Description of role
|: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
`xorg 'x Windows
`cde ' | CDE provides a traditional desktop environment
`wqy-fonts '
`xdg-user-dirs ' manages user directories such as “desktop”, “download” etc. Zenium



# See post-installation information

```sh '
root@ykla:/home/ykla
cde-2.5.2_4:
On install:
The Common Desktop Envirronment is an X Windows desktop envirronment
That was commonly used on commercial UNIX varians such as Sun Solaris,
Developed between 1993 and 1999, it has now been
If you don't mind, then you'll have to wait for the Open Group.
# CDE (General Desktop Environment) is an early X Windows desktop environment that was used extensively for commercial UNIX systems such as Solaris, HP-UX and AIX.
# Development time approximately 1993-1999, now published by The Open Group as an open source protocol.

Common Desktop Environmental concerns the Subprocess Control Service,
Dtcms, and the inward subserve to full play.
# To run the CDE in its entirety, the sub-process control service (dtspc), the calendar management service (dtcms) and the inetd Superserver are enabled.

First, add the following line to/etc/inetd.conf:

dtspc stread tcp nowait root/usr/local/dt/bin/dtspcd/usr/local/dt/bin/dtspcd
# First step, add dtspcd service line in /etc/inetd.conf.

Second, add the following line to/etc/services:

Dtspc 6112/tcp
# Step two, register dtspc service port in /etc/services.

# Sysrc rpcbind_enable
# Sysrc dtcms #
# Sysrc inetd_enable
# Service rpcbind start & service dtcms start & service interd
# Enable and start the rpcbind, dtcms and inetd services, which are the components on which CDE relies.

Really, make sure to add/usr/local/dt/bin to your path.
# Finally, add /usr/local/dt/bin to your PATH environment variable.

To start the Common Desktop Environment:
%env LANG=Cstartx /usr/local/dt/bin/Xsession
# Use the above command to start the CDE desktop environment and set the environment variable LANG=C to avoid localization problems.

Technically, if you want to use the Login Manager as well,
/usr/local/etc/X11/Xwrapper.config and add this line:

All right, allowed_users=anybody
# If you want to enable the Graphic Login Manager (Login Manager), create Xwrapper.config and add a listed_user=anybody.

To start the Common Development Login Manager:

_usr/local/dt/bin/dtlogin-daemon

# Starts the CDE login manager (dæmon mode) with the dtlogin-daemon command.
````

# Configure services and files


- Configure services

```sh '
# With service rpcbind #
♪ service dtcms available
♪ service ined enough
# For service dlogin 'enable
````

- Configure users for login desktops

```sh '
# Echo "allowed_user=anybody" > /usr/local/etc/X11/Xwrapper.config
````

- For 'startx'

```sh '
#In-s /usr/local/dt/bin/Xsession~/.xinitrc
````

- Add the following to `/etc/inetd.conf ':

```sh '
dtspc stread tcp nowait root/usr/local/dt/bin/dtspcd/usr/local/dt/bin/dtspcd
````

- Add the following to `/etc/services ':

```sh '
dtspc 6112/tcp
````


Chinese Configuration

Edit `/etc/login.conf ' : find `default:\, amend `:lang=C.UTF-8 ' to `:lang=zh_CN.UTF-8 ' .

Refresh database:

```sh '
#cap_mkdb/etc/login.conf
````

# Desktop appreciation


[dtlogin]

...! [FreeBSD installation .. ..gitbook/assets/cde4.png]

Every time you start, it's stuck in here for a few minutes.

...! [FreeBSD installation CED] (..gitbook/assets/cde1.png)

. [Terminal] (.. .getbook/assets/cde3.png)

# Fragmentation and unfinished business

- Can't speak Chinese.

Pending


# References

- [cde Common Desktop Environment] (https://www.freshports.org/x11/cde)
- [Setting up Common Desktop Environnement for mobile use] (https://forums.freebsd.org/threads/setting-up-compon-desktop-environment-for-modern-use69475/), with detailed configuration available here
- [CDE - Common Development Wiki] (https://sourceforge.net/p/cdesktopenv/wiki/FreeBSDBuild/), CDE project official WiKi
