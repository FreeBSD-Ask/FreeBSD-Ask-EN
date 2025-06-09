# Section 4.17 Fluxbox

# Install

- install with pkg:

```sh
# pkg install xorg fluxbox fluxbox-tenr-styles-pack slim wqy-fonts xdg-user-dirs
```

- Or install with Ports:

```sh
# cd /usr/ports/x11-wm/fluxbox/ && make install clean # fluxbox
# cd /usr/ports/x11-themes/fluxbox-tenr-styles-pack/ && make install clean 
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/slim/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- Explain


| Package Name | Description of role |
|:-----------------------------|:--------------------------------------------------------------------------|
| `xorg ' | X Windows |
| `fluxbox ' | Window Manager |
| 'fluxbox-tenr-styles-pack ' | Fluxbox theme package provided by Tenner |
| `slim' | Lightweight Graphic Login Manager |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manage user directories such as desktops, downloads, etc |



# CODESPAN_0__

EDIT __CODESPAN_0_, ADD (TO BE WRITTEN BY WHOM TO LOG IN):

```sh
exec startfluxbox
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

# Chinese Configuration


EDIT __CODESPAN_0: FIND __CODESPAN_1_, AND MODIFY __CODESPAN_2_ TO __ ___ CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```

# Desktop appreciation

[FreeBSD integration flexbox]

[FreeBSD integration flexbox]

# Fragmentation and unfinished business

-light, xdm not available to start flexbox

Pending

- No Chinese

Pending
