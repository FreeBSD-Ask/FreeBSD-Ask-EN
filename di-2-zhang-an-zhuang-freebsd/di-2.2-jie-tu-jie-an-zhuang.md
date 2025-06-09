# Section 2.2 FreeBSD installation diagram (new introductory version)

>** Skills**
>
>VereBSD 14.2 Basic installation configuration course] (https://www.bilibili.com/video/BV1STExzEeh (physical machine), [002-VMware17 installation FreeBSD14.2] (https://www.bilibili.com/video/BV1gji2YLEoC) (virtual machine).

I don't...

The following description of installation is based on `FreeBSD-14.2-RELEASE-amd64-disc1.iso ' . `-dvd1.iso ' and `-memstick.img ' are very different.

>** Warning**
>
>This paper is based on VMware 17 for demonstration (using UEFI).
>
>In the case of physics machines, please consider using [rufus] (https://rufus.ie/zh/) + [img mirrors] (https://download.freebsd.org/ftp/releases/ISO-IMAGES/14.1/FreeBSD-14.1-RELEEASE-amd64-memstick.img).


> ** Warning**
>
> If UEFI is to be used on VMware Virtual Machine, FreeBSD 13.0-RELEASE and above must be used, otherwise the screen will start.

# Start installation disk

![.. ..gitbook/assets/ins1.png]

This interface does not require any operation and waits for 10 seconds to automatically enter `1. Boot Insteller [Enter] ' ; it can also enter directly by pressing ** Return Key**.

Press **space key** to pause and select the following options.

>** Skills**
>
>If you press any other keyboard, you can enter `menu ' and press ** Back to the menu.

The following operation: a number at the beginning is selected. `on ' Representative has been opened and `off ' Representative has been closed.

| Options | Explanation |
|: -: | | | | | | |
|1. Boot Installer [Enter] ` for installation of systems
|2. Boot Single user`s single-user mode, which will be used to retrieve root passwords and fix disks
|3. Escape to loader prompt` | exit menu, enter command mode, enter `reboot ' return to restart
`4. Rebot ' reboot ' reboot
|5. Cons: Video ' | Select output mode: video (`Video ' ), serial (`Serial ' ) and simultaneous output, but first (`Dual (Serial Primary) ' and then simultaneously, but first video (`Dial (Video Primary) ' optional)
|6. Lennel: default/kernal (1 of 1) `select the kernel to start

![.. ..gitbook/assets/ins2.png]

** ** '7. Boot Options '** ** start-up parameters
|: -: | | | | | | |
|1. Back to Main Menu
|2. Load Systems Refusal Default Configuration
`3. ACPI `Advanced configuration and power interface
|4. Safe Mode ' | security mode
|5. Single user mode
|6. Verbose`s chatter mode with more debugging information output


![.. ..gitbook/assets/ins3.png]

Welcome menu.

`Welcome to FreeBSD! Do you want to start installing or using the Live system? `

Select `install ' , press ** Return key** to install. The middle `Shell ' is the command line, and the left and right `Live System ' is the Live CD mode.

>** Skills**
>
>In the absence of a special description, press **TAB** or ** Direction** to select different entries; press ** Return** to select highlighted entries;

>** Skills**
>
>Take note of the red and rough capital letters in the pictures, such as ** ** `I'**, ** `S'** and ** ** `L'** in the `Install ' , `Shell ' and `Live System ' respectively. If you press the peg on the keyboard directly (in case of case), you select and enter the interface directly.


>** Warning**
>
> Press **ESC** at any step ** cannot** return to the previous menu, and will jump directly to the next step until you exit or finish the installation.

# Set keyboard layout

![.. ..gitbook/assets/ins4.png]

The `FreeBSD system console driver defaults on the standard `US ' (American) keyboard layout. You can select another keyboard layout below. `

Here's the keyboard layout menu, press ** Back to car** with the default keyboard layout (as China currently uses the US keyboard layout).

# Set hostname

![.. ..gitbook/assets/ins5.png]

`Please select the host name for this machine. If you are running on a managed network, ask your network administrator for appropriate names. `

Sets the hostname menu here.

>** Warning**
>
> ** Don't ** Press ** Back at this step**! This leads to an empty host name! Login manager sddm will not be able to start.

# Select the components to install

![.. ..gitbook/assets/ins6.png]

`Select an optional system component to install '

>** Skills**
>
>In the absence of a special description, press **space key** to select an entry - that is, to make `[ ] `[*] ` .
>
>Recommend: On a default basis,** extra** select `src ' As part of the card drive (e.g. `drm ' ) and other programs require `src ' , the test `lib32 ' installation was invalid the day after the test.

>** Warning**
>
> ** Do not** select components other than `kernel-dbg ' , `lib32 ' , `src ' that need to be networked and installed very slowly. If necessary, they can be installed on their own day after tomorrow.
>
> If the question of which mirror should be selected in the installation is because you have selected all the components, please do not do so.


| Options | Explanation |
|: -: |: | | | |
`base-dbg ' basic system debugging tool
`kernel-dbg ' kernel debugger tool
Debugging tool for the library of `lib32-dbg '32-bit applications
`lib32 'is a library for running 32-bit applications on 64-bit FreeBSD
`ports ' ports
`src ' system source code
`tests ' test tool

# Disk Partition

FreeBSD 14.2 RELEASE `/ ' Division supports both UFS and ZFS file systems. The old FreeBSD system root division supports only one UFS file system: `bsdinstall ' from 10.0 [start] (http://svn.freebsd.org/view/base?view=review &vision=256361) supports zfs, with 8.0 [may] (https://blog.delphij.net/posts/2008/11/zfs-1/) using zfs as root partition.

![.. ..gitbook/assets/ins7.png]

area menu. `How do you want to partition your disk? `

| Configuration Options
| - | - |
|Auto (ZFS) – Guided Root-on-ZFS' Auto (ZFS) – Guided ZFS root partition
`Auto (UFS) – Guided UFS Disk Setup`UFS' – Guided UFS disk settings
|Manual – Manual Disk Setup (experts) `Manual ' — Manual Disk Settings (for specialist)
{\cHFFFFFF}{\cH00FF00} Open a shell and partition by hand \

The file system is described in more detail in other chapters (manual partition decompression `txz ' documents are self-defined, see other chapters). Here, the default option `auto ZFS ' is recommended: Generally, memory less than 8GB should choose UFS, memory 8G and above should choose ZFS.


Manual partitions and Shell partitions can be found in the section about manually installing FreeBSD.


## Auto (ZFS) (Use ZFS as `/ ' File System)

>** Skills**
>
> tested, in fact 256M memory can also be used for ZFS (UEFI); 128M memory is sufficient if the old BIOS is used.

> ** Note**
>
>If you use manual partitions to always indicate damage to the partition table (`coreted ') or similar words, please exit to restart, enter shell mode and refresh the partition table:
>
> ```sh '
#Gpart cover aada0
> ````
>
> When manually installed, you can determine which hard drive to determine what this parameter is.
>
>If you do not determine which piece of your hard drive is (e.g. if you do not know `da0 ' or `nv0 ' ) you can view it using the command in the picture.
>
>![ ] (. ..gitbook/assets/ins11.png)
>
>
> Refresh, enter `bsdinstall ' to enter the installation mode.
>
See [FreeBSD Manual] (https://handbook.bsdcn.org/di-18-zhang-cun-chu/18.3.-tiao-zheng-he-zeng-jia-ci-pan-da-xiao.html), but I think this is a bug.

![.. ..gitbook/assets/zfs1.png]

`In the process of detecting equipment, please wait (this may take some time)... ♪ ... ♪

![.. ..gitbook/assets/ins8.png]

Modern computers should choose `GPT+UEFI ' . Older computers (e.g. before 2013) should choose option `GPT (BIOS)' — this default option is compatible with both.

![.. ..gitbook/assets/ins 8.2.png]

| Configuration Options
|-|-|-|-|
Installation
|T Pool Type/Disks: stripe: 0disks ' | storage tank type/disc: striped: 0 pieces of disk |
 *-Recan Services  * Re-scan equipment*
 *-Disk Info  *- Disk Information  *
|N PoolName zroot ' | storage pool name `zroot ' | default pool name `zroot ' |
YES' mandatory 4K sector?
♪ E Encrypt Disks? No. Encrypted login system options.
|P Partition Scheme ' |GPT (UEFI) Partition Program GPT (UEFI) | Options `GPT (BIOS+UEFI) '
`Swap Size 2g ' Swap Swap 2g ' Swap size 2g | If you do not really need Swap, `Swap Size ' enter `0 ' or `0G ' Zenium
`M Mirror Swap? Whether or not to mirror the exchange partition between multiple disks, and if not, each disk exchange partition is independent.
`W Encrypt Swap? No, no, no.


>** Skills**
>
>The subsequent partition and system update process would be simpler if `P Part Scheme ' were set here as `GPT (UEFI) ' instead of anything else.

Note**
>
>It is best to think clearly of setting again the size of `Swap Size ' (i.e., an exchange section) (general theory is twice the memory, but should not exceed 64G due to design problems), because the zfs, ufs file systems cannot reduce the file system, and `dd ' a swap file or file system can have a negative effect.

>** Skills**
>
>If it is not clear which disk should be selected, you can select `-Disk Info * ' at this stage to view disk information:
>
>![ ] (..gitbook/assets/diskinfo.png)
>
>This interface selects the disk to press ** Back to car** to see details; select <Back' to return to the previous menu.
>
>![ ] (..gitbook/assets/diskinfo2.png)
>
>This interface press ** Up and Down key** to browse. Press ** Return key** to return to the previous menu.

![.. .gitbook/assets/ins9.png]

`Select virtual equipment type: '

| Configuration Options | Chinese | Characteristics |
|-|-|-|-|
`Stripe ' Belt, i.e. `RAID 0 ' , without redundancy, a single hard drive is enough
|miror' | | mirror, i.e. `RAD 1 ' | n road mirror, with a minimum of 2 hard disks
|raid10 ' |RAID 1+0 | n group 2 mirrors with a minimum of 4 hard disks (even hard drives required)
|raidz1 | RAID-Z1 | Single redundancy RAID, minimum 3 pieces of hard disk
|raidz2 ' |RAID-Z2 | Double redundancy RAID, minimum 4 pieces of hard disk
|raidz3 ' |RAID-Z3 | Triple Redundred RAID with a minimum of 5 pieces of hard disk

We'll just press **back ** with the default 'Stripe 'just fine.

![.. ..gitbook/assets/ins10.png]

Select your hard drive and press ** Back to the car**

>** Skills**
>
> If you want to install the system to a U-disk or move hard drive, but the system is not identified, re-plug the storage device. Then press the `-Rescan Services* `, re-scanning the equipment, which should be sufficient.

Note**
>
> If your hard drive is eMC, three options may emerge, similar to `mmcsd0 ' , `mmcsd0boot0 '  and `mmcboot1 ' . Please select `mmcsd0 ' . In addition, `Mounting from zfs: zroot/ROOT/default secured with error 22: retrying for 3 more subds ' . And if you specify it manually, it'll go straight to Panic. Suspected Bug, but I do not know how to report and cannot obtain further details.


![.. ..gitbook/assets/ins12.png]

`Final chance! Are you sure you want to destroy the current contents of the following disk:

This is the last warning and confirmation. You've done the backup and the disk will be formatted as a whole. Press ** Direction Key** and ** Tab Key** to switch to <YES>, ** Return Key** to choose.

>** Warning**
>
It's a complete installation, it'll lose all the data! For non-comprehensive installation, please refer to other articles of the book.

## Auto (UFS) (Use UFS as `/ ' File System)

![.. ..gitbook/assets/ufs1.png]

`How do you want to partition your disk? `

>** Skills**
>
>If `Partition ' (partition) is selected, the option follows.

![.. ..gitbook/assets/ufs2.png]

`Do you want to use the entire disk or partition it to share it with other operating systems? Use the entire disk to erase all directories currently stored there. `

![.. ..gitbook/assets/ufs3.png]


`Selection of a divisional formula for the volume '

English English Chinese English
|-|-|-|-|
`APM Apple Partition Map ' Zoom Table | Apple `PowerPC ' with `2006
`BSD BSD Labels' |BSD disk label | BSD only
|GPT GUID Partition Table Table |GPT General Only Marked Partition Table
|MBR DOS Partitions |MBR Master Guided Records Partition Table

![.. ..gitbook/assets/ufs4.png]

`Please review disk settings. If there's no problem, click "Finish" button '

English
| - | - |
`Create ' Created
`Delete ' delete
`Modivy ' Adjustment
`Revert '
`Auto `Auto |
`Finish ' complete

![...gitbook/assets/ufs5.png]

`Your changes will not be saved to disk. If you choose to overwrite existing data. It will be deleted. Are you sure you want to submit your changes? `

English
| - | - |
`Commit' submission
`Revert & Exit `Return and exit
`Back ' returns

![.. ..getbook/assets/ufs6.png]

Initializing Disk - This interface flashes through

- WhatI don't...

![.. ..getbook/assets/ins13.png]

![.. ..gitbook/assets/ins14.png]


# Set root password

![.. ..gitbook/assets/ins15.png]

`Please select the password for the System Management Account (root): The characters entered are invisible. Changing the root password of the system to be installed. `

Enter the root password here, the password will not be displayed on the screen, and it will be ** there is nothing ** and so will the password elsewhere. Re-entry is required twice to confirm consistency. Password strength default is not required.

# Network Settings

Ethernet settings

![.. ..gitbook/assets/ins17.png]

`Select a network interface to configure '

is the selection card. Press ** Direction key** toggle, press ** Return key** to select.

![.. ..gitbook/assets/ins18.png]

`Do you want to configure IPv4 for this interface? `

Configure IPv4. Press ** Return key** to choose.

![.. ..gitbook/assets/ins19.png]

`Do you want to configure this interface with DHCP? `

Configure using DHCP. Press ** Return key** to choose.

![.. ..gitbook/assets/ins20.png]

`Do you want to configure IPv6 for this interface? `

Configure IPv6. `No ' , press ** return key** to be selected because IPv6 is not used in the course. If needed, you can configure your own IPv6.

![.. .gitbook/assets/ins21.png]

`Settle Resolutionr '

Usually keep the DNS that DHCP acquires and can use other DNSs. Ali DNS `223.5.5 ' is used here. Press ** Direction key** toggle, press ** Return key** to select.

# # WiFi/ WiFi settings

Note**
>
>Bopnet card should be installed and then referred to the WiFi chapter.

![.. ..gitbook/assets/ins-w1.png]

`Please select the network interface to configure '



![.. ..gitbook/assets/ins-w2.png]

`Reforming the region/country (FCC/US)? `

Modify the WiFi area code, press back to confirm.

![.. ..gitbook/assets/ins-w3.png]

"Select your area code."

We should choose `none Row'.


![.. ..gitbook/assets/ins-w4.png]

♪ Choose your area ♪

Selection:

![.. .gitbook/assets/ins-w5.png]

`Waiting 5 seconds, scanning the wireless network... '

Scan.

>** Skills**
>
>As long as you can identify the card, it will be useful, but it may not be possible to search WiFi correctly when the system is installed. Please leave empty and restart to the new system after installation and then refer to the WiFi chapter for processing.

Find your WiFi in the list. If you cannot find it, change the channel.

![.. ..gitbook/assets/ins-w6.png]

"Select the wireless network you want to link."

Enter the WiFi password to link:

![.. ..gitbook/assets/ins-w7.png]

![.. ..gitbook/assets/ins18.png]

`Do you want to configure IPv4 for this interface? '

Configure IPv4. Press ** Return key** to choose.

![.. ..gitbook/assets/ins19.png]

`Do you want to configure this interface with DHCP? `

Configure using DHCP. Press ** Return key** to choose.

![.. ..gitbook/assets/ins20.png]

`Do you want to configure IPv6 for this interface? `

Configure IPv6. `No ' , press ** return key** to be selected because IPv6 is not used in the course. If needed, you can configure your own IPv6.

![.. .gitbook/assets/ins21.png]

`Settle Resolutionr '

Usually keep the DNS that DHCP acquires and can use other DNSs. Ali DNS `223.5.5 ' is used here. Press ** Direction key** toggle, press ** Return key** to select.

References

- [Regulatory Domain Sport] (https://wiki.freebsd.org/WiFi/RegulatoryDomainSupport)
- [regdomain.xml - 802.11 Wireless regulatory solutions] (https://man.freebsd.org/cgi/man.cgi?query=regdomain&sektion=5) The corresponding coding is in the `/etc/regdomain.xml ' file in the reference system.
- [Ali Public DNS] (https://www.alidns.com/)


# Time zone settings

![.. ..gitbook/assets/ins22.png]

`Selection Area '

Sets the time zone. China is located in `5 Asia` (Asia). Press ** Direction key** toggle, press ** Return key** to select.

![.. ..gitbook/assets/ins23.png]

`Setting countries or areas '

China chose `9 China` (China). Press ** Direction key** toggle, press ** Return key** to select.

![.. ..gitbook/assets/ins24.png]

China uses the Eastern Region time, Beijing time, and please choose `1 Beijing Time' (Beijing time). Press ** Direction key** toggle, press ** Return key** to select.

![.. ..gitbook/assets/ins25.png]

Does the time zone abbreviation 'CST' look reasonable? `

We use Chinese standard time: China Standard Time (CST), no problem, press ** Return Key** to select `Yes ' .

![.. ..gitbook/assets/ins26.png]

`Time and date '

Press **back keys** enough.

![.. ..gitbook/assets/ins27.png]

`Time and date '

Press **back keys** enough.

# Start service settings

![.. ..gitbook/assets/ins28.png]

`Select the service you want to start when you turn it on. '

>** Warning**
>
>** Do not choose all! **
>
>** Do not** select `local_unborn ' , which could affect DNS, see [https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=262290] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=262290). Unless you know what this is.


| Options | Explanation |
|: - - -: |: | | |
|local_unborn`enborn. This is preset by the basic system and is used only for local cache forward resolution. Note: If you turn it on, your system will not be properly connected and will need to be manually configured for DNS. If you don't know what this isn't about, Zoo.
`sshd ' open ssh service
`moused '| Show mouse in tty interface
`ntpd '| Network Time Protocol (NTP) daemon for automatic clock sync
|ntpd_sync_on_start`synctime
`powerd ' | power management, CPU frequency dynamic adjustment
`dumpdev '| Enable crash dumps for debugging systems

# Secured

![.. ..gitbook/assets/ins29.png]

`Selection of system security enhancements '

This is the security reinforcement, and it's up to you to choose.

>** Skills**
>
>In the previous version of FreeBSD 14, this step will appear `disable_sendmail ' . Please select that if this service is not banned, it will be stuck for a few minutes each time you turn on, and the service itself will be useless and mailed.

| Options | Explanation |
|: - - -: |: | | |
|0 phild_uids | Process to hide other users
|1 Hide_gids | Process to hide other groups
|2 Hide_jail `hidden process in jail
|3 read_msgbuf ` | non-privileged users are prohibited from reading the kernel buffer zone (generally `dmesg ' )
|4 process_debug ` Debug function for non-privileged users
PID for the `5 Randall_pid' process
`6 clear_tmp ' , clear `/tpm `
|7 Disable_syslogd`| Disable Syslogd web package (disable remote log log)|
|8 security_console`enable console password (root password also required in single user mode)
|9 Disable_ddtrace ` prohibits DTrace destructive


# Install solid

'! [Virtual machine unencrypted] (. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .)

(https://cgit.freebsd.org/src/committee/?id=03c07bdc8b31))

** This image is from the Virtual Machine Installation Interface**.

! [Physical machines may have some solids to install] (..getbook/assets/2-install.png)

** This picture is from a physical machine installation interface (using a pick-up card)**


>** Warning**
>
> You'd better cancel the check at this point, that is, not to install any solids (which is also problematic), otherwise you'll be stuck here indefinitely because of the network problem. If you do not remember what needs to be installed, you can take a look at it with the order `fwget ' once installed.
>
>![ ] (. .gitbook/assets/1-install.png)
>
> ** This image is from a physical machine installation interface (using a pick-up card)**

# Create normal users

![.. ..gitbook/assets/ins30.png]

`Do you now wish to add users to the installed system? `

To create, press ** Return key** to select `Yes ' ; if no ordinary user is needed, ~ root death squad~, use ** Direction key** to select `No ' .


>** Skills**
>
> The majority of login managers are default-ban root users. In other words, you may not be able to log on to the desktop with root without some change (see other chapters) in the default. ~ although FreeBSD does not have a desktop under the default status, or can also be directly ~startx.

![.. ..gitbook/assets/ins31.png]


Note**
>
> If you want to create a normal user, you must add it to the `wheel ' group (see arrow position).


```sh '
FreeBSD Insteller
== sync, corrected by elderman ==
Add Users

Username: ykla# Enter username here
Full name: # Enter the full name of the user here
# User UID
Login group [ykla]:
Login group is ykla. Invite ykla into other groups? [] :wheel # type "wheel" here and invite user "ykla" to add "wheel" to the additional group for the use of commands su
Login class [default]: # User rating
Shell (sh csh tcsh nologin) [sh]: # User Default shell
Home directory [/home/ykla]: # User directory
Home directory missions (Leave empty for default): # User directory permissions
Use password-based authorization? [yes]: # Enable password authentication
Use an empty password? (yes/no)
Use a random password? (yes/no)
Enter password: # Enter the password, the password does not appear on the screen, it will not be ****, nothing.
Enter password again:
Lock out the account after creation?
Username: ykla
Password: *****
Full Name:
Uid: 1001
Class:
Groups: ykla sheel
Home: /home/ykla
Home Mode:
Shell: /bin/sh
Locked: no
(yes/no) [yes]:
# Successfully added ykla to the user database
Add another user? (yes/no)
````



Other parameters keep the default settings unchanged. The default shell of all users was unified for `sh ' at FreeBSD 14 et seq.

Finally, ask `Add another user? (yes/no) [no] `, ** return key** to complete creation;

If you enter `yes ' , press ** Return key** to create a second common user.

# End installation

![.. ..gitbook/assets/ins32.png]

`Your FreeBSD system setup is almost complete. You can modify your configuration options now. After this menu, you can use the shell to make more complex changes. `

Press ** Return key** to finish installation.

![.. ..gitbook/assets/ins33.png]

`The installation has now been completed. Do you want to open shell in the new system before you quit the installation to make the last manual change? `

Press ** Return key** to complete installation.

![.. ..gitbook/assets/ins34.png]

`FreeBSD installation complete! Do you now want to restart and enter the installed system? `

Press ** Return key** to restart the newly installed system.



Welcome to FreeBSD

Restart to FreeBSD new system after installation:

![.. ..gitbook/assets/ins35.png]

After full start:

>** Skills**
>
>FreeBSD basic system does not have a graphical interface and Xorg is not installed, so this is the case.



![.. ..gitbook/assets/ins36.png]

Enter the username `root ' and the `root ' password set at the time of installation for login into the system.

>** Skills**
>
>The password will not be displayed on the screen, nor will it be `*** ' , and there is nothing, just enter the back car.

![.. ..getbook/assets/ins37.png]

# Fragmentation and unfinished business

- Unable to access installation interface

In the case of virtual machines, check your configuration;

If a physics machine:

>Please check the following list in turn:
>
> - Are you a regular home computer?
> - Processor is intel or amd?
> - Has the safe start (Secure Boot) in the BIOS closed?
> - Is the image downloaded from <https://freebsd.org>?
> - Did you download the latest RELEASE mirror?
> - Did you download the mirror suffix name `img '?
> - Is the mirror verification (sha256) approved?
> - Do you download mirrors with the words `amd64 '?
> - See clearly `amd64 ' ** Not ** `arm64 ' (for development boards)!
> - Is your U-drive expanded?
- Did you use Ventoy?
> -Booking software please use [Rufus] (https://rufus.ie/zh/), not [Ventoy] (https://www.ventoy.net/cn/index.html)


If there is still a problem, ask first in English in the [official forum] (https://forums.freebsd.org/); in case of no result, the bug can be presented in other sections.

- Restart and go againInstalled

In the case of a virtual machine, please actively eject/ disconnect an automatic connection to the DVD starter and restart it; in the case of a physical machine, remove the U-disk or pop-up installed disk and restart it.

- It's stuck in a service.

In previous versions, services such as sendmail may be stuck on start-up for long periods, or static IP addresses need to be configured, but the system has been trying DHCP.

You can try to enter **ctrl**+**c** to interrupt the service to start the system.
。