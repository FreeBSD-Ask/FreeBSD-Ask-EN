Section 4.20 Remote desktop

# x11vnc

x11vnc will mirror the screen directly like remote software todesk, in short, all your operations will be synchronized to the monitor, which, in turn, you can see on VNC。

---|---

x11vnc cannot be used without a monitor。

# # install x11vnc

- install with pkg:

```
# pkg install x11vnc
```

- Or install with Ports:

```sh
# cd /usr/ports/net/x11vnc/
# make install clean
```

# Create Password #

```sh
$ x11vnc -storepasswd
Enter VNC password: 
Verify password:    
Write password to /root/.vnc/passwd?  [y]/n y #此处键入 y 回车
Password written to: /root/.vnc/passwd
```

# # START SERVER (KDE 6 SDDM)

```sh
$ x11vnc -display :0 -rfbauth ~/.vnc/passwd -auth $(find /var/run/sddm/ -type f)
```

>** Warning**
>
> SDDM Bottom Left __CODESPAN_0 __ cannot get in! Because x11vnc does not support Wayland。


- LightDM

```sh
$ x11vnc -display :0 -rfbauth ~/.vnc/passwd -auth /var/run/lightdm/root/\:0
```

- GDM

```sh
$ x11vnc -display :0 -rfbauth ~/.vnc/passwd -auth /var/lib/gdm/:0.Xauth #或 /run/user/120/gdm/Xauthority，取决于你的 gdm 版本，自己 ls 看一下
```

[SDDM X11VNC] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

References

- [we're going to have to get X11 pictures] (https://man.freebsd.org/cgi/man.cgi?query=x11vnc&sektion=&manpath=freebsd-release-ports)
- [X11vnc] (https://wiki.archlinux.org/title/X11vnc)

# TigerVNC

Enable VNC services (currently Ports is the only one left)

# Install TigerVNC Server

```sh
# pkg install tigervnc-server
```

Or:

```sh
# cd /usr/ports/net/tigervnc-server/ 
# make install clean
```

# Make some settings #

SETS THE ACCESS PASSWORD TO EXECUTE COMMAND __CODESPAN_0_ AT THE TERMINAL。

CREATE __CODESPAN_0_FILE:


```sh
$ mkdir -p ~/.vnc/
$ ee ~/.vnc/xstartup
```

It reads as follows:

```sh
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
[ -x /etc/X11/xinit/xinitrc ] && exec /etc/X11/xinit/xinitrc
[ -f /etc/X11/xinit/xinitrc ] && exec sh /etc/X11/xinit/xinitrc
xsetroot -solid grey
#exec startplasma-x11 & 
#exec mate-session &
#exec xfce4-session &
#exec gnome-session & 
```

WHICH DESKTOP DO YOU USE TO DELETE THE NOTE IN FRONT OF THAT DESKTOP。

>** Warning**
>
> PLEASE NOTE THE RETENTION OF __CODESPAN_0_**。

The authority to execute an order after saving is granted。

```sh
$ chmod 755 ~/.vnc/xstartup
```

- We'll proceed to the terminal
- What

```sh
$ vncserver
```

or

```sh
$ vncserver :1

You will apply a password to access your files.

Password:
Verify:
Would you like to enter a view-only password (y/n)
A view-only password is not used

New 'ykla: 1 (ykla)' desktop is ykla:

Creating default config/ home/ykla/.vnc/config
Starting applications delivered in/home/ykla/.vnc/xstartup
Log file is /home/ykla/.vnc/ykla:1.log
````

AMONG THEM, "__CODESPAN_0" MEANS __CODESPAN_1 __, I.E., THE SPECIFIED COMMUNICATIONS PORT ON THE DESKTOP IS __CODESPAN_2 __ AND THE PORT FOR THE VNC SERVICE IS __CODESPAN_3 __. DESKTOP DISPLAYS THE COMMUNICATIONS PORT STARTING FROM 0, BUT THE PORT IS ALREADY OCCUPIED BY THE CURRENT DESKTOP (EXCEPT FOR MIRROR VNC), SO THE VNC SERVICE DEFAULT PORT IS 5900, BUT THE ACTUAL IMPLEMENTATION MUST START WITH __CODESPAN_4_. THEREFORE, IF YOU WANT A LINK, YOU MUST SPECIFY THE PORT AS __CODESPAN_5_。

> Test:
>
> ```sh '
>$vncserver:0
>
>
>Warning: ykla:0 is taken because of /tmp/.X11-unix/X0
>Remove this file if there is no X server ykla:0
>A VNC server is already running as:0
> ````

If the service is launched without a communication port, the system is automatically assigned according to usage。

Can view process:

```
$ ps
 PID TT  STAT    TIME COMMAND
……省略无用内容……
4769  0  S    0:02.72 /usr/local/bin/Xvnc :1 -auth /home/ykla/.Xauthority -desktop ykla:1 (ykla)
```

CLOSE THE SERVICE BY COMMAND __CODESPAN_0, HERE YOU MUST SPECIFY THE PORT OF COMMUNICATION。

- if the firewall is activated, for example ipfw, enter the command at the terminal:

```sh
# ipfw add allow tcp from any to me 5900-5910 in keep-state
```

THE FIRST LINE COMMAND IS TO RELEASE PORT 5900-5910, I.E. DISPLAY 0-10。

References

- (https://forums.freebsd.org/threads/xfce4-is-not-displayed-only-wen-i-conect-vncviewer-in-linux-to-tightvnc-server-on-freebsd.85709)

# XRDP (FreeBSD is the accused)

# # Install XRDP (kde6 based)

```sh
# pkg install xorg kde xrdp wqy-fonts xdg-user-dirs pulseaudio-module-xrdp
```

Or:

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/kde/ && make install clean
# cd /usr/ports/net/xrdp/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
# cd /usr/ports/audio/pulseaudio-module-xrdp && make install clean
```

View profile:

```sh
root@ykla:/usr/ports/net/xrdp # pkg info -D xrdp
xrdp-0.10.2_2,1:
On install:
xrdp has been installed.
# xrdp 已成功安装。

There is an rc.d Script, so the service can be made by adding this line
in /etc/rc.conf:

"YES."
"YES"
# provides rc.d start-up scripts that can be enabled by adding the above two lines to /etc/rc.conf。
# first start xrdp master service, second start session manager (sesman)。

Do not forget to dig the confession files in "/usr/local/etc/xrdp"
and the "/usr/local/etc/xrdp/startwm.sh".
# don't forget to edit the profile under /usr/local/etc/xrdp
# and modify /usr/local/etc/xrdp/startwm.sh to set the desktop environment that starts after login。

To an able Audio direction, install the following reports/packages to meet
your environment.
# To enable audio redirection (telephone sound transfer), install the following packages according to your system environment:

- audio/pipwire-module-xrdp
- audio/pulseudio-module-xrdp
# the above-mentioned module to support xrdp audio can be installed according to the audio system you use。
````

Configure

```sh
# service xrdp enable 
# service xrdp-sesman enable 
# service dbus enable
```

EDIT __CODESPAN_0_:

FIND __CODESPAN_0_, AMEND AS FOLLOWS:

```sh
#### start desktop environment
# exec gnome-session # Gnome 须删除此处开头的 #
# exec mate-session # mate 须删除此处开头的 #
# exec start-lumina-desktop # lumina 须删除此处开头的 #
# exec ck-launch-session startplasma-x11 # KDE6 须删除此处开头的 #
# exec startxfce4                        # xfce 须删除此处开头的 #
# exec xterm                             # xterm 须删除此处开头的 #
```

Then restart the system, then。

## # middle culture (user uses default sh)


```sh
# ee /usr/local/etc/xrdp/startwm.sh
```

```sh
#### set environment variables here if you want
export LANG=zh_CN.UTF-8
```

# # troubleshooting and unfinished business

- XRDP, NO SOUND

Try the fire fox browser

# Remote access to FreeBSD via Windows by TigerVNC

Download TigerVNC viewer:

download address: <https://sourceforge.net/projects/tigervnc/files/stable/>

View VNC port for FreeBSD:

```sh
root@ykla:/usr/ports/deskutils/anydesk # sockstat -4l
USER     COMMAND    PID   FD  PROTO  LOCAL ADDRESS         FOREIGN ADDRESS      
root     Xvnc        2585 4   tcp4   127.0.0.1:5910        *:*  #VNC 占用
root     xrdp        2580 13  tcp46  *:3389                *:*  #XRDP 占用
root     Xvnc        2016 5   tcp4   *:5901                *:*  #VNC 占用
root     sshd        1164 4   tcp4   *:22                  *:*  #SSH 占用
ntpd     ntpd        1127 21  udp4   *:123                 *:* 
ntpd     ntpd        1127 24  udp4   127.0.0.1:123         *:*
ntpd     ntpd        1127 26  udp4   192.168.31.187:123    *:*
root     syslogd     1021 7   udp4   *:514                 *:*
```

> ** troubleshooting and unfinished business: unable to connect due to active refusal of the target server**
>
> non-film vnc must specify the port when connecting, otherwise connect by default port 5900, but you are not a mirror screen (which you use is not x11vnc) and must not be connected。
>
>! [SDDM VNC] (. .gitbook/assets/vnc1.png)
>
> Example:
>
> ```sh '
>192.168.31.187:5901
> ````

[SDDM VNC](. . .gitbook/assets/vnc2.png)

# # troubleshooting and unfinished business

- Through VNC remote FreeBSD no sound, no idea how to configure。

# Remote access to FreeBSD via Windows' own desktop connection (RDP)

[xrdp FreeBSD] (..gitbook/assets/xrdp1.png)

WHEN YOU ENTER THE DEVICE FOR THE FIRST TIME, YOU WILL HAVE A SECURITY ALERT, ENTER __CODESPAN_0, AND YOU WILL POP UP A REMOTE DESKTOP WINDOW WHEN YOU RETURN TO THE CAR。

[xrdp FreeBSD] (..gitbook/assets/xrdp2.png)

[xrdp FreeBSD] (..gitbook/assets/xrdp3.png)

[xrdp FreeBSD] (..gitbook/assets/xrdp4.png)

[xrdp FreeBSD] (..gitbook/assets/xrdp5.png)

# # troubleshooting and unfinished business

-Windows ' remote desktop window is blurred if it is not displayed at the top left corner or full screen

Please ** Cancel** Check out "Intelligent Resize"。

![...gitbook/assets/xrdp6.png]

# Use Android remote access to FreeBSD via XRDP

First, you need to download the required software:

RDP software developed officially by Microsoft: Remote Desktop

- [Remote Desktop] (https://play.google.com/store/apps/details?id=com.microsoft.rdc.androidx&hl=zh_CN)

The software is easy to operate。

PLEASE NOTE THAT THE TOP LEFT PIPING SHOULD BE REPLACED WITH PIPING. THE DEFAULT MOUSE OPERATION IS INCONVENIENT: OR YOU CAN CHOOSE A CELL PHONE ODG AS A MOUSE AND KEYBOARD。

[Remote Desktop FreeBSD] (..gitbook/assets/wrdp3.png)


A link diagram (the Chromium is being compiled and will be occupied very high):

[Remote Desktop FreeBSD] (..gitbook/assets/wrdp4.png)

# Remote access to Windows by XDRP via FreeBSD

##freerdp3 (new stabilizer, NLA)

install with pkg:

```
# pkg ins freerdp3
```

Or with Ports:

```sh
# cd /usr/ports/net/freerdp3/ 
# make install clean
```

Use FreeBSD to link remotely to Windows 11 24H2:

```
ykla@ykla:~ $ xfreerdp3 /u:ykla /p:z  /v:192.168.31.213

.
[1924: dca12700] [ERROR] [com.freerdp.crypto] - [tls_print_new_certificate_warn]: Host key delivery.
Certificate details for 192,168,31213:3389 (RDP-Server):
Common Name: DESKTOP-U72I6SS
Subject: CN = DESKTOP-U72I6SS
Issuer: CN = DESKTOP-U72I6SS
Valid from: Mar 4 12:39:28 2025 GMT
Valid to: Sep 3 12:39:28 2025 GMT
Thumbprint: 36:b9:be:66:ab:2b:54:32:28:b:46:b6:98:68:68:d:68:d:6f:20:a5:d1:58:c:09:de:cc:3d:30:e1:06:f:4:62:54:de
The above X.509
i'm sorry, but I'm sorry, but I'm sorry, but I'm sorry.
Please look at the OpenSSL documentation on how to add a price CA to the store.
Do you trust the above link? (Y/T/N) y # Enter y to confirm the link by pressing the return key

```

__CODESPAN_0:

- CODESPAN_0, BE AWARE THAT THERE'S ONE IN FRONT。
-_CODESPAN_0,_CODESPAN_1_name is Username username. It's my Windows login
- __CODESPAN_0_, the Password password. It's a login password for Windows user __CODESPAN_2_
- __CODESPAN_0_, the Server server。

[freerdp] (..gitbook/assets/freerdp3.png)

References

- [FreeRDP User Manual] (https://github.com/wakecoding/FreeRDP-Manuals/blob/master/User/FreeRDP-User-Manual.markdown), with command descriptions and some examples of usage


##freerdp2 (old stabilizer, NLA)

install with pkg:

```sh
# pkg ins freerdp
```

Or with Ports:

```sh
# cd /usr/ports/net/freerdp/ 
# make install clean
```

Use FreeBSD remote link to Windows 11 24H2:

```sh
ykla@ykla:~ $ xfreerdp 192.168.31.213 # 注意是 xfreerdp。
[20:35:20:041] [1105:7c412000] [WARN][com.freerdp.client.common.cmdline] - ----------------------------------------
……省略一部分……
Certificate details for 192.168.31.213:3389 (RDP-Server):
        Common Name: DESKTOP-U72I6SS
        Subject:     CN = DESKTOP-U72I6SS
        Issuer:      CN = DESKTOP-U72I6SS
        Thumbprint:  36:b9:be:66:ab:2b:54:32:28:46:b6:98:68:8d:6f:20:a5:d1:58:8c:09:de:cc:3d:30:e1:06:6f:4f:62:54:de
The above X.509 certificate could not be verified, possibly because you do not have
the CA certificate in your certificate store, or the certificate has expired.
Please look at the OpenSSL documentation on how to add a private CA to the store.
Do you trust the above certificate? (Y/T/N) y # 输入 y 回车
Domain:   # 留空
Password: # 输入密码，密码不会显示出来 ***。
……省略一部分……
```


[freerdp]

# # failure and unfinished business #

- But I'm connected without a username

I don't know. Is it because my FreeBSD username is the same as Windows

# rdektop (NLA not supported)

__CODESPAN_0_is a graphical frontend for rdesktop, but my keyboard settings are stuck when I open them。

---|---

install rdesktop with pkg:

```sh
# pkg install rdesktop
```

Or with Ports:

```sh
# cd /usr/ports/net/rdesktop/
# make install clean
```

rdektop without frontend GUI so to enter command at terminal:

```sh
# rdesktop ip:端口 # 比如 192.168.31.155:3389
```

`:端口` is not required if Windows configuration is not specifically changed。

For the Windows 11 24H2 I tested, it's a mistake:

```sh
ykla@ykla:~ $ rdesktop 192.168.31.213
Failed to connect, CredSSP required by server (check if server has disabled old TLS versions, if yes use -V option).
```

According to [CredSS does not work] (https://github.com/rdektop/rdektop/issues/71), this is an old problem。

The solution affecting security is to disable network-level authentication (NLA) and operate on Windows to connect remotely:

```powershell
PS C:\Users\ykla> reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 0 /f
操作成功完成。
PS C:\Users\ykla> gpupdate /force
正在更新策略...

Computer strategy update successfully completed。
User strategy update successfully completed。
````

Retest Link:

```sh
ykla@ykla:~ $ rdesktop 192.168.31.213

The service uses and involves security, which can not be trusted for
(a) the following environment;

Certificate issuer is not trusted by this system.

     Issuer: CN=DESKTOP-U72I6SS


Review the follow-up information before you trust it to be Amended as an exception.
If you do not trust the credit given the transaction atom will be aborted:

Subject: CN=DESKTOP-U72I6SS
Issuer: CN=DESKTOP-U72I6SS
Valid From: Tue Mar 4 20:39:28 2025
To: Wed Sep 3:39:28 2025

Certificate flies:

       sha1: 599c0e8bbc57c5ee8de8993d5241fb0f0d70e98d
     sha256: 36b9be66ab2b54322846b698688d6f20a5d1588c09decc3d30e1066f4f6254de


# Enter yes, press Return
````

[i don't know... .gitbook/assets/rdektop1.png]

[i don't know... .getbook/assets/rdektop2.png]

# # failure and unfinished business #

- No sound on the video

Pending

References

- The method of opening and closing NLA (https://learn.microsoft.com/zh-cn/troubleshoot/azure/virtual-machines/windows/cannot-content-rdp-azure-vm) After testing off, rdesktop did not match again。


# AnyDesk

Use AnyDesk for remote access, FreeBSD only supports x86 structures:

As a result of copyright issues (private software is banned from distribution by default without permission), users must compile themselves using Ports:

```sh
# cd /usr/ports/deskutils/anydesk/
# make install clean
```

NO PARAMETERS __CODESPAN_0_ MAY BE USED BECAUSE A LICENCE AGREEMENT IS REQUIRED TO USE:

[no, nodek]

View AnyDesk installed to describe:

```sh
root@ykla:/ # pkg info -D anydesk
anydesk-6.1.1_2:
On install:
1. Minimum OS version.
======================
Anydesk is a binary package for FreeBSD.
Minimal recommended is 1 GiB system memory
installed but performence will be reduced.
For good performance is recommended and 2 GiB
system memory.
# Anydesk 是适用于 FreeBSD 的二进制软件包。
# 最低推荐内存为 1 GiB，但这将导致性能下降。
# 若要获得良好性能，建议至少配备 2 GiB 系统内存。

2. Important settings
== sync, corrected by elderman ==
Since Version 2.9.1 the following prerequisites have to be met:
# From Version 2.9.1, the following prerequisites must be met:

You need a Mounted/Proc Directory
# need to mount / proc directories, which can be mounted manually or written to /etc/fstab for automatic mount:

fstab: proc / proc procfs rw 0
# add this line to /etc/fstab to enable procfs。

manually: #mount-t procfs proc / proc
# or manually execute this command to mount the proc file system。
````

THE HINT REQUIRES __CODESPAN_0, AND THE EXECUTION PROGRAM DOES NOT REACT IF IT IS NOT TESTED。

```sh
# mount -t procfs proc /proc # 临时用一下。持久化可以参照上面的说明做
```

root user cannot run AnyDesk. _Other Organiser

```
$ ykla@ykla:~ $ anydesk

(<unknown>:18311) Gtk-WarnING**: 21:07:13.54: Unable to find the theme engine “adwaita” in the modular path

.
````

This interface pops up after the order:

![..gitbook/assets/anydesk2.png]

Note that the connected party “accepts” to continue the link。

# Windows via AnyDesk Remote FreeBSD

[Windows via AnyDesk FreeBSD] (..gitbook/assets/anydesk3.png)

FreeBSD via AnyDesk Remote Windows

[Windows via AnyDesk FreeBSD] (..gitbook/assets/anydesk4.png)

# # troubleshooting and unfinished business

- FreeBSD via AnyDesk Remote Windows does not seem to be able to move the mouse in Windows。

Pending。

# RustDesk Relay Server

Note**
>
> THIS IS A RELAY ID SERVER THAT CANNOT BE REMOTELY CONTROLLED PER SE。

In other words, you can't control FreeBSD with RustDesk。

Installation:

```sh
# pkg install rustdesk-server
```

Or:

```sh
# cd /usr/ports/net/rustdesk-server/ 
# make install clean
```

Configure:

- start hbbr:

```sh
root@ykla:~ # /usr/local/bin/hbbs
[2024-08-10 23:02:13.782550 +08:00] INFO [src/common.rs:122] Private key comes from id_ed25519
[2024-08-10 23:02:13.782587 +08:00] INFO [src/rendezvous_server.rs:1191] Key: mgRwOWJy9Vnz3LqQYjtNHwZQYg73uhdj9iCTMmIyoP4=  #此处是 Key
[2024-08-10 23:02:13.782655 +08:00] INFO [src/peer.rs:84] DB_URL=./db_v2.sqlite3
[2024-08-10 23:02:13.786349 +08:00] INFO [src/rendezvous_server.rs:99] serial=0
[2024-08-10 23:02:13.786381 +08:00] INFO [src/common.rs:46] rendezvous-servers=[]
[2024-08-10 23:02:13.786388 +08:00] INFO [src/rendezvous_server.rs:101] Listening on tcp/udp :21116
[2024-08-10 23:02:13.786391 +08:00] INFO [src/rendezvous_server.rs:102] Listening on tcp :21115, extra port for NAT test
[2024-08-10 23:02:13.786395 +08:00] INFO [src/rendezvous_server.rs:103] Listening on websocket :21118
[2024-08-10 23:02:13.786430 +08:00] INFO [libs/hbb_common/src/udp.rs:35] Receive buf size of udp [::]:21116: Ok(42080)
[2024-08-10 23:02:13.786581 +08:00] INFO [src/rendezvous_server.rs:138] mask: None
[2024-08-10 23:02:13.786594 +08:00] INFO [src/rendezvous_server.rs:139] local-ip: ""
[2024-08-10 23:02:13.786603 +08:00] INFO [src/common.rs:46] relay-servers=[]
[2024-08-10 23:02:13.786703 +08:00] INFO [src/rendezvous_server.rs:153] ALWAYS_USE_RELAY=N
[2024-08-10 23:02:13.786734 +08:00] INFO [src/rendezvous_server.rs:185] Start
[2024-08-10 23:02:13.786793 +08:00] INFO [libs/hbb_common/src/udp.rs:35] Receive buf size of udp [::]:0: Ok(42080)
[2024-08-10 23:09:11.043094 +08:00] INFO [src/peer.rs:102] update_pk 1101115918 [::ffff:192.168.31.90]:37057 b"\x06\xef\x81\xb4\xe2\x9e\xff(\xcb\xd7\x985S\x95)~1O\xe2\xfcu\xeeE\x91\xf1\xf2\xa1\xbe\rk\xcd\xc1" b"\x06\xef\x81\xb4\xe2\x9e\xff(\xcb\xd7\x985S\x95)~1O\xe2\xfcu\xeeE\x91\xf1\xf2\xa1\xbe\rk\xcd\xc1" #代表设备接入
^C[2024-08-10 23:10:06.746255 +08:00] INFO [src/common.rs:176] signal interrupt
```

- start hbbs:

```sh
root@ykla:~ # /usr/local/bin/hbbr
[2024-08-10 22:58:26.593397 +08:00] INFO [src/relay_server.rs:61] #blacklist(blacklist.txt): 0
[2024-08-10 22:58:26.593439 +08:00] INFO [src/relay_server.rs:76] #blocklist(blocklist.txt): 0
[2024-08-10 22:58:26.593445 +08:00] INFO [src/relay_server.rs:82] Listening on tcp :21117
[2024-08-10 22:58:26.593449 +08:00] INFO [src/relay_server.rs:84] Listening on websocket :21119
[2024-08-10 22:58:26.593452 +08:00] INFO [src/relay_server.rs:87] Start
[2024-08-10 22:58:26.593546 +08:00] INFO [src/relay_server.rs:105] DOWNGRADE_THRESHOLD: 0.66
[2024-08-10 22:58:26.593556 +08:00] INFO [src/relay_server.rs:115] DOWNGRADE_START_CHECK: 1800s
[2024-08-10 22:58:26.593559 +08:00] INFO [src/relay_server.rs:125] LIMIT_SPEED: 4Mb/s
[2024-08-10 22:58:26.593564 +08:00] INFO [src/relay_server.rs:136] TOTAL_BANDWIDTH: 1024Mb/s
[2024-08-10 22:58:26.593567 +08:00] INFO [src/relay_server.rs:146] SINGLE_BANDWIDTH: 16Mb/s
^C[2024-08-10 23:10:04.393365 +08:00] INFO [src/common.rs:176] signal interrupt
```

Opens the rustdesk client on other devices with the same "ID server (FreeBSD IP address or domain name)" and "Key" on both sides. The others are empty and can be connected by entering the ID displayed at the control end。

References

- [rustdesk-server Self held RustDesk servicer] (https://www.freshports.org/net/rustdesk-server/)
- [Remote contorl software RustDesk Self-built Server Full Platform Development and Use of Tutor] (https://www.cnblogs.com/safe-rabbit/p/18020812)

