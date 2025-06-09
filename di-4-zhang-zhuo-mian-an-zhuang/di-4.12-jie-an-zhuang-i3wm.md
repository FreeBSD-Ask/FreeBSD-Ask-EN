# Section 4.12 i3wm

# Install i3wm

- Install with pkg:

```sh '
# pkg install xi3 i3status dmenu i3lock
````

- Or use Ports:

````
#cd/usr/ports/x11/xorg/
# Make install clean
````

- Explain:

Name of package Description of role
|: - - | | | | |
`xorg 'X Windows
`i3 ' | Lightweight flat window manager
`i3status ' Status Bar
|dmenu ' | Dynamic Menu Generator
`i3lock ' | lock screen tool


# Configure 'startx '

```sh '
$eho "/usr/local/bin/i3" > ~/.xinitrc
````

Use which user logs in to edit.

# Start i3

I3 can be started with `startx '.

The image below is pure i3, no plugin!

[i3 on freebsd] (..gitbook/assets/i3wm_preview.png)


# Virtual machine extension

If you use the VirtualBox, the VirtualBox extension is enabled below:

```sh '
~.config/i3/config
````

# References

- [i3 Usage manual] (https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html)
- [Installing i3wm on FreeBSD]
- [How to setup FreeBSD with a riced desktop - part 3 - i3] (https://unixsheikh.com/tutorias/how-to-setup-freebsd-with-a-riced-desktop-part-3-i3.html#xterm)
- [How to install i3?] (https://forums.freebsd.org/threads/how-to-install-i3.62305)
- [i3 - an improved dynamic, tinging window manager] (https://www.freebsd.org/cgi/man.cgi?query=i3&apropos=0&sektion=1&manpath=freebsd-ports&format=html)
