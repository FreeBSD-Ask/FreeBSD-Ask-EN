# SECTION 4.18 KDE6

KDE aims to develop a modern desktop system. If you think the KDE interface is like Windows, it's like "Windows are like KDE" in time。

>** Skills**
>
>Visual course [003-FreeBSD14.2 Install KDE6] (https://www.bilibili.com/video/BV12zAyeKeej)

Note**
>
> OLD VERSION UPGRADE INSTRUCTIONS: INSTALL NEW KDE AFTER UNMOUNTING。
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

Then you can just do the following。

# Install

- install with pkg:

```sh
# pkg install xorg sddm kde plasma6-sddm-kcm wqy-fonts xdg-user-dirs
```

> ** troubleshooting and unfinished business**
>
> Click [x11/kde] (https://www.freshports.org/x11/kde) to see if the binary package is not constructed. Sometimes it is necessary to switch to quarterly (to be constructed upstream and replaced with the latest source, CODESPAN_1_update) or to the last source. Similar methods apply to all software and are therefore not repeated at the back. If not, the Port above needs to be compiled on its own。


- Or install with Ports:

```sh
# cd /usr/ports/x11/xorg/ && make install clean 
# cd /usr/ports/x11/kde/ && make install clean 
# cd /usr/ports/x11/sddm/ && make install clean 
# cd /usr/ports/deskutils/plasma6-sddm-kcm/ && make install clean 
# cd /usr/ports/x11-fonts/wqy/ && make install clean 
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
```

- Explain

| Package Name | Role |
|:----------------------|:------------------------|
| `xorg ' | GUI Foundation, providing X Windows |
| `sddm ' | Login Manager |
| `kde ' | KDE DESKTOP ENVIRONMENT |
| `plasma6-sdm-kcm ' | CONFIGURES THE KDE MODULE FOR SDDM, WHICH CAN LOOK AT PARAMETERS SUCH AS THE CONFIGURATION LOGIN INTERFACE。 |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Automatically manage a subdirectories (optional) |


# Start Item Settings

```sh
# service dbus enable # 用于桌面环境的进程间通信
# service sddm enable # SDDM 登录管理器
```

[KDE 6 INTERFACE] (..gitbook/assets/kde6-1.png)

# CODESPAN_0__

```sh
# echo "exec ck-launch-session startplasma-x11" > ~/.xinitrc
```

> If you have already implemented it under root, the new user will still have to do it again for normal use (no root privileges or sudo etc.) > CODESPAN_0_。

# Permission Settings

Ordinary users also need to add the user to the Wheel group (or `video`group):

```sh
# pw groupmod wheel -m 用户名
```

# Login interface theme

- install with pkg:

```sh
# pkg install sddm-freebsd-black-theme
```

- or install with Ports:

```sh
# cd /usr/ports/x11-themes/sddm-freebsd-black-theme/ 
# make install clean
```


- View installation configuration:

```sh
root@ykla:/home/ykla # pkg info -D sddm-freebsd-black-theme
sddm-freebsd-black-theme-1.3:
On install:
To enable this theme edit:

/usr/local/etc/sdm.conf
# to enable this theme, please edit the /usr/local/etc/sdm.conf file。

This theye use the x11-fonts/montserrat by default
can be changed to any compromised font editing:

/usr/local/share/sddm/themes/sdm-freebsd-black-theme/theme.conf
# default use of the montserrat font for this theme (x11-fonts/montserrat to be installed)
# you can edit theme.conf files to any font you want。

Always:
NOTICE:
# Attention:

The sdm-freebsd-black-them port historically does not have a master
more like to have unsolved issues, not be up-to-date, or even be moved in
to follow this report, please create an issue at:

https://bugs.freebsd.org/bugzilla
# this port currently has no maintainer, so there may be unresolved issues, not timely updates, or even future removal。
# if you want to take over the maintenance, please go to the link and create a problem (issue)。

More information about port capacity is available at:

https://docs.freebsd.org/en/articles/contributing/#ports-contributing
# For more information about port maintenance, refer to the section of FreeBSD official document on contribution port。
````

- EDIT __CODESPAN_0_, WRITE:

```sh
[Theme]
Current=sddm-freebsd-black-theme
```

Restart, settings complete:

[KDE 6 FreeBSD Theme] (..gitbook/assets/kde-theme.png)

References

- [ENVIRONMANT STRUCTURE - 4-7. LXQT QUEST GUY SETTINGS (LXQT 2.0)] (http://silversack.my.jp/bsd/fbsd11x_bde-4-7_lxqt.htm)

Middle culture

# # SSDDM MEDIUM CULTURE

```sh
# sysrc sddm_lang="zh_CN"
```

## # cultural method in the system 1 user rating

EDIT __CODESPAN_0: FIND __CODESPAN_1_, AND MODIFY __CODESPAN_2_ TO __ ___ CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```

[SDDM](./.gitbook/assets/sdmcn.png)

[KDE 6] (..gitbook/assets/kde6-2.png)

## # System cultural method 2 system settings

Click to start - > System Settings - > CODESPAN_0 _ in __CODESPAN_2_... to click on `Modify` to the right (generally second in penultimate, if all __CODESPAN_4_, check if your Chinese font is installed). Then click the __CODESPAN_5_button; logout (cancelled) and re-entry will then become Chinese。

[KDE 6] (..gitbook/assets/kde6-4.png)

[KDE 6] (..gitbook/assets/kde6-5.png)

References

- [SDDM login screen with KDE: change language?] (https://forums.freebsd.org/threads/sdm-login-screen-with-kde-change-language.80535)


# Fragmentation and unfinished business

# sddm login #


If you cannot see the bottommost option of sddm when using the VMware virtual machine, use the tutorial to configure the screen automatically。


## Start sddm alarm_CODESPAN_0_, but `startx`_

YOU NEED TO CHECK IN ___CODESPAN_0 TO SEE IF YOUR __CODESPAN_1_ IS EMPTY (IN THEORY IT SHOULDN'T BE EMPTY) AND WHETHER THERE ARE SETTINGS:

![..gitbook/assets/errornohostname.png]

SET __CODESPAN_0_ON DEMAND。

# # The menu's missing the switch, restarting the four buttons

If this is not valid, please see if you have selected __CODESPAN_0_(read __CODESPAN_1_) in the sddm interface。

AMEND ___CODESPAN_0 TO CHANGE THE VALUE OF __CODESPAN_1 TO __CODESPAN_2 (__CODESPAN_3_ IS OPEN). RESTART AFTER THAT。

References

- [Missing power buttons when logged in from SDDM] (https://forums.freebsd.org/threads/missing-power-buttons-whon-logged-in-fom-sddm.88231/)

# Unlock automatic

Click Set > > Safety and Privacy > Lock Screen > Automatic Lock Screen 's choice " Non-automatic Lock Screen " , and then click Apply. (Lock screen as required after hibernation)

Once written off, re-entry is sufficient。


[CLOSE KDE 6 LONK] (.../.gitbook/assets/supping.png)

# # Statusbar does not show clocks and times

CLICK THE TIME ZONE SETTINGS, ENTER __CODESPAN_0_, AND SET SHANGHAI. UPDATE THE PACKAGE IF IT IS NOT VALID。
