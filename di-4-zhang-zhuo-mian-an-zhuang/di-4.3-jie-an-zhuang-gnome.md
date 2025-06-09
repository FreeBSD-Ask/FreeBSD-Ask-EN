SECTION 4.3 GNOME

GNOME was a GNU project to develop a fully functional desktop environment. It is noteworthy that in the English word __CODESPAN_0_ does not sound (/ˈnoʊm/)。

# Install

- install with pkg:

```sh
# pkg install xorg gnome noto-sc xdg-user-dirs
```

- Or install with Ports:

```
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/gnome/ && make install clean
# cd /usr/ports/x11-fonts/noto-serif-sc/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean # 自动管理家目录子目录
```

- Explain:

| Software | Purpose |
| :-----------: | :------------------------: |
| xorg | X11 |
| ♪ gnome ♪ | Gnome Master |
| noto-sc | C_lose - Chinese |
| xdg-user-dirs | AutoManger Subdirectories |

# # Appendix: streamline installation

- install with pkg:

```sh
# pkg install xorg-minimal gnome-lite wqy-fonts xdg-user-dirs
```


- Or install with Ports:

```sh
# cd /usr/ports/x11/xorg-minimal/ && make install clean
# cd /usr/ports/x11/gnome/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

- Explain


| Package Name | Role |
|:------------------|:------------------|
| `xorg-minimal ' | SIMPLIFIED X GRAPHIC ENVIRONMENT |
| `gnome-lite ' | STREAMLINED GNOME DESKTOP |

a full version of the game software can also be unloaded with a pkg package manager if installed:

```sh
# pkg delete gnome-2048 gnome-klotski gnome-tetravex gnome-mines gnome-taquin gnome-sudoku gnome-robots gnome-nibbles lightsoff tali quadrapassel swell-foop gnome-mahjongg five-or-more iagno aisleriot four-in-a-row
```

../ .gitbook/assets/gnome-lite.png)

Configure

```sh
# ee /etc/fstab
```

Add the following text:

```sh
proc /proc procfs rw 0 0
```

Configure startup:

```sh
# service dbus enable
# sysrc gdm_enable="YES"
```

Enter the following command:

```sh
$ echo "/usr/local/bin/gnome-session" > ~/.xinitrc
```

FreeBSD Gnome (../.gitbook/assets/gnome1.png)

default forbids root login。

[FreeBSD Gnome] (.. .gitbook/assets/gnome2.png)

That's the default wallpaper。


Middle culture

# # GNOME INTERFACE

> this subsection configuration parameter has nothing to do with the user shell, even the csh should be so configured。

```sh
# ee /usr/local/etc/gdm/locale.conf
```

Add the following:

```sh
LANG="zh_CN.UTF-8"
LC_CTYPE="zh_CN.UTF-8"
LC_MESSAGES="zh_CN.UTF-8"
LC_ALL="zh_CN.UTF-8"
```

# In Chinese

__CODESPAN_0, __CODESPAN_1_。

# ibus #

gnome bound input method panel is __CODESPAN_0_。

```sh
# pkg install zh-ibus-libpinyin
```

Or..

```sh
# cd /usr/ports/chinese/ibus-libpinyin/
# make install clean
```

RUN INITIALIZATION COMMAND AFTER INSTALLATION __CODESPAN_0_.

# # fcitx 5 #

First of all, look at your own shell

```sh
# echo $0
```

If yes, continue; if no, refer to the relevant sections of the input method。

INSTALL __CODESPAN_0_:

```sh
# pkg install fcitx5 fcitx5-qt5 fcitx5-qt6 fcitx5-gtk2 fcitx5-gtk3 fcitx5-gtk4 fcitx5-configtool zh-fcitx5-chinese-addons
```

Or:

```sh
# cd /usr/ports/textproc/fcitx5/ && make install clean
# cd /usr/ports/textproc/fcitx5-qt/ && make install clean #同时包含 QT 5 和 QT 6
# cd /usr/ports/textproc/fcitx5-gtk/ && make install clean #同时包含 gtk 2、3、4
# cd /usr/ports/textproc/fcitx5-configtool/ && make install clean
# cd /usr/ports/chinese/fcitx5-chinese-addons/ && make install clean
```

OPEN OR CREATE __CODESPAN_0_, WRITE:

```sh
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
```

Reference: The following is an example of this document:

```sh
# $FreeBSD$
#
# .profile - Bourne Shell startup script for login shells
#
# see also sh(1), environ(7).
#

♪ These are probably set through/etc/login. ♪
# if wanted.
#PATH=/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/sbin:/usr/local/bin: $HOME/bin; export PATH

Setting TERM is most likely done through/etc/ttys
# if you're sure that you'll never log in via taline or xerm or a
# serial line.
# TERM=xterm; export TERM

EDITOR=vi;export EDITOR
PAGER=less;export PAGER

♪ Set ENV to a file enclosed each time sh is started for interactive use.
ENV = $HOME/.shrc; export ENV

Let sh(1) know it's at home, depitate/ come being a symlink.
& [ "$PWD" - ef "$HOME"]; then cd; fi

♪ Query technical size; useful for security lines. ♪.
if [-x/usr/bin/resizewin]; then/usr/bin/resizewin-z

♪ Display a random cookie on each login. ♪.
if [-x/usr/bin/fortune]; then/usr/bin/fortunefreebsd-tips; fi

i'm sorry
qT_IM_MODULE=fcitx
@m=fcitx
````


## # terminal display in Chinese (file user root directory)

Note**
>
>This is valid for FreeBSD 14 below。

```sh
# ee ~/.cshrc
```

Add the following

```sh
setenv LANG zh_CN.UTF-8
setenv LC_CTYPE zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
```

# Optimizing the system

```sh
# pkg install gnome-tweaks
```

Or:

```sh
# cd /usr/ports/deskutils/gnome-tweaks/ 
# make install clean
```

Some anti-human adjustments

GNOME HAS BEEN KNOWN AS ANTI-HUMAN: DESKTOPS DO NOT ALLOW ICONS, TOP RIGHT CORNER DOES NOT HAVE TRAYS, ETC. CAN'T THERE BE ANY GARBAGE IN THE TRASH CAN, PEOPLE CAN'T BE IN BED, DOORS CAN'T BE CLOSED, ANYTHING ON THE TABLE CAN BE DIFFERENT

# # RESTORE THE TRAY ICON FOR THE GNOME TOPBAR

As [TopIcons Plus] (https://extensions.gnome.org/extension/1031/topicons/) has not been updated for a long time, only [AppIndicator and Kstatus notifierItem Support] can be used (https://extensions.gnome.org/extension/615/appindicator-support/)。

[Gnome Resource Tray Icon for GNOME Topbar]

[Gnome Resource Tray Icon for GNOME Topbar]

[Gnome Resource Tray Icon for GNOME Topbar]

[Gnome Resource Tray Icon for GNOME Topbar]

[Gnome Resource Tray Icon for GNOME Topbar]

[Gnome Resource Tray Icon for GNOME Topbar]

References

- [RESTORE TRIY ICON FOR GNOME TOPBAR] (https://linuxstory.org/restore-tray-coon-for-gnome-top-bar/)

# Put the icon on the desktop #

Extension [gnome-shell-extension-desktop-icons] (https://extensions.gnome.org/extension/1465/desktop-icons/) has not been updated for a long time and project address: [Desktop Icons] (https://gitlab.gnome.org/World/ShelExtensions/desktop-icons)。

The solution can be found in [Desktop Icons NG (DING)] (https://extensions.gnome.org/extension/2087/desktop-icons-ng-ding/). As above。

[Gnome Put Icon on Desktop]

The wallpaper was set by myself. I set the fire fox myself. The rest is by default。
