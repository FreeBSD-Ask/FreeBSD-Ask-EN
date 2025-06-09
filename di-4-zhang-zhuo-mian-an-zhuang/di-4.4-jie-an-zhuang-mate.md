# Section 4.4 Mate

Mate developed by GNOME 2 after all.

You may not know mate, Ilex paraguariensis, but you may have heard of "Madeh tea". Many South American players (e.g. Massey) are very interested in this plant-made tea.

# Install

- Install with pkg:

```sh '
# pkg install mate x wqy-fonts lightdm slick-greener xdg-user-dirs
````

- Or install with Ports:

```sh '
# cd /usr/ports/x11/mate/ & make install clean
#cd/usr/ports/x11/xorg/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd/usr/ports/x11/lightdm/ & make install clean
#cd /usr/ports/x11/slick-greener/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````

- Explain.


Name of package Description of role
|: - - - - - |: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
`mate ' | MATE Desktop Environment
`xorg 'X Windows
`wqy-fonts '
`lightdm ' | Display Manager providing a graphical login interface
`slick-greener ' | LightDM 's aesthetic login interface plugin, missing which will not be able to start LightDM|
`xdg-user-dirs ' |Automable Manager Subdirectories (optional) |

# Post-installation start-up service

```sh '
# For service dbus able
♪ service lightdm able
````

# `startx ' Profile

Add the following line to the ~/.xinitrc ' document:

```sh '
This post is part of our special coverage Syria Protests 2011.
````

# Show Chinese Desktop Environment


Edit `/etc/login.conf ' : find `default:\, amend `:lang=C.UTF-8 ' to `:lang=zh_CN.UTF-8 ' .

Refresh database:

```sh '
#cap_mkdb/etc/login.conf
````



# Input Method

. . . . .gitbook/assets/mate4.png

The ibus test was successful. Please refer to the relevant section of the input method.


# Desktop appreciation

. . . . .gitbook/assets/cinnamon1.png

! [FreeBSD installation ..]

.! [FreeBSD installation ..]

# Fragmentation and unfinished business

# # Configure slick-greener

Create `/usr/local/etc/lightdm/slick-greener.conf '

```ini '
[Greeter]
# Sets the background image path for the login interface
Background=/home/ykla/cat.png

# Whether to draw user-defined background pictures
= false

# Set GTK+ Theme Name
=Dracula

# Set icon theme name
ion-theme-name=Adwaita

# Whether to show hostname
Show-hostname=true

# Set font name and size
font-name=Sans12

# Whether to show virtual keyboard options
Show-keyboard = true

# Whether to show power management options (e.g. shut down, restart)
Show-power=true

# Whether to show the clock
Show-cock=true

# Whether to show exit options
Show-quit = true
````

. . . . .gitbook/assets/mate1.png)

References

- [lightdm not reading slick-greener.conf] (https://forums.freebsd.org/threads/lightdm-not-reading-slick-greener-conf.922256)
