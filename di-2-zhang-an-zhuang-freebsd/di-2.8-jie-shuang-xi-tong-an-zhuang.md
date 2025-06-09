Section 2.8 Manual installation of dual systems (after installation of FreeBSD)

This is based on __CODESPAN_0 and demonstrates the installation of two systems in the UEFI environment, FreeBSD 14.2 RELEASE and Windows 11 24H2。

>** Skills**
>
>The example of this paper requires the installation of other operating systems, followed by the installation of FreeBSD。

# Simple method (no data sets available)

> ** Note**
>
> When using ZFS in the way described in this part, only a zpool named __CODESPAN_0_ will be created and mounted directly to `/`_. Do not create ___CODESPAN_2_ and many data sets like automatic installation. You can create datasets later for replacement, but if you want to use the same layout as automatically installed at the start of the installation, jump to this section of the Shell partition。

FreeBSD needs to be left space on the hard drive first: not necessarily at the end of the hard drive, but also in the middle of the hard drive, because the normal Windows installation of the last partition (in this case __CODESPAN_0_) is the restoration of the partition. After the partition is completed under FreeBSD, it looks like this:

```sh
# gpart show
=>       34  419430333  nda0  GPT  (200G)
         34       2014        - free -  (1.0M)
       2048     204800     1  efi  (100M) # EFI 分区
     206848      32768     2  ms-reserved  (16M) # MSR 分区
     239616  207992832     3  ms-basic-data  (99G) # 这个是 C 盘，原先有 200G 这么大。现在 C 盘和恢复分区之间空余了 100G
  417947648    1478656     4  ms-recovery  (722M) # 恢复分区
  419426304       4063        - free -  (100G)
```

You should turn off secure start-up and quick start -- or you can start from the Windows Settings -- > Windows Updates -- > Advanced Options -- > Restore -- > Advanced Start-up Options from UCD Devices. FreeBSD is then normally directed to the installation process until the partition is selected。

![.. ..gitbook/assets/shuangxitong1.png]

SELECT __CODESPAN_0_

>** Skills**
>
>It's actually the software __CODESPAN_0_(sysadmins disk editor, system administrator disk editor), and __CODESPAN_1_。

Here you can see the hard drive partition. There is only one hard drive: the EFI partition with 300M, the MSR partition with 16M, the Windows partition with 64G (i. e. the C disc) and the empty space not shown. Select __CODESPAN_0_(create) directly。

![..gitbook/assets/shuangxitong2.png]

here, the first line enters the type of partition (i.e. __CODESPAN_0_, which will be listed below). If you want to add swap partitions, add them first, and then add partition sizes that are difficult to control. When adding UFS, ZFS, add `/` to __CODESPAN_3_. __CODESPAN_4_ is a volume label for FreeBSD that facilitates the identification of partitions and can be filled in or not filled out as appropriate. Use ZFS here, do not add swap partitions and fill in the volume label __CODESPAN_5_。

![..getbook/assets/shuangxitong3.png]

USE **TAB** TO SELECT __CODESPAN_0_ TO PRESS BACK。

![..gitbook/assets/shuangxitong4.png]

THIS WILL WARN THAT THE ZFS PARTITION CAN NOT BE ACTIVATED, BUT IT IS DETERMINED THAT IT CAN BE STARTED NORMALLY, AND CHOOSE __CODESPAN_0_ TO IGNORE:

![. . . .gitbook/assets/shuangxitonong5.png]

SELECT __CODESPAN_0_(COMPLETED)

![.. ..gitbook/assets/shuangxitonong6.png]

SELECT __CODESPAN_0_(CONFIRM)

![..gitbook/assets/shuangxitong7.png]


This will be followed by the normal installation process. Upon installation:

```sh
# zfs list
NAME  USED   AVAIL  REFER  MOUNTPOINT
root  534M    130G   534M  nont
```

When you enter the system, you can see that there is only one data set __CODESPAN_0_. Manually, you can change the data set to an automatic installation, and you can also use the following as a reference for partitioning into shell at installation。

# Shell partition

ORGANISATION

![.. ..gitbook/assets/shuangxitong9.png]

THEN WE'LL ENTER TTY:

![.../.gitbook/assets/shuangxitong10.png]

Execute the following orders。

# # LOAD ZFS KERNEL MODULE

```sh
# kldload zfs
```

## CONFIGURE ZFS ALIGNMENT (IMPACTING ONLY NEWLY CREATED HARD DISK PARTITIONS)

```sh
# 强制 4K 对齐
# sysctl vfs.zfs.vdev.min_auto_ashift=12
vfs.zfs.vdev.min_auto_ashift: 9 -> 12
```

>** Skills**
>
> __CODESPAN_0_I.E. 2^12 = 4096 BYTES (4KB) SECTOR SIZE. THE DEFAULT PARAMETER (COMMAND __CODESPAN_1 _ THE DEFAULT PARAMETER FOR SEEING ISO) IS __CODESPAN_2 __, I.E. 2^9 = 512 BYTES。

>** Thinking issues**
>
>If you use NVME, the default parameter for normal new loading system (UEFI+GPT without freebsd-boot partition) should be __CODESPAN_0_. But what exactly is 4K alignment? Because SSD solid hard drives are not called fan zones。

Create partitions

```sh
# 创建 swap 分区（-t），卷标为 swap（-l），大小为 4G（-s），对齐（-a），注意替换 nda0
# gpart add -a 4k -l swap -s 4G -t freebsd-swap nda0

# Create ZFS partition, volume marked zroot, use all available space, and be careful to replace nda0
# gpart add-a 4k-l zroot-t freebsd-zfs
````

# # See partitions

```sh
# gpart show
=>       34  419430333  nda0  GPT  (200G)
         34       2014        - free -  (1.0M)
       2048     204800     1  efi  (100M)
     206848      32768     2  ms-reserved  (16M)
     239616  207992832     3  ms-basic-data  (99G)
  208232448    8388608     5  freebsd-swap  (4.0G)
  216621056  201326592     6  freebsd-zfs  (96G)
  417947648    1478656     4  ms-recovery  (722M)
  419426304       4063        - free -  (2.0M)
```

# # Mounting temporary file system ready for installation

```sh
# mount -t tmpfs tmpfs /mnt
```

CREATE ZFS POOL

```sh
# 创建 ZFS 池，暂时挂载至 /mnt（-o altroot=/mnt），使用 lz4 压缩（-O compress=lz4。可换成 zstd 等），关闭时间标签（-O atime=off），/dev/gpt/zroot 是我们刚建立的卷标
# zpool create -f -o altroot=/mnt -O compress=lz4 -O atime=off -m none zroot /dev/gpt/zroot
```

## CREATE ZFS DATASET

```sh
# 创建根数据集
# zfs create -o mountpoint=none zroot/ROOT
# 创建一个名为 `zroot/ROOT` 的数据集，不设置挂载点（`mountpoint=none`），通常用于作为系统底层的根数据集，可以用于创建下面的子数据集。

# Create default root dataset
# zfs create-o trackpoint=/ zroot/ROOT/default
# CREATES A DATA SET CALLED __CODESPAN_0_ AND MOUNTS IT TO THE ROOT DIRECTORY __CODESPAN_1_ FOR THE DEFAULT ROOT FILE SYSTEM OF THE SYSTEM。

# create /home data sets
# zfs create-o mountain point #
# CREATE A DATA SET CALLED __CODESPAN_0 AND MOUNT IT TO __CODESPAN_1_, WHICH IS USUALLY USED TO STORE THE USER HOME DIRECTORY。

# create /tmp data set, setting exec on, setuid on off
# zfs create-o mountain point #
# Create __CODESPAN_0_ data sets and mount them to __CODESPAN_1 and allow the execution document (`exec=on`), but disable the use of __CODESPAN_3_) to prevent files in this directory from using satuid to enhance their privileges。

# create /usr data sets and set canmount as off
# zfs create-o trackpoint #
# CREATE __CODESPAN_0_ DATA SETS AND MOUNT THEM TO __CODESPAN_1_, BUT BECAUSE OF __CODESPAN_2_, THE DATA SETS ARE NOT AUTOMATICALLY MOUNTED, USUALLY FOR SPECIFIC SYSTEM CONFIGURATIONS。

# create /usr/ports dataset, set settuid as off
# zfs create-o set=off zroot/usr/ports

# create /usr/ src data sets
# zfs create zroot/usr/src

# create / var data sets, set canmount as off
# zfs create-o mountain point #

# create / var/udit dataset, set exec and setuid as off
# zfs create-o exec #

# create / var/ crush data sets, set exec and setuid as off
# zfs create-o exec #

# create / var/ log data sets, setting exec and setuid as off
# zfs create-o exec #

# create / var/tmp dataset, set settuid as off
# zfs create-o setuid=off zroot/var/tmp

# create / var/mail dataset, set atime on
# zfs create-o age #
# CREATE __CODESPAN_0_ DATASETS AND SET __CODESPAN_1_, WHICH MEANS THAT ACCESS TIMES ARE UPDATED EVERY TIME A FILE IS READ, USUALLY TO STORE MAIL DATA。
````

>** Skills**
>
>The parameters are from [bsdinstall (8)] (https://man.freebsd.org/cgi/man.cgi?bsdinstall (8)). You can also view it in the installed system with commands from CODESPAN_0. The code is in src __CODESPAN_1_。

# # Modify folder privileges

```sh
# 修改 /mnt/tmp 和 /mnt/var/tmp 权限为 1777，保证临时目录权限正确
# chmod 1777 /mnt/tmp
# chmod 1777 /mnt/var/tmp
```

# SET EXCHANGE PARTITION TO __CODESPAN_0_

```
# 配置 swap 分区挂载，注意替换 /dev/nda0p5，可以用命令 gpart show nda0 看一下
# printf "/dev/nda0p5\tnone\tswap\tsw\t0\t0\n" >> /tmp/bsdinstall_etc/fstab
```

>** Skills**
>
>_CODESPAN_0_ is a transliteration character, which means that the Tab key was pressed once, and this is used to split it in alignment, and the same effect is given to space. You can also use the ee editor to manually write the corresponding entries (__CODESPAN_1_):
>
> ```sh '
>/dev/nda0p5 none swap sw 0 0
> ````
>
> Same。

# # SET STARTER WITH UEFI

```
# 设置 ZFS 启动路径为 zroot/ROOT/default
# zpool set bootfs=zroot/ROOT/default zroot

# Configure FreeBSD to load ZFS1 on startup
# printf 'zfs_enable="YES"\ /tmp/bsdinstall_etc/rc.conf

# MOUNT EFI SYSTEM PARTITION
# Mount the existing EFI partition, note to replace /dev/nda0p1
# mount -t msdosfs/dev/nda0p1/media

CREATE A STARTUP DIRECTORY IN THE EFI SYSTEM PARTITION
#mkdir-p/media/efi/freebsd

# COPY EFI STARTUP FILE TO EFI SYSTEM PARTITION
#cp/boot/loader.efi/media/ef/freebsd/

# Add UEFI startup with efibootmgr
# efibootmgr-create-activate-label "FreeBSD"-loader "/media/efi/freebsd/loader.efi"

# UNMOUNT EFI PARTITION
♪ unmount / media
# Exit shell, FreeBSD will continue to install the process
# exit
````

- 1:_CODESPAN_0_ represents the Unix break. Each paragraph in Windows actually ends with ___ CODESPAN_1 _ _ _ _ _ _ _ that is, back to the car and then change. This corresponds to __CODESPAN_2 and insert __CODESPAN_3_。

# Finish

SO WE CREATED THE SAME STRUCTURE MANUALLY AND AUTOMATICALLY

```sh
root@ykla:/home/ykla # zfs list
NAME                 USED  AVAIL  REFER  MOUNTPOINT
zroot                921M  91.6G    96K  none
zroot/ROOT           919M  91.6G    96K  none
zroot/ROOT/default   919M  91.6G   919M  /
zroot/home           128K  91.6G   128K  /home
zroot/tmp            104K  91.6G   104K  /tmp
zroot/usr            288K  91.6G    96K  /usr
zroot/usr/ports       96K  91.6G    96K  /usr/ports
zroot/usr/src         96K  91.6G    96K  /usr/src
zroot/var            636K  91.6G    96K  /var
zroot/var/audit       96K  91.6G    96K  /var/audit
zroot/var/crash       96K  91.6G    96K  /var/crash
zroot/var/log        156K  91.6G   156K  /var/log
zroot/var/mail        96K  91.6G    96K  /var/mail
zroot/var/tmp         96K  91.6G    96K  /var/tmp
```


# References

- [How to ensure effective FreeBSD on a renewable service] (https://stanislas.blog/2018/12/how-to-install-freebsd-server/)
- [RootOnZFS/GPTZFSBoot] (https://wiki.freebsd.org/RootOnZFS/GPTZFSBoot)
