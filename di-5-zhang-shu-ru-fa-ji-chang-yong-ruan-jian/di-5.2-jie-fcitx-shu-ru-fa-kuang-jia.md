# Section 5.2 Fcitx input method framework

The input method framework and the input method themselves are two things that must not be confused and rely on the input method framework. Even on Windows: Windows currently uses [TSF MANAGER] (https://learn.microsoft.com/zh-cn/windows/win32tsf/text-services-framework)。

fcitx is the Penguin input method "A flexible input method method" See [History] (https://fcitx-im.org/wiki/History/zh-cn) for its English-language naming source。

>** Skills**
>
>See video course [006-FreeBSD14.2 Install fcitx5 and its input method] (https://www.bilibili.com/video/BV13ji2YLE3m)


> ** Note**
>
> There may be many unexpected anomalies in FreeBSD-CURRENT bug: fcitx5 diagnostic information is coded in English, the input method shows strange Chinese characters, fcitx5-qt5 environments are not properly loaded..

# Install Fcitx

# # Install Fcitx 4.X

> ** Note**
>
> The tutorial is only tested under KDE 5/csh。

- install with pkg:


```sh
# pkg install zh-fcitx zh-fcitx-configtool fcitx-qt5 fcitx-m17n zh-fcitx-libpinyin
```

- Or install with Ports:

```
# cd /usr/ports/chinese/fcitx/ && make install clean # 输入法框架
# cd /usr/ports/chinese/fcitx-configtool/ && make install clean # 输入法图形化配置工具
# cd /usr/ports/textproc/fcitx-qt5/ && make install clean # 支持 qt5 软件
# cd /usr/ports/textproc/fcitx-m17n/ && make install clean # 多语种支持
# cd /usr/ports/chinese/fcitx-libpinyin/ && make install clean # 拼音输入法
```


# # On-board Fcitx 4.X

```sh
$ mkdir -p ~/.config/autostart/ # 若使用其他用户则需要在其命令行下再执行之
$ cp /usr/local/share/applications/fcitx.desktop ~/.config/autostart/
```

## Install Fcitx 5.X

fcitx 5 has increased support for Wayland and is said to be more fluid than the previous generation。

---|---

- install with pkg:

```sh
# pkg install fcitx5 fcitx5-qt5 fcitx5-qt6 fcitx5-gtk2 fcitx5-gtk3 fcitx5-gtk4 fcitx5-configtool-qt5 fcitx5-configtool-qt6 zh-fcitx5-chinese-addons
```

- Or install with Ports:

```
# cd /usr/ports/textproc/fcitx5/ && make install clean # 主程序
# cd /usr/ports/textproc/fcitx5-qt/ && make install clean  # 同时包含 QT 5 和 QT 6
# cd /usr/ports/textproc/fcitx5-gtk/ && make install clean # 同时包含 gtk 2、3、4
# cd /usr/ports/textproc/fcitx5-configtool/ && make install clean # fcitx5 的图形配置工具。同时包含 QT 5 和 QT 6
# cd /usr/ports/chinese/fcitx5-chinese-addons/ && make install clean # 输入法
```


A test under the SLIM window will prompt IBus to find ... Suspected bug. It could also be a question of configuration。

> ** Skills**
>
> you can also choose to install rime:
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
> rime will not automatically be added to the input method, which needs to be manually added to complete initialization (only if the fcitx configuration tool is found in the program, add the rime input method). This input method does not know where the configuration file is and the interested person can install it. And you always switch to the plethora, even if you choose no, BUG is more, for reasons unknown. Check if your own shell has selected a corresponding tutorial for setting if it is not effective for an ordinary user. Please also add the user to the Wheel group。


# # Open self-start Fcitx 5.X

```sh
$ mkdir -p ~/.config/autostart/ # 若使用其他用户则需要在其命令行下再执行之
$ cp /usr/local/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart/
```


# Configure Fcitx4/5 environment variable

use the desktop manager and shell selected for use:

Sddm lightdm gdm can write A group configuration in __CODESPAN_0_
2. Lightdm gdm can write A group configuration in __CODESPAN_0_
3. sddm can write configurations in user login shell profiles

---|---

-sh: __CODESPAN_0_ Write A group configuration
-bash: __CODESPAN_0 or __CODESPAN_1_for group A configuration
-zsh: __CODESPAN_0_ Write A group configuration
-csh: __CODESPAN_0_ Write B Group Configuration

Note**
>
> if the user account that logs on to the desktop is not root, you cannot set with root identity: you must switch to the user and configure without using sudo。

- Group A (sh/bash/zsh):

```sh
export LANG=zh_CN.UTF-8
export LANGUAGE=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8
export XMODIFIERS='@im=fcitx'
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
```

- Group B (csh)

```sh
setenv LANG zh_CN.UTF-8
setenv LC_ALL zh_CN.UTF-8
setenv LANGUAGE zh_CN.UTF-8
setenv XMODIFIERS @im=fcitx
setenv GTK_IM_MODULE fcitx
setenv QT_IM_MODULE fcitx
```


# Fragmentation and unfinished business

IF YOU HAVE A PROBLEM, RUN __CODESPAN_0_ FAILURE DIAGNOSIS, BUT THE OUTPUT ONLY CONFIGURES __CODESPAN_1_. THIS MEANS THAT HIS OUTPUT OF ENVIRONMENTAL VARIABLES ONLY APPLIES TO SHELLS ___ CODESPAN_2 __, ___ CODESPAN_3 __ AND ___ CODESPAN_4 __, AND NOT __ CODESPAN_5 __. THE ENVIRONMENTAL VARIABLE CONFIGURATION IN __CODESPAN_6 REQUIRES REFERENCE ABOVE。

IF ___CODESPAN_0_ AND IT IS NOT POSSIBLE TO EXPORT DIAGNOSTIC INFORMATION, __CODESPAN_1_:_CODESPAN_2_

#fcitx 4.x

```sh
# fcitx-diagnose
```

For fcitx 4.x, it is normal not to find support __CODESPAN_0_。

#fcitx 5.x

```sh
# fcitx5-diagnose
```

For fcitx 5.x, it is normal not to find support __CODESPAN_0_。

