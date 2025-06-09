# Section 4.10 IceWM

# Install

- install with pkg:

```sh
# pkg install xorg icewm slim wqy-fonts xdg-user-dirs
```

- Or install with Ports:

```sh
# cd /usr/ports/x11-wm/icewm/ && make install clean # fluxbox
# cd /usr/ports/x11-themes/icewm-extra-themes/ && make install clean 
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/slim/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

- Explain

| Package Name | Description of role |
|:------------------|:-----------------------------------------------------------------------|
| `xorg ' | X Windows |
| `icewm ' | Lightweight Window Manager |
| `slim' | Lightweight Graphic Login Manager |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manage user directories such as Desktop, Download.. |


# CODESPAN_0__

EDIT __CODESPAN_0_, ADD (TO BE WRITTEN BY WHOM TO LOG IN):

```sh
exec icewm-session
```

# Starter

```sh
# service dbus enable
# sysrc slim_enable="YES"
```

# fshab

EDIT __CODESPAN_0_, ADD:

```sh
proc           /proc       procfs  rw  0   0
```


# Desktop appreciation

[FreeBSD institutionicewm] (./.gitbook/assets/fluxbox1.png)

[FreeBSD institutionicewm] (..gitbook/assets/icewm1.png)

[..gitbook/assets/icewm2.png]

# Fragmentation and unfinished business

- Menu missing text

Pending

- No Chinese

Pending
