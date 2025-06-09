# Section 4.18 KDE6

KDE aims to develop a modern desktop system. If you think the KDE interface is like Windows, it's like "Windows are like KDE" in time.

>** Skills**
>
>Video course [003-FreeBSD14.2 Installing KDE6] (https://www.bilibili.com/video/BV12zAeyeKeej)

Note**
>
> Old version upgrade instructions: install new KDE after unmounting.
>
> ````
>pkg remove -f kde5 & pkg autoromove
> ````
>
> or
>
> ````
>pkg remove -f kde6 & pkg autoromove
> ````

Then you can just do the following.

# Install

- Install with pkg:

```sh '
# pkg install xorg sddm kde plasma6-sdm-fonts xdg-user-dirs
````

> ** troubleshooting and unfinished business**
>
> Click [x11/kde] (https://www.freshports.org/x11/kde) to see if the binary package has not been constructed if `pkg ' is sometimes not found or is not available. Sometimes it is necessary to switch to quarterly (to be constructed upstream and then replaced by a latest source, `pkg upgrade ' ) or to a late source. Similar methods apply to all software and are therefore not repeated at the back. If not, the Port above needs to be compiled on its own.


- Or install with Ports:

```sh '
#cd/usr/ports/x11/xorg/ & make install clean
#cd/usr/ports/x11/kde/ & make install clean
#cd /usr/ports/x11/sdm/ & make install clean
#cd /usr/ports/deskutils/plasma6-sdm-kcm/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````

- Explain.

The name of the bag.
|: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
`xorg ' | GUI Foundation, providing X Windows
`sdm ' login manager
`kde ' |K Desktop Environment
The KDE module for the `plasma6-sddm-kcm ' configuration of SDDM can look like parameters in the configuration login interface. Zenium
`wqy-fonts '
`xdg-user-dirs ' |Automable Manager Subdirectories (optional) |


# Start Item Settings

```sh '
# service dbus available # inter-process communication for desktop environment
# service sddm capable # SDDM login manager
````

! [KDE 6 Interface] (..gitbook/assets/kde6-1.png)

# # 'startx' #

```sh '
# "exec ck-launch-session Startplasma-x11" #
````

> If you have already implemented it under root, the new user will still have to do it again to be used properly (no root privileges or sudo etc.) 'startx '.

# Permission Settings

Ordinary users also need to add users to the Wheel group (or `video ' group):

```sh '
# pw groupmod whel-m username
````

# Login interface theme

- Install with pkg:

```sh '
# pkg install sddm-freebsd-black-theme
````

- or install with Ports:

```sh '
#cd/usr/ports/x11-themes/sdm-freebsd-black-theme/
# Make install clean
````


- View installation configuration:

```sh '
Root@ykla:/home/ykla
sddm-freebsd-black-theme-1.3:
On install:
To make this available

/usr/local/etc/sdm.conf
# To enable this theme, please edit the /usr/local/etc/sdm.conf file.

This theye use the x11-fonts/montserrat by default.
Can be changed to any compromised font editing:

/usr/local/share/sddm/themes/sdm-freebsd-black-theme/theme.conf
# Default use of the Montserrat font for this theme (x11-fonts/montserrat to be installed)
# You can edit theme.conf files to any font you want.

Always:
NOTICE:
# Attention:

The sdm-freebsd-black-them port historically does not have a master.
More like to have unsolved issues, not be up-to-date, or even be moved in
To follow this report, please create an issue at:

https://bugs.freebsd.org/bugzilla
# This port currently has no maintainer, so there may be unresolved issues, not timely updates, or even future removal.
# If you want to take over the maintenance, please go to the link and create a problem (issue).

More information about port capacity is available at:

https://docs.freebsd.org/en/articles/contributing/#ports-contributing
# For more information about port maintenance, refer to the section of FreeBSD official document on contribution port.
````

- Edit `/usr/local/etc/sdm.conf ' to read:

```sh '
[Theme]
Current=sdm-freebsd-black-theme
````

Restart, settings complete:

[KDE 6 FreeBSD Theme] (..gitbook/assets/kde-theme.png)

References

- [Ethic Environments and Structures - 4-7. LXQT Quest (LXQT 2.0.1)] (http://silversack.my.coocan.jp/bsd/fbsd11x_bde-4-7_lxqt.htm)

Middle culture

# # SSDDM medium culture

```sh '
# Sysrc sddm_lang #
````

## # cultural method in the system 1 user rating

Edit `/etc/login.conf ' : find `default:\, amend `:lang=C.UTF-8 ' to `:lang=zh_CN.UTF-8 ' .

Refresh database:

```sh '
#cap_mkdb/etc/login.conf
````

[SDDM](./.gitbook/assets/sdmcn.png)

[KDE 6] (..gitbook/assets/kde6-2.png)

## # System cultural method 2 system settings

Click to start - > System Settings - > `Language & Time ' to find "Credit Chinese" (generally the second last, if all are □ □, check your Chinese font installation) click on the `Language ' column in `Region & Language ' to the right. Then click the `Apply ' button; logout (cancellation) and re-entry, when the system language becomes Chinese.

[KDE 6] (..gitbook/assets/kde6-4.png)

[KDE 6] (..gitbook/assets/kde6-5.png)

References

- [SDDM login screen with KDE: change language?] (https://f)orums.freebsd.org/threads/sddm-login-screen-with-kde-change-language.80535)


# Fragmentation and unfinished business

# sddm login #


If you cannot see the bottommost option of sddm when using the VMware virtual machine, use the tutorial to configure the screen automatically.


Start sddm reminder `/usr/bin/xauth: (stdin): 1: bad display name ' but normal `startx '

You need to check if your `hostname ' is empty in `/etc/rc.conf ' (theoretically it should not be empty) and set up:

![..gitbook/assets/errornohostname.png]

Set `hostname 'as required.

# # The menu's missing the switch, restarting the four buttons

If this is not valid, please see if you have chosen `user session ' (read `.xinitrc ' ) in the sddm interface.

Amend `/etc/sysctl.conf ' to replace `security.bsd.see_other_uid ' with `1 ' (`1 ' is open). Restart after that.

References

- [Missing power buttons when logged in from SDDM] (https://forums.freebsd.org/threads/missing-power-buttons-whon-logged-in-fom-sddm.88231/)

# Unlock automatic

Click Set > > Safety and Privacy > Lock Screen > Automatic Lock Screen 's choice " Non-automatic Lock Screen " , and then click Apply. (Lock screen as required after hibernation)

Once written off, re-entry is sufficient.


! [Close KDE 6 Lock] (. .gitbook/assets/ generaling.png)

# # Statusbar does not show clocks and times

Click the time zone settings, enter `beijing ' , set Shanghai. Update the package if it is not valid.
。