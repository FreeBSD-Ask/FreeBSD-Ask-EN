Section 3.4 Installation of binary packages by pkg package manager

FreeBSD binary package manager is currently a pkg, or "package", package.

`pkg install ' can be abbreviated as `pkg ins ' , other similar.

> ** Note**
>
> pkg only manages third-party software packages and does not serve to upgrade systems to secure security updates. This is because the FreeBSD project maintains the kernel and user space as a whole, rather than the Linux-like linus torvalds, which maintain the kernel, and the issuers maintain the GNU tools (they are actually designed as individual packages, so they can upgrade and upgrade the system with a package manager).
>
>FreeBSD is also [attempting to use pkg] to update user space and kernels (https://wiki.freebsd.org/PkgBase). Address the above issues.
>
> FreeBSD uses `freebsd-update ' to upgrade the system to get a security patch. <https://pkg-status.freebsd.org/> can view the current pkg compilation status.
>
>
> Graphical users can install `ports-mgmt/octopkg ', a graphical frontend to pkg developed by ghostbsd.


>** Skills**
>
> This can be done if you need to look into the specifics of a package in FreeBSD: Google or "freebsd reports " should (must be searched often). If this is not available, you can search the package name directly on the website. https://www.freshports.org/] (https://www.freshports.org).

# Install pkg

>** Skills**
>
>In accordance with man [pkg(7)] (https://man.freebsd.org/cgi/man.cgi?query=pkg)
>
In order to avoid problems of backward compatibility, the actual `pkg (8) ' tool will not be pre-assessed in the basic system.

Basic system default does not have pkg.

```sh '
root@ykla:/home/ykla #pkg #Input pkg back
The package capability tool is not yet installed on your system.
Do you want to fitch and install it now?
Bootstreaming pkg from pkg+https://pkg.FreeBSD.org/FreeBSD:14:amd64qarterly, please wait...
Verifying signature with trusted certified pkg.freebsd.org.2013102301.doe
Installing pkg-1.21.3...
Expressing pkg-1.21.3: 100%
Pkg: not enough arguments
Usage: pkg [-v] [-d] [-l] [-N] [-j <jail name or id> |-c <choot path> |r <rootdir>] [-R <repo config dir>] [-o var=value] [-4|-6] [<args>]

For more information on avilable committees and options see 'pkg help'.
````


>** Skills**
>
>If you have a long time stuck in `Bootstrapping pkg from ..., please wait... ' , press **Ctrl + C** to interrupt the process and do it after the internal source.

>** Skills**
>
>In case of prompting `00206176BC68000:error:0A00000086:SSL routines:tls_post_process_server_certificate:certificate verified:/usr/src/crypto/opensl/sl/statem/statem_clnt.c:1890: `
>
> ```sh '
#ntpdate-u pool.ntp.org
> ````

>** Skills**
>
>pkg download path is `/var/cache/pkg/ '


# List files where pkg packages are installed

Note**
>
> Only the installed package file can be listed, and uninstalled cannot use this command.

```sh '
root@ykla: ~pkginfo-l xrdp
xrdp-0.10.2_2,1:
/usr/local/bin/xrdp-dis
/usr/local/bin/xrdp-dumpfv1
/usr/local/bin/xrdp-genkeymap
/usr/local/bin/xrdp-keygen
/usr/local/bin/xrdp-sesadmin
/usr/local/bin/xrdp-sesrun
/usr/local/etc/pam.d/xrdp-sesman
/usr/local/etc/rc.d/xrdp
. . . . . . . . . . .
````


# Install python 3


```sh '
# Pkg install python
````

or

```sh '
# cd/usr/ports/lang/python/
# Make install clean
````

# pkg upgrade software

```sh '
# Pkg upgrad
````

Error: `You must update the ports-mgmt/pkg port first '

Resolve:

```sh '
#cd /usr/ports/ports-mgmt/pkg
# Make disstall restall
````

# View all installed software

```sh '
# pkginfo
````

# Unmount software

Direct use of `pkg delete ' would undermine normal dependency relationships and should be avoided to the extent possible (the same is true of `make deinstall ' in ports) and instead of using the `pkg_rmleaves ' order, which belongs to software that needs to be installed on its own.

```sh '
# pkg install pkg_rmleaves
````

Or...

```sh '
#cd /usr/ports/ports-mgmt/pkg_rmleaves/
# Make disstall
````

How to unload all self-installed third-party software?

```sh '
root@ykla: ~ #pkg delete-fa # If you take parameter f, you delete pkg yourself, because pkg is also the software that the user started to install.
Checking integration... done.
Deinstance has been listed for the following 87 packages:

Installed packs to be REMOVED:
alsa-lib: 1.2.12
Brotli: 1.1.0,1
Curl: 8.8.0
. . . . . . . . . . .
pcre2: 10.43
Perl5: 5.36.3_1
pkg: 1.21.3 # If the parameter f is taken, the pkg itself will be deleted, because this pkg is also the software that the user installed at the outset.
png: 1.6.43
Xorg-fonts-trutype: 7.7_1
Xorgproto: 2024.1
zstd: 1.5.6

Number of packs to be moved: 87

The operation will be free 825 MiB.

-Proceed with developing packs?
````

# How to find missing `.so ' (for Linux Compatible)

>** Warning**
>
>This part only addresses the lack of `.so ' for Linux Compatibility. If you encounter such problems in FreeBSD, you should first update the system. The source and software are then updated.

# # Install pkg-provides

```sh '
# pkg install pkg-provides
````

Or:

```sh '
#cd/usr/ports/ports-mgmt/pkg-provides/
# Make install clean
````

# # Configure pkg-provides

- View profile:

```sh '
root@ykla:/home/ykla
pkg-provides-0.7.4:
On install:
In order to use the pkg-provisions plus you need to be able to pkg.
# To use pkg-provides plugins, the plugin function must be enabled first in pkg.

To do this, without the following lines in/usr/local/etc/pkg.conf file
And add pkg-provides to the supported plugin list:
# By removing the following line comments in /usr/local/etc/pkg.conf file and adding pkg-provides to the list of supported plugins:

PKG_PLUGINS_DIR = "/usr/local/lib/pkg/";
PKG_ENABLE_PLUGINS = true;
[provides];
# Plugin Configuration Example, where provides means pkg-provides plugins are enabled.

After that `pkg pugs' to see the pugins handled by pkg.
# When settings are finished, run `pkg plugins ' to see the enabled plugin.

On upward:
# Upgrade description:

To update the files run `pkg programmes-u'.
# To update provides database, run 'pkg provides-u '.
````

- Edit `/usr/local/etc/pkg.conf ' to find empty lines and write:


```sh '
PKG_PLUGINS_DIR = "/usr/local/lib/pkg/";
PKG_ENABLE_PLUGINS = true;
[provides];
````

- Run: `pkg plugins ' :

```sh '
#pkg plugins
NAME DESC Version
I mean, I'm not sure if I'm going to be able to do that, but I'm not going to do that.
Root@ykla:/home/ykla#
````

Update database:

```sh '
Root@ykla:/home/ykla
Fetching programmes database: 100% 19 MiB 6.6MB/s 00:03
Extracing data...
````

### Example: Find `libxcb-icccm.so.4 '

```sh '
Root@ykla:/home/ykla #pkg contributions libxcb-icccm.so.4
Name: xcb-util-wm-0.4.2
Comment: Framework for windowmanager application
Repo: FreeBSD
Filename: usr/local/lib/libxcb-icccm.so.4.0.0
Wer/local/lib/libxcb-iccm.so.4
````



# Fragmentation and unfinished business

# `ld-elf.so.1: Shared subject "libmd.so.6" not found, reported by "pkg"

This problem is generally due to changes in the software source that did not synchronize the basic system ABI in a timely manner.

For general RELEASE, an updated system is sufficient. For the CURRENT/ STABLE system, recompile `pkg ' is sufficient.


- RELEASE.

Switch to last source and reload pkg package from software source:

```sh '
# Pkg-static Bootstream-f
````

If invalid, then:

```sh '
# Freebsd-update fix
# Freebsd-update all
# Pkg-static update-f
# Pkg-static upgrad-f pkg
````

- CURRENT/STABLE

```sh '
# pkg-static delete-f pkg # Force unmount current pkg
# cd /usr/ports/ports-mgmt/pkg # Switch directory
# make BATCH=yes install clean
````

# 'pw: user `package'

Example of question:

```sh '
Installing package...
Creating groups.
Creating group 'package' with gid '000.
Creating users
Creating us with uid '000'.
Pw: our `package' drew
pkg: PRE-INTAL script failed
````

The problem is that the database is not synchronized.

Refresh database:

```sh '
#/usr/sbin/pwd_mkdb-p/etc/master.passwd
````

♪ 'Shared object 'x.so.x' not found by 'xx'

The problem is usually caused by ABI sabotage, so just update.

Install `bsdadminscripts2 ':

```sh '
# pkg install bsdadmincripts2
````

Or...

```sh '
#cd /usr/ports/ports-mgmt/bsdadminscripts2/
# Make install clean
````

```sh '
# pkg_libchk
Doxygen-1.9.6_1,2: /usr/local/bin/doxygen issues libmd.so.6
Jbig2dec-0.20_1: /usr/local/bin/jbig2diss libmd.so.6
jbig2dec-0.20_1: /usr/local/lib/libjbig2dec.so issues libmd.so.6
````

Based on the above list of software, re-compile it using Ports (RELEASE can be updated directly `pkg ' ).



#### `bsdadminscripts2' Extension and References


- [BSD Administration Scripts II] (https://github.com/lonkamikaze/bsda2), project address, including detailed user instructions

- If pkgbase, `bsdadminscripts2 ' can ** check the integrity of the system** to find out which system documents were tampered with:

```sh '
#pkg_validate
FreeBSD-pkg-bootstrap-15. snap 2024100422339: checksum mismatch for/etc/pkg/FreeBSD.conf
FreeBSD-runtime-15.snap2024100422339: checksum metatch for/etc/group
FreeBSD-runtime-15.snap2024100422339: checksum metatch for/etc/master.passwd
````

- `bsdadminscripts2 ' can also find outdated software for the current system:

```sh '
@ykla: /usr/ports #pkg_version-ql<
konadi-23.08.5_1
bueld2-0.17.0
Chromium-128.0.6613.137
````

# # 'Newer FreeBSD #

Example of question:

```sh '
Newer FreeBSD version for package pkg:
To signor this error set IGNORE_OSVERSION=yes
- Package: 1402843
- Running kelnel: 14,00042.
Ignare the mismatch and continue?
````

This usually occurs on systems that have lost security support or are in CURRENT/STABLE versions, without prejudice to use, and `y ' is sufficient.

If the root causes are to be addressed, it is necessary to unload the pkg and install `ports-mgmt/pkg ' from the ports; or to update the entire system from the source code.

If you simply do not want to see this hint, you simply have to write `IGNORE_OSVERSION=yes ' to `/ etc/make.conf ' (if not new).

# References

- [pkg delete -- deletes packs from the database and the system] (https://man.freebsd.org/cgi/man.cgi?query=pkg-delete&sektion=8&n=1)
