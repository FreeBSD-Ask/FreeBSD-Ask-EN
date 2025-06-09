# Section 4.17 Fluxbox

# Install

- Install with pkg:

```sh '
# pkg install xorg fluxbox-tenr-styles-pack slim wqy-fonts xdg-user-dirs
````

- Or install with Ports:

```sh '
#cd /usr/ports/x11-wm/fluxbox/ & make install clean
#cd/usr/ports/x11-themes/fluxbox-tenr-styles-pack/ & make install clean
#cd/usr/ports/x11/xorg/ & make install clean
#cd /usr/ports/x11/slim/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````

- Explain.


Name of package Description of role
|:-----------------------------------------------------------------
`xorg 'X Windows
`fluxbox ' window manager
Fluxbox Theme Package provided by `fluxbox-tenr-styles-pack '
`slim ' | lightweight graphic login manager
`wqy-fonts '
`xdg-user-dirs ' | to manage user directories such as desktops, downloads, etc.



# 'startx'

Edit ~/.xinitrc ' , Add (for login, write by):

```sh '
I'm sorry, exec startfluxbox.
````

# Starter

```sh '
# For service dbus able
# Sysrc slim_enable
````

# fshab

Edit `/etc/fstab ' , add:

```sh '
Proc / proc procfs rw 0 0
````

# Chinese Configuration


Edit `/etc/login.conf ' : find `default:\, amend `:lang=C.UTF-8 ' to `:lang=zh_CN.UTF-8 ' .

Refresh database:

```sh '
#cap_mkdb/etc/login.conf
````

# Desktop appreciation

! [FreeBSD installation flexbox] (./.gitbook/assets/flexbox1.png)

! [FreeBSD installation flexbox] (..gitbook/assets/flexbox2.png)

# Fragmentation and unfinished business

-light, xdm not available to start flexbox

Pending

- No Chinese.

Pending
