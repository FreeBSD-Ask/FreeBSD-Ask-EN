# Section 5.2 Fcitx input method framework

The input method framework and the input method themselves are two things that must not be confused and rely on the input method framework. Even on Windows: Windows currently uses [TSF manager] (https://learn.microsoft.com/zh-cn/windows/win32tsf/text-services-framework).

fcitx is the Penguin input method "A flexible input method method" For its English-language naming source, see [Historical] (https://fcitx-im.org/wiki/History/zh-cn).

>** Skills**
>
>Video presentation [006-FreeBSD14.2 Install fcitx5 and its input method] (https://www.bilibili.com/video/BV13ji2YLE3m)


> ** Note**
>
> There may be many unexpected anomalies in FreeBSD-CURRENT bug: fcitx5 diagnostic information is coded in English, the input method shows strange Chinese characters, fcitx5-qt5 environments are not properly loaded...

# Install Fcitx

# # Install Fcitx 4.X

> ** Note**
>
> The tutorial is only tested under KDE 5/csh.

- Install with pkg:


```sh '
#pkg installzh-fcitx zh-fcitx-configtool fcitx-qt5 fcitx-m17nzh-fcitx-libpiniin
````

- Or install with Ports:

````
# cd /usr/ports/chinese/fcitx/ & make install clean #
#cd /usr/ports/chinese/fcitx-configtool/ & make input
# cd /usr/ports/textproc/fcitx-qt5/ & make effective clean # qt5
#cd /usr/ports/textproc/fcitx-m17n/ & make effective clean
# cd /usr/ports/chinese/fcitx-libpnyin/ & make install clean #
````


# # On-board Fcitx 4.X

```sh '
$ mkdir-p ~/.config/autostart/ # If you use other users, you need to execute it under its command
$cp /usr/local/share/applications/fcitx.desktop ~/.config/autostart/
````

## Install Fcitx 5.X

fcitx 5 has increased support for Wayland and is said to be more fluid than the previous generation.

I don't...

- Install with pkg:

```sh '
#pkg install fcitx5 fcitx5-qt5 fcitx5-qtx5-gtk2 fcitx5-gtk3 fcitx5-gtk4 fcitx5-configtool-qt5 fcitx5-qt6 zh-fcitx5chinese-addons
````

- Or install with Ports:

````
# cd /usr/ports/textproc/fcitx5/ & make install clean # master
# cd /usr/ports/textproc/fcitx5-qt/ & make install clean
#cd /usr/ports/textproc/fcitx5-gtk/ & make install clean #gtk 2, 3, 4
Graphical configuration tool for #cd /usr/ports/textproc/fcitx5-configtool/ & make install clean #fcitx5 Include both QT 5 and QT 6
# cd/usr/ports/chinese/fcitx5-chinese-addons/ & make install clean# input method
````


A test under the SLIM window will prompt IBus to find ... Suspected bug. It could also be a question of configuration.

> ** Skills**
>
> You can also choose to install rime:
>
> ````
>pkg install zh-fcitx5-rime zh-rime-essay
> ````
>
> or:
>
> ````
>cd /usr/ports/chinese/fcitx5-rime/ & make install clean
>cd /usr/ports/chinese/rime-essay/ & make install clean
> ````
>
> rime will not automatically be added to the input method, which needs to be manually added to complete initialization (only if the fcitx configuration tool is found in the program, add the rime input method). This input method does not know where the configuration file is and the interested person can install it. And you always switch to the plethora, even if you choose no, BUG is more, for reasons unknown. Check if your own shell has selected a corresponding tutorial for setting if it is not effective for an ordinary user. Please also add the user to the Wheel group.


# # Open self-start Fcitx 5.X

```sh '
$ mkdir-p ~/.config/autostart/ # If you use other users, you need to execute it under its command
$cp /usr/local/share/applications/org.fcitx.Fcitx5desktop ~/.config/autistart/
````


# Configure Fcitx4/5 environment variable

Use the desktop manager and shell selected for use:

1. Sddm lightdm gdm can all write A group configuration in '~/.xfile '
2. Lightdm gdm can write A group configuration in ~/.profile '
3. Sddm can write configurations in user login shell profiles

I don't...

-sh: ~/.profile 'writing group A configuration
-bash: ~/.bash_profile ` or ~/.profile ' for group A configuration
-zsh: ~/.zprofile 'writing group A configuration
-csh: ~/.cshrc 'for group B configuration

Note**
>
> If the user account that logs on to the desktop is not root, you cannot set with root identity: you must switch to the user and configure without using sudo.

- Group A (sh/bash/zsh):

```sh '
Export LANG=zh_CN.UTF-8
Export LANGUAGE=zh_CN.UTF-8
LC_ALL=zh_CN.UTF-8
=m=fcitx'
I'm sorry.
QT_IM_MODULE=fcitx
````

- Group B (csh)

```sh '
Setenv LANG zh_CN.UTF-8
LC_ALL zh_CN.UTF-8
Setenv LANGUAGE zh_CN.UTF-8
@im=fcitx
Setenv GTK_IM_MODULE fcitx
Setenv QT_IM_MODULE fcitx
````


# Fragmentation and unfinished business

In case of problems, run the `fcitx ' failure diagnosis, but the output only configures the environmental variables for `bash '. This means that his output of environmental variables applies only to SHELLs such as `bash ' , `sh ' and `zsh ' and not to `csh ' . The environment variable configuration in `csh ' needs reference above.

If the `bash ' words are hinted and it is not possible to output the diagnostic information, the `bash ': #pkg install rash ' needs to be installed first

#fcitx 4.x

```sh '
#fcitx-diagnose
````

For fcitx 4.x, it is normal to find no support for `GTK 4 ' .

#fcitx 5.x

```sh '
#fcitx5-diagnose
````

For fcitx 5.x, it is normal to find no support for `fcitx qt 4 ' .

。