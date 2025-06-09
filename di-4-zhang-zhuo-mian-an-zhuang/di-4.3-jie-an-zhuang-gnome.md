Section 4.3 GNOME

GNOME was a GNU project to develop a fully functional desktop environment. It is noteworthy that `G ' in GNOME does not sound (/ˈnoʊm/).

# Install

- Install with pkg:

```sh '
# pkg install xorg gno come noto-sc xdg-user-dirs
````

- Or install with Ports:

````
#cd/usr/ports/x11/xorg/ & make install clean
#cd /usr/ports/x11/gnome/ & make install clean
#cd /usr/ports/x11-fonts/noto-serif-sc/ & make install clean
# cd /usr/ports/devel/xdg-user-dirs/ & make automatic clean
````

- Explain:

Software Use
|: - - -: |: | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
X11
|gnome|Gnome master
Noo-sc
xdg-user-dirs

# # Appendix: streamline installation

- Install with pkg:

```sh '
# pkg install xorg-minimal gnome-lite wqy-fonts xdg-user-dirs
````


- Or install with Ports:

```sh '
#cd /usr/ports/x11/xorg-minimal/ & make install clean
#cd /usr/ports/x11/gnome/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````

- Explain.


The name of the bag.
|: - - - - |: |
`xorg-minimal ' | Simplified X Graphic Environment |
`gnome-lite`simplified version of the GNOME desktop

A full version of the game software can also be unloaded with a pkg package manager if installed:

```sh '
# pkg delete gnome-2048 gnome-klotski gnome-tetravex gnome-mines gnome-taquine gnome-sudoku gnome-robots gnome-nibbles lights off tali Quadrapassel swell-foop gnome-mahjongg five-or-more igno anisleriot Four-in-a-row
````

! [Gnome streamline installation] (..gitbook/assets/gnome-lite.png)

Configure

```sh '
# ee / etc/fstab
````

Add the following text:

```sh '
Proc / proc procfs rw 0 0
````

Configure startup:

```sh '
# For service dbus able
# Sysrc gdm_enable
````

Enter the following command:

```sh '
$eho "/usr/local/bin/gnome-session" ~/.xinitrc
````

FreeBSD Gnome (../.gitbook/assets/gnome1.png)

Default forbids root login.

[FreeBSD Gnome] (.. .gitbook/assets/gnome2.png)

That's the default wallpaper.


Middle culture

# # GNOME Interface

> This subsection configuration parameter has nothing to do with the user shell, even the csh should be so configured.

```sh '
#ee /usr/local/etc/gdm/locale.conf
````

Add the following:

```sh '
LANG = "zh_CN.UTF-8"
LC_CTYPE= "zh_CN.UTF-8"
LC_MSAGES = "zh_CN.UTF-8"
LC_All= "zh_CN.UTF-8"
````

# In Chinese

`ibus ' , `fcitx5 ' .

# ibus #

The gnome bundled input method panel is `ibus ' .

```sh '
# pkg install zh-ibus-libpiniin
````

Or...

```sh '
#cd/usr/ports/chinese/bus-libpnyin/
# Make install clean
````

Run initialization command after installation `ibus-setup '.

# # fcitx 5 #

Let's start with our own shell.

```sh '
# echo zero
````

If yes, continue; if no, refer to the relevant sections of the input method.

Installation of `fcitx5 ':

```sh '
#pkg install fcitx5 fcitx5-qt5 fcitx5-qt6 fcitx5-gtk2 fcitx5-gtk3 fcitx5-gtk4 fcitx5 zh-fcitx5-chinese-addons
````

Or:

```sh '
#cd /usr/ports/textproc/fcitx5/ & make install clean
#cd /usr/ports/textproc/fcitx5-qt/ & make install clean
#cd /usr/ports/textproc/fcitx5-gtk/ & make install clean #gtk 2, 3, 4
#cd /usr/ports/textproc/fcitx5-configtool/ & make install clean
#cd/usr/ports/chinese/fcitx5-chinese-addons/ & make install clean
````

Open or create new files ~/.xprofile ' , writing:

```sh '
I'm sorry.
QT_IM_MODULE=fcitx
@m=fcitx
````

Reference: The following is an example of this document:

```sh '
# FreeBSD
# I don't know
.profile - Bourne Shell starts script for login' shells
# I don't know
# See also sh(1), environ(7).
# I don't know

♪ These are probably set through/etc/login. ♪
# If wanted.
#PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin: $HOME/bin; export PATH

Setting TERM is most likely done through/etc/ttys.
# If you're sure that you'll never log in via taline or xerm or a
# Serial line.
# TERM=xterm; export TERM

EDITOR=vi;export EDITOR
PAGER=less;export PAGER

♪ Set ENV to a file enclosed each time sh is started for interactive use.
ENV = $HOME/.shrc; export ENV

Let sh(1) know it's at home, depitate/ come being a symlink.
& [ "$PWD" - ef "$HOME"]; then cd; fi

♪ Query technical size; useful for security lines. ♪
If [-x/usr/bin/resizewin]; then/usr/bin/resizewin-z;

♪ Display a random cookie on each login. ♪
If [-x/usr/bin/fortune]; then/usr/bin/fortunefreebsd-tips; fi

I'm sorry.
QT_IM_MODULE=fcitx
@m=fcitx
````


## # terminal display in Chinese (file user root directory)

Note**
>
>This is valid for FreeBSD 14 below.

```sh '
# eee ~ /.cshrc
````

Add the following

```sh '
Setenv LANG zh_CN.UTF-8
Setenv LC_CTYPE zh_CN.UTF-8
LC_ALL zh_CN.UTF-8
````

# Optimizing the system

```sh '
# pkg install gnome-tweaks
````

Or:

```sh '
#cd/usr/ports/deskutils/gnome-tweaks/
# Make install clean
````

Some anti-human adjustments

GNOME has been known as anti-human: desktops do not allow icons, top right corner does not have trays, etc. Can't there be any garbage in the trash can, people can't be in bed, doors can't be closed, anything on the table can be different

# # Restore the tray icon for the GNOME topbar

As [TopIcons Plus] (https://extensions.gnome.org/extension/1031/topicons/) has not been updated for a long time, only [AppIndicator and KStatusNotifierItem Port] (https://extensions.gnome.org/extension/615/appindicator-support/).

. [Gnome restores the tray icon for the GNOME topbar] (. . .getbook/assets/gnome3.png)

. [Gnome restores the tray icon for the GNOME topbar] (.. . .gitbook/assets/gnome4.png)

! [Gnome restores the tray icon for the GNOME topbar] (.. .gitbook/assets/gnome5.png)

. [Gnome restores the tray icon for the GNOME topbar] (.. .getbook/assets/gnome6.png)

! [Gnome restores the tray icon for the GNOME topbar] (. . .gitbook/assets/gnome7.png)

! [Gnome restores the tray icon for the GNOME topbar] (.. . . .gitbook/assets/ gnome8.png)

References

- [Recovering the tray icon for the GNOME topbar] (https://linuxstory.org/restore-tray-coon-for-gnome-top-bar/)

# Put the icon on the desktop #

Extension [gnome-shell-extension-desktop-icons] (https://extensions.gnome.org/extension/1465/desktop-icons/) has not been updated for a long time and project address: [Desktop Icons] (https://gitlab.gnome.org/World/ShelExtensions/desktop-icons).

The solution can be found in [Desktop Icons NG (DING)] (https://extensions.gnome.org/extension/2087/desktop-icons-ng-ding/). As above.

! [Gnome on desktop display icon] (.. . .gitbook/assets/gnome9.png)

The wallpaper was set by myself. I set the fire fox myself. The rest is by default.
。