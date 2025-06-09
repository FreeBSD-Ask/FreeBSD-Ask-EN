# Section 5.6 Q (Linux version)


# Based on RockyLinux (FreeBSD Port)

Note**
>
>Please first install RockyLinux Compatibility (FreeBSD Port) with reference to other chapters of the book

# # Install rpm tools

- Install with pkg

```sh '
# pkg install rpm4
````

- Or install with Ports:

```sh '
#cd/usr/ports/archivers/rpm4/
# Make install clean
````

# # Download installation QQQQQ

- Download QQ, official link: [QQ Linux Edition - Easy to be yourself] (https://im.qq.com/linuxqq/index.shtml)

```sh '
#fetch https://dldir1.qq.com/qqfile/qq/QQNT/Linux/Q_3.2.17_250521_x86_64_01.rpm#
````

- Install QQ:

```sh '
Root@ykla: #cd /compat/linux/
Root@ykla:/compat/linux #rpm2cpio < /home/ykla/Q_3.2.17_250521_x86_01.rpm | cpio-id # Pay attention to changing the QQQ path to your own
./usr/share/icons/hicolor/512x512/apps/qq.png: Cannot except through symlink Usr/share/icons/hicolor/512x512/apps/qq.png
1055863 blocks
````

# Solve the dependency library #

- View dependency:

```sh '
# /compat/linux/usr/bin/bash
bash-51.1#ldd /opt/QQ/qq
linux-vdso.so.1.
(0x00000000080000)
..and omit some...
````

As can be seen, `ldd ' is normal and does not need to address the issue of dependency.

## Solve the problem of fcitx Chinese input method not available in QQQ

- Installation of `ibus-gtk3 ' and `ibus-libs ' in the compatibility layer, after downloading:

````
#fetch https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/i/bus-gtk3-1.5.25-6.el9.x86_64.rpm
#fetch https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/Packages/i/bus-libs-1.5.25-6.el9.x86_64.rpm
# cd /compat/linux
#rpm2cpio < /home/ykla/bus-gtk3-1.5.25-6.el9.x86_64.rpm |cpio-id
#rpm2cpio < /home/ykla/bus-libs-1.5.25-6.el9.x86_64.rpm|cpio-id
````

- Next:

```sh '
Root@ykla:/compat/linux#/compat/linux/usr/bin/bash# Switch to Rockylinux
bash-51.1#gtk-query-immodules-3.0-64 --update-cache# Refresh Cache
````


# Start QQQQQ

```sh '
$ /compat/linux/opt/Q/qq-no-sandbox-in-process-gpu
````

[FreeBSD Q] (..gitbook/assets/rlqq.png)

fcitx5 input method normal:

[FreeBSD Q] (..gitbook/assets/rlqq2.png)

Based on ArchLinux Compatibility Layer

Please see the ArchLinux compatibility segment of the Linux compatibility layer.

```sh '
# Create your own script as aarch.sh, see the relevant section on compatibility.
# sharch.sh # run the script
# chorot /compat/arch// bin/bash # enter Arch Compatible Layer
# Passwd # sets a password for the root of Arch
# passwd test # sets a password for Arch's test, the script has been created! The password cannot be used properly without setting.

````

Start a new terminal and enter `reboot ' to restart FreeBSD, otherwise the password set may not be recognized.

```sh '
# chorot /compat/arch// bin/bash # enter Arch Compatible Layer
It's in Arch Compatibility! Switch to normal user to use aur
That's right. At this time the user is test
This is Arch Compatible! Restore user to root
````

```sh '
# export LANG=zh_CN.UTF-8 # at this time in Arch Compatible Layer!
# export LC_ALL=zh_CN.UTF-8 # at this time in Arch Compatible Layer! If the environment variable is not added, the Chinese input method is not available. Restart FreeBSD host once if settings fail. It's on Arch Compatible!
# /opt/QQ/qq-no-sandbox-in-process-gpu # at this time in Arch Compatibility Layer!
````

# Based on Ubuntu Compatibility Layer

Please install the Ubuntu compatibility layer first.

```sh '
#choot /compat/ubuntu//bin/bash #into Ubuntu Compatible
#wget https://dldir1.qq.com/qqfile/qq/QNT/ad5b5393/linuxq_3.1.2-13107_amd64.deb# At this time in Ubuntu Compatible Layer
````

```sh '
#apt install./linuxq_3.1.1.0-9572_amd64.deb #at this time in Ubuntu Compatible
````

Install dependent files and fonts:

```sh '
#apt install libgbm-dev libasund2-dev #
# ldconfig # at this time in Ubuntu Compatible Layer
````

Install Chinese fonts: Find Chinese fonts with a package manager, e.g. wqy

Start QQQ:

```sh '
# export LANG=zh_CN.UTF-8 # at this time in Ubuntu Compatible Layer
#export LC_ALL=zh_CN.UTF-8 # At this time in Ubuntu Compatible Layer
# /bin/qq-no-sandbox-in-process-gpu # at this time in Ubuntu Compatibility
````

> ** Note**
>
> If you have a double-net card, such as a wire, open a wireless QQQ Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q Q  Q Q Q Q Q Q Q Q Q Q Q Q Q  Q  Q Q Q Q Q Q Q Q Q Q Q Q Q    Q  Q  Q  Q  Q  Q  Q Q   Q  Q   Q    Q  Q      Q   Q    Q                          
>
> See Linux Compatibility Malfunction and Unfinished
>
> If you do not go after exit, add the parameter `-in-process-gpu ' , i.e. `/bin/qq-no-sandbox-in-process-gpu ' .

[FreeBSD Q](. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

# It's broken

# QQuick

Within compatibility:

```sh '
$ rm ~/.config/Q/crash_files/*
$chmod a-wx ~/.config/Q/crash_files/
````

References

- [Linux] New QQ Bug & Fix (repeal related)] (https://zhuanlan.zhihu.com/p/645895811)
