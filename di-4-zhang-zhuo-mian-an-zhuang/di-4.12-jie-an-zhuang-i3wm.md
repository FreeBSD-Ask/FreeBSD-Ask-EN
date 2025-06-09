# section 4.12 i3wm

# install i3wm

- install with pkg:

```sh
# pkg install xorg i3 i3status dmenu i3lock
```

- Or use Ports:

```
# cd /usr/ports/x11/xorg/
# make install clean
```

- Explain:

| Package Name | Description of role |
|:------------|:--------------------------------------------------|
| `xorg ' | X Windows |
| `i3 ' | Lightweight smooth window manager |
| `i3status ' | Status Bar |
| `dmenu ' | Dynamic Menu Generator |
| `i3lock ' | Lock Screen Tool |


# CONFIGURE __CODESPAN_0_

```sh
$ echo "/usr/local/bin/i3" > ~/.xinitrc
```

USE WHICH USER LOGS IN TO EDIT。

# start i3

I can start i3 with __CODESPAN_0。

the image below is pure i3, no plugin

[i'm three on freebsd]


# Virtual machine extension

If you use the VirtualBox, the VirtualBox extension is enabled below:

```sh
& echo "exec VBoxClient-all" >> ~/.config/i3/config
```

# References

- [i3 use manual] (https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html)
- [Setting i3wm on FreeBSD]
- [How to set FreeBSD with a rich desktop-part 3-i3] (https://unixsheikh.com/tutorias/how-to-setup-freebsd-with-a-riced-desktop-part-3-i3.html#xterm)
- [How to install i3?] (https://forums.freebsd.org/threads/how-to-install-i3.62305)
- [i'm not sure i'm gonna be able to do that] (https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html)
