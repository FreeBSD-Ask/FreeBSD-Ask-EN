Section 2.8 Manual installation of dual systems (after installation of FreeBSD)

This paper is based on `FreeBSD-14.2-RELEASE-amd64-disc1.iso ' , which demonstrates the installation of two systems in the UEFI environment, FreeBSD 14.2 RELEEASE and Windows 11 24H2.

>** Skills**
>
>The example of this paper requires the installation of other operating systems, followed by the installation of FreeBSD.

# Simple method (no data sets available)

> ** Note**
>
> When using ZFS in this part, only a zpool called `root ' will be created and mounted directly to `/ ' . `zroot/ROOT/default ' and numerous data sets will not be created like automatic installation. You can create datasets later for replacement, but if you want to use the same layout as automatically installed at the start of the installation, jump to this section of the Shell partition.

First, there is a need to leave room for FreeBSD on the hard drive: it is not necessarily required at the end of the hard drive, or in the middle of the hard drive, since the normal Windows installation of the last partition (as `nda0p4 ' in this case) is the restoration of the partition. After the partition is completed under FreeBSD, it looks like this:

```sh '
# Gpart show
= >344194303333 nda0 GPT(200G)
34 2014 - free - (1.0M)
2048 204800 1 efi (100M)# EFI partition
206848 32768 2 ms-reserved (16M)# MSR Division
239616 207992832 3 ms-basic-data (99G) Now, there's 100 G left between the C drive and the restoration section.
417947648 1478656 4 ms-recovery (722M)# Rehabilitation of partitions
419426304 4063 - free - (100G)
````

You should turn off secure start-up and quick start -- or you can start from the Windows Settings -- > Windows Updates -- > Advanced Options -- > Restore -- > Advanced Start-up Options from UCD Devices. FreeBSD is then normally directed to the installation process until the partition is selected.

![.. ..gitbook/assets/shuangxitong1.png]

Select `Manual 'here

>** Skills**
>
> This is actually the software `sade ' (sysadmins dissk editor, system administrator disk editor), and `bsdconfig ' is also called.

Here you can see the hard drive partition. There is only one hard drive: the EFI partition with 300M, the MSR partition with 16M, the Windows partition with 64G (i. e. the C disc) and the empty space not shown. Select `Create ' (creation) directly.

![..gitbook/assets/shuangxitong2.png]

Here, enter the type of partition in the first line (i.e. `Filesystem type' below). If you want to add swap partitions, add them first, and then add partition sizes that are difficult to control. When adding UFS, ZFS, add `/ ' to the `Montpoint ' to the list indicating that the partition will be mounted to `/ ' . `Label ' is a volume label for FreeBSD that facilitates the identification of partitions, which may or may not be filled out as appropriate. Use ZFS here, do not add swap partitions and fill in the volume label `zroot '.

![..getbook/assets/shuangxitong3.png]

Use **TAB** to select to `OK ' to press back.

![..gitbook/assets/shuangxitong4.png]

This will warn that the ZFS partition cannot be activated, but it is determined that it can be started normally, choosing `Yes ' to ignore:

![. . . .gitbook/assets/shuangxitonong5.png]

Select `Finish '(completed)

![.. ..gitbook/assets/shuangxitonong6.png]

Select `Commit ' (confirm)

![..gitbook/assets/shuangxitong7.png]


This will be followed by the normal installation process. Upon installation:

```sh '
# zfs list
NAME USED AVAIL REFER MOUNTPOINT
Root 534M 130G 534M nont
````

Once in the system, it can be seen that there is only one `root ' data set. Manually, you can change the data set to an automatic installation, and you can also use the following as a reference for partitioning into shell at installation.

# Shell partition

Still proceed to partition selection, choose `Shell '

![.. ..gitbook/assets/shuangxitong9.png]

Then we'll enter TTY:

![.../.gitbook/assets/shuangxitong10.png]

Execute the following orders.

# # Load ZFS kernel module

```sh '
# kldload zfs
````

## Configure ZFS alignment (impacting only newly created hard disk partitions)

```sh '
# Force 4K Alignment
#sysctl vfs.zfs.vdev.min_auto_ashift=12
Vfs.zfs.vdev.min_auto_ashift: 9 - > 12
````

>** Skills**
>
> `12 ' or 2^12 = 4096 bytes (4KB) sector size. The default parameter (the default parameter for `sysctl vfs.zfs.vdev.min_auto_ashift ' can see ISO) is `9 ' , i.e. 2^9 = 512 bytes.

>** Thinking issues**
>
>If you use NVME, the default parameter for normal new loading system (UEFI+GPT, without freebsd-boot partition) should be `12 '. But what exactly is 4K alignment? Because SSD solid hard drives are not called fan zones.

Create partitions

```sh '
# Create swap partition (-t), volume marked swap(-l), size 4G(-s), alignment (-a), note to replace nda0
# Gpart add-a 4k-l swap-s 4G-t freebsd-swap nda0

# Create ZFS partition, volume marked zroot, use all available space, and be careful to replace nda0
# Gpart add-a 4k-l zroot-t freebsd-zfs
````

# # See partitions

```sh '
# Gpart show
= >344194303333 nda0 GPT(200G)
34 2014 - free - (1.0M)
2048 204800 1 efi (100M)
206848 32768 2 ms-reserved (16M)
239616 207992832 3 ms-basic-data (99G)
208232448 8388608 5 freebsd-swap (4.0G)
216621056 201326592 6 freebsd-zfs (96G)
417947648 1478656 4 ms-recovery (722M)
419426304 4063 - free - (2.0M)
````

# # Mounting temporary file system ready for installation

```sh '
# Mount-tmpfs #
````

Create ZFS pool

```sh '
# Creates the ZFS pool, temporarily mounts to /mnt (-o altroot=/mnt) and uses lz4 compression (-O compress=lz4). /dev/gpt/zroot is our new volume label
# zpool create-f-o altroot # mnt-O companies #
````

## Create ZFS dataset

```sh '
# Create a root data set
# zfs create-o mountain point #
# Create a data set called `zroot/ROOT ' without setting a mount point (`mountpoint=none ' ), which is usually used as a root data set at the bottom of the system and can be used to create a sub-data set below.

# Create default root dataset
# zfs create-o trackpoint=/ zroot/ROOT/default
# Create a data set called `zroot/ROOT/default ' and load it to the root directory `/ ' for the default root file system of the system.

# Create /home data sets
# zfs create-o mountain point #
# Create a data set called `zroot/home ' and mount it to `/home ' , which is usually used to store the user home directory.

# Create /tmp data set, setting exec on, setuid on off
♪ zfs create-o mountainpoint=tmp-o exec=on-o setuid=off zroot/tmp
# Creates the `zroot/tmp ' dataset and mounts it to `/tmp ' to allow the execution document (`exec=on ' ), but disables the setuid (`setuid=off ' ) to prevent files in this directory from using sutuid to enhance their privileges.

# Create /usr data sets and set canmount as off
# zfs create-o trackpoint #
# Create the `zroot/usr ' data set and mount it to `/usr ' , but because of the `canmount = off ' set, the data set will not be automatically mounted, usually for specific system configurations.

# Create /usr/ports dataset, set settuid as off
# zfs create-o set=off zroot/usr/ports

# Create /usr/ src data sets
# zfs create zroot/usr/src

# Create / var data sets, set canmount as off
# zfs create-o mountain point #

# Create / var/udit dataset, set exec and setuid as off
# zfs create-o exec #

# Create / var/ crush data sets, set exec and setuid as off
# zfs create-o exec #

# Create / var/ log data sets, setting exec and setuid as off
# zfs create-o exec #

# Create / var/tmp dataset, set settuid as off
# zfs create-o setuid=off zroot/var/tmp

# Create / var/mail dataset, set atime on
# zfs create-o age #
# Create `zroot/var/mail ' datasets and set up `atime=on ' , which means that access times are updated every time a document is read, usually to store mail data.
````

>** Skills**
>
>Bsdinstall (8) (https://man.freebsd.org/cgi/man.cgi?bsdinstall(8)). You can also view `zfs get exec, setuid, mountainpoint ' in the installed system. The code is located in src `/usr.sbin/bsdinstall/scripts/zfsboot ' .

# # Modify folder privileges

```sh '
# Modify the /mnt/tmp and /mnt/var/tmp privileges to 1777 to ensure that temporary directory privileges are correct
#chmod 1777/mnt/tmp
#chmod 1777/mnt/var/tmp
````

# Set exchange partition to `fstab '

````
# Configure swap partition mounted, note to replace /dev/nda0p5 with command group show nda0
#printf "/dev/nda0p5\tone\tswap\tsw\tsw> /tmp/bsdinstall_etc/fstab
````

>** Skills**
>
> `t ' is a transliterated character, which means that the Tab key was pressed once, and this is used to split it in alignment, and the same effect is given to the space. You can also use the ee editor to manually write corresponding entries (`ee /tmp/bsdinstall_etc/fstab ' ):
>
> ```sh '
>/dev/nda0p5 none swap sw 0 0
> ````
>
> Same.

# # Set starter with UEFI

````
# Set ZFS boot path to zroot/ ROOT/default
# zpool set Boots=zroot/ROOT/default zroot

# Configure FreeBSD to load ZFS1 on startup
# printf 'zfs_enable="YES"\ /tmp/bsdinstall_etc/rc.conf

# Mount EFI system partition
# Mount the existing EFI partition, note to replace /dev/nda0p1
# Mount -t msdosfs/dev/nda0p1/media

Create a startup directory in the EFI system partition
#mkdir-p/media/efi/freebsd

# Copy EFI startup file to EFI system partition
#cp/boot/loader.efi/media/ef/freebsd/

# Add UEFI startup with efibootmgr
# efibootmgr-create-activate-label "FreeBSD"-loader "/media/efi/freebsd/loader.efi"

# Unmount EFI partition
♪ Unmount / Media
# Exit shell, FreeBSD will continue to install the process
# Exit
````

- 1: `n ' represents the Unix break. The end of each paragraph in Windows is actually `r\n' — that is, to get back to the car and change the line. This is equivalent to `ee /tmp/bsdinstall_etc/rc.conf ' and insert `zfs_enable= "YES" ' .

# Finish

So we created the same structure manually as the automatic installation (except for `/home/username ' partitions).

```sh '
# zfs list
NAME USED AVAIL REFER MOUNTPOINT
Zroot 921M 91.6G 96K none
Zroot/ROOT 919M 91.6G 96K none
Zroot/ROOT/default 919M 91.6G 919M /
Zroot/home 128K 91.6G 128K/home
Zroot/tmp 104K 91.6G 104K/tmp
Zroot/usr 288K 91.6G 96K/usr
zroot/usr/ports 96K 91.6G 96K/usr/ports
Zroot/usr/src 96K 91.6G 96K/usr/src
Zroot/var 636K 91.6G 96K/var
Zroot/var/udit 96K 91.6G 96K/var/udit
Zroot/var/crash 96K 91.6G 96K/var/crash
Zroot/var/log 156K 91.6G 156K/var/log
zroot/var/mail 96K 91.6G 96K/var/mail
zroot/var/tmp 96K 91.6G 96K/var/tmp
````


# References

- [How to Manually effective FreeBSD on a remote server (with UFS, ZFS, encryption...)]
- [RootOnZFS/GPTZFSBoot] (https://wiki.freebsd.org/RootOnZFS/GPTZFSBoot)
