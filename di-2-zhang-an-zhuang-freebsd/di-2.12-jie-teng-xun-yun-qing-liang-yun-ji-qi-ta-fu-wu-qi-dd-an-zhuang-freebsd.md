# Section 2.12 Cloud Server Installation FreeBSD


# Virtual machine using virtio technology semi-virtual

> ** Note**
>
> The following are for information purposes only and are to be tested. If your test passes, let us know!

According to feedback, the installation or upgrading of FreeBSD on a semi-virtual platform such as VMware EXSI (e.g., if there is a problem with the virtio-blk drive) requires **ESC** on start-up and then enter `set kern.maxphys = 65536 `back and then enter `boot ' . Once installed, `kern.maxphys = 65536 ' would have to be added to `/boot/loader.conf ' to avoid duplication of operations at each turn-off. Once the Alion upgrade has been completed, it may be necessary to restart and re-enter the VNC at a time when such problems are stuck in the lead interface.

> ** Note**
>
> ** For versions no longer supported by security, such as `9.2 ' , please refer to this and install the FreeBSD chapter manually. **

>** Warning**
>
> ** Please look at your IP and netmask on the old Linux system before installation, using commands `ip addr ' and `ip route show ' to view gateway information. Since some servers do not use DHCP services, they need to specify an IP manually. **

# Video tutorial

[08 - Light Clouds and other Server Installations FreeBSD] (https://www.bilibili.com/video/BV1y8411d7pp)


There's a difference between the video and the curriculum, either way. SCP commands can be replaced by graphical Winscp. Finally, it is recommended that key login be set along with other chapters and that password authentication be banned to enhance security.


# General

[The telecommunication cloud light application server (i.e. the telecommunication cloud light cloud) (https://cloud.tencent.com/product/lighthouse) and [Ariyun light application server] (https://www.aliyun.com/project/swas) do not have the support of the FreeBSD system and can only be installed by their own violence through special methods.


>** Warning**
>
> Please note the data security, the following curriculum is dangerous and requires you to have some ability to do it.

There are no FreeBSD mirrors on the server panel mentioned above, so we have to install them in an alternative way. Because the kernels for FreeBSD and Linux are not universal and the executables are not universal, they cannot be installed by chroot and then delete the source system. The method of installation is to start the FreeBSD system in the memory disk, by installing [mfsBSD] (https://mfsbsd.vx.sk) and then formatting the hard drive to install the new system. mfsBSD is a fully RAM-enabled FreeBSD system, similar to the Windows-like PE system.

We need to download [mfsBSD mirrors in img format] (https://mfsbsd.vx.sk/files/images/14/amd64/mfsbsd-se-14.2-RELEASE-amd64.img), which can go down in advance and then use WinSCP to access the server, which may take two hours to download directly.


# Use mfsLinux to write mfsBSD

As mentioned above, and because FreeBSD and Linux are different ecologys, we need to go to Linux's memory disk, then write mfsBSD in Linux's memory and install the system through the `bsdinstall ' tool.

At the bottom of the mfsBSD download position is [mfsLinux] (https://mfsbsd.vx.sk/files/iso/mfslinux/mfslinux-0.111-94b1466.iso), which is the Linux we want. Because it only has an ISO format, it cannot be activated directly in the current environment, because it is of a pure initrd type, we remove the initrd and kernel that activates it and start it manually on the hard drive.

In the general Linux system, initrd is a small and complete Linux root directory packed into a memory disk, which can load a drive, mount a hard drive and contain the necessary data to start the initialization process. Bootloader loads kernels and initrd at the start of the operation by a script in initrd and then runs the initialization program in the hard drive.

First, we place the kernel and initrd files extracted from the ISO under the root directory, and then restart the machine into the GRUB command line interface (which can enter the editing mode by `e ' at countdown, delete the original content of the `linux ' and `initrd ' lines, and then load them by `Ctrl X ' ), and manually activate the specified kernel and initrd (which can be completed with the `Tab ' key). The `boot ' is then entered and the vehicle returns to continue with the operating system.

```sh '
llinux (hd0, msdos1)/vmlinuz
Initrd (hd0, msdos1)/initramfs.igz
Boot # Enter Boot and get back to work.
````

>** Skills**
>
> Not necessarily ** (hd0, msdos1)**, in the light of actual facts, not to delete everything that does not appear.

![.. ..gitbook/assets/2.png]

This specially designed initrd started without loading the original system on the hard drive, but instead connected itself to the network and opened the SSH server. So we got a run-in Linux system.

This should be time to use the ssh to connect to the server and to format the hard drive safely.

mfsBSD and mfsLinux mirror password default is `mfsroot '

```sh '
# cd /tmp # switch to temporary path
#wget https://mfsbsd.vx.sk/files/images/14/amd64/mfsbsd-se-14.2-RELEASE-amd64.img #mfsbsd
# dd if=mfsbsd-se-14.2-RELEASE-amd64.img of=/dev/vda #
# Reboot
````

>** Skills**
>
>It is recommended that the server be backed up here using the server's "scanning" function in case the following tutorials fail again.

# Install FreeBSD

Ssh connects to the server using `kldload zfs 'to load the zfs module and then runs `bsdinstall ' , and points `Other ' to the specified mirror version of the `Other ' input diagram when the following pictures appear (the address is available, you can change it yourself):

Example: <https://mirrors.ustc.edu.cn/freebsd/releases/amd/64/14.2-RELEASE/> or <https://mirrors.nju.edu.cn/freebsd/snapshots/amd/64/15.0-CURRENT/>

FreeBSD (. .gitbook/assets/installBSD1.png)

FreeBSD (..gitbook/assets/installBSD2.png)

FreeBSD (. .gitbook/assets/installBSD3.png)


- We can also manually download FreeBSD installation files using the `MANIFEST ' file as an example:

```sh '
#mkdir-p /usr/freebsd-dist # Create directory
# cd /usr/freebsd-dist
#fetch http://ftp.freebsd.org/pub/FreeBSD/releases/amd/64/14.2-RELEASE/MANIFEST#
````

# Fragmentation and unfinished business

- Why not just dd? (fault demonstration, only for illustration, please do not execute)

Directly put mfsBSD img dd in the hard drive in the normal Linux system, and after restarting, although it is normal to load bootloader, it may not be possible to mount the memory disk properly because the system has written the hard drive again.

```sh '
#wgethttps://mfsbsd.vx.sk/files/images/13/amd64.img-O-dd of=dev/vda
````

Explanation:

- `| ' is the meaning of the conduit, using the standard output of the previous command as the standard input for the next command
- `-O- ' means downloading a file to a standard output, while dd automatically reads content from a standard input when no specified if

Dd reports errors as follows:

![.. ..gitbook/assets/1.png]


- If there is a cloud server with lvm, all of it needs to be placed in `/boot ' , otherwise the Grub and mfslinux cannot be opened.

# References

- (https://docs.freebsd.org/en/articles/remote-intall/)

