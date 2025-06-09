# Section 5.8 Kinshan WPS (Linux version)

>** Warning**
>
>Do not use the Golden Hill WGS in the ports, as no update is available. It is recommended that the compatible layer be installed.

# Based on RockyLinux Compatibility (FreeBSD Port)

Note**
>
>Please first install RockyLinux Compatibility (FreeBSD Port) with reference to other chapters of the book

# # Install rpm tools

```sh '
# pkg install rpm4
````

Or:

````
#cd/usr/ports/archivers/rpm4/
# Make install clean
````

# Download Gold Mountain WFS

Official address: [WPS Office for Linux] (https://linux.wps.cn/)


<https://wps-linux-person.wpscdn.cn/wps/download/ep/Linux2023/1790/wps-office-12.01.1790-1.x86_64.rpm?t=1731150867&k=8e9446b92a6e5b727047ec25707be78>

Please find a valid link. I use the browser to download it.

>** Remarks**
>
There's a problem with this link, and I don't know how to use a Fetch download, or a wget. If you know how to solve this, please submit PR or issue.

# # Installing Golden Mountain WFS

```sh '
Root@ykla: #cd /compat/linux/
Root@ykla:/compat/linux#rpm2cpio < /home/ykla/Downloads/wps-office-12.1.0.1790-1.x86_64.rpm | cpio-id # Note that the path needs to be changed to your own
````


# Solve dependency #

View dependency:

```bash
Root@ykla:/compat/linux#/compat/linux/usr/bin/bash# Switch to compatible shell
bash-51.1#ldd /opt/kingsoft/wps-office/office6/wps
linux-vdso.so.1.
Libdl.so.2 =>/lib64libdl.so.2 (0x00000080105c000)
Libpthread.so.0=>/lib64/libpthread.so.0 (0x00000000801061000)
Libtcmalloc_minimal.so.4 =>/opt/kingsoft/wps-office/office6/libtcmalloc_minimal.so.4 (0x0000080160000)
Liblibsafec.so =>/opt/kingsoft/wps-office/office6/libsafec.so (0x000000000801066,000)
libstdc+.so.6 =>/opt/kingsoft/wps-office/office6/libstdc+.so.6 (0x00000001a0000)
Libm.so.6 =>/lib64libm.so.6 (0x00000080083,000)
libgcc_s.so.1 =>/lib64libgcc_s.so.1 (0x00000080115e000)
Libc.so.6 =>/lib64libc.so.6 (0x0000008001e00000)
/lib64/ld-linux-x86-64.so.2 (0x0000000001021,000)
Librt.so.1 =>/lib64librt.so.1 (0x000000801179,000)
````

You can see, rely on it all.

# Run the Golden Mountain WFS #


```bash
ykla@ykla: ~ $ /compat/linux//opt/kingsoft/wps-office/office6/wps
````


[FreeBSD WFS] (..gitbook/assets/wps1.png)

The input method is normal.

[FreeBSD WPS] (..gitbook/assets/wps2.png)

Based on ArchLinux Compatibility Layer

```sh '
#fetch http://book.bsdcn.org/arch.sh # download scripts to build compatibility layer
# sharch.sh # run the script
# chorot /compat/arch// bin/bash # enter Arch Compatible Layer
# Passwd # sets a password for the root of Arch
# passwd test # sets a password for Arch's test, script already created the user!
````

Start a new terminal and enter `reboot ' to restart FreeBSD, otherwise the password set may not be recognized.

```sh '
# chorot /compat/arch// bin/bash # enter Arch Compatible Layer
It's in Arch Compatibility! Switch to normal user to use aur
````

Start installation:

```sh '
$ yy -S wps-office-cn ttf-wps-fonts wps-office-mui-zh-cn # is in Arch Compatible Layer at this time! At this time the user is test
AUR Express (2): wps-office-cn-11.1.0.11698-1, ttf-wps-fonts-1.0-5
:: (1/1) Downloaded PKGBUILD: ttf-wps-fonts
2 wps-office-cn (Build Files Exchange)
1 ttf-wps-fonts
Packages to cleanBuild?
=[N]one [A]ll [Ab]ort [I]nstalled [No]tInstalled or (1 2, 3, 1-3,}4)
♪ Here's one ♪
:: Deleting (1/1): /home/test/.cache/yay/ttf-wps-fonts
HEAD is now at ba3222c Add upstream URL
2 wps-office-cn (Build Files Exchange)
1 ttf-wps-fonts
Diffs to show?
=[N]one [A]ll [Ab]ort [I]nstalled [No]tInstalled or (1 2, 3, 1-3,}4)
♪ Here's one ♪
diff-git/home/test/.cache/yay/ttf-wps-fonts/.gitignore/home/test/.cache/yay/ttf-wps-fonts/.gitignore
New file mode 100644.
index 10000.12be320
---/dev/null
+++/home/test/.cache/yay/ttf-wps-fonts/.gitignore
@-0, 0 + 1, 5 @
+.pkg.tar.xx
+.src.tar.gz
+src/
+pkg/
+
Diff-git/home/test/.cache/yay/ttf-wps-fonts/PKGBUILD/home/test/.cache/yay/ttf-wps-fonts/PKGBUILD
New file mode 100644.
index00000.21a51bb
---/dev/null
I don't know.
+url= "https://github.com/IamDH4/tf-wps-fonts"
+source=("$pkgname.zip: https://github.com/IamDH4/$pkgname/archive/master.zip")
+ "license.txt")
+sha1sums=('cbc7d2c733b5d3461f3c2200756d4efce9e951d5'
+ '6134a63d775540588ce4884e8cdc47d4a9a62f3')
+
# Enter q here
-Process with emergency?
== sync, corrected by elderman == @elder_man
I don't know.
Leaving fakeroot environment.
== sync, corrected by elderman == @elder_man
Clearing up...

We trust you have received the usuali'm sure from the local system
It usually counts down to these three things:

Recover the nature of others.
Think before you type.
With great power comes great responsiveness.

For security reasons, the password you type will not be witness.

[sudo] password for test: # Enter the password for test here. Note: If the password is correct but repeatedly indicates a password error, please reboot the FreeBSD system to restart the above.

Packages (2) ttf-wps-fonts-1.0-5 wps-office-cn-11.1.0.11698-1

Total Installed Size: 1370.17 MiB

:: Project with installation?
(2/2) Checking keys in keyring [################################# # # # # # # # # # # # 100%
(2/2) Checking capacity integrity [################################## ## # # # # # # # # # 100%
I don't know.
(2/2) Installing ttf-wps-fonts [############################################### ## ####### # # # # ## # # # # # # #
Running post-transaction books...
Arming ConditionsUpdate...
Updating wontconfig Cache...
Updating the desk file mime type carche...
Updating X wontdir views...
[test@ykla~]
# Pacman - S libxcomposite #
````

Installation complete.

Fcitx5 input method does not react. To be tested. If you know what to do, please tell us.

# Based on Ubuntu Compatibility Layer

```sh '
#fetch http://book.bsdcn.org/ubuntu.sh #download scripts build compatibility layer
# sh ubuntu.sh # run the script
#choot /compat/ubuntu//bin/bash #into Ubuntu Compatible
````

```sh '
#apt installation bsdmainutils xdg-utils libxslt1.1 libqt5gui5 xcb # install dependency packages
#wgethttps://wps-linux-person.wpscdn.cn/wps/download/ep/Linux2019/11698/wps-office_11.1.0.116998_amd64.deb
#apt install./wps-office_11.1.01.11698_amd64.deb
````

Installation complete.

Note**
>
>Fcitx5 input did not react when writing. To be tested. If you know what to do, please tell us.

# Fragmentation and unfinished business

- It's not working.

```sh '
#ldd /usr/lib/office6/wps
````

What's missing.

Need root to start.

- WPS under KDE5 may not be able to start.

Because the WPS startup file was called by bash shell. So when you install a bash, you can start it normally:

```sh '
# Pkg install rash
````

Or...

````
#cd/usr/ports/shells/bash/
# Make install clean
````
