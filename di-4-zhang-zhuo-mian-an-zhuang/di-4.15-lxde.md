# Section 4.15 LXDE

# Install

- Install with pkg:

```sh '
# pkg install lxde-meta xorg lightdm lightdm-gtk-greenter wqy-fonts xdg-user-dirs
````


- Or install with Ports:

```sh '
#cd /usr/ports/x11/lxde-meta/ & make install clean
#cd/usr/ports/x11/xorg/ & make install clean
#cd/usr/ports/x11/lightdm/ & make install clean
#cd /usr/ports/x11/lightdm-gtk-greener/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````


- Explain:


Name of package Description of role
|: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
`xorg 'X Windows
`lxde-meta ' |LXDE desktop environment
`lightdm ' | Lightweight Display Manager
GTK+ login plugin for `lightdm-gtk-greener ' | LightDM. Missing LightDM |
`wqy-fonts '
`xdg-user-dirs ' | to manage user directories such as desktops, downloads, etc.


# 'startx'

Edit ~/.xinitrc ' , add:

```sh '
I don't know, exec startlxde.
````

# Starter

```sh '
# For service dbus able
♪ service lightdm able
````

# fshab

Edit `/etc/fstab ' , add:

```sh '
Proc / proc procfs rw 0 0
````

Chinese Configuration

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

...! [FreeBSD installation LXDE] (./.gitbook/assets/lxde1.png)

. [FreeBSD installation LXDE] (./.gitbook/assets/lxde2.png)

! [FreeBSD installation LXDE] (./.gitbook/assets/lxde3.png)

# References

(https://wiki.freebsd.org/LXDE)
