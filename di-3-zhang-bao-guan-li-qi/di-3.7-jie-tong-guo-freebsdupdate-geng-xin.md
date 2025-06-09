# Section 3.7 Update FreeBSD by freebsd-update


> ** Front row tip**
>
> Alion server users upgraded to 13.x See section 2.1, "Virtio virtualization using virtio technology".

> **Note:**
>
> Only releasing version of the first-level architecture provides the source. Which means the current and stable are not. Support level notes on architecture are available at: [https://www.freebsd.org/platforms] (https://www.freebsd.org/platforms)
>
> In the FreeBSD 15 development plan, `pkgbase ' is expected to replace `freebsd-update ' .



Note**
>
>ZFS for upgrades see ZFS Chapter

# Update System

FreeBSD provides a practical tool `freebsd-update ' to install system updates, including upgrades to large versions. `freebsd-update ' received formal support in FreeBSD 7.0-RELEASE.

References

- [FreeBSD 7.0-RELEASE Announcement] (https://www.freebsd.org/releases/7.0R/announce/), `freebsd-update (8) contributions socially supported binary upgrades to new returns in order to security fixes and errata watches.


# Environmental readiness

- If csh (14 below root default is csh):

````
# Setenv /usr/bin/ee
# Setenv VISUAL/usr/bin/ee
````

- If bash, zsh or sh (14 and above root default is sh):

```sh '
# export EDITOR=/usr/bin/ee # toggle vi to ee, vi not to use
# Export VISUAL=/usr/bin/ee # Switch vi to ee, vi will not be used
````

Check to verify:

```sh '
Root@ykla:/home/ykla #echo $EDITOR
/usr/bin/ee
Root@ykla:/home/ykla #echo $VISUAL
/usr/bin/ee
````

Regular security update

```sh '
# Freebsd-update fix
````

When information similar to:

```sh '
Usrlinklude/c+/vl/trllvector usrlinklude/c+/vl/trversion usrlinklude/c+/v1/trl/wchar.h usr/include/c+/v1/tr1/wctype.h usrlinkclude/c+/vllunwind-armh
Usrlinklude/c+/v1/unwind-itaniumh Usrlinklude/c+/vllunwindh
Usr/include/crypto/crypto/crypto/cbcmac.h usr/include/crypto/deflate.h usrlinklude/crypto/gfmsult.h usr/include/crypto/gmoc.h
Usr/include/crypto/rijndael.h usrlinclude/crypto/rmd160.h usr/include/crypto/xform.h
Wer/lib/clang/11.01.1/include
:
````

All you have to do is enter the q ' car back. Then:

```sh '
# Freebsd-update all
````

# # Size update #

Note**
>
>freebsd-update ' downloads are slow not because of the source of their updates outside the country (as are the days when you use an offshore server to update; and when the freebsdcn source is still valid). Probably because of its design deficiencies. [This is an issue that has always been prevalent] (https://freebsd-qastions.freebsd.narkive.com/xjVoeetUM/why-is-freebsd-update-so-horrible-slow).

** Take FreeBSD 14.1-RELEASE Upgrade 14.2-RELEASE**

, which is now updated to `14.2-RELEASE':

```sh '
# Freebsd-update upward-r 14.2-RELEASE
````


When information similar to the following appears, act on the bottom hint:

```sh '
#freebsd-update upgrad -r 14.2-RELEASE
I don't know what you're talking about.
Looking up upwards.
Fetching metada signature for 141-RELEASE from update2.freebsd.org... done.
Fetching metadata index... done.
Fetching 1 metadata matches.
Applying metadata matches... done.
Fetching 1 metadata fields... done.
Inspecting system... done.

The following conventions of FreeBSSD seem to be updated:
Kernel/generic kelnel/generic-dbg world/base world/lib32

The following companies of FreeBSD do not seem to be involved:
World/base-dbg world/lib32-dbg

Does this look relevant (y/n)?

Fetching metada signature for 14.2-RELEASE from update2.freebsd.org...doe.
Fetching metadata index... done.
Fetching 1 metadata matches.
Applying metadata matches... done.
Fetching 1 metadata fields... done.
Inspecting system... done.
Fetching files from 141-RELEASE for changing... done.
Preparing to download files...
# It needs to wait about 30 minutes below. It's normal to wait five hours longer when you're going to have to update a big version.
Fetching 4070 watches....10....20...30...40...

* Reissued for technical reasons.

4000 4010 4020 4030 4040 4050 4060 4070 done.
Fetching 35 files.10.20.30.doe.
Atting to automatically change in files... done.

The following changes, which accepted between FreeBSD 14.1-RELEASE and
FreeBSD 14.2-RELEASE have been made into/etc/ssh/sshd_config:
Could not close temporary folder: %s
++ new version
@-103, 11 + 103, 11 @
#PidFile/var/run/sshd.pid
#MaxStartups 10:30:100
#PermitTunnel no
# ChootDirectory none
#UseBlacklist no
- #VersionAddendum FreeBSD-20240318
+VersionAddendum FreeBSD-202440806

# No different banner path
# Banner none

# Override default of no subsystems
Does this look relevant (y/n)?
The followini'm sorry, I'm sorry.
14.2-RELEASE-p0:
/usr/lib/ossl-modules/fips.so
/usr/lib32/ossl-modules/fips.so
/usr/share/examples/ sound/README
/usr/share/examples/ sound/basic.c
/usr/share/examples/ sound/ossinit.h
/usr/share/examples/ sound/ossmidi.h
/usr/share/man/man9/ifaddr_byindex.9.gz
/var/db/etcupdate/log
/var/db/locate.database
(END) # Enter q here, confirm the change
The following files will be added as part of updating to
14.2-RELEASE-p0:
/boot/kernel/bnxt_re.ko
/boot/kernel/gpioaei.ko
/boot/kernel/if_rtw89.ko
/boot/kernel/linuxkpi_video.ko
* Reissued for technical reasons.
/usr/share/examples/son/sndstat_nv.c
: # Enter q here to confirm the change until no new content appears

* Reissued for technical reasons.

The following files will be updated as part of updating to
14.2-RELEASE-p0:
/bin/[
/bin/cat
/bin/chflags

* Reissued for technical reasons.

/bin/ln
/bin/ls
/bin/mkdir
To begin the downloaded upgrades, run 'freebsd-update [options] install'.
````

Run `freebsd-update install ' to install updates:

```sh '
#freebsd-update
I don't know what you're talking about.
Creating snapshot of emerging bot environment... done.
Installing updates...
Kernel updates have been updated.
'freebsd-updates' install' again to finish updating dates.
````

The kernel upgrade has been installed and the system requires a restart:

```sh '
#reboot
````

Run `freebsd-update installation install ' for update of user space:

```sh '
# Freebsd-update all
I don't know what you're talking about.
Creating snapshot of emerging bot environment... done.
Installing updates...
Restaring sshd after upward
Checking on sshd communication.
Stomping sshd.
Waiting for PDIS: 868.
Checking on sshd communication.
Starting sshd.
Scanning/usr/share/certs/untrusted for
Scanning/usr/share/certs/trusted for certainities...
Scanning/usr/local/share/certs for certain...
I don't know, do.
````


Reload `pkg ':


```sh '
#pkg Bootstream-f
The package capability tool is not yet installed on your system.
Do you want to fitch and install it now?
Bootstrapping pkg from https://mirrors.nju.edu.cn/freebsd-pkg/FreeBSD:14:amd64/latest, please wait... # I changed pkg source, you may not be like me, you're fine
Installing pkg-1.21.3...
Package pkg is already settled,
Expressing pkg-1.21.3: 100%
````

Checking third-party software ABI changes (FreeBSD ABI is very stable, usually without error):

```sh '
#pkg upgrad
#pkg upgrad
Updating nju repository catalogue...
Fetching meta.conf: 0%
Fetching data.pkg: 100% 7 MiB 7.6MB/s 00:01
Profiting events: 100%
35765 packages covered.
All returns are up to date.
Updating data categories format: 100%
Checking for upgrades (215 candidates): 100%
Processing candidates (215 candidates): 100%
The following 223 package(s) will be imposed (of 0 checked):

New packs to be INSTRAW:
ceres-solver: 2.2.0_10

* Reissued for technical reasons.

The process will release 45 MiB more space.
687 MiB to be downloaded.

-Proceed with this action?

The following omissions
````


That's it.

Verify update:

```sh '
#freebsd-version-k
14.2-RELEASE
#freebsd-version-u
14.2-RELEASE
````

# # Update EFI Guide

>** Warning**
>
> The EFI-guided system, EFI-system partition (ESP) contains a copy of the pilot loading program for solidware-guided kernel. If the root file system is ZFS, the lead loader must be able to read the ZFS guide file system. Following system upgrades and before `zpool upgrade ' , the guidance loader on the ESP must be updated, otherwise the system may not be able to guide. Although not mandatory, the same should be true of UFS as the root file system.

The command `efibootmgr-v ' can be used to determine the location of the current guided loading program. The value shown in `BootCurrent ' is the number of the current guidance configuration used to guide the system. The corresponding entry of the output starts with `+ ', if

```sh '
# efibootmgr-v
Boot to FW: false
BootCurrent: 0004
BootOrder: 0004, 0000, 0001, 0002, 0003
+Boot0004* FreeBSD HD (1, GPT, f83a9e2f-bd87-11ef-95b-7-000c29761cd2, 0x28, 0x82000)/File(\freebsd\loader.ef)#
nda0p1:/efi/freebsd/loader.efi (null)
Boot000* EFI VMware Virtual NVME Namespace (NSID 1) PciRoot (0x0)/Pci(0x15,0x0)/Pci(0x0,0x0)/NVME(0x1,00-00-00-00-00-00-00-00)
Boot0001* EFI VMware Vital IDE CDROM Drive (IDE 1:0) PciRoot (0x0)/Pci (0x7,0x1)/Ata (Secondary, Master,0x0)
Boot0002* EFI Network PciRoot (0x0)/Pci (0x11x0)/Pc(0x1x0)/MAC(000c29761cd2,0x0)
Boot0003* EFI Internal Shell (Unsuppleted option) MemollyMapped (0xb, 0xbeb4d018,0xbf07e017)/FvFile (c57ad6b7-0515-40a8-9d21-551652854e37)


Unreferenced Variables:
````

ESP should have been mounted to **/boot/efi**. If not, manually mounted partitions listed in the `efibootmgr ' output (this example is `nda0p1 ' ): `mount_msdosfs/dev/nda0p1/boot/efi ' . For another example, see [loader.efi (8)] (https://man.freebsd.org/cgi/man.cgi?query=loader.efi&sektion=8&format=html).

The value of the `File ' field exported in `efibootmgr-v ' , e.g. `\efi\freebsd\loader.efi ' , is the location of the guidance load that is being used on the EFI. If the mount point is **/boot/efi**, the document is `/boot/efi/efi/freebsd/loader.efi'. Another common value for `File ' (in FAT32 file system) may be `FeeBSD using lowercase) `File ' , where `XXX ' is amd64 (i.e. `x64 ' ), aarch64 (i.e. `aa64 ' ) or riscv64 (i.e. `riscv ' ); if not configured, the default lead loader. **/boot/loader.efi** should be copied to the correct path in **/boot/efi** to update the configured and default guided loader.

I don't...

{\i1 \cH30D3F4}It's bullshit up there


After the version is updated, the following image may appear before the start-up menu appears

Note**
>
> This interface appears for a very short period of about 20 ms. You can use a camera to take an observation.

! [loader update alert interface] (..gitbook/assets/loader.png)

Name

```sh '
*************************************************************************************************************
*************************************************************************************************************
****
**** BOOT LOADER IS TOO OLD, PLEASE UPGRADE.**
****
*************************************************************************************************************
*************************************************************************************************************
````

This means loader needs to be updated. You can also use the command to verify the version:

```sh '
#strings /boot/efi/efi/freebsd/loader.efi|grep FreeBSD|EFI
FreeBSD/amd64 EFI loader, Review 1.1
#strings/boot/loader.efi|grep FreeBS|EFI
FreeBSD/amd64 EFI loader, Review 3.0
````

Reference is made to the examples in the manual [loader.efi] (https://man.freebsd.org/cgi/man.cgi?query=loader.efi). `/boot/efi/efi/freebsd/loader.efi ' is a loader in use (the version is indeed old)

Update:

```sh '
#cp /boot/loader.efi /boot/efi/efi/freebsd/
````

>** Warning**
>
> Please update the loader, then update the ZFS version!

>** Important**
>
> Non-EFI, Bootcode, ZFS, etc.


# Optional update #


# View FreeBSD version

> **Note:**
>
> Sometimes a patch does not involve a kernel, the kernel version does not change, it is not visible with `uname-r ' , but the user space version changes. So you might see two versions, whichever is higher.

# freebsd-version command

View FreeBSD kernel version and patch number:

```sh '
Ykla@ykla: ~ %freebsd-version-k
13.1-RELEASE-p3
````

View installed user space version and patch program level:

```sh '
Ykla@ykla: %freebsd-version-u
13.1-RELEASE-p5
````

# # uname command

```sh '
@ykla: %uname-a
FreeBSD ykla 13.1-RELEASE 13.1-RELEASE releng/13.1-n250148-fc952ac2212 GENERIC amd64
````

```sh '
Ykla@ykla: %uname-mrs
FreeBSD 13.1-RELEASE amd64
````

# Fragmentation and unfinished business

# Roll back #

```sh '
# Freebsd-update rollback
````

# # pkg can't find '.so '

Terminal Execute Command

```sh '
♪ Pkg Bootstream-f
````

No ntp user

Terminal Execute Command

```sh '
# Pw grouped ntpd-g 123
# Pw used ntpd-u 123-g ntpd-h-d/var/db/ntp-s/usr/sbin/nologin-c "NTP Daemon"
````
