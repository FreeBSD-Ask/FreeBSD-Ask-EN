# Section 5.6 Q (Linux version)


# Based on RockyLinux (FreeBSD Port)

Note**
>
>Please first install RockyLinux Compatibility (FreeBSD Port) with reference to other chapters of the book

# # install rpm tools

- install with pkg

```sh
# pkg install rpm4
```

- Or install with Ports:

```sh
# cd /usr/ports/archivers/rpm4/ 
# make install clean
```

# # DOWNLOAD INSTALLATION QQQQQ

- Download Q, official link: [QQ Linux Evaluation - Easy to be yourself] (https://im.qq.com/linuxqq/index.shtml)

```sh
# fetch https://dldir1.qq.com/qqfile/qq/QQNT/Linux/QQ_3.2.17_250521_x86_64_01.rpm # 写作本文时链接如此，请自行获取最新链接
```

- INSTALL QQ:

```sh
root@ykla:/ # cd /compat/linux/
root@ykla:/compat/linux # rpm2cpio < /home/ykla/QQ_3.2.17_250521_x86_64_01.rpm | cpio -id # 注意把 QQ 所在路径改成你自己的
./usr/share/icons/hicolor/512x512/apps/qq.png: Cannot extract through symlink usr/share/icons/hicolor/512x512/apps/qq.png
1055863 blocks
```

# Solve the dependency library #

- View dependency:

```sh
# /compat/linux/usr/bin/bash # 切换到兼容层的 shell
bash-5.1# ldd /opt/QQ/qq 
	linux-vdso.so.1 (0x00007fffffffe000)
	libffmpeg.so => /opt/QQ/libffmpeg.so (0x000000080c000000)
	....省略一部分...
```

YOU CAN SEE THAT __CODESPAN_0_ IS NORMAL AND DOES NOT NEED TO SOLVE THE PROBLEM OF DEPENDENCY。

## Solve the problem of fcitx Chinese input method not available in QQQ

- INSTALLATION OF __CODESPAN_0_ AND __CODESPAN_1_ IN A COMPATIBLE LAYER, AFTER DOWNLOADING:

```
# fetch https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/i/ibus-gtk3-1.5.25-6.el9.x86_64.rpm
# fetch https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/i/ibus-libs-1.5.25-6.el9.x86_64.rpm
# cd /compat/linux 
# rpm2cpio < /home/ykla/ibus-gtk3-1.5.25-6.el9.x86_64.rpm | cpio -id
# rpm2cpio < /home/ykla/ibus-libs-1.5.25-6.el9.x86_64.rpm | cpio -id
```

- Next:

```sh
root@ykla:/compat/linux #  /compat/linux/usr/bin/bash # 切换到 Rockylinux 的 bash
bash-5.1# gtk-query-immodules-3.0-64 --update-cache   # 刷新缓存
```


# START QQQQQ

```sh
$ /compat/linux/opt/QQ/qq --no-sandbox  --in-process-gpu
```

[FreeBSDQ] (.. . . . .gitbook/assets/rlqq.png)

fcitx5 input method normal:

[FreeBSDQ] (..gitbook/assets/rlqq2.png)

Based on ArchLinux Compatibility Layer

Please see the ArchLinux compatibility segment of the Linux compatibility layer。

```sh
# 自行将脚本创建为 arch.sh，请参看兼容层相关章节。
# sh arch.sh #运行脚本
# chroot /compat/arch/ /bin/bash #进入 Arch 兼容层
# passwd #为 Arch 的 root 设置一个密码
# passwd test #为 Arch 的 test 设置一个密码，上述脚本已经创建过该用户了！不设置密码无法正常使用 aur。

```

Start a new terminal and enter __CODESPAN_0_ to restart FreeBSD, otherwise the password set may not be recognized。

```sh
# chroot /compat/arch/ /bin/bash #进入 Arch 兼容层
# su test # 此时位于 Arch 兼容层！切换到普通用户才能使用 aur
$ yay -S linuxqq # 此时位于 Arch 兼容层！此时用户为 test
# exit # 此时位于 Arch 兼容层！此时用户恢复为 root
```

```sh
# export LANG=zh_CN.UTF-8 # 此时位于 Arch 兼容层！
# export LC_ALL=zh_CN.UTF-8 # 此时位于 Arch 兼容层！如果不添加环境变量，则中文输入法无法使用。如果设置失败请重启一次 FreeBSD 主机。此时位于 Arch 兼容层！
# /opt/QQ/qq --no-sandbox --in-process-gpu  # 此时位于 Arch 兼容层！
```

# Based on Ubuntu Compatibility Layer

Please install the Ubuntu compatibility layer first。

```sh
# chroot /compat/ubuntu/ /bin/bash #进入 Ubuntu 兼容层
# wget https://dldir1.qq.com/qqfile/qq/QQNT/ad5b5393/linuxqq_3.1.2-13107_amd64.deb #此时位于 Ubuntu 兼容层
```

```sh
# apt install ./linuxqq_3.1.0-9572_amd64.deb  #此时位于 Ubuntu 兼容层
```

Install dependent files and fonts:

```sh
# apt install libgbm-dev libasound2-dev #此时位于 Ubuntu 兼容层
# ldconfig #此时位于 Ubuntu 兼容层
```

install chinese fonts: find chinese fonts with a package manager, e.g. wqy

START QQQ:

```sh
# export LANG=zh_CN.UTF-8 # 此时位于 Ubuntu 兼容层
# export LC_ALL=zh_CN.UTF-8 # 如果不添加则中文输入法无法使用。此时位于 Ubuntu 兼容层
# /bin/qq --no-sandbox --in-process-gpu #此时位于 Ubuntu 兼容层
```

> ** Note**
>
> IF YOU HAVE A DOUBLE-NET CARD, SUCH AS A WIRE, OPEN A WIRELESS QQQ Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q  Q Q Q Q Q Q Q Q Q Q Q Q Q  Q  Q Q Q Q Q Q Q Q Q Q Q Q Q    Q  Q  Q  Q  Q  Q  Q Q   Q  Q   Q    Q  Q      Q   Q    Q                          。
>
> See Linux Compatibility Malfunction and Unfinished
>
> IF YOU DO NOT GO AFTER EXIT, ADD THE PARAMETER __CODESPAN_0_, I. E. __CODESPAN_1_。

[FreeBSDQ] (..gitbook/assets/qq3.0.png)

# It's broken

# QQUICK

Within compatibility:

```sh
$ rm ~/.config/QQ/crash_files/*
$ chmod a-wx ~/.config/QQ/crash_files/
```

References

- [Linux new QBug & Fix] (https://zhuanlan.zhihu.com/p/645895811)
