section 3.4 installation of binary packages by pkg package manager

FreeBSD binary package manager is currently a pkg, or "package", package。

___ CODESPAN_0 __ CAN BE ABBREVIATED AS ___ CODESPAN_1 __, OTHER SIMILAR。

> ** Note**
>
> pkg only manages third-party software packages and does not serve to upgrade systems to secure security updates. This is because the FreeBSD project maintains the kernel and user space as a whole, rather than the Linux-like linus torvalds, which maintain the kernel, and the issuers maintain the GNU tools (they are actually designed as individual packages, so they can upgrade and upgrade the system with a package manager)。
>
>FreeBSD is also [trying to use pkg to update user space and kennel] (https://wiki.freebsd.org/PkgBase). Address the above issues。
>
> FreeBSD uses __CODESPAN_0_ to upgrade the system and get a security patch. <https://pkg-status.freebsd.org/> can view the current pkg compilation status。
>
>
> A graphical user can install __CODESPAN_0_, a graphical frontend for pkg, developed by ghostbsd。


>** Skills**
>
> This can be done if you need to look into the specifics of a package in FreeBSD: Google or "freebsd reports " should (must be searched often). If this is not available, you can search the package name directly on the website. https://www.freshports.org/] (https://www.freshports.org)。

# install pkg

>** Skills**
>
>in accordance with man [pkg(7)] (https://man.freebsd.org/cgi/man.cgi?query=pkg)
>
IN ORDER TO AVOID BACKWARD COMPATIBILITY PROBLEMS, THE ACTUAL ___CODESPAN_0_ TOOL WILL NOT BE PRESET IN THE BASIC SYSTEM。

basic system default does not have pkg

```sh
root@ykla:/home/ykla # pkg # 输入 pkg  回车
The package management tool is not yet installed on your system.
Do you want to fetch and install it now? [y/N]: y # 请在这里输入 y 或 直接回车
Bootstrapping pkg from pkg+https://pkg.FreeBSD.org/FreeBSD:14:amd64/quarterly, please wait...
Verifying signature with trusted certificate pkg.freebsd.org.2013102301... done
Installing pkg-1.21.3...
Extracting pkg-1.21.3: 100%
pkg: not enough arguments
Usage: pkg [-v] [-d] [-l] [-N] [-j <jail name or id>|-c <chroot path>|-r <rootdir>] [-C <configuration file>] [-R <repo config dir>] [-o var=value] [-4|-6] <command> [<args>]

For more information on avilable committees and options see 'pkg help'.
````


>** Skills**
>
>If you have been stuck at __CODESPAN_0 for a long time, press **Ctrl + C** to interrupt the process and to replace it with a domestic source。

>** Skills**
>
>IF YOU HAVE A HINT __CODESPAN_0_, CALIBRATE FIRST。
>
> ```sh '
#ntpdate-u pool.ntp.org
> ````

>** Skills**
>
>pkg download path is __CODESPAN_0_。


# list files where pkg packages are installed

Note**
>
> Only the installed package file can be listed, and uninstalled cannot use this command。

```sh
root@ykla:~ # pkg info -l xrdp
xrdp-0.10.2_2,1:
	/usr/local/bin/xrdp-dis
	/usr/local/bin/xrdp-dumpfv1
	/usr/local/bin/xrdp-genkeymap
	/usr/local/bin/xrdp-keygen
	/usr/local/bin/xrdp-sesadmin
	/usr/local/bin/xrdp-sesrun
	/usr/local/etc/pam.d/xrdp-sesman
	/usr/local/etc/rc.d/xrdp
	……省略一部分……
```


# install python 3


```sh
# pkg install python
```

or

```sh
# cd /usr/ports/lang/python/
# make install clean
```

# pkg upgrade software

```sh
# pkg upgrade
```

ERROR: __CODESPAN_0_

Resolve:

```sh
# cd /usr/ports/ports-mgmt/pkg
# make deinstall reinstall
```

# View all installed software

```sh
# pkg info
```

# Unmount software

Direct use of __CODESPAN_0 would undermine normal dependency relationships and should be avoided to the extent possible (the same is true of __CODESPAN_1 in ports) and instead of __CODESPAN_2_, the software to which this command belongs needs to be installed。

```sh
# pkg install pkg_rmleaves
```

Or..

```sh
# cd /usr/ports/ports-mgmt/pkg_rmleaves/
# make deinstall
```

How to unload all self-installed third-party software

```sh
root@ykla:~ # pkg delete -fa # 如果带上参数 f，会把 pkg 自己也删掉，因为 pkg 也是用户一开始自行安装的软件。
Checking integrity... done (0 conflicting)
Deinstallation has been requested for the following 87 packages (of 0 packages in the universe):

Installed packs to be REMOVED:
alsa-lib: 1.2.12
brotli: 1.1.0,1
curl: 8.8.0
.
pcre2: 10.43
perl5: 5.36.3_1
pkg: 1.21.3 # if the parameter f is taken, the pkg itself will be deleted, because this pkg is also the software that the user installed at the outset。
png: 1.6.43
xorg-fonts-trutype: 7.7_1
xorgproto: 2024.1
zstd: 1.5.6

Number of packs to be moved: 87

The operation will be free 825 MiB.

-Proceed with developing packs
````

# How to find missing __CODESPAN_0_(for Linux Compatibility)

>** Warning**
>
>This part only addresses the lack of __CODESPAN_0_ for Linux Compatibility. If you encounter such problems in FreeBSD, you should first update the system. The source and software are then updated。

# # install pkg-provides

```sh
# pkg install pkg-provides
```

Or:

```sh
# cd /usr/ports/ports-mgmt/pkg-provides/ 
# make install clean
```

# # configure pkg-provides

- View profile:

```sh
root@ykla:/home/ykla # pkg info -D pkg-provides
pkg-provides-0.7.4:
On install:
In order to use the pkg-provides plugin you need to enable plugins in pkg.
# 要使用 pkg-provides 插件，必须先在 pkg 中启用插件功能。

To do this, uncommit the following lines in/usr/local/etc/pkg.conf file
and add pkg-provides to the supported plugin list:
# by removing the following line comments in /usr/local/etc/pkg.conf file and adding pkg-provides to the list of supported plugins:

PKG_PLUGINS_DIR = "/usr/local/lib/pkg/";
PKG_ENABLE_PLUGINS = true;
[provides];
# plugin configuration example, where provides means pkg-provides plugins are enabled。

After that `pkg pugs' to see the pugins handled by pkg.
# WHEN SETTINGS ARE FINISHED, RUN __CODESPAN_0_ TO SEE THE ENABLED PLUGIN。

On upward:
# Upgrade description:

To update the files run ___ CODESPAN_0_.
# To update the provides database, run __CODESPAN_0_。
````

- EDIT __CODESPAN_0, FIND EMPTY LINES, WRITE:


```sh
PKG_PLUGINS_DIR = "/usr/local/lib/pkg/";
PKG_ENABLE_PLUGINS = true;
PLUGINS [ provides ];
```

- RUN: __CODESPAN_0:

```sh
root@ykla:/home/ykla # pkg plugins
NAME       DESC                                          VERSION   
provides   A plugin for querying which package provides a particular file 0.7.4     
root@ykla:/home/ykla # 
```

Update database:

```sh
root@ykla:/home/ykla # pkg provides -u
Fetching provides database: 100%   19 MiB   6.6MB/s    00:03    
Extracting database....success
```

## # EXAMPLE: FIND __CODESPAN_0_

```sh
root@ykla:/home/ykla # pkg provides libxcb-icccm.so.4
Name    : xcb-util-wm-0.4.2
Comment : Framework for window manager implementation
Repo    : FreeBSD
Filename: usr/local/lib/libxcb-icccm.so.4.0.0
          usr/local/lib/libxcb-icccm.so.4
```



# Fragmentation and unfinished business

# CODESPAN_0__

THIS PROBLEM IS GENERALLY DUE TO CHANGES IN THE SOFTWARE SOURCE THAT DID NOT SYNCHRONIZE THE BASIC SYSTEM ABI IN A TIMELY MANNER。

FOR GENERAL RELEASE, AN UPDATED SYSTEM IS SUFFICIENT. FOR THE CURRENT/ STABLE SYSTEM, RECOMPILE __CODESPAN_0_。


- RELEASE

switch to last source and reload pkg package from software source:

```sh
# pkg-static bootstrap -f
```

If invalid, then:

```sh
# freebsd-update fetch
# freebsd-update install
# pkg-static update -f
# pkg-static upgrade -f pkg
```

- CURRENT/STABLE

```sh
# pkg-static delete -f pkg #强制卸载当前的 pkg
# cd /usr/ports/ports-mgmt/pkg #切换目录
# make BATCH=yes install clean #使用 Ports 重新安装 pkg
```

# CODESPAN_0__

Example of question:

```sh
[1/1] Installing package…
===> Creating groups.
Creating group ‘package’ with gid ‘000’.
===> Creating users
Creating user ‘package’ with uid ‘000’.
pw: user ‘package’ disappeared during update
pkg: PRE-INSTALL script failed
```

The problem is that the database is not synchronized。

Refresh database:

```sh
# /usr/sbin/pwd_mkdb -p /etc/master.passwd
```

# CODESPAN_0__

THE PROBLEM IS USUALLY CAUSED BY ABI SABOTAGE, SO JUST UPDATE。

INSTALL __CODESPAN_0_:

```sh
# pkg install bsdadminscripts2
```

Or..

```sh
# cd /usr/ports/ports-mgmt/bsdadminscripts2/ 
# make install clean
```

```sh
# pkg_libchk
doxygen-1.9.6_1,2: /usr/local/bin/doxygen misses libmd.so.6
jbig2dec-0.20_1: /usr/local/bin/jbig2dec misses libmd.so.6
jbig2dec-0.20_1: /usr/local/lib/libjbig2dec.so misses libmd.so.6
```

Based on the above list of software, re-compile it with Ports (RELEASE can be updated directly __CODESPAN_0_)。



#### __CODESPAN_0_EXTENSION AND REFERENCE


- [BSD Adminization Scripts II] (https://github.com/lonkamikaze/bsda2), project address, including detailed user instructions

- If pkgbase, CODESPAN_0 is used, ** check the integrity of the system** and find out which system documents were tampered with:

```sh
root@ykla:/ # pkg_validate
FreeBSD-pkg-bootstrap-15.snap20241004232339: checksum mismatch for /etc/pkg/FreeBSD.conf
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/group
FreeBSD-runtime-15.snap20241004232339: checksum mismatch for /etc/master.passwd
```

- __CODESPAN_0_ ALSO IDENTIFIES OBSOLETE SOFTWARE FOR THE CURRENT SYSTEM:

```sh
@ykla:/usr/ports # pkg_version -ql\<
akonadi-23.08.5_1
build2-0.17.0
chromium-128.0.6613.137
```

# CODESPAN_0__

Example of question:

```sh
Newer FreeBSD version for package pkg:
To ignore this error set IGNORE_OSVERSION=yes
- package: 1402843
- running kernel: 1400042
Ignore the mismatch and continue? [y/N]:
```

THIS USUALLY OCCURS ON SYSTEMS THAT HAVE LOST SECURITY SUPPORT OR ARE IN CURRENT/ STABLE VERSION, WITHOUT PREJUDICE TO USE, BY ENTERING __CODESPAN_0_。

If you want to address the root causes, you need to unload the pkg and install _`ports-mgmt/pkg` from the ports; or update the entire system from the source code。

IF YOU DON'T WANT TO SEE THIS HINT, YOU JUST HAVE TO WRITE ___CODESPAN_0_INTO __CODESPAN_1_1_。

# References

- [pkg delete-deletes packs from the database and the system]
