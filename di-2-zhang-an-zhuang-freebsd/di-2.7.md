# Section 2.7 Manually install dual systems (first FreeBSD)

Note**
>
>This document requires the installation of FreeBSD and the installation of Windows or other operating systems.

# Install FreeBSD 14.2 RELEASE

All normal settings and parameters are not specified here.

![..gitbook/assets/shuang1.png]

![.. .gitbook/assets/shuang2.png]

>** Skills**
>
> If `P Part Scheme ' is set here as `GPT (UEFI) ' instead of other (the only option that old computers need is `GPT (BIOS+UEFI) ' ), the subsequent partition and system update process will be simpler and can achieve 4K alignment.


![.. ..gitbook/assets/shuang3.png]

At this step, resize `S Swap Size ' (calculated as swap size + Windows size).

In this paper, Swap accounts for 8G, while the other 200G is left to Windows.

![.. .getbook/assets/shuang4.png]


View disk partitions:

```sh '
Root@ykla:/home/ykla #gpart show
= > 9 639659 cd0 MBR (1.2G)
9 639659 - free - (1.2G)

>9 639659 iso966014_2_RELEASE_AMD64_CD MBR(1.2G)
9 639659 - free - (1.2G)

= >40 62914520 nda0 GPT (300G)
40 532480 1 efi (260M)
532520 1024 2 freebsd-boot (512K)
53344 984 - free - (492K)
534528 436207616 3 freebsd-swap (208G)
436742144 1924008 4 freebsd-zfs (92G)
629143552 2008 - free - (1.0M)

````

View swap partitions:

```sh '
#swapinfo-mh
Device Size Used Avail Capability
/dev/nda0p3 208G 0B 208G 0%
````

You can see the size of the swap section that we set at 208 GB.

Edit `/etc/fstab ' , add `# ' at the top of the line of swap, in the third line of this example, as follows:

```sh '
# Device Mountain FStype Options Dump Pass #
/dev/gpt/efiboot0 /boot/efi msdosfs rw 2 2
#/dev/nda0p3 none swap sw 00
````

# Install Windows 11

Inserts Windows starter, sets the BIOS from which to start, and starts installing Windows.

![.. ..gitbook/assets/shuang5.png]

When partitioning, delete (Delete Partition) the entire 208G swap (in this example, " Disk 0 Division 3 " ).

![.. ..gitbook/assets/shuang6.png]

Click to create partition (Create Partition) and click to refresh (Refresh) if you have an error in hinting.

Select the " Disk 0 Unallocated Space " for 208G, click " Next " for installation.

![./.gitbook/assets/shuang7.png]

# Revert Swap

We set up 208 G, and obviously 8 G was created for swap. Now it needs to be restored. You need to use [disskgenius] (https://www.diskgenius.com/).

![.. ..gitbook/assets/shuang8.png]

Opens disskgenius, compresses the C disc, emptys the remaining 8G space.

![.. ..gitbook/assets/shuang9.png]


Format this 8G remaining space into `FreeBSD Swap Part ' and then click Save Changes.

![.. ..gitbook/assets/shuang10.png]

![.. ..gitbook/assets/shaung11.png]

Back to FreeBSD, check disk:

```sh '
Root@ykla:/home/ykla #gpart show
= >34 629145533 nda0 GPT (300G)
34 6 - free - (3.0K)
40 532480 1 efi (260M)
532520 1024 2 freebsd-boot (512K)
53344 984 - free - (492K)
534528 32768 3 ms-reserved (16M)
567296 417953792 4 ms-basic-data (199G)
4188521088 16777216 5 freebsd-swap (8.0G)
435298304 1441792 6 ms-recovery (704M)
436740096 2048 - free - (1.0M)
4367421444 1924008 7 freebsd-zfs (92G)
629143552 2015 - free - (1.0M)

````

As you can see, nda0p5 is our new swap. Test it out:

```sh '
Root@ykla:/home/ykla #swapon/dev/nda0p5
````

There were no errors and no hints of normality.

Edit `/etc/fstab ' , remove `# ' at the top of the line of swap and change the partition to correct in the third line of this example as follows:

```sh '
# Device Mountain FStype Options Dump Pass #
/dev/gpt/efiboot0 /boot/efi msdosfs rw 2 2
/dev/nda0p5 none swap sw 0
````

Start testing again:

```sh '
#swapinfo-mh
Device Size Used Avail Capability
/dev/nda0p5 8.0G 0B 8.0G 0%
````

View ZFS rolls:

```sh '
Root@ykla:/home/ykla #zpool list
NAME SIZE ALLOC FREE CAPOINT EXPANDSZ FRAG CAP DEDUP HEALTH ALTOROT
Zroot 91.5G 922M 90.6G - 0% 1.00x ONLINE -
# zfs list
NAME USED AVAIL REFER MOUNTPOINT
Zroot 922M 87.8G 96K /zroot
Zroot/ROOT 919M 87.8G 96K none
Zroot/ROOT/default 919M 87.8G 919M /
Zroot/home 224K 87.8G 96K/home
Zroot/home/ykla 128K 87.8G /home/ykla
zroot/tmp 104K 87.8G 104K /tmp
Zroot/usr 288K 87.8G 96K /usr
Zroot/usr/ports 96K 87.8G 96K/usr/ports
Zroot/usr/src 96K 87.8G 96K/usr/src
Zroot/var 668K 87.8G 96K/var
Zroot/var/udit 96K 87.8G 96K/var/udit
zroot/var/crash 96K 87.8G 96K/var/crash
Zroot/var/log 188K 87.8G 188K/var/log
Zroot/var/mail 96K 87.8G 96K/var/mail
zroot/var/tmp 96K 87.8G 96K/var/tmp
````

