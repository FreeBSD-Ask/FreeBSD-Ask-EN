SECTION 3.6 INSTALLING SOFTWARE VIA DVD

# MOUNT DVD TO __CODESPAN_0_ DIRECTORY

- DIRECTLY MOUNT LOCAL ISO:

```sh
# mdconfig /home/ykla/FreeBSD-14.2-RELEASE-amd64-dvd1.iso # 请换成你自己的路径，可以用 pwd 命令查看当前路径
md0
# mkdir -p /dist
# mount -t cd9660 /dev/md0 /dist # 不能直接挂载 ISO，会报错 block device required
```

- DIRECT USE OF DVD DEVICES (E.G. ISO MIRRORS MOUNTED DIRECTLY THROUGH VIRTUAL MACHINES):

WATCH ISO MOUNT:

```sh
# gpart show

...leave the useless disk..

=>9 2356635 cd0 MBR (4.5G)
9 2356635 - free - (4.5G)
````

YOU CAN SEE THERE'S A ___ CODESPAN_0... AND THE SIZE MATCHES。

```sh
# mkdir -p /dist # 创建挂载点
# mount -t cd9660 /dev/cd0 /dist # 挂载 ISO
# ls /dist/ # 查看挂载情况
.cshrc		bin		lib		net		root		var
.profile	boot		libexec		packages	sbin
.rr_moved	dev		media		proc		tmp
COPYRIGHT	etc		mnt		rescue		usr
```

# # troubleshooting and unfinished business

**/dist** If the directory is changed to another, the environment variable method is not valid, as __CODESPAN_0_does not modify the path。

# INSTALL DVD SOFTWARE USING __CODESPAN_0_ (CURRENTLY INVALID)

Let's start with the way above。

```sh
# bsdconfig
```

__CODESPAN_0> >CODESPAN_1__

There's bug, and it's wrong。

# INSTALL DVD SOFTWARE DIRECTLY USING ENVIRONMENT VARIABLES

Test installation:

```sh
# env REPOS_DIR=/dist/packages/repos pkg install xorg
Updating FreeBSD_install_cdrom repository catalogue...
FreeBSD_install_cdrom repository is up to date.
All repositories are up to date.
Checking integrity... done (0 conflicting)
The following 1 package(s) will be affected (of 0 checked):

New packs to be INSTRAW:
xorg: 7.7_3

Number of packs to be involved: 1

[y/N]:
````

TO LIST AVAILABLE SOFTWARE IN DVD:

```sh
# env REPOS_DIR=/dist/packages/repos pkg rquery "%n"
```

# SWITCH SOURCE TO DVD

CREATE DVD SOURCE

```sh
# cp /dist/packages/repos/FreeBSD_install_cdrom.conf /etc/pkg/
```

# # Test installation

```sh
# pkg install xorg
Updating FreeBSD_install_cdrom repository catalogue...
FreeBSD_install_cdrom repository is up to date.
All repositories are up to date.
Checking integrity... done (0 conflicting)
The following 1 package(s) will be affected (of 0 checked):

New packs to be INSTRAW:
xorg: 7.7_3

Number of packs to be involved: 1

[y/N]:
````

# References

- [Project Data] (https://www.freebsdmal.com/cgi-bin/fm/bsdvd10.1)
- [Install binary package without internet access] (https://forums.freebsd.org/threads/howtoinstall-binary-package-without-internet-accesses.67723/)
