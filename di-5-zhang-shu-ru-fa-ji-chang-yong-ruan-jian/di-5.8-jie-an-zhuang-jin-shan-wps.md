# Section 5.8 Kinshan WPS (Linux version)

>** Warning**
>
>Do not use the Golden Hill WGS in the ports, as no update is available. It is recommended that the compatible layer be installed。

# Based on RockyLinux Compatibility (FreeBSD Port)

Note**
>
>Please first install RockyLinux Compatibility (FreeBSD Port) with reference to other chapters of the book

# # install rpm tools

```sh
# pkg install rpm4
```

Or:

```
# cd /usr/ports/archivers/rpm4/ 
# make install clean
```

# DOWNLOAD GOLD MOUNTAIN WFS

Official address: [WPS Office for Linux] (https://linux.wps.cn/)


<https://wps-linux-person.wpscdn.cn/wps/download/ep/Linux2023/1790/wps-office-12.01.1790-1.x86_64.rpm?t=1731150867&k=8e9446b92a6e5b727047ec25707be78>

Please find a valid link. I use the browser to download it。

>** Remarks**
>
There's a problem with this link, and I don't know how to use a Fetch download, or a wget. If you know how to solve this, please submit PR or issue。

# # INSTALLING GOLDEN MOUNTAIN WFS

```sh
root@ykla:/ # cd /compat/linux/
root@ykla:/compat/linux #  rpm2cpio < /home/ykla/Downloads/wps-office-12.1.0.17900-1.x86_64.rpm  | cpio -id  # 注意路径要换成你自己的
```


# Solve dependency #

View dependency:

```bash
root@ykla:/compat/linux # /compat/linux/usr/bin/bash # 切换到兼容层的 shell
bash-5.1# ldd /opt/kingsoft/wps-office/office6/wps
	linux-vdso.so.1 (0x00007fffffffe000)
	libdl.so.2 => /lib64/libdl.so.2 (0x000000080105c000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x0000000801061000)
	libtcmalloc_minimal.so.4 => /opt/kingsoft/wps-office/office6/libtcmalloc_minimal.so.4 (0x0000000801600000)
	liblibsafec.so => /opt/kingsoft/wps-office/office6/liblibsafec.so (0x0000000801066000)
	libstdc++.so.6 => /opt/kingsoft/wps-office/office6/libstdc++.so.6 (0x0000000801a00000)
	libm.so.6 => /lib64/libm.so.6 (0x0000000801083000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x000000080115e000)
	libc.so.6 => /lib64/libc.so.6 (0x0000000801e00000)
	/lib64/ld-linux-x86-64.so.2 (0x0000000001021000)
	librt.so.1 => /lib64/librt.so.1 (0x0000000801179000)
```

You can see, rely on it all。

# RUN THE GOLDEN MOUNTAIN WFS #


```bash
ykla@ykla:~ $ /compat/linux//opt/kingsoft/wps-office/office6/wps
```


[FreeBSD WFS] (..gitbook/assets/wps1.png)

The input method is normal。

[FreeBSD WPS] (..gitbook/assets/wps2.png)

Based on ArchLinux Compatibility Layer

```sh
# fetch http://book.bsdcn.org/arch.sh #下载脚本构建兼容层
# sh arch.sh #运行脚本
# chroot /compat/arch/ /bin/bash #进入 Arch 兼容层
# passwd #为 Arch 的 root 设置一个密码
# passwd test #为 Arch 的 test 设置一个密码，脚本已经创建过该用户了！
```

Start a new terminal and enter __CODESPAN_0_ to restart FreeBSD, otherwise the password set may not be recognized。

```sh
# chroot /compat/arch/ /bin/bash #进入 Arch 兼容层
# su test # 此时位于 Arch 兼容层！切换到普通用户才能使用 aur
```

Start installation:

```sh
$ yay -S wps-office-cn ttf-wps-fonts wps-office-mui-zh-cn # 此时位于 Arch 兼容层！此时用户为 test
AUR Explicit (2): wps-office-cn-11.1.0.11698-1, ttf-wps-fonts-1.0-5
:: (1/1) Downloaded PKGBUILD: ttf-wps-fonts
  2 wps-office-cn                            (Build Files Exist)
  1 ttf-wps-fonts                            (Build Files Exist)
==> Packages to cleanBuild?
==> [N]one [A]ll [Ab]ort [I]nstalled [No]tInstalled or (1 2 3, 1-3, ^4)
==> 1  #这里输入 1 回车
:: Deleting (1/1): /home/test/.cache/yay/ttf-wps-fonts
HEAD is now at ba3222c Add upstream URL
  2 wps-office-cn                            (Build Files Exist)
  1 ttf-wps-fonts                            (Build Files Exist)
==> Diffs to show?
==> [N]one [A]ll [Ab]ort [I]nstalled [No]tInstalled or (1 2 3, 1-3, ^4)
==> 1 #这里输入 1 回车
diff --git /home/test/.cache/yay/ttf-wps-fonts/.gitignore /home/test/.cache/yay/ttf-wps-fonts/.gitignore
new file mode 100644
index 0000000..12be320
--- /dev/null
+++ /home/test/.cache/yay/ttf-wps-fonts/.gitignore
@@ -0,0 +1,5 @@
+*.pkg.tar.xz
+*.src.tar.gz
+src/
+pkg/
+
diff --git /home/test/.cache/yay/ttf-wps-fonts/PKGBUILD /home/test/.cache/yay/ttf-wps-fonts/PKGBUILD
new file mode 100644
index 0000000..21a51bb
--- /dev/null
…………
+url="https://github.com/IamDH4/ttf-wps-fonts"
+source=("$pkgname.zip::https://github.com/IamDH4/$pkgname/archive/master.zip"
+        "license.txt")
+sha1sums=('cbc7d2c733b5d3461f3c2200756d4efce9e951d5'
+          '6134a63d775540588ce48884e8cdc47d4a9a62f3')
+
#这里输入 q
:: Proceed with install? [Y/n] y #这里输入 y 回车
==> Making package: ttf-wps-fonts 1.0-5 (Thu Jul  6 06:23:35 2023)
…………
==> Leaving fakeroot environment.
==> Finished making: wps-office-cn 11.1.0.11698-1 (Thu Jul  6 06:37:32 2023)
==> Cleaning up...

We trust you have received the usual rule from the local system
It usually counts down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

For security reasons, the password you type will not be witness.

[sudo] password for test: # Enter the password for test here. Note: If the password is correct but repeatedly indicates a password error, please reboot the FreeBSD system to restart the above。

Packages (2) ttf-wps-fonts-1.0-5 wps-office-cn-11.1.0.11698-1

Total Installed Size: 1370.17 MiB

:: Project with installation
(2/2) checking keys in keyring [################################# # # # # # # # # # # # 100%
(2/2) checking capacity integrity [################################## ## # # # # # # # # # 100%
I don't know
(2/2) installing ttf-wps-fonts [############################################### ## ####### # # # # ## # # # # # # #
Running post-transaction books...
Arming ConditionsUpdate...
Updating wontconfig Cache...
Updating the desk file mime type carche...
Updating X wontdir views...
[test@ykla~]
# Pacman - S libxcomposite #
````

Installation complete。

Fcitx5 input method does not react. To be tested. If you know what to do, please tell us。

# Based on Ubuntu Compatibility Layer

```sh
# fetch http://book.bsdcn.org/ubuntu.sh #下载脚本构建兼容层
# sh ubuntu.sh #运行脚本
# chroot /compat/ubuntu/ /bin/bash #进入 Ubuntu 兼容层
```

```sh
# apt install  bsdmainutils xdg-utils libxslt1.1 libqt5gui5 xcb # 安装依赖包
# wget https://wps-linux-personal.wpscdn.cn/wps/download/ep/Linux2019/11698/wps-office_11.1.0.11698_amd64.deb
# apt install ./wps-office_11.1.0.11698_amd64.deb
```

Installation complete。

Note**
>
>Fcitx5 input did not react when writing. To be tested. If you know what to do, please tell us。

# Fragmentation and unfinished business

- It's not working

```sh
# ldd /usr/lib/office6/wps
```

What's missing。

need root to start。

- WPS UNDER KDE5 MAY NOT BE ABLE TO START。

Because the WPS startup file was called by bash shell. So when you install a bash, you can start it normally:

```sh
# pkg install bash
```

Or..

```
# cd /usr/ports/shells/bash/
# make install clean
```
