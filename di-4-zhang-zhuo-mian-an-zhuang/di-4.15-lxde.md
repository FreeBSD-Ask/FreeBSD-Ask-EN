# SECTION 4.15 LXDE

# Install

- install with pkg:

```sh
# pkg install lxde-meta xorg lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```


- Or install with Ports:

```sh
# cd /usr/ports/x11/lxde-meta/ && make install clean 
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/lightdm/ && make install clean 
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```


- Explain:


| Package Name | Description of role |
|:--------------------------|:-------------------------------------------|
| `xorg ' | X Windows |
| `lxde-meta ' | PACKAGE FOR LXDE DESKTOP ENVIRONMENT |
| `lightdm ' | Lightweight Display Manager LightDM |
| `lightdm-gtk-greenter ' | LightDM 's GTK+ login interface plugin, missing will not be able to login LightDM |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manage user directories such as desktops, downloads, etc |


# CODESPAN_0__

EDIT __CODESPAN_0_, ADD:

```sh
exec startlxde
```

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

EDIT __CODESPAN_0: FIND __CODESPAN_1_, AND MODIFY __CODESPAN_2_ TO __ ___ CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```

# Desktop appreciation

./.gitbook/assets/lxde1.png

[..gitbook/assets/lxde2.png]

../.gitbook/assets/lxde3.png

# References

(https://wiki.freebsd.org/LXDE)
