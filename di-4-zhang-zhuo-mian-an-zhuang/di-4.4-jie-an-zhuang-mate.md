# Section 4.4 Mate

Mate developed by GNOME 2 after all。

You may not know mate, Ilex paraguariensis, but you may have heard of "Madeh tea". Many South American players (e.g. Massey) are very interested in this plant-made tea。

# Install

- install with pkg:

```sh
# pkg install mate xorg wqy-fonts lightdm slick-greeter xdg-user-dirs
```

- Or install with Ports:

```sh
# cd /usr/ports/x11/mate/ && make install clean
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/lightdm/ && make install clean 
# cd /usr/ports/x11/slick-greeter/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- Explain


| Package Name | Description of role |
|:--------------------|:--------------------------------------|
| `mate ' | MATE DESKTOP ENVIRONMENT |
| `xorg ' | X Windows |
| `wqy-fonts ' | Chinese fonts |
| `lightdm ' | Show manager and provide a graphical login interface |
| `slick-greenter ' | LightDM beauty login plugin, missing will not enable LightDM to start |
| `xdg-user-dirs ' | Automatically manage a subdirectories (optional) |

# Post-installation start-up service

```sh
# service dbus enable 
# service lightdm enable 
```

#__CODESPAN_0_CONFIG FILE

ADD THE FOLLOWING LINE TO __CODESPAN_0_:

```sh
exec mate-session
```

# Show Chinese Desktop Environment


EDIT __CODESPAN_0: FIND __CODESPAN_1_, AND MODIFY __CODESPAN_2_ TO __ ___ CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```



# Input Method

[FreeBSD Install MATE] (./.gitbook/assets/mate4.png)

the ibus test was successful. please refer to the relevant section of the input method。


# Desktop appreciation

[FreeBSD Install MATE] (..gitbook/assets/cinnamon1.png)

[FreeBSD Install MATE] (./.gitbook/assets/mate2.png)

[FreeBSD Install MATE] (./.gitbook/assets/mate3.png)

# Fragmentation and unfinished business

# # configure slick-greener

CREATE __CODESPAN_0_, WRITE

```ini
[Greeter]
# 设置登录界面的背景图片路径
background=/home/ykla/cat.png

# Whether to draw user-defined background pictures
= false

# SET GTK+ THEME NAME
=Dracula

# Set icon theme name
ion-theme-name=Adwaita

# Whether to show hostname
show-hostname=true

# Set font name and size
font-name=Sans12

# Whether to show virtual keyboard options
show-keyboard = true

# Whether to show power management options (e.g. shut down, restart)
show-power=true

# Whether to show the clock
show-cock=true

# Whether to show exit options
show-quit = true
````

[FreeBSD Install MATE] (..gitbook/assets/mate1.png)

References

- [if you're going to do it, it's time not to read slick-greener.org/threads/lightdm-not-reaking-slick-green-conf.922256]
