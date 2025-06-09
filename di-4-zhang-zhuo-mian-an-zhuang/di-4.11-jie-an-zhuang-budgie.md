# Section 4.11 Budgie

Budgie is the default desktop for Solus Linux.

# Install

- Install with pkg:

```sh '
# Pkg install buggie wq-fonts
````

- Or install with Ports:

```sh '
#cd /usr/ports/x11/budgie & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
````

>** Skills**
>
> will automatically install lightdm.

- Explain:

Name of package Description of role
|: - - - - - - - | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
`budgie ' | Desktop Environment
`wqy-fonts '

# View installation hints

```sh '
root@ykla:/home/ykla #pkginfo-Dbuggie
Budgie-10.8:
On install:
Copy 'xprofile' into your home directory:
cp /usr/local/share/examples/budgie/xprofile~/.xprofile
# Copy the example profile xprofile to your master directory to set the user environment variable for desktop environment startup.

More Information, https://codeberg.org/olivierd/freebsd-ports-budgie/wiki
# More information can be found on the official wiki page.

If you want to launch new session from a console,
cp /usr/local/share/examples/budgie/xinitrc~/.xinitrc
# If you want to start a session directly from the console (without login manager), copy the example xinitrc to the main directory.
````

# Configure 'startx '

```sh '
$cp/usr/local/share/examples/budgie/xprofile~/.xprofile
$cp/usr/local/share/examples/budgie/xinitrc~/.xinitrc
````

# Configure `fstab '

Edit `/etc/fstab ' , add:

```sh '
Proc / proc procfs rw 0 0
````

# Service management

```sh '
# For service dbus able
♪ service lightdm able
````

# Chinese Environment

Under `/etc/rc.conf ' , insert:

```sh '
Lightdm_env=“LC_MSAGES=zh_CN.UTF-8”
````

I don't...

Edit `/etc/login.conf ' : find `default:\, amend `:lang=C.UTF-8 ' to `:lang=zh_CN.UTF-8 ' .

Refresh database:

```sh '
#cap_mkdb/etc/login.conf
````

# Desktop appreciation

[FreeBSD installation Budgie] (./.gitbook/assets/budgie1.png)

[FreeBSD installation Budgie] (./.gitbook/assets/budgie2.png)

The wallpaper is the default. Photo taken from the Gulf of Singapore.

[FreeBSD installation Budgie] (./.gitbook/assets/budgie3.png)

# References

- [Installation] (https://codeberg.org/olivierd/freebsd-ports-butgie/wiki/Installation) This paper is mainly supplemented by this but was tested without the need to configure `05-subsend.rules ' to make it possible to restart.
。