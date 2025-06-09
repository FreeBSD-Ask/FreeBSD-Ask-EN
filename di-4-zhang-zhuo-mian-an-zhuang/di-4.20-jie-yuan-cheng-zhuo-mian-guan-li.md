Section 4.20 Remote desktop

# x11vnc

x11vnc will mirror the screen directly like remote software todesk, in short, all your operations will be synchronized to the monitor, which, in turn, you can see on VNC.

I don't...

x11vnc cannot be used without a monitor.

# # Install x11vnc

- Install with pkg:

````
# pkg install x11vnc
````

- Or install with Ports:

```sh '
#cd/usr/ports/net/x11vnc/
# Make install clean
````

# Create Password #

```sh '
$ 11vnc-storepasswd
Enter VNC password:
Verify password:
Write password to / root/.vnc/passwd? [y]/n y # type y
Passwordwritten to: / root/.vnc/passwd
````

# # Start Server (KDE 6 SDDM)

```sh '
$x11vnc-display:0-rfbauth~/.vnc/passwd-auth$(find/var/run/sddm/-typef)
````

>** Warning**
>
> SDDM Bottom Left Point `Wayland ' cannot get in! Because x11vnc does not support Wayland.


- LightDM.

```sh '
$ x11vnc-display: 0-rfbauth ~/.vnc/passwd-auth/var/run/lightdm/root/:0
````

- GDM.

```sh '
$ x11vnc-display: 0-rfbauth ~/.vnc/passwd-auth/ var/lib/gdm/:0Xauth # or /run/user/120/gdm/Xauthority depending on your gdm version, see ls for yourself
````

[SDDM X11VNC] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

References

- [x11vnic-allow VNC communications to real X11 reports]
- [X11vnc] (https://wiki.archlinux.org/title/X11vnc)

# TigerVNC

Enable VNC services (currently Ports is the only one left)

# Install TigerVNC Server

```sh '
# Pkg install Tigervnc-server
````

Or:

```sh '
#cd/usr/ports/net/tigervnc-server/
# Make install clean
````

# Make some settings #

Execute command `vncpasswd ' at terminal, set access password.

Create ~/.vnc/xstartup 'file:


```sh '
$ mkdir-p ~/.vnc/
$ee ~/.vnc/xstartup
````

It reads as follows:

```sh '
#!/bin/sh
I'm sorry, I'm sorry, but I'm sorry.
I'm sorry, I'm sorry, but I'm sorry.
[-x /etc/X11/xinit/xinitrc] & & exec/etc/X11/xinit/xinitrc
[-f/etc/X11/xinit/xinitrc] & exec sh/etc/X11/xinit/xinitrc
- Solid Grey.
#exec startplasma-x11 #
#exec mate-session #
#exec xfce4-session #
#exec gnome-session #
````

Which desktop you use to delete the note in front of that desktop.

>** Warning**
>
> Please note to retain `& `**.

The authority to execute an order after saving is granted.

```sh '
$chmod755~.vnc/xstartup
````

- We'll proceed to the terminal.
- What?

```sh '
$ vncserver
````

or

```sh '
$ vncserver:

You will apply a password to access your files.

Password:
Verify:
Would you like to enter a view-only password (y/n)?
A view-only password is not used

New 'ykla: 1 (ykla)' desktop is ykla:

Creating default config/ home/ykla/.vnc/config
Starting applications delivered in/home/ykla/.vnc/xstartup
Log file is /home/ykla/.vnc/ykla:1.log
````

`1 ' means `DISPLAY=1 ' , i.e., the specified communication port for desktop displays is `1 ' and the port for VNC services is `5901 ' . Desktop displays the communications port starting from 0, but the port is already occupied by the current desktop (except for mirror VNC), so the VNC service default port is 5900, but the actual execution must start with the `5901 ' port. Therefore, if you want a link, you must specify the port as `5901 ' .

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

If the service is launched without a communication port, the system is automatically assigned according to usage.

Can view process:

````
That's right.
PID TT STAT TIME COMMAND
...it's useless to omit...
4769 S 0:02.72 /usr/local/bin/Xvnc 1-auth/home/ykla/. Xauthority-desktop ykla: 1 (ykla)
````

For closing the service, please use the command `vncserver-kill 1 ' , which must specify the port of communication.

- If the firewall is activated, for example ipfw, enter the command at the terminal:

```sh '
# ipfw add allow tcp from any to me 5900-5910 in keep-state
````

The first line command is to release port 5900-5910, i.e. DISPLAY 0-10.

References

- (https://forums.freebsd.org/threads/xfce4-is-not-displayed-

# XRDP (FreeBSD is the accused)

# # Install XRDP (kde6 based)

```sh '
# pkg install xorg kde xrdp wqy-fonts xdg-user-dirs pulseudio-module-xrdp
````

Or:

```sh '
#cd/usr/ports/x11/xorg/ & make install clean
#cd/usr/ports/x11/kde/ & make install clean
#cd /usr/ports/net/xrdp/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
#cd /usr/ports/udio/pulseudio-module-xrdp & make install clean
````

View profile:

```sh '
root@ykla:/usr/ports/net/xrdp#pkginfo-D xrdp
xrdp-0.10.2_2,1:
On install:
I don't know.
# xrdp has been successfully installed.

There is an rci'm sorry, rvice can be enabled by adding this line
In /etc/rc.conf:

"YES."
"YES"
# Provides rc.d start-up scripts that can be enabled by adding the above two lines to /etc/rc.conf.
# First start xrdp master service, second start session manager (sesman).

Do not forget to dig the confession files in "/usr/local/etc/xrdp"
And the "/usr/local/etc/xrdp/startwm.sh".
# Don't forget to edit the profile under /usr/local/etc/xrdp
# and modify /usr/local/etc/xrdp/startwm.sh to set the desktop environment that starts after login.

To an able Audio direction, install the following reports/packages to meet
Your environment.
# To enable audio redirection (telephone sound transfer), install the following packages according to your system environment:

- Audio/pipwire-module-xrdp
- Audio/Pulseudio-module-xrdp
# The above-mentioned module to support xrdp audio can be installed according to the audio system you use.
````

Configure

```sh '
# With service xrdp available
# With service xrdp-sesman #
# For service dbus able
````

Edit `/usr/local/etc/xrdp/startwm.sh ':

Found ###start task environment', amend to read:

```sh '
# Start task environment
# Exec gnome-session #
# Except date-session #
# exec start-lumina-desktop # Lumina has to delete the beginning #
# exec ck-launch-session Startplasma-x11 # KDE6 must delete the beginning of this #
# Exec startxfce4
# exec xterm # xterm has to delete the beginning of this #
````

Then restart the system, then.

## # Middle culture (user uses default sh)


```sh '
#ee /usr/local/etc/xrdp/startwm.sh
````

```sh '
# Set envirronments here if you want
Export LANG=zh_CN.UTF-8
````

# # troubleshooting and unfinished business

- XRDP, no sound.

Try the fire fox browser.

# Remote access to FreeBSD via Windows by TigerVNC

Download TigerVNC viewer:

Download address: <https://sourceforge.net/projects/tigervnc/files/stable/>

View VNC port for FreeBSD:

```sh '
Root@ykla:/usr/ports/deskutils/anydesk #sockstat-4l
USER COMMAND PID FD PROTO LOCAL ADDRESS FOREIGN ADDRESS
root Xvnc 2585 4 tcp 4 127.0.0.1:5910 *:* * #VNC occupation
root xrdp 2580 13 tcp46 *:3389 *:* * #XRDP occupation
root Xvnc 2016 5 tcp4 *:5901 * * #VNC occupation
root sshd 1164 4 tcp4 * 22 * * #SSH occupation
*: 123 *
ntpd ntpd 1127 24 udp 4127.0.0.1:123 *:*
* *
♪ Root sysloged 1021 7 udp4 ♪
````

> ** troubleshooting and unfinished business: unable to connect due to active refusal of the target server**
>
> non-film vnc must specify the port when connecting, otherwise connect by default port 5900, but you are not a mirror screen (which you use is not x11vnc) and must not be connected.
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

- Through VNC remote FreeBSD no sound, no idea how to configure.

# Remote access to FreeBSD via Windows' own desktop connection (RDP)

[xrdp FreeBSD] (..gitbook/assets/xrdp1.png)

The first-entry device will have a security alert, enter `yes ' and eject a remote desktop window upon return.

[xrdp FreeBSD] (..gitbook/assets/xrdp2.png)

[xrdp FreeBSD] (..gitbook/assets/xrdp3.png)

[xrdp FreeBSD] (..gitbook/assets/xrdp4.png)

[xrdp FreeBSD] (..gitbook/assets/xrdp5.png)

# # troubleshooting and unfinished business

-Windows ' remote desktop window is blurred if it is not displayed at the top left corner or full screen

Please ** Cancel** Check out "Intelligent Resize".

![...gitbook/assets/xrdp6.png]

# Use Android remote access to FreeBSD via XRDP

First, you need to download the required software:

RDP software developed officially by Microsoft: Remote Desktop

- [Remote Desktop] (https://play.google.com/store/apps/details?id=com.microsoft.rdc.androidx&hl=zh_CN)

The software is easy to operate.

Please note that the top left piping should be replaced with piping. The default mouse operation is inconvenient: Or you can choose a cell phone ODG as a mouse and keyboard.

[Remote Desktop FreeBSD] (..gitbook/assets/wrdp3.png)


A link diagram (the Chromium is being compiled and will be occupied very high):

[Remote Desktop FreeBSD] (..gitbook/assets/wrdp4.png)

# Remote access to Windows by XDRP via FreeBSD

##freerdp3 (new stabilizer, NLA)

Install with pkg:

````
♪ pkg in freerdp3
````

Or with Ports:

```sh '
#cd /usr/ports/net/freerdp3/
# Make install clean
````

Use FreeBSD to link remotely to Windows 11 24H2:

````
ykla@ykla:~$xfreradp3 /u:ykla /p:z /v:192.168.31.213

. . . . . . . . . . .
[1924: dca12700] [ERROR] [com.freerdp.crypto] - [tls_print_new_certificate_warn]: Host key delivery
Certificate details for 192,168,31213:3389 (RDP-Server):
Common Name: DESKTOP-U72I6SS
Subject: CN = DESKTOP-U72I6SS
Issuer: CN = DESKTOP-U72I6SS
Valid from: Mar 4 12:39:28 2025 GMT
Valid to: Sep 3 12:39:28 2025 GMT
Thumbprint: 36:b9:be:66 ab:2b:54:32:28:46:b6:98:68:8 d:6f:20:a5:d1:58:d1:08:c:09:cc:3d:30:e1:06:6f:4f:62:54:de
The above X.509
I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry.
Please look at the OpenSSL documentation on how to add a price CA to the store.
Do you trust the above link? (Y/T/N) y # Enter y to confirm the link by pressing the return key

````

`xfreerdp3 /u:ykla /p:z /v:192.168.31.213 `:

- `xfreerdp3 ' , note a `x ' in front.
- `/u: ykla ' , `/u: `i.e. Username user name. `ykla ' is my Windows login
- `/p ' , the Password password. `z ' is the login password for the Windows user `ykla '
- `/v: `, the Server server.

[freerdp] (..gitbook/assets/freerdp3.png)

References

- [FreeRDP User Manual] (https://github.com/wakecoding/FreeRDP-Manuals/blob/master/User/FreeRDP-User-Manual.markdown), with command descriptions and some examples of usage


##freerdp2 (old stabilizer, NLA)

Install with pkg:

```sh '
♪ Pkg in front ♪
````

Or with Ports:

```sh '
#cd/usr/ports/net/freerdp/
# Make install clean
````

Use FreeBSD remote link to Windows 11 24H2:

```sh '
Ykla@ykla: ~ $ xfrerdp 192,168,31213# Note is xfrerdp.
[20:35:20:041] [1105:7c412000] [WARN][com.freerdp.cent.common.cmdline] - - - - - - - -
. . . . . . . . . . .
Certificate details for 192,168,31213:3389 (RDP-Server):
Common Name: DESKTOP-U72I6SS
Subject: CN = DESKTOP-U72I6SS
Issuer: CN = DESKTOP-U72I6SS
Thumbprint: 36:b9:be:66:ab:2b:54:32:28:b:46:b6:98:68:68:d:68:d:6f:20:a5:d1:58:c:09:de:cc:3d:30:e1:06:f:4:62:54:de
The above X.509
I'm sorry, but I'm sorry, but I'm sorry, but I'm sorry.
Please look at the OpenSSL documentation on how to add a price CA to the store.
Do you trust the above certain? (Y/T/N) y # Enter y
Domain: # Leave space
Password: # Enter the password, the password will not show ***.
. . . . . . . . . . .
````


[freerdp]

# # failure and unfinished business #

- But I'm connected without a username?

I don't know. Is it because my FreeBSD username is the same as Windows?

# rdektop (NLA not supported)

`net/xrdektop2 ' is a graphical frontend for rdesktop, but my keyboard settings are stuck when I open them.

I don't...

Install rdesktop with pkg:

```sh '
# pkg install rdesktop
````

Or with Ports:

```sh '
#cd/usr/ports/net/rdektop/
# Make install clean
````

rdektop without frontend GUI so to enter command at terminal:

```sh '
# rdesktop ip: Port #
````

If there is no deliberate change in Windows configuration, add `:port ' .

For the Windows 11 24H2 I tested, it's a mistake:

```sh '
ykla
Failed to conceit, CredSSP was given by service.
````

According to [CredSSP does not work] (https://github.com/rdektop/rdektop/issues/71), this is an old problem.

The solution affecting security is to disable network-level authentication (NLA) and operate on Windows to connect remotely:

``Powershell '
PSC: \Users\ykla>reg add "HKEY_LOCAL_MACHINEE\SYSTEM\CurrentcontrolSet\Control\InternationalServer\WinStations\RDP-Tcp"/v UserAutation/t REG_DWORD/d 0/f
Operation successfully completed.
PS C: \uses\ykla>gpupdate/force
Updating policy...

Computer strategy update successfully completed.
User strategy update successfully completed.
````

Retest Link:

```sh '
ykla

The service uses and involves security, which can not be trusted for
(a) The following environment;

Certificate issuer is not trusted by this system.

Issuer: CN=DESKTOP-U72I6SS


Review the follow-up information before you trust it to be Amended as an exception.
If you do not trust the credit given the transaction atom will be aborted:

Subject: CN=DESKTOP-U72I6SS
Issuer: CN=DESKTOP-U72I6SS
Valid From: Tue Mar 4 20:39:28 2025
To: Wed Sep 3:39:28 2025

Certificate flies:

Sha1: 599c0e8bc57c57e8de8993d5241fb0d70e98d
Sha256: 36b9be66ab2b54322846b698688d6f20a5d1588c09dec3d30e1066f4f6254de


# Enter yes, press Return
````

[rdektop] (..gitbook/assets/rdektop1.png)

[rdesktop] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# # failure and unfinished business #

- No sound on the video.

Pending

References

- The method to open and close NLA is here. After testing off, rdesktop did not match again.


# AnyDesk

Remote access with AnyDesk supported only on FreeBSDx86 Structure:

As a result of copyright issues (private software is banned from distribution by default without permission), users must compile themselves using Ports:

```sh '
#cd/usr/ports/deskutils/anydesk/
# Make install clean
````

The `BATCH=yes ' parameter may not be used because a licence agreement is required for its use:

[anydesk](../.gitbook/assets/anydesk1.png)

View AnyDesk installed to describe:

```sh '
root@ykla:/ #pkginfo-D anydesk
No, nodesk-6.1.1_2:
On install:
Minimm OS version.
== sync, corrected by elderman ==
Anydesk is a binary package for FreeBSD.
Minimal returned is 1 GiB system memory
I'm sorry to bother you, but perhaps you will be retraced.
For good reason is returned and 2 GiB
I'm sorry.
# Anydesk is a binary package for FreeBSD.
# Minimum recommended memory is 1 GiB, but this will result in a decrease in performance.
# For good performance, it is recommended that at least 2 GiB be stored.

2. Important settings
== sync, corrected by elderman ==
Since Version 2.9.1 the following prerequisites have to be met:
# From Version 2.9.1, the following prerequisites must be met:

You need a Mounted/Proc Directory.
# Need to mount / proc directories, which can be mounted manually or written to /etc/fstab for automatic mount:

fstab: proc / proc procfs rw 0
# Add this line to /etc/fstab to enable procfs.

Manually: #mount-t procfs proc / proc
# Or manually execute this command to mount the proc file system.
````

A reminder is required `/proc ' , and the execution procedure, if not tested, does not respond.

```sh '
# Mount-t issues proc/ proc # temporary. Endurance can be done by reference to the above description.
````

root user cannot run AnyDesk. _Other Organiser

````
$ ykla

(<unknown>:18311) Gtk-WarnING**: 21:07:13.54: Unable to find the theme engine “adwaita” in the modular path

. . . . . . . . . . .
````

This interface pops up after the order:

![..gitbook/assets/anydesk2.png]

Note that the connected party “accepts” to continue the link.

# Windows via AnyDesk Remote FreeBSD

[Windows via AnyDesk Remote FreeBSD] (...gitbook/assets/anydesk3.png)

FreeBSD via AnyDesk Remote Windows

[Windows via AnyDesk Remote FreeBSD]

# # troubleshooting and unfinished business

- FreeBSD via AnyDesk Remote Windows does not seem to be able to move the mouse in Windows.

Pending.

# RustDesk Relay Server

Note**
>
> This is a relay ID server that cannot be remotely controlled per se.

In other words, you can't control FreeBSD with RustDesk.

Installation:

```sh '
# pkg install rustdesk-server
````

Or:

```sh '
#cd/usr/ports/net/rustdesk-server/
# Make install clean
````

Configure:

- Start hbbr:

```sh '
Root@ykla:~ /usr/local/bin/hbbs
[2024-08-10 23:02: 13.78255 + 08:00] INFO [src/common.rs: 122]
[2024-08-10 23:02:13.782587 +08.00] INFO [src/rendezvous_server.rs:1191] Key: mgrwOWJy9Vnz3LQYjtNHZQYg73uhdj9iCTMmIyoP4=#key
[2024-08-10 23:02:13.782655 +08:00] INFO [src/peer.rs:84]DB_URL=./db_v2.sqlite3
[2024-08-10 23:02:13.786349 +08.00] INFO [src/rendezvous_server.rs:99] serial=0
[2024-08-10 23:02: 13.786381 + 08:00] INFO [src/common.rs:46] rendezvous-servers=[]
[2024-08-10 23:02:13.786388 +08:00] INFO [src/rendezvous_server.rs:101]Listing on tcp/udp:21116
[2024-08-10 23:02:13.786391 +08:00] INFO [src/rendezvous_server.rs:102]
[2024-08-10 23:02:13.786395 +08.00) INFO [src/rendezvous_server.rs:103]Listing on websocket: 21118
[2024-08-10 23:02:13.786430 +08:00] INFO [libs/hbb_common/src/udp.rs:35] Received buf size of dup [:]: 2116: Ok (42080)
[2024-08-10 23:02:13.786581 +08:00] INFO [src/rendezvous_server.rs:138] Mask: None
[2024-08-10 23:02:13.786594 +08.00] INFO [src/rendezvous_server.rs: 139] local-ip: ""
[2024-08-10 23:02: 13.786603 + 08:00] INFO [src/common.rs:46] Relay-servers=[]
[2024-08-10 23:02: 13.786703 + 08:00] INFO [src/rendezvous_server.rs: 153] ALWAYS_USE_RELY=N
[2024-08-10 23:02:13.786734 +08:00] INFO [src/rendezvous_server.rs:185]
[2024-08-10 23:02:13.786793 +08:00] INFO [libs/hbb_common/src/udp.rs:35] Received buf size of dup[:]: 0: Ok (42080)
[2024-08-10 23:09:11.0409 +08.00] INFO [src/peer.rs:102] update_pk 1101115918 [:ff: 192.168.31.90]: 37057 b"\x06\xf\x2\x9ff(\\xcb\xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\xxxxxxxxxxx\xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\xxxxxxxxxxxxxx
^C [2024-08-10 23:10:06.746255 +08:00] INFO [src/common.rs:176] signature interrupt
````

- Start hbbs:

```sh '
Root@ykla:~ /usr/local/bin/hbbr
[2024-08-10 22:58:26.593397 +08.00] INFO [src/relay_server.rs:61] #backlist (blacklist.txt): 0
[2024-08-10 22:58:26.593439 +08:00] INFO [src/relay_server.rs:76] #blocklist (blocklist.txt): 0
[2024-08-10]22:58: 26:593445 + 08:00] INFO [src/relay_server.rs:82]
[2024-08-10 22:58:26.593449 +08:00] INFO [src/relay_server.rs:84]Listing on websocket: 21119
[2024-08-10 22:58:26.593452 +08:00] INFO [src/relay_server.rs:87]
[2024-08-10 22:58:26.593546 +08.00] INFO [src/relay_server.rs:105] DOWNGRADE_THRESHOLD: 0.66
[2024-08-10 22:58:26.593556 +08.00] INFO [src/relay_server.rs:115] DoWNGRADE_START_CHENK: 1800s
[2024-08-10 22:58:26.593559 +08.00] INFO [src/relay_server.rs:125] LIMIT_SPED: 4Mb/s
[2024-08-10 22:58:26.593564 +08.00] INFO [src/relay_server.rs:136] TOTAL_BANDWIDTH: 1024 Mb/s
[2024-08-10 22:58:26.593567 +08.00] INFO [src/relay_server.rs: 146] SINGLE_BandWIDTH: 16Mb/s
^C [2024-08-10 23:10:04.393365 +08:00] INFO [src/common.rs:176] signature interrupt
````

Opens the rustdesk client on other devices with the same "ID server (FreeBSD IP address or domain name)" and "Key" on both sides. The others are empty and can be connected by entering the ID displayed at the control end.

References

- [rustdesk-server Self held RustDesk servicer] (https://www.freshports.org/net/rustdesk-server/)
- [Remote Control Software RustDesk Self-Building Server Full Platform Deployment and Use Academy] (https://www.cnblogs.com/safe-rabbit/p/18020812)

