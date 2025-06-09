# Section 4.19 The theme beautification

FreeBSD, with its desktop environment, often comes with a simple tone. This unmodified setting may at times be unacceptable to new users. For the sake of system beauty, we will try to add **Themes** and ** Icons** in this section.

Note**
>
>This section covers only the desktop theme of the `GTK ' library and covers desktop environments such as `Gnome ' , `XFCE ' , `MATE ' , `Cinnamon ' and `LXDE ' .

Only some of the icons and themes are listed below and more resources are available for access [FreshPorts] (https://www.freshports.org).

# Theme

-Matcha theme: #pkg install matcha-gtk-themes'
- Qogir theme: #pkg install qogir-gtk-themes
- Pop Theme: #pkg install pop-gtk-themes'
-Flat theme: #pkg install flat-remix-gtk-themes'
- Numix theme: #pkg install Numix-gtk-theme'
- Siera theme: #pkg install sierra-gtk-themes
- Yaru theme: #pkg install yaru-gtk-themes'
- Canta theme: #pkg install canta-gtk-themes'

# Icon

- Papirus icon: `#pkg install papirus-icon-theme'
- Qogir icon: #pkg install qogir-colon-themes '
- Pop icon: #pkg install pop-coon-theme'
- Flat icon: #pkg install flat-remix-icon-themes'
- Numix icon: #pkg install Numix-icon-theme'
- Numix circle icon: '#pkg install Numix-icon-theme-circle '
- Yaru icon: #pkg install yaru-icon-theme'
- Canta icon: #pkg install canta-icon-theme'


# KDE theme beautification

We're going to install the theme [whiteSur] (https://www.pling.com/p/1398840).

1. Downloading of the thematic source package: `git code https://github.com/vinceliuice/whiteSur-kde '
2. Access to the subject package directory: `cd WhiteSur-kde '
3. Amend Shebang: `ee install.sh ' , amend the first act `#!/usr/local/bin/bash ' and save it.
4. Implementation installation: `bash install.sh '

# Gnome theme beautification

We are also going to install [WhiteSur] (https://www.pling.com/p/1403328/).

1. Downloading of the subject source package: `git code https://github.com/vinceliuice/whiteSur-gtk-theme '
2. Access to the subject package directory: `cd WhiteSur-gtk-theme '
3. Amend Shebang: `ee install.sh ' , amend the first act `#!/usr/local/bin/bash ' and save it.
4. Implementation installation: `bash install.sh '

(https://www.pling.com/p/1405756)

Downloading icons: `git clone https://github.com/vinceliuice/whiteSur-icon-theme'
2. Access to the software catalogue: `cd WhiteSur-icon-theme '
3. Amend Shebang: `ee install.sh ' , amend the first act `#!/usr/local/bin/bash ' and save it.
4. Implementation installation: `bash install.sh '

(https://www.pling.com/p/1355701).

1. Download cursor: `git clone https://github.com/vinceliuice/McMojave-cursors '
2. Access to the software catalogue: `cd McMojave-cursors '
3. Amend Shebang: `ee install.sh ' , amend the first act `#!/usr/local/bin/bash ' and save it.
4. Implementation installation: `bash install.sh '

# Background pictures

[Down address] (https://github.com/finance/whiteSur-kde/tree/master/wallpaper)

Thinking

Try to install [Papirus icon] at the terminal as follows (https://www.gnome-look.org/p/1166289/):

```sh '
I'm not sure I'm going to be able to do that, but I'm not sure I'm going to be able to do that.
I'd like to talk to you.
/install.sh
````

# System update hint 'freebsd-update-notify '

>** Skills**
>
KDE6 on >FreeBSD carries a similar feature without the need to install `freebsd-update-notify ' , with examples only.


`freebsd-update-notify ' can automatically detect updated FreeBSD systems and pkg packages.

# # Install `freebsd-update-notify'

```sh '
# pkg install freebsd-update-notify
````

or

```sh '
#cd/usr/ports/deskutils/freebsd-update-notify/
# Make install clean
````

# # Configure 'freebsd-update-notify'

The profile is in `/usr/local/etc/freebsd-update-notify/freebsd-update-notify.conf ':

The default configuration update is too late to be replaced by:

```ini '
max-days-between-updates 1 # Update detection interval (days)
Hours-between-reminders 8# Alarm interval (hours)
````

Picture example


Note**
>
>The screenshot is an example of manual execution, in fact the program can run automatically in the backstage without manual validation. If this cannot be repeated, an attempt can be made to replace both values of `freebsd-update-notify.conf ' with `0 ' and then manually implement `usr/local/libexec/freebsd-update-notify ' .

The log is located in `/var/log/freebsd-update-cron ' , `/var/log/freebsd-update-notify ' . For feedback failures, please submit [issue] in English (https://github.com/outpaddling/freebsd-update-notify/issues).


[freebsd-update-notify on FreeBSD] (./.gitbook/assets/notify1.png)

[freebsd-update-notify on FreeBSD] (./.gitbook/assets/notify1.png)


[freebsd-update-notify on FreeBSD] (..getbook/assets/notify2.png)

[freebsd-update-notify on FreeBSD] (. .getbook/assets/notify3.png)

