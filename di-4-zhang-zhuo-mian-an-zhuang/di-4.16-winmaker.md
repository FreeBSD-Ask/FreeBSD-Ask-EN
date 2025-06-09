# 4.16 Window Maker

Windows Maker is a window manager. The design objective is to recreate NeXTSTEP (based on this) user interface and user experience。

# Install

- install with pkg:

```sh
# pkg install windowmaker wmakerconf xorg lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```

- Or use Ports:

```sh
# cd /usr/ports/x11/windowmaker/ && make install clean
# cd /usr/ports/x11-wm/wmakerconf/ && make install clean 
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/lightdm/ && make install clean 
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- Explain:



| Package Name | Description of role |
|:--------------------------|:-------------------------------------------------------|
| `xorg ' | X Windows |
| `windowmaker ' | X11 WINDOW MANAGER |
| `wmakerconf ' | Windows Maker configuration tool, not installed as a relying package; contains language packages but is not available in Chinese |
| `lightdm ' | Lightweight Display Manager LightDM |
| `lightdm-gtk-greenter ' | LightDM 's GTK+ login interface plugin, missing will not enable LightDM to start |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manage user directories such as desktops, downloads, etc |



# CODESPAN_0__

EDIT __CODESPAN_0_, ADD:

```sh
exec wmaker
```

References

- [How to startx window maker?] (https://www.linuxquestions.org/questions/debian-26/how-to-startx-window-maker-230516/)

# Starter

```sh
# service dbus enable
# service lightdm enable
```

# fshab

EDIT __CODESPAN_0_, ADD:

```sh
proc           /proc       procfs  rw  0   0
```

Chinese Configuration

ADD UNDER __CODESPAN_0_:

```sh
lightdm_env="LC_MESSAGES=zh_CN.UTF-8" 
```

---|---

EDIT __CODESPAN_0, FIND __CODESPAN_1_, AND AMEND __CODESPAN_2_ TO __CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```

Picture

[FreeBSD integration Windows Maker]

FreeBSD integration Windows Maker (../.gitbook/assets/WindowMaker2.png)

# Fragmentation and unfinished business

- CODESPAN_0_

Could enter at terminal

```sh
# /usr/local/GNUStep/Applications/WPrefs.app/WPrefs
```

../.gitbook/assets/WindowMaker3.png

- I can't live with culture

Pending。

References

- [windowmaker could not execute wprefs!] (https://forums.freebsd.org/threads/windowmaker-could-not-execute-wprefs92625/)
