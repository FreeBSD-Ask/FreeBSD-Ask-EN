# Section 2.12 Cloud Server Installation FreeBSD


# virtual machine using virtio technology semi-virtual

> ** Note**
>
> The following are for information purposes only and are to be tested. If your test passes, let us know

According to feedback, the installation or upgrading of FreeBSD on semi-virtual platforms such as VMware EXSI (e.g., if there is a problem with the virtio-blk drive) requires **ESC** on start-up, and then enter __CODESPAN_0_back, then enter __CODESPAN_1_. When installed, __CODESPAN_2_ will need to be added __CODESPAN_3_ to avoid duplication of operations at each start. Once the Alion upgrade has been completed, it may be necessary to restart and re-enter the VNC at a time when such problems are stuck in the lead interface。

> ** Note**
>
> ** For a version that is no longer supported by security, such as ___CODESPAN_0, please refer to this document and install the FreeBSD chapter manually. **

>** Warning**
>
>** Read your IP and netmask on the old Linux system before installation and view the gateway information using commands __CODESPAN_0 and __CODESPAN_1_. Since some servers do not use DHCP services, they need to specify an IP manually. **

# Video tutorial

[08 - Light Cloud and other servvers included FreeBS] (https://www.bilibili.com/video/BV1y8411d7pp)


There's a difference between the video and the curriculum, either way. SCP commands can be replaced by graphical Winscp. Finally, it is recommended that key login be set along with other chapters and that password authentication be banned to enhance security。


# General

[Light application service (i.e. light system)] (https://cloud.tencent.com/product/lighthouse) and [Ariyun Light Application Server] (https://www.aliyun.com/product/swas) are not supported by the FreeBSD system and can only be installed through violence through special methods。


>** Warning**
>
> Please note the data security, the following curriculum is dangerous and requires you to have some ability to do it。

There are no FreeBSD mirrors on the server panel mentioned above, so we have to install them in an alternative way. Because the kernels for FreeBSD and Linux are not universal and the executables are not universal, they cannot be installed by chroot and then delete the source system. The method of installation is to start the FreeBSD system in the memory disk, by installing [mfsBSD] (https://mfsbsd.vx.sk) and then formatting the hard drive to install the new system. mfsBSD is a fully RAM-enabled FreeBSD system, similar to the Windows-like PE system。

We need to download [mfsBSD mirror in img format] (https://mfsbsd.vx.sk/files/images/14/amd64/mfsbsd-se-14.2-RELEASE-amd64.img), which can be ready in advance and then re-enter the server with WinSCP, which may take two hours to download directly。


# Use mfsLinux to write mfsBSD

As mentioned above, and because FreeBSD and Linux are different ecologys, we need to go to Linux's memory disk, then write mfsBSD into the memory and install the system through __CODESPAN_0_。

At the bottom of the mfsBSD download position is [mfsLinux] (https://mfsbsd.vx.sk/files/iso/mfslinux/mfslinux-0.111-94b1466.iso), which is the Linux we want. Because it only has an ISO format, it cannot be activated directly in the current environment, because it is of a pure initrd type, we remove the initrd and kernel that activates it and start it manually on the hard drive。

In the general Linux system, initrd is a small and complete Linux root directory packed into a memory disk, which can load a drive, mount a hard drive and contain the necessary data to start the initialization process. Bootloader loads kernels and initrd at the start of the operation by a script in initrd and then runs the initialization program in the hard drive。

First, we place the kernel and initrd files extracted from the ISO under the root directory, and then restart the machine into the GRUB command line interface (can enter the editing mode at __CODESPAN_0_, delete __CODESPAN_1_, __CODESPAN_2_, and then press __CODESPAN_3_ to load) and manually activate the specified kernel and initrd (can be filled with __CODESPAN_4_). Then enter __CODESPAN_5 and return to the car to start the operating system。

```sh
linux (hd0,msdos1)/vmlinuz
initrd (hd0,msdos1)/initramfs.igz
boot # 输入 boot 后回车即可继续启动
```

>** Skills**
>
> not necessarily ** (hd0, msdos1)**, in the light of actual facts, not to delete everything that does not appear。

![.. ..gitbook/assets/2.png]

This specially designed initrd started without loading the original system on the hard drive, but instead connected itself to the network and opened the SSH server. So we got a run-in Linux system。

this should be time to use the ssh to connect to the server and to format the hard drive safely。

mfsBSD and mfsLinux mirror `root`_ password is `mfsroot`_

```sh
# cd /tmp # 切换到临时路径
# wget https://mfsbsd.vx.sk/files/images/14/amd64/mfsbsd-se-14.2-RELEASE-amd64.img # 下载 mfsbsd
# dd if=mfsbsd-se-14.2-RELEASE-amd64.img of=/dev/vda # 你可以看下你是不是 /dev/vda
# reboot # 重启
```

>** Skills**
>
>It is recommended that the server be backed up here using the server's "scanning" function in case the following tutorials fail again。

# Install FreeBSD

the ssh connects to the server and uses __CODESPAN_0_to load the zfs module and then runs __CODESPAN_1_, and enters the specified version of the mirror in the image (in the address, you can change it yourself if you have):

Example: <https://mirrors.ustc.edu.cn/freebsd/releases/amd/64/14.2-RELEASE/> or <https://mirrors.nju.edu.cn/freebsd/snapshots/amd/64/15.0-CURRENT/>

[FreeBSD integration of light club and other servicers]

[FreeBSD integration of light claud and other services] (. .gitbook/assets/installBSD2.png)

[FreeBSD integration of light claud and other servicers] (. .gitbook/assets/installBSD3.png)


- We can also manually download FreeBSD installation files, for example ___CODESPAN_0_:

```sh
# mkdir -p /usr/freebsd-dist # 创建目录
# cd /usr/freebsd-dist # 切换目录
# fetch http://ftp.freebsd.org/pub/FreeBSD/releases/amd64/14.2-RELEASE/MANIFEST # 下载所需文件
```

# Fragmentation and unfinished business

- why not just dd? (fault demonstration, only for illustration, please do not execute)

Directly put mfsBSD img dd in the hard drive in the normal Linux system, and after restarting, although it is normal to load bootloader, it may not be possible to mount the memory disk properly because the system has written the hard drive again。

```sh
# wget https://mfsbsd.vx.sk/files/images/13/amd64/mfsbsd-se-13.1-RELEASE-amd64.img -O- | dd of=/dev/vda
```

Explanation:

- __CODESPAN_0 __ IS A CONDUIT THAT USES THE STANDARD OUTPUT OF THE PREVIOUS COMMAND AS THE STANDARD INPUT FOR THE NEXT COMMAND
- `-O-` refers to downloading a file into a standard output, while dd automatically reads content from a standard input when no specified if

dd reports errors as follows:

![.. ..gitbook/assets/1.png]


- If there's a cloud server with Ivm, you need to put it all in ___CODESPAN_0, otherwise the Grub and mfslinux can't open。

# References

- [Remote Information of the FreeBSD Operation A Remote Console] (https://docs.freebsd.org/en/articles/remote-intall/)

