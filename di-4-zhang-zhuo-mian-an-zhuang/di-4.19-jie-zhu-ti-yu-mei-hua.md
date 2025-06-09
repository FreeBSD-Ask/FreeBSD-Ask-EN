# Section 4.19 The theme beautification

FreeBSD, with its desktop environment, often comes with a simple tone. This unmodified setting may at times be unacceptable to new users. For the sake of system beauty, we will try to add **Themes** and ** Icons** in this section。

Note**
>
>THIS SECTION DEALS ONLY WITH THE DESKTOP THEME OF THE __CODESPAN_0_ LIBRARY AND COVERS THE DESKTOP ENVIRONMENT OF __CODESPAN_1, __CODESPAN_2_, _CODESPAN_3_, _CODESPAN_4_ AND _CODESPAN_5_。

Only some of the icons and themes are listed below and more resources are available for access [FreshPorts] (https://www.freshports.org)。

# Theme

-Matcha Theme: _CODESPAN_0_
- Qogir theme: __CODESPAN_0_
- Pop Theme: ___CODESPAN_0_
-Flat Theme: ___CODESPAN_0_
- Numix Theme: __CODESPAN_0_
- Sierra Theme: CODESPAN_0_
- Yaru Theme: __CODESPAN_0_
- Canta theme: CODESPAN_0_

# Icon

-Papirus Icon: __CODESPAN_0_
- Qogir icon: __CODESPAN_0_
- Pop Icon: __CODESPAN_0_
- Plat icon: __CODESPAN_0_
- Numix Icon: __CODESPAN_0_
- Numix Circle Icon: __CODESPAN_0_
- Yaru icon: __CODESPAN_0_
- Canta Icon: __CODESPAN_0_


# KDE THEME BEAUTIFICATION

We're going to install the theme [whiteSur] (https://www.pling.com/p/1398840)。

DOWNLOADING THE SUBJECT SOURCE PACKAGE: __CODESPAN_0_
2. ACCESS TO THE SUBJECT PACKAGE DIRECTORY: __CODESPAN_0_
3. Modify shebang: ___ CODESPAN_0_, modify the first act_CODESPAN_1___ and save it。
4. IMPLEMENTATION INSTALLATION: __CODESPAN_0_

# Gnome theme beautification

We are also going to install [WhiteSur] (https://www.pling.com/p/1403328/)。

DOWNLOADING THE SUBJECT SOURCE PACKAGE: __CODESPAN_0_
2. ACCESS TO THE SUBJECT PACKAGE DIRECTORY: __CODESPAN_0_
3. Modify shebang: ___ CODESPAN_0_, modify the first act_CODESPAN_1___ and save it。
4. IMPLEMENTATION INSTALLATION: __CODESPAN_0_

# [Icon] (https://www.pling.com/p/1405756)

DOWNLOAD ICON: __CODESPAN_0_
ACCESS TO SOFTWARE CATALOGUE: __CODESPAN_0_
3. Modify shebang: ___ CODESPAN_0_, modify the first act_CODESPAN_1___ and save it。
4. IMPLEMENTATION INSTALLATION: __CODESPAN_0_

# [Cursor] (https://www.pling.com/p/1355701)

DOWNLOAD CURSOR: __CODESPAN_0_
ACCESS TO SOFTWARE CATALOGUE: __CODESPAN_0_
3. Modify shebang: ___ CODESPAN_0_, modify the first act_CODESPAN_1___ and save it。
4. IMPLEMENTATION INSTALLATION: __CODESPAN_0_

# Background pictures

[Download Address] (https://github.com/vinceliuice/whiteSur-kde/tree/master/wallpaper)

Thinking

Try to install at the terminal as follows (https://www.gnome-look.org/p/1166289/):

```sh
git clone https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
cd papirus-icon-theme
./install.sh
```

# SYSTEM UPDATE HINT __CODESPAN_0_

>** Skills**
>
KDE6 on >FreeBSD has a similar feature and does not need to be installed with __CODESPAN_0_, and this course is only illustrative。


__CODESPAN_0_ can automatically detect updated FreeBSD systems and pkg packages。

# # INSTALL __CODESPAN_0_

```sh
# pkg install freebsd-update-notify
```

or

```sh
# cd /usr/ports/deskutils/freebsd-update-notify/
# make install clean
```

## CONFIGURE __CODESPAN_0_

PROFILE AT __CODESPAN_0_:

The default configuration update is too late to be replaced by:

```ini
max-days-between-updates    1   # 更新检测间隔（日）      
hours-between-reminders     8   # 提醒间隔（小时）
```

Picture example


Note**
>
>THE SCREENSHOT IS AN EXAMPLE OF MANUAL EXECUTION, IN FACT THE PROGRAM CAN RUN AUTOMATICALLY IN THE BACKSTAGE WITHOUT MANUAL VALIDATION. IF THIS CANNOT BE REPEATED, YOU CAN TRY TO CHANGE BOTH VALUES OF ___CODESPAN_0 TO __CODESPAN_1 AND THEN MANUALLY EXECUTE `root` WITH THE PERMISSION OF __CODESPAN_3_。

The log is located at __CODESPAN_0, __CODESPAN_1_. For feedback failures, please submit [miss] in English (https://github.com/outpaddling/freebsd-update-notify/issues)。


[freebsd-update-notify on FreeBSD] (./.gitbook/assets/notify1.png)

[freebsd-update-notify on FreeBSD] (./.gitbook/assets/notify1.png)


[freebsd-update-notify on FreeBSD] (..getbook/assets/notify2.png)

[freebsd-update-notify on FreeBSD] (. .getbook/assets/notify3.png)

