# Section 4.6 Cinnamon

Cinnamon is based on GNOME Shell from Linux Mint Project。

# Install

- install with pkg:

```sh
# pkg install xorg lightdm slick-greeter cinnamon wqy-fonts xdg-user-dirs
```

- Or install with Ports:

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11/cinnamon/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean 
# cd /usr/ports/x11/lightdm/ && make install clean 
# cd /usr/ports/x11/slick-greeter/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- Explain

| Package Name | Description of role |
|:--------------------|:----------------------------------|
| `xorg ' | X Windows |
| `lightdm ' | Lightweight Display Manager LightDM |
| `slick-greenter ' | LightDM beauty login plugin, missing will not enable LightDM to start |
| `cinnamon ' | MODERN DESKTOP ENVIRONMENT BASED ON GNOME 3 |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manage user directories such as desktops, downloads, etc |

# CONFIGURE __CODESPAN_0_

EDIT __CODESPAN_0_, ADD:

```sh
exec cinnamon-session
```

# CONFIGURE __CODESPAN_0_

EDIT __CODESPAN_0_, ADD:

```sh
proc /proc procfs rw 0 0
```

# Service management

```sh
# service dbus enable 
# service lightdm enable
```

Middle culture

EDIT __CODESPAN_0: FIND __CODESPAN_1 (COLUMN 24) AND CHANGE __CODESPAN_2 TO __ CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```

# Desktop appreciation

[cinnamon on FreeBSD] (..gitbook/assets/cinnamon1.png)

[cinnamon on FreeBSD] (..gitbook/assets/cinnamon2.png)

Wallpapers are black, not something's wrong。

[cinnamon on FreeBSD] (..gitbook/assets/cinnamon3.png)

Custom wallpaper。
