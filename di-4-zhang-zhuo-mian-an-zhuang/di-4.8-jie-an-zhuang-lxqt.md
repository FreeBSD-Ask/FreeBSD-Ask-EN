# Section 4.8 LXQt

# Install LXQt

- install by pkg

```sh
# pkg install xorg sddm lxqt gvfs wqy-fonts xdg-user-dirs
```

- Or install with Ports:

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11-wm/lxqt/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/sddm/ && make install clean
# cd /usr/ports/devel/gvfs/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

Explanation:

| Package Name | Description of role |
|:--------------------|:--------------------------------------------------------------------------|
| `xorg ' | X Windows |
| `sddm ' | Login Manager |
| `lxqt ' | LXQt's preferred display manager |
| `gvfs ' | GNOME Virtual Filesystem, LXQt relies on this to open Computer and Network, otherwise hinting 'Operation not supported ' |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manage user directories, such as desktops, downloads, etc., and process localization of directory names |


# Service management


```sh
# service dbus enable
# service sddm enable
```

# CODESPAN_0__

EDIT __CODESPAN_0_, ADD:

```sh
proc	/proc	procfs	rw	0	0
```

# Start LXQt by startx

```sh
$ echo "exec ck-launch-session startlxqt" > ~/.xinitrc
```

Use who logs in and write in。

# Set the Chinese display

MIDDLE CULTURE SDDM

```sh
# sysrc sddm_lang="zh_CN"
```

[FreeBSD integration LXQt]

[FreeBSD integration LXQt] (..gitbook/assets/lxqt2.png)

[FreeBSD integration LXQt] (..gitbook/assets/lxqt3.png)

Medium Cultural Desktop

After LXQt menu - > "Preferences" - > "LXQt Settings" - > "Locale" - > "Region"

../.gitbook/assets/lxqt4.png

[FreeBSD integration LXQt] (..gitbook/assets/lxqt5.png)

# Fragmentation and unfinished business

- Desktop icons are not shown

Please install other icons you like in advance. And then: menu - > "Preferences" - > "LXQt Settings" - > "Appearance" - > "Icons Theme" selects the icon you installed - > > "Apply" and re-entry after。

