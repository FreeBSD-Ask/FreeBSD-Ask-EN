# Section 4.7 Lumina

Lumina uses the BSD license. Lumina Technology Bark is QT5 and does not use any Linux-based desktop frame to advocate light quantification.

2025.1.8 The test does not allow access to the desktop in VMware, enters and exits. See [Some problem Under FreeBSD 13.2 with Xorg and Lumina Desktop...ow to Solve?] (https://forums.freebsd.org/threads/some-problem-under-freebsd-13-2-west-xorg-and-lumina-desktop-how-to-solve888882/). But show normal in VirtualBox.


Note**
>
>[Lumina] (https://github.com/lumina-desktop/lumina) With the change of developer, development has been stalled for a long time, and the pull I have submitted to it has been unprocessed for a long time, and no new information is available.

# Install

- Install with pkg:

```sh '
# pkg install Lumina xorg lightdm lightdm-gtk-greener wqy-fonts xdg-user-dirs
````

- Or install with Ports:

```sh '
#cd/usr/ports/x11/xorg/ & make install clean
#cd /usr/ports/x11/lumina/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd/usr/ports/x11/lightdm/ & make install clean
#cd /usr/ports/x11/lightdm-gtk-greener/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````

- Explain.

Name of package Description of role
|: - - - - - - - - | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
`lumina ' | Lumina Desktop Environment
`xorg 'X Windows
`lightdm ' | Lightweight Display Manager LightDM|
GTK+ login interface plugin for `lightdm-gtk-greenter ' . Without will not be able to start LightDM
`wqy-fonts '
`xdg-user-dirs ' | to manage user directories such as desktops, downloads, etc.


# Configure Services


```sh '
# For service dbus able
♪ service lightdm able
````

# Configure 'startx '

Edit ~/.xinitrc ', add:

```sh '
For example, Lumina-desktop
````

Middle culture

Under `/etc/rc.conf ' , insert:

```sh '
Lightdm_env=“LC_MSAGES=zh_CN.UTF-8”
````

I don't...

Edit `/etc/login.conf ' : find `default:\, amend `:lang=C.UTF-8 ' to `:lang=zh_CN.UTF-8 ' .

Refresh database:

```sh '
#cap_mkdb/etc/login.conf
````

# Desktop appreciation

[FreeBSD installation Lumina] (./.gitbook/assets/lumina1.png)

[FreeBSD installation Lumina] (./.gitbook/assets/lumina2.png)

[FreeBSD installation Lumina] (./.gitbook/assets/lumina3.png)
