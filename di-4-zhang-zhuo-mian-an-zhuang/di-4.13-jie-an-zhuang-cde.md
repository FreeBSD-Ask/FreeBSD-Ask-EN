# SECTION 4.13 CODE

The CDE is the abbreviation for Common Desktop Environment. It is a long-standing desktop environment that is often used for the Unix commercial release。


# Install software

- install with pkg:

```sh
# pkg install xorg cde wqy-fonts xdg-user-dirs
```

- Or install with Ports:

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/cde/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```


- Explain:

| Package Name | Description of role |
|:------------------|:--------------------------------------------------------------------------|
| `xorg ' | X Windows |
| `cde ' | CODE PROVIDES A TRADITIONAL DESKTOP ENVIRONMENT |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manages user directories such as " Desktop " , " Download " , etc。 |



# See post-installation information

```sh
root@ykla:/home/ykla # pkg info -D cde
cde-2.5.2_4:
On install:
CDE - The Common Desktop Environment is an X Windows desktop environment
that was commonly used on commercial UNIX variants such as Sun Solaris,
HP-UX, and IBM AIX. Developed between 1993 and 1999, it has now been
released under an Open source license by The Open Group.
# CDE（通用桌面环境）是早期 X Windows 的桌面环境，曾广泛用于商用 UNIX 系统如 Solaris、HP-UX 和 AIX。
# 开发时间大致为 1993–1999 年，现由 The Open Group 以开源协议发布。

Common Desktop Environmental concerns the Subprocess Control Service,
dtcms, and the inward subserve to full play.
# To run the CDE in its entirety, the sub-process control service (dtspc), the calendar management service (dtcms) and the inetd Superserver are enabled。

First, add the following line to/etc/inetd.conf:

dtspstreampnowaitroot /usr/local/dt/bin/dtspcd/usr/local/dt/bin/dtt/dtspcd
# first step, add dtspcd service line in /etc/inetd.conf。

Second, add the following line to/etc/services:

dtspc612/tcp
# step two, register dtspc service port in /etc/services。

# Sysrc rpcbind_enable
# Sysrc dtcms #
# Sysrc inetd_enable
# service rpcbind start & service dtcms start & service interd
# Enable and start the rpcbind, dtcms and inetd services, which are the components on which CDE relies。

Really, make sure to add/usr/local/dt/bin to your path.
# Finally, add /usr/local/dt/bin to your PATH environment variable。

To start the Common Desktop Environment:
%env LANG=Cstartx /usr/local/dt/bin/Xsession
# USE THE ABOVE COMMAND TO START THE CDE DESKTOP ENVIRONMENT AND SET THE ENVIRONMENT VARIABLE LANG=C TO AVOID LOCALIZATION PROBLEMS。

Technically, if you want to use the Login Manager as well
/usr/local/etc/X11/Xwrapper.config and add this line:

all right, allowed_users=anybody
# If you want to enable the Graphic Login Manager (Login Manager), create Xwrapper.config and add a listed_user=anybody。

To start the Common Development Login Manager:

_usr/local/dt/bin/dtlogin-daemon

# Starts the CDE login manager (dæmon mode) with the dtlogin-daemon command。
````

# Configure services and files


- Configure services

```sh
# service rpcbind enable
# service dtcms enable
# service inetd enable
# service dtlogin enable
```

- Configure users for login desktops

```sh
# echo "allowed_users=anybody" > /usr/local/etc/X11/Xwrapper.config
```

- FOR CODESPAN

```sh
# ln -s /usr/local/dt/bin/Xsession ~/.xinitrc
```

- ADD THE FOLLOWING TO __CODESPAN_0:

```sh
dtspc	stream	tcp	nowait	root	 /usr/local/dt/bin/dtspcd	/usr/local/dt/bin/dtspcd
```

- ADD THE FOLLOWING TO __CODESPAN_0:

```sh
dtspc		6112/tcp
```


Chinese Configuration

EDIT __CODESPAN_0: FIND __CODESPAN_1_, AND MODIFY __CODESPAN_2_ TO __ ___ CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```

# Desktop appreciation


[dtlogin]

[FreeBSD establishment] (..gitbook/assets/cde4.png)

Every time you start, it's stuck in here for a few minutes。

[FreeBSD establishment] (..gitbook/assets/cde1.png)

[Terminal] (..gitbook/assets/cde3.png)

# Fragmentation and unfinished business

- Can't speak Chinese

Pending


# References

- [i'm sorry, Mr. Common Desktop Environment]
- [Setting up Common Desktop Envirron for motor use] (https://forums.freebsd.org/threads/setting-up-common-desktop-environment-for-modern-use69475/), with detailed configurations available here
- [CDE-Common Desktop Environmental Wiki] (https://sourceforge.net/p/cdesktopenv/wiki/FreeBSDBuild/), CDE Project Official WiKi
