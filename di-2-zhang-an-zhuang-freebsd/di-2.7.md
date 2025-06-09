# Section 2.7 Manually install dual systems (first FreeBSD)

Note**
>
>This document requires the installation of FreeBSD and the installation of Windows or other operating systems。

# Install FreeBSD 14.2 RELEASE

All normal settings and parameters are not specified here。

![..gitbook/assets/shuang1.png]

![.. .gitbook/assets/shuang2.png]

>** Skills**
>
> IF __CODESPAN_0 IS SET HERE AS __CODESPAN_1 AND NOT (ONLY OLD COMPUTERS NEED __CODESPAN_2_ ETC.), THE SUBSEQUENT PARTITION AND SYSTEM UPDATE PROCESS WILL BE SIMPLER AND CAN ACHIEVE 4K ALIGNMENT。


![.. ..gitbook/assets/shuang3.png]

Resize __CODESPAN_0_ at this step (calculated by swap size + Windows size)。

In this paper, Swap accounts for 8G, while the other 200G is left to Windows。

![.. .getbook/assets/shuang4.png]


View disk partitions:

```sh
root@ykla:/home/ykla # gpart show
=>     9  639659  cd0  MBR  (1.2G)
       9  639659       - free -  (1.2G)

>9 639659 iso966014_2_RELEASE_AMD64_CD MBR(1.2G)
9 639659 - free - (1.2G)

= >40 62914520 nda0 GPT (300G)
40 532480 1 efi (260M)
532520 1024 2 freebsd-boot (512K)
53344 984 - free - (492K)
534528 436207616 3 freebsd-swap (208G)
436742144 1924008 4 freebsd-zfs (92G)
629143552 2008 - free - (1.0M)

```

View swap partitions:

```sh
root@ykla:/home/ykla # swapinfo -mh
Device              Size     Used    Avail Capacity
/dev/nda0p3          208G       0B     208G     0%
```

YOU CAN SEE THE SIZE OF THE SWAP SECTION THAT WE SET AT 208 GB。

Edit __CODESPAN_0, add __CODESPAN_1 at the top of the line of swap, for the third line of this example:

```sh
# Device                Mountpoint      FStype  Options         Dump    Pass#
/dev/gpt/efiboot0               /boot/efi       msdosfs rw              2       2
#/dev/nda0p3             none    swap    sw              0       0
```

# Install Windows 11

Inserts Windows starter, sets the BIOS from which to start, and starts installing Windows。

![.. ..gitbook/assets/shuang5.png]

When partitioning, delete (Delete Partition) the entire 208G swap (in this example, " Disk 0 Division 3 " )。

![.. ..gitbook/assets/shuang6.png]

Click to create partition (Create Partition) and click to refresh (Refresh) if you have an error in hinting。

SELECT THE " DISK 0 UNALLOCATED SPACE " FOR 208G, CLICK " NEXT " FOR INSTALLATION。

![./.gitbook/assets/shuang7.png]

# Revert Swap

We set up 208 G, and obviously 8 G was created for swap. Now it needs to be restored. You need to use [i'm sorry] (https://www.disskgenius.com/)。

![.. ..gitbook/assets/shuang8.png]

Opens disskgenius, compresses the C disc, emptys the remaining 8G space。

![.. ..gitbook/assets/shuang9.png]


FORMATS THE REMAINING 8G SPACE INTO __CODESPAN_0_, THEN CLICK SAVE CHANGES。

![.. ..gitbook/assets/shuang10.png]

![.. ..gitbook/assets/shaung11.png]

Back to FreeBSD, check disk:

```sh
root@ykla:/home/ykla # gpart show
=>       34  629145533  nda0  GPT  (300G)
         34          6        - free -  (3.0K)
         40     532480     1  efi  (260M)
     532520       1024     2  freebsd-boot  (512K)
     533544        984        - free -  (492K)
     534528      32768     3  ms-reserved  (16M)
     567296  417953792     4  ms-basic-data  (199G)
  418521088   16777216     5  freebsd-swap  (8.0G)
  435298304    1441792     6  ms-recovery  (704M)
  436740096       2048        - free -  (1.0M)
  436742144  192401408     7  freebsd-zfs  (92G)
  629143552       2015        - free -  (1.0M)

```

as you can see, nda0p5 is our new swap. test it out:

```sh
root@ykla:/home/ykla # swapon /dev/nda0p5
```

There were no errors and no hints of normality。

Edit __CODESPAN_0, remove __CODESPAN_1_1_ in front of the line swap, and correct the partition as follows:

```sh
# Device                Mountpoint      FStype  Options         Dump    Pass#
/dev/gpt/efiboot0               /boot/efi       msdosfs rw              2       2
/dev/nda0p5             none    swap    sw              0       0
```

Start testing again:

```sh
root@ykla:/home/ykla # swapinfo -mh
Device              Size     Used    Avail Capacity
/dev/nda0p5         8.0G       0B     8.0G     0%
```

VIEW ZFS ROLLS:

```sh
root@ykla:/home/ykla # zpool list
NAME    SIZE  ALLOC   FREE  CKPOINT  EXPANDSZ   FRAG    CAP  DEDUP    HEALTH  ALTROOT
zroot  91.5G   922M  90.6G        -         -     0%     0%  1.00x    ONLINE  -
root@ykla:/home/ykla # zfs list
NAME                 USED  AVAIL  REFER  MOUNTPOINT
zroot                922M  87.8G    96K  /zroot
zroot/ROOT           919M  87.8G    96K  none
zroot/ROOT/default   919M  87.8G   919M  /
zroot/home           224K  87.8G    96K  /home
zroot/home/ykla      128K  87.8G   128K  /home/ykla
zroot/tmp            104K  87.8G   104K  /tmp
zroot/usr            288K  87.8G    96K  /usr
zroot/usr/ports       96K  87.8G    96K  /usr/ports
zroot/usr/src         96K  87.8G    96K  /usr/src
zroot/var            668K  87.8G    96K  /var
zroot/var/audit       96K  87.8G    96K  /var/audit
zroot/var/crash       96K  87.8G    96K  /var/crash
zroot/var/log        188K  87.8G   188K  /var/log
zroot/var/mail        96K  87.8G    96K  /var/mail
zroot/var/tmp         96K  87.8G    96K  /var/tmp
```

