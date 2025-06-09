# Section 4.8 LXQt

# Install LXQt

- Install by pkg

```sh '
# pkg install xorg sddm lxqt gvfs wqy-fonts xdg-user-dirs
````

- Or install with Ports:

```sh '
#cd/usr/ports/x11/xorg/ & make install clean
#cd /usr/ports/x11-wm/lxqt/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd /usr/ports/x11/sdm/ & make install clean
#cd /usr/ports/devel/gvfs/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````

Explanation:

Name of package Description of role
|: - - - - - - | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
`xorg 'X Windows
`sdm ' login manager
`lxqt '|LXQt' Preferred Display Manager
`gvfs '| GNOME Virtual File System, LXQt relies on this to open Computer and Network, otherwise `Operation not supported '|
`wqy-fonts '
`xdg-user-dirs ' | to manage user directories such as "desktop", "download" etc., and to process localized | for directory names


# Service management


```sh '
# For service dbus able
# With service sddm capable
````

# `fstab'

Edit `/etc/fstab ' , add:

```sh '
Proc / proc procfs rw 0 0
````

# Start LXQt by startx

```sh '
$ ~.xinitrc
````

Use who logs in and write in.

# Set the Chinese display

Middle culture SDDM

```sh '
# Sysrc sddm_lang #
````

! [FreeBSD installation LXQt] (..gitbook/assets/lxqt1.png)

! [FreeBSD installation LXQt] (./.gitbook/assets/lxqt2.png)

. [FreeBSD installation LXQt] (./.gitbook/assets/lxqt3.png)

Medium Cultural Desktop

After LXQt menu - > "Preferences" - > "LXQt Settings" - > "Locale" - > "Region"

! [FreeBSD installation LXQt] (..gitbook/assets/lxqt4.png)

! [FreeBSD installation LXQt] (..gitbook/assets/lxqt5.png)

# Fragmentation and unfinished business

- Desktop icons are not shown

Please install other icons you like in advance. And then: menu - > "Preferences" - > "LXQt Settings" - > "Appearance" - > "Icons Theme" selects the icon you installed - > > "Apply" and re-entry after.

。