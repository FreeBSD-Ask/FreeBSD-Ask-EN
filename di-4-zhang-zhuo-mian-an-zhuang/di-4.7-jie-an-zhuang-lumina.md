# Section 4.7 Lumina

Lumina uses the BSD license. Lumina Technology Bark is QT5 and does not use any Linux-based desktop frame to advocate light quantification。

2025.1.8 The test does not allow access to the desktop in VMware, enters and exits. See [Some problem Under FreeBS 13.2 with Xorg and Lumina Desktop... How to solve?] (https://forums.freebsd.org/threads/some-problem-under-freebsd-13-2-with-xorg-and-lumina-desktop-how-to-solve888882/). But show normal in VirtualBox。


Note**
>
>[Lumina] (https://github.com/lumina-desktop/lumina) With the change of developer, development has been stalled for a long time, and the pull I have submitted to it has been unprocessed for a long time, and no new information is available。

# Install

- install with pkg:

```sh
# pkg install lumina xorg lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```

- Or install with Ports:

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/lumina/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/lightdm/ && make install clean
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- Explain

| Package Name | Description of role |
|:------------------------|:--------------------------------------------------------------------------|
| `lumina ' | Lumina Desktop Environment |
| `xorg ' | X Windows |
| `lightdm ' | Lightweight Display Manager LightDM |
| `lightdm-gtk-greenter ' | LightDM 's GTK+ login interface plugin. Without will not start LightDM |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manage user directories such as desktops, downloads, etc |


# Configure Services


```sh
# service dbus enable
# service lightdm enable
```

# CONFIGURE __CODESPAN_0_

EDIT __CODESPAN_0_, ADD:

```sh
exec lumina-desktop
```

Middle culture

ADD UNDER __CODESPAN_0_:

```sh
lightdm_env="LC_MESSAGES=zh_CN.UTF-8" 
```

---|---

EDIT __CODESPAN_0: FIND __CODESPAN_1_, AND MODIFY __CODESPAN_2_ TO __ ___ CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```

# Desktop appreciation

[FreeBSD integration Lumina]

[..gitbook/assets/lumina2.png]

[FreeBSD integration Lumina]
