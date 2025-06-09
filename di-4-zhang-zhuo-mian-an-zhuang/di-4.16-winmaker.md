# 4.16 Window Maker

Windows Maker is a window manager. The design objective is to recreate NeXTSTEP (based on this) user interface and user experience.

# Install

- Install with pkg:

```sh '
# pkg install windowmaker wmakerconf xorg lightdm lightdm-gtk-greenter wqy-fonts xdg-user-dirs
````

- Or use Ports:

```sh '
# cd /usr/ports/x11/windowmaker/ & make install clean
#cd /usr/ports/x11-wm/wmakerconf/ & make install clean
#cd/usr/ports/x11/xorg/ & make install clean
#cd/usr/ports/x11/lightdm/ & make install clean
#cd /usr/ports/x11/lightdm-gtk-greener/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````

- Explain:



Name of package Description of role
|: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
`xorg 'X Windows
`windowmaker ' |X11 Window Manager |
The configuration tool for `wmakerconf ' |Window Maker was not installed as a relying package; it contains language packages but is not available in Chinese
`lightdm ' | Lightweight Display Manager
GTK+ login plugin for `lightdm-gtk-greener ' | LightDM, missing will not be able to start LightDM|
`wqy-fonts '
`xdg-user-dirs ' | to manage user directories such as desktops, downloads, etc.



# 'startx'

Edit ~/.xinitrc ' , add:

```sh '
That's right, exec wmaker.
````

References

- [How to startx window maker?] (https://www.linuxquestions.org/questions/debian-26/how-to-startx-window-maker-230516/)

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

Edit `/etc/login.conf ' , find `default:\, amend `:lang=C.UTF-8 ' to `:lang=zh_CN.UTF-8 ' .

Refresh database:

```sh '
#cap_mkdb/etc/login.conf
````

Picture

! [FreeBSD installation] Windows Maker (..gitbook/assets/WindowMaker1.png)

! [FreeBSD installation] Windows Maker (..gitbook/assets/WindowMaker2.png)

# Fragmentation and unfinished business

- ♪ Could not execute company: exec WPrefs ♪

Could enter at terminal

```sh '
#/usr/local/GNUStep/Applications/WPrefs.app/WPrefs
````

! [FreeBSD installation] Windows Maker (..gitbook/assets/WindowMaker3.png)

- I can't live with culture.

Pending.

References

- [Windowmaker could not execute wprefs!] (https://forums.freebsd.org/threads/windowmaker-could-not-execute-wprefs92625/)
