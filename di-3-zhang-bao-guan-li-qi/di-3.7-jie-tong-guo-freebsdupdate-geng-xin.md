# Section 3.7 Update FreeBSD by freebsd-update


> ** Front row tip**
>
> alion server users upgraded to 13.x see section 2.1, "virtio virtualization using virtio technology"。

> **Note:**
>
> only releasing version of the first-level architecture provides the source. which means the current and stable are not. support level notes on architecture are available at: [https://www.freebsd.org/platforms] (https://www.freebsd.org/platforms)
>
> In the FreeBSD 15 development plan, __CODESPAN_0_ is expected to replace __CODESPAN_1_。



Note**
>
>ZFS FOR UPGRADES SEE ZFS CHAPTER

# Update System

FreeBSD provides a practical tool __CODESPAN_0_ to install system updates, including upgrades to large versions. __CODESPAN_1 _ received formal support in FreeBSD 7.0-RELEASE。

References

- [FreeBSD 7.0-RELEASE Announcement] (https://www.freebsd.org/releases/7.0R/announce/),_CODESPAN_0_


# Environmental readiness

- if csh (14 below root default is csh):

```
# setenv EDITOR /usr/bin/ee # 切换 vi 为 ee，vi 不会用
# setenv VISUAL /usr/bin/ee # 切换 vi 为 ee，vi 不会用
```

- if bash, zsh or sh (14 and above root default is sh):

```sh
# export  EDITOR=/usr/bin/ee # 切换 vi 为 ee，vi 不会用
# export  VISUAL=/usr/bin/ee # 切换 vi 为 ee，vi 不会用
```

Check to verify:

```sh
root@ykla:/home/ykla # echo $EDITOR
/usr/bin/ee
root@ykla:/home/ykla # echo $VISUAL
/usr/bin/ee
```

Regular security update

```sh
# freebsd-update fetch
```

When information similar to:

```sh
usrlinclude/c++/vl/trllvector usrlinclude/c++/vl/trllversion usrlinclude/c++/v1/trl/wchar.h usr/include/c++/v1/tr1/wctype.h usrlinclude/c++/vllunwind-armh
usrlinclude/c++/v1/unwind-itaniumh usrlinclude/c++/vllunwindh
usr/include/crypto/ cryptodevh usrlinclude/crypto/cbcmac.h usr/include/crypto/deflate.h usrlinclude/crypto/gfmult.h usr/include/crypto/gmac.h
usr/include/crypto/rijndael.h usrlinclude/crypto/rmd160.h usr/include/crypto/xform.h
usr/lib/clang/11.0.1/include
:
```

YOU JUST HAVE TO ENTER CODESPAN_0_BACK TO THE CAR. THEN:

```sh
# freebsd-update install
```

# # Size update #

Note**
>
The >__CODESPAN_0_ download is not slow because the source of the update is outside the country (as is the case when you use an offshore server to update; and in the days when the source is valid in freebsdcn). Probably because of its design deficiencies. [It's always a problem]。

** Take FreeBSD 14.1-RELEASE Upgrade 14.2-RELEASE**

NOW UPDATE TO ___CODESPAN_0_:

```sh
# freebsd-update upgrade -r 14.2-RELEASE
```


When information similar to the following appears, act on the bottom hint:

```sh
root@ykla:/home/ykla # freebsd-update upgrade -r 14.2-RELEASE
src component not installed, skipped
Looking up update.FreeBSD.org mirrors... 3 mirrors found.
Fetching metadata signature for 14.1-RELEASE from update2.freebsd.org... done.
Fetching metadata index... done.
Fetching 1 metadata patches. done.
Applying metadata patches... done.
Fetching 1 metadata files... done.
Inspecting system... done.

The following conventions of FreeBSSD seem to be updated:
kernel/generic kelnel/generic-dbg world/base world/lib32

The following companies of FreeBSD do not seem to be involved:
world/base-dbg world/lib32-dbg

Does this look relevant (y/n)。

Fetching metada signature for 14.2-RELEASE from update2.freebsd.org...doe.
Fetching metadata index... done.
Fetching 1 metadata matches.
Applying metadata matches... done.
Fetching 1 metadata fields... done.
Inspecting system... done。
Fetching files from 141-RELEASE for changing... done.
Preparing to download files..。
# It needs to wait about 30 minutes below. It's normal to wait five hours longer when you're going to have to update a big version。
Fetching 4070 watches....10....20...30...40...

* Reissued for technical reasons

4000 4010 4020 4030 4040 4050 4060 4070 done.
Fetching 35 files.10.20.30.doe
Atting to automatically change in files... done.

The following changes, which accepted between FreeBSD 14.1-RELEASE and
FreeBSD 14.2-RELEASE have been made into/etc/ssh/sshd_config:
could not close temporary folder: %s
++ new version
@-103, 11 + 103, 11 @
#PidFile/var/run/sshd.pid
#MaxStartups 10:30:100
#PermitTunnel no
# ChootDirectory none
#UseBlacklist no
- #VersionAddendum FreeBSD-20240318
+VersionAddendum FreeBSD-202440806

# no different banner path
# Banner none

# override default of no subsystems
Does this look relevant (y/n)。
The following fields will be moved as part of updating to
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
* Reissued for technical reasons
/usr/share/examples/son/sndstat_nv.c
: # enter q here to confirm the change until no new content appears

* Reissued for technical reasons

The following files will be updated as part of updating to
14.2-RELEASE-p0:
/bin/[
/bin/cat
/bin/chflags

* Reissued for technical reasons

/bin/ln
/bin/ls
/bin/mkdir
To begin the downloaded upgrades, run 'freebsd-update [options] install'.
````

RUN __CODESPAN_0_ TO INSTALL UPDATES:

```sh
root@ykla:/home/ykla # freebsd-update install
src component not installed, skipped
Creating snapshot of existing boot environment... done.
Installing updates...
Kernel updates have been installed.  Please reboot and run
'freebsd-update [options] install' again to finish installing updates.
```

The kernel upgrade has been installed and the system requires a restart:

```sh
root@ykla:/home/ykla # reboot
```

RUN __CODESPAN_0_ INSTALL AN UPDATED USER SPACE SECTION:

```sh
# freebsd-update install
src component not installed, skipped
Creating snapshot of existing boot environment... done.
Installing updates...
Restarting sshd after upgrade
Performing sanity check on sshd configuration.
Stopping sshd.
Waiting for PIDS: 868.
Performing sanity check on sshd configuration.
Starting sshd.
Scanning /usr/share/certs/untrusted for certificates...
Scanning /usr/share/certs/trusted for certificates...
Scanning /usr/local/share/certs for certificates...
 done.
```


RELOAD __CODESPAN_0_:


```sh
root@ykla:/home/ykla # pkg bootstrap -f
The package management tool is not yet installed on your system.
Do you want to fetch and install it now? [y/N]: y # 此处输入 y 后回车
Bootstrapping pkg from https://mirrors.nju.edu.cn/freebsd-pkg/FreeBSD:14:amd64/latest, please wait... # 我换过 pkg 源，你可能和我不一样，没有问题
Installing pkg-1.21.3...
package pkg is already installed, forced install
Extracting pkg-1.21.3: 100%
```

Checking third-party software ABI changes (FreeBSD ABI is very stable, usually without error):

```sh
root@ykla:/home/ykla # pkg upgrade
root@ykla:/home/ykla # pkg upgrade
Updating nju repository catalogue...
Fetching meta.conf:   0%
Fetching data.pkg: 100%    7 MiB   7.6MB/s    00:01    
Processing entries: 100%
nju repository update completed. 35765 packages processed.
All repositories are up to date.
Updating database digests format: 100%
Checking for upgrades (215 candidates): 100%
Processing candidates (215 candidates): 100%
The following 223 package(s) will be affected (of 0 checked):

New packs to be INSTRAW:
ceres-solver: 2.2.0_10

* Reissued for technical reasons

The process will release 45 MiB more space.
687 MiB to be downloaded.

-Proceed with this action

The following omissions
````


That's it。

Verify update:

```sh
root@ykla:/home/ykla # freebsd-version -k
14.2-RELEASE
root@ykla:/home/ykla # freebsd-version -u
14.2-RELEASE
```

# # UPDATE EFI GUIDE

>** Warning**
>
> THE EFI-GUIDED SYSTEM, EFI-SYSTEM PARTITION (ESP) CONTAINS A COPY OF THE PILOT LOADING PROGRAM FOR SOLIDWARE-GUIDED KERNEL. IF THE ROOT FILE SYSTEM IS ZFS, THE LEAD LOADER MUST BE ABLE TO READ THE ZFS GUIDE FILE SYSTEM. AFTER THE SYSTEM IS UPGRADED AND BEFORE __CODESPAN_0_IS EXECUTED, THE GUIDANCE LOADER ON THE ESP MUST BE UPDATED, OTHERWISE THE SYSTEM MAY NOT BE ABLE TO GUIDE. ALTHOUGH NOT MANDATORY, THE SAME SHOULD BE TRUE OF UFS AS THE ROOT FILE SYSTEM。

YOU CAN USE THE COMMAND __CODESPAN_0_ TO DETERMINE THE LOCATION OF THE CURRENT PILOT LOAD. THE VALUE __CODESPAN_1_ IS THE NUMBER OF THE CURRENT GUIDANCE CONFIGURATION USED TO GUIDE THE SYSTEM. THE CORRESPONDING ENTRY OF THE OUTPUT STARTS WITH __CODESPAN_2_, IF

```sh
root@ykla:~ # efibootmgr -v
Boot to FW : false
BootCurrent: 0004
BootOrder  : 0004, 0000, 0001, 0002, 0003
+Boot0004* FreeBSD HD(1,GPT,f83a9e2f-bd87-11ef-95b7-000c29761cd2,0x28,0x82000)/File(\efi\freebsd\loader.efi) # 就是这条
                      nda0p1:/efi/freebsd/loader.efi (null)
 Boot0000* EFI VMware Virtual NVME Namespace (NSID 1) PciRoot(0x0)/Pci(0x15,0x0)/Pci(0x0,0x0)/NVMe(0x1,00-00-00-00-00-00-00-00)
 Boot0001* EFI VMware Virtual IDE CDROM Drive (IDE 1:0) PciRoot(0x0)/Pci(0x7,0x1)/Ata(Secondary,Master,0x0)
 Boot0002* EFI Network PciRoot(0x0)/Pci(0x11,0x0)/Pci(0x1,0x0)/MAC(000c29761cd2,0x0)
 Boot0003* EFI Internal Shell (Unsupported option) MemoryMapped(0xb,0xbeb4d018,0xbf07e017)/FvFile(c57ad6b7-0515-40a8-9d21-551652854e37)


Unreferenced Variables:
````

ESP should have been mounted to **/boot/efi**. If not, it can be mounted manually, using __CODESPAN_0_ for the divisions listed in the output (this example is __CODESPAN_1): __CODESPAN_2_. For another example, see [i don't know] (https://man.freebsd.org/cgi/man.cgi?query=loader.efi&sektion=8&format=html)。

The value of `File`_ in the output field of __CODESPAN_1_, e. g. __CODESPAN_2_, is the location of the guidance load that is being used on the EFI. If the mount point is **/boot/efi**, the document is __CODESPAN_3_. Another common value for CODESPAN_5 __, of which __CODESPAN_6 __ is amd64 (i.e. __CODESPAN_7 __), aarch64 (i.e. __CODESPAN_8 __) or riscv64 (i.e. __CODESPAN_9 __) if not configured. **/boot/loader.efi** should be copied to the correct path in **/boot/efi** to update the configured and default guided loader。

---|---

{\i1 \cH30D3F4}It's bullshit up there


After the version is updated, the following image may appear before the start-up menu appears

Note**
>
> This interface appears for a very short period of about 20 ms. You can use a camera to take an observation。

[loader update hint interface]

Name

```sh
**************************************************************
**************************************************************
*****                                                    *****   
*****      BOOT LOADER IS TOO OLD, PLEASE UPGRADE.       *****
*****                                                    *****
**************************************************************
************************************************************** 
```

this means loader needs to be updated. you can also use the command to verify the version:

```sh
# strings /boot/efi/efi/freebsd/loader.efi|grep FreeBSD|grep EFI
DFreeBSD/amd64 EFI loader, Revision 1.1
# strings /boot/loader.efi|grep FreeBSD|grep EFI
DFreeBSD/amd64 EFI loader, Revision 3.0
```

The order refers to examples from the manual [i don't know] (https://man.freebsd.org/cgi/man.cgi?query=loader.efi). __CODESPAN_0_ for the use of loader

Update:

```sh
# cp /boot/loader.efi /boot/efi/efi/freebsd/
```

>** Warning**
>
> Please update the loader, then update the ZFS version

>** Important**
>
> Non-EFI, Bootcode, ZFS, etc


# Optional update #


# View FreeBSD version

> **Note:**
>
> SOMETIMES THE PATCH DOES NOT INVOLVE THE KERNEL, THE KERNEL VERSION DOES NOT CHANGE, IT IS NOT VISIBLE WITH __CODESPAN_0_, BUT THE USER SPACE VERSION CHANGES. SO YOU MIGHT SEE TWO VERSIONS, WHICHEVER IS HIGHER。

# freebsd-version command

View FreeBSD kernel version and patch number:

```sh
ykla@ykla:~ % freebsd-version -k
13.1-RELEASE-p3
```

View installed user space version and patch program level:

```sh
ykla@ykla:~ % freebsd-version -u
13.1-RELEASE-p5
```

# # uname command

```sh
ykla@ykla:~ % uname -a
FreeBSD ykla 13.1-RELEASE FreeBSD 13.1-RELEASE releng/13.1-n250148-fc952ac2212 GENERIC amd64
```

```sh
ykla@ykla:~ % uname -mrs
FreeBSD 13.1-RELEASE amd64
```

# Fragmentation and unfinished business

# Roll back #

```sh
# freebsd-update rollback
```

# # pkg could not find __CODESPAN_0_

Terminal Execute Command

```sh
# pkg bootstrap -f
```

No ntp user

Terminal Execute Command

```sh
# pw groupadd ntpd -g 123
# pw useradd ntpd -u 123 -g ntpd -h - -d /var/db/ntp -s /usr/sbin/nologin -c "NTP Daemon"
```
