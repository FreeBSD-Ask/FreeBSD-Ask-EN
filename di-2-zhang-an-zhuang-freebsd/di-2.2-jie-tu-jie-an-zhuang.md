# Section 2.2 FreeBSD installation diagram (new introductory version)

>** Skills**
>
>ViewSystem presentation [FreeBSD 14.2 Basic integration configuration course] (https://www.bilibili.com/video/BV1STExzEeh) (physical machine), [002-VMware17 Information FreeBSD14.2] (https://www.bilibili.com/video/BV1gji2YLEEC) (virtual machine)。

---|---

THE FOLLOWING INSTALLATION DESCRIPTION IS BASED ON __CODESPAN_0_. ___ CODESPAN_1 _ AND __ CODESPAN_2 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO CO SP CO CO CO CO CO CO SP SP SP SP SP SP SP CO SP CO SP SP SP SP SP SP SP SP SP SP SP 。

>** Warning**
>
>This paper is based on VMware 17 for demonstration (using UEFI)。
>
>In the case of physics machines, please consider using [rufus] (https://rufus.ie/zh/) + [img mirror] (https://download.freebsd.org/ftp/releases/ISO-IMAGES/14.1/FreeBSD-14.1-RELEEASE-amd64-memstick.img)。


> ** Warning**
>
> If UEFI is to be used on VMware Virtual Machine, FreeBSD 13.0-RELEASE and above must be used, otherwise the screen will start。

# Start installation disk

![.. ..gitbook/assets/ins1.png]

THIS INTERFACE DOES NOT REQUIRE ANY OPERATION AND WAITS FOR 10 SECONDS TO AUTOMATICALLY ENTER __CODESPAN_0; IT CAN ALSO ENTER DIRECTLY BY PRESSING ** RETURN KEY**。

Press **space key** to pause and select the following options。

>** Skills**
>
>IF YOU PRESS ANY OTHER KEYBOARD YOU WILL ENTER __CODESPAN_0, ENTER __CODESPAN_1 AND PRESS ** RETURN KEY** TO THE MENU。

THE FOLLOWING OPERATION: A NUMBER AT THE BEGINNING IS SELECTED. __CODESPAN_0_ REPRESENTATIVE HAS BEEN OPENED, __CODESPAN_1_ REPRESENTATIVE HAS BEEN CLOSED。

| Options | Explanation |
| :----------: | :----------------------------------------------------------------------- |
| `1. Boot Insteller [Enter] ' | To install the system |
| `2. Boot Single user' | single user mode will be used to retrieve root passwords and fix disks |
| `3. Escape to loader prompt ' | leave menu, enter command mode, enter `reboot ' and return car to restart |
| `4. Rebot ' | Restart |
| `5. Cons: Video ' | Select output mode: video (`Video ' ), serial (`Serial ' ) and simultaneous output, with priority given to serial (`Dual (Serial Primary) ' and simultaneous output, with priority given to video (`Dual (Video Primary) ' optional) |
| `6. Lennel: default/kernal (1 of 1) ' | Select kernel to start |

![.. ..gitbook/assets/ins2.png]

| ** '7. Boot Options '** | Start Parameter |
| :----------: | :----------------------------------------------------------------------- |
| `1. Back to mine | Press ** Deleting Key** to return to the parent menu |
| `2. Load System Defaults ' | Restore Default Configuration |
| `3. ACPI ' | Advanced configuration and power interface |
| `4. Safe Mode ' | Security mode |
| `5. Single user' | Single User Mode |
| `6. Verbose ' | Shut up mode. Add more debugging messages |


![.. ..gitbook/assets/ins3.png]

Welcome menu。

_CODESPAN_0_

_CODESPAN_0_, press ** Return key** to install. __CODESPAN_1 is the command line, __CODESPAN_2 __ is the LiveCD mode。

>** Skills**
>
>IN THE ABSENCE OF A SPECIAL DESCRIPTION, PRESS **TAB** OR ** DIRECTION** TO SELECT DIFFERENT ENTRIES; PRESS ** RETURN** TO SELECT HIGHLIGHTED ENTRIES

>** Skills**
>
> NOTE THAT THE RED AND ROUGH INITIALS IN THE PICTURES, SUCH AS __CODESPAN_0, __CODESPAN_1 AND __CODESPAN_2**, **, _CODESPAN_4**, ** ** CODESPAN_5** ARE, RESPECTIVELY, RED AND ROUGH. IF YOU PRESS THE PEG ON THE KEYBOARD DIRECTLY (IN CASE OF CASE), YOU SELECT AND ENTER THE INTERFACE DIRECTLY。


>** Warning**
>
> PRESS **ESC** AT ANY STEP ** CANNOT** RETURN TO THE PREVIOUS MENU, AND WILL JUMP DIRECTLY TO THE NEXT STEP UNTIL YOU EXIT OR FINISH THE INSTALLATION。

# Set keyboard layout

![.. ..gitbook/assets/ins4.png]

__CODESPAN_0_US_CODESPAN_1_

Here's the keyboard layout menu, press ** Back to car** with the default keyboard layout (as China currently uses the US keyboard layout)。

# Set hostname

![.. ..gitbook/assets/ins5.png]

_CODESPAN_0_

Sets the hostname menu here。

>** Warning**
>
> ** don't ** press ** back at this step**! this leads to an empty host name! login manager sddm will not be able to start。

# Select the components to install

![.. ..gitbook/assets/ins6.png]

_CODESPAN_0_

>** Skills**
>
>IN THE ABSENCE OF A SPECIAL DESCRIPTION, PRESS **SPACE KEY** TO SELECT AN ENTRY _CODESPAN_0_TO BECOME `[ * ]`_。
>
>RECOMMEND: ON A DEFAULT BASIS, **ADDITIONAL** SELECT `src` ENOUGH. ___ CODESPAN_1_) AND OTHER PROGRAMS REQUIRE __CODESPAN_2_, THE INSTALLATION OF __CODESPAN_3_ WAS TESTED AS INVALID THE DAY AFTER TOMORROW。

>** Warning**
>
>** DO NOT** SELECT COMPONENTS OTHER THAN __CODESPAN_0, __CODESPAN_1_, __CODESPAN_2_, WHICH REQUIRE NETWORK INSTALLATION, VERY SLOW. IF NECESSARY, THEY CAN BE INSTALLED ON THEIR OWN DAY AFTER TOMORROW。
>
> If the question of which mirror should be selected in the installation is because you have selected all the components, please do not do so。


| Options | Explanation |
| :--------: | :------------------------------------------------------------------- |
| `base-dbg ' | Basic system debugging tool |
| `kernel-dbg ' | kernel debugging tool |
| `lib32-dbg ' | Debugging library for 32-bit applications |
| `lib32 ' | Compatible library for running 32-bit applications on 64-bit FreeBSD |
| `ports ' | i don't know |
| `src ' | System Source Code |
| `tests ' | Test Tool |

# Disk Partition

FreeBSD 14.2 RELEASE __CODESPAN_0_ Division supports both UFS and ZFS file systems. The old FreeBSD system Root Division supports only one UFS file system: ___ CODESPAN_1_ from 10.0 [Start] (http://svn.freebsd.org/view/base?view=review &vision=256361) supports zfs, with the use of zfs as the root partition at 8.0 if installed manually。

![.. ..gitbook/assets/ins7.png]

AREA MENU. _CODESPAN_0_

| Configure Options | Note in Chinese |
|---|---|
| `Auto (ZFS) – Guided Root-on-ZFS ' | Automatic (ZFS) - Lead ZFS root partition |
| `Auto (UFS) – Guided UFS Disk Setup' | AUTO (UFS) - GUIDED UFS DISK SETTINGS |
| `Manual – Manual Disk Setup (experts)' | Manual – Manual disk settings (suitable for specialists) |
| ‘Open a shell and partition by hand’ | Shell – Open Shell and manually partition |

THE FILE SYSTEM IS DESCRIBED IN MORE DETAIL IN OTHER CHAPTERS (MANUAL PARTITION DECOMPRESSION __CODESPAN_0_ DOCUMENT FOR DEFINITION, SEE OTHER SECTIONS). HERE, SELECT THE DEFAULT OPTION __CODESPAN_1_: NORMALLY, MEMORY LESS THAN 8GB SHOULD CHOOSE UFS, MEMORY 8G AND ABOVE SHOULD CHOOSE ZFS。


Manual partitions and Shell partitions can be found in the section about manually installing FreeBSD。


## Auto (ZFS)

>** Skills**
>
> TESTED, IN FACT 256M MEMORY CAN ALSO BE USED FOR ZFS (UEFI); 128M MEMORY IS SUFFICIENT IF THE OLD BIOS IS USED。

> ** Note**
>
>If you use a manual partition to always indicate damage to the partition table (__CODESPAN_0_) or similar words, please exit to restart, enter shell mode and refresh the partition table:
>
> ```sh '
#gpart cover aada0
> ````
>
> WHEN YOU ARE MANUALLY INSTALLED, YOU CAN JUDGE WHICH HARD DRIVE TO DETERMINE WHAT THIS PARAMETER IS。
>
>IF YOU DON'T KNOW WHICH PIECE OF YOUR HARD DRIVE IS (E.G. __CODESPAN_0 _ OR __CODESPAN_1 __) YOU CAN VIEW IT USING THE COMMAND IN THE PICTURE。
>
>![ ] (. ..gitbook/assets/ins11.png)
>
>
> AFTER REFRESHING, ENTER __CODESPAN_0_ TO ENTER THE INSTALLATION MODE。
>
See [FreeBSD Handbook] (https://handbook.bsdcn.org/di-18-zhang-cun-chu/18.3.-tiao-zheng-he-zeng-jia-ci-pan-da-xiao.html), but I think it is a bug。

![.. ..gitbook/assets/zfs1.png]

_CODESPAN_0_

![.. ..gitbook/assets/ins8.png]

MODERN COMPUTERS SHOULD CHOOSE CODESPAN_0_. THE OLDER COMPUTER (E.G. BEFORE 2013) SHOULD CHOOSE OPTION __CODESPAN_1 -- THIS DEFAULT OPTION IS COMPATIBLE WITH BOTH。

![.. ..gitbook/assets/ins 8.2.png]

| Configure Options | Chinese | Annotations |
|---|---|---|
| Install Production with Establishment | > Installation Continue installation |  |
| `T Pool Type/Disks: stripe: 0 Disks' | Storage tank type/disk: striped: 0 pieces of disk | See the details |
| `-Rescan Devices * | - Re-scan equipment* |  |
| `-Disk Info* ` | - Disk Information * |  |
| 'N Pool Name zroot ' | store name `zroot ' | default pool name `zroot ' |
| '4 Force 4K Sections | FORCE 4K SECTOR? YES | 4K ALIGNMENT |
| ♪ E Encrypt Disks | Encrypted disk? Yes | Encrypted login system options refer to other articles in this book |
| `P Part Scheme' | GPT (UEFI) DIVISIONAL PROGRAM GPT (UEFI) | ONLY OLD COMPUTERS NEED OPTIONS LIKE `GPT (BIOS+UEFI) ' |
| `S Swap Size 2g ' | exchange partition size 2g | If you do not really need Swap, the `Swap Size ' enter `0 ' or `0G ' instead of setting up exchange partitions。 |
| `M Mirror Swap | Swap mirrors? Yes | Whether mirror exchange partitions between disks and, if not, each disk exchange partition is independent |
| `W Encrypt Swap | Encrypted exchange partitions? Yes |  |


>** Skills**
>
> IF __CODESPAN_0 IS SET HERE AS __CODESPAN_1 AND NOT ELSE, THE SUBSEQUENT PARTITION AND SYSTEM UPDATE PROCESS WILL BE SIMPLER。

Note**
>
>Better think clearly about setting up the __CODESPAN_0_(i.e., exchange partition) size (general theory is twice the memory, but not more than 64G due to design problems) because the zfs and ufs file systems are not able to downsize the file system, whereas __CODESPAN_1_ a swap file or file system has a negative effect。

>** Skills**
>
> IF IT IS NOT CLEAR WHICH DISK SHOULD BE CHOSEN, CHOOSE __CODESPAN_0_ AT THIS STEP TO VIEW DISK INFORMATION:
>
>![ ] (..gitbook/assets/diskinfo.png)
>
>THIS INTERFACE SELECTS THE DISK TO PRESS ** BACK TO CAR** TO SEE DETAILS; SELECT __CODESPAN_0_ TO RETURN TO THE PREVIOUS MENU。
>
>![ ] (..gitbook/assets/diskinfo2.png)
>
>This interface press ** Up and Down key** to browse. Press ** Return key** to return to the previous menu。

![.. .gitbook/assets/ins9.png]

_CODESPAN_0_

| Configure Options | Chinese | Characteristics |
|---|---|---|
| `Stripe ' | BANDED, KNOWN AS `RAD 0 ' | No redundancy. A hard drive |
| `miror ' | MIRROR, KNOWN AS `RAD 1 ' | n mirror, minimum 2 hard drive required |
| `raid10 ' | RAID 1+0 | n group 2 road mirror, with a minimum of 4 hard drives (even hard drives required) |
| `raidz1 ' | RAID-Z1 | SINGLE REDUNDANCY RAID, MINIMUM 3 HARD DRIVE REQUIRED |
| `raidz2 ' | RAID-Z2 | DOUBLE REDUNDANT RAD, MINIMUM 4 HARD DRIVE REQUIRED |
| `raidz3 ' | RAID-Z3 | TRIPLE REDUNDANCY RAD, MINIMUM 5 HARD DRIVE REQUIRED |

WE'LL JUST PRESS ** BACK TO THE CAR** USING THE DEFAULT __CODESPAN_0_。

![.. ..gitbook/assets/ins10.png]

Select your hard drive and press ** Back to the car**。

>** Skills**
>
> IF YOU WANT TO INSTALL THE SYSTEM TO A U-DISK OR MOVE HARD DRIVE, BUT THE SYSTEM IS NOT IDENTIFIED, RE-PLUG THE STORAGE DEVICE. AND THEN PRESS THE ABOVE CODESPAN_0 AND RE-SCAN THE DEVICE, IT SHOULD BE OKAY。

Note**
>
> If your hard drive is eMMC, there may be three options similar to __CODESPAN_0, __CODESPAN_1 and __CODESPAN_2_. Please select __CODESPAN_3_. Also, if multiple hard drives coexist with eMMC, if the size of another hard drive is more than five, the FreeBSD in eMMC will be stuck to __CODESPAN_4. And if you specify it manually, it'll go straight to Panic. Suspected Bug, but I do not know how to report and cannot obtain further details。


![.. ..gitbook/assets/ins12.png]

_CODESPAN_0_

This is the last warning and confirmation. You've done the backup and the disk will be formatted as a whole. Press ** Direction key** and ** Tab key** to switch to __CODESPAN_0_, press ** Return key** to choose。

>** Warning**
>
It's a complete installation, it'll lose all the data! For non-comprehensive installation, please refer to other articles of the book。

## Auto (UFS) (Use UFS as __CODESPAN_0_ filesystem)

![.. ..gitbook/assets/ufs1.png]

_CODESPAN_0_

>** Skills**
>
> IF __CODESPAN_0_(DIVISION) IS SELECTED, THE OPTION IS THE FOLLOWING。

![.. ..gitbook/assets/ufs2.png]

_CODESPAN_0_

![.. ..gitbook/assets/ufs3.png]


_CODESPAN_0_

| English | Chinese | Comment |
|---|---|---|
| `APM Apple Part Map ' | Apple partition table | Apple `PowerPC ' for 2006 |
| `BSD BSD Labels ' | BSD DISK TAB | BSD ONLY RECOGNISED |
| `GPT GUID Part Table ' | GPT GLOBAL SINGLE MARK PARTITION TABLE | Modern computer usage (2013+) |
| `MBR DOS Parties ' | MBR MAIN LEAD RECORD PARTITION TABLE | Usage of older computers (XP, Win7 years) |

![.. ..gitbook/assets/ufs4.png]

_CODESPAN_0_

| English | Chinese |
|---|---|
| `Create ' | Create |
| `Delete ' | Delete |
| `Modivy ' | Adjustment |
| `Revert ' | Revert |
| `Auto ' | Automatic |
| `Finish ' | Completed |

![...gitbook/assets/ufs5.png]

_CODESPAN_0_

| English | Chinese |
|---|---|
| `Commit' | Submit |
| `Revert & Exit ' | Revert and exit |
| `Back ' | Back |

![.. ..getbook/assets/ufs6.png]

Initializing Disk - This interface flashes through

---|---

![.. ..getbook/assets/ins13.png]

![.. ..gitbook/assets/ins14.png]


# set root password

![.. ..gitbook/assets/ins15.png]

_CODESPAN_0_

enter the root password here, the password will not be displayed on the screen, and it will be ** there is nothing ** and so will the password elsewhere. re-entry is required twice to confirm consistency. password strength default is not required。

# Network Settings

Ethernet settings

![.. ..gitbook/assets/ins17.png]

_CODESPAN_0_

is the selection card. Press ** Direction key** toggle, press ** Return key** to select。

![.. ..gitbook/assets/ins18.png]

_CODESPAN_0_

Configure IPv4. Press ** Return key** to choose。

![.. ..gitbook/assets/ins19.png]

_CODESPAN_0_

CONFIGURE USING DHCP. PRESS ** RETURN KEY** TO CHOOSE。

![.. ..gitbook/assets/ins20.png]

_CODESPAN_0_

Configure IPv6. __CODESPAN_0_, press ** Return key** to select __. If needed, you can configure your own IPv6。

![.. .gitbook/assets/ins21.png]

_CODESPAN_0_

USUALLY KEEP THE DNS THAT DHCP ACQUIRES AND CAN USE OTHER DNSS. ALI DNS_CODESPAN_0_ IS USED HERE. PRESS ** DIRECTION KEY** TOGGLE, PRESS ** RETURN KEY** TO SELECT。

# # WiFi/ WiFi settings

Note**
>
>Bopnet card should be installed and then referred to the WiFi chapter。

![.. ..gitbook/assets/ins-w1.png]

_CODESPAN_0_



![.. ..gitbook/assets/ins-w2.png]

_CODESPAN_0_

Modify the WiFi area code, press back to confirm。

![.. ..gitbook/assets/ins-w3.png]

_CODESPAN_0_

WE SHOULD CHOOSE CODESPAN。


![.. ..gitbook/assets/ins-w4.png]

_CODESPAN_0_

Selection:

![.. .gitbook/assets/ins-w5.png]

_CODESPAN_0_

Scan。

>** Skills**
>
>As long as you can identify the card, it will be useful, but it may not be possible to search WiFi correctly when the system is installed. Please leave empty and restart to the new system after installation and then refer to the WiFi chapter for processing。

Find your WiFi in the list. If you cannot find it, change the channel。

![.. ..gitbook/assets/ins-w6.png]

_CODESPAN_0_

Enter the WiFi password to link:

![.. ..gitbook/assets/ins-w7.png]

![.. ..gitbook/assets/ins18.png]

_CODESPAN_0_

Configure IPv4. Press ** Return key** to choose。

![.. ..gitbook/assets/ins19.png]

_CODESPAN_0_

CONFIGURE USING DHCP. PRESS ** RETURN KEY** TO CHOOSE。

![.. ..gitbook/assets/ins20.png]

_CODESPAN_0_

Configure IPv6. __CODESPAN_0_, press ** Return key** to select __. If needed, you can configure your own IPv6。

![.. .gitbook/assets/ins21.png]

_CODESPAN_0_

USUALLY KEEP THE DNS THAT DHCP ACQUIRES AND CAN USE OTHER DNSS. ALI DNS_CODESPAN_0_ IS USED HERE. PRESS ** DIRECTION KEY** TOGGLE, PRESS ** RETURN KEY** TO SELECT。

References

- [Regulatory Domain Sport] (https://wiki.freebsd.org/WiFi/RegulatoryDomainSupport)
- [i'm sorry] (https://man.freebsd.org/cgi/man.cgi?query=regdomain&sektion=5) for encoded __CODESPAN_0_file in the reference system。
- [ALI PUBLIC DNS] (https://www.alidns.com/)


# Time zone settings

![.. ..gitbook/assets/ins22.png]

_CODESPAN_0_

SETS THE TIME ZONE. CHINA IS LOCATED IN __CODESPAN_0_ (ASIA). PRESS ** DIRECTION KEY** TOGGLE, PRESS ** RETURN KEY** TO SELECT。

![.. ..gitbook/assets/ins23.png]

_CODESPAN_0_

CHINA CHOOSE __CODESPAN_0_ (CHINA). PRESS ** DIRECTION KEY** TOGGLE, PRESS ** RETURN KEY** TO SELECT。

![.. ..gitbook/assets/ins24.png]

CHINA USES THE EASTERN REGION TIME, BEIJING TIME. PLEASE CHOOSE __CODESPAN_0_ (BEIJING TIME). PRESS ** DIRECTION KEY** TOGGLE, PRESS ** RETURN KEY** TO SELECT。

![.. ..gitbook/assets/ins25.png]

_CODESPAN_0_

We use Chinese standard time: China Standard Time (CST), no problem, press ** Return Key** to select __CODESPAN_0_。

![.. ..gitbook/assets/ins26.png]

_CODESPAN_0_

Press **back keys** enough。

![.. ..gitbook/assets/ins27.png]

_CODESPAN_0_

Press **back keys** enough。

# Start service settings

![.. ..gitbook/assets/ins28.png]

_CODESPAN_0_

>** Warning**
>
>** Do not choose all! **
>
> ** Do not** choose __CODESPAN_0, which could affect DNS, see [https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=262290] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=262290). Unless you know what this is。


| Options | Explanation |
| :-----------: | :------------------------ |
| `local_unbound ' | Enable Unborn. This is preset by the basic system and is used only for local cache forward resolution. Note: If you turn it on, your system will not be properly connected and will need to be manually configured for DNS. If you don't know what this isn't about |
| `sshd ' | open ssh service |
| `moused ' | show mouse in tty interface |
| `ntpd ' | NETWORK TIME PROTOCOL (NTP) DAEMON FOR AUTOMATIC CLOCK SYNC |
| 'ntpd_sync_on_start ' | Synchronise Time on |
| `powerd ' | POWER MANAGEMENT, CPU FREQUENCY DYNAMIC ADJUSTMENTS |
| `dumpdev ' | Enable crash dump for debugging systems |

# Secured

![.. ..gitbook/assets/ins29.png]

_CODESPAN_0_

This is the security reinforcement, and it's up to you to choose。

>** Skills**
>
>In the previous version of FreeBSD14, this step will appear __CODESPAN_0. Please choose, if this service is not banned, you will be stuck for a few minutes each time you turn on, and the service itself is of no use, sending mail。

| Options | Explanation |
| :-----------: | :------------------------ |
| `0 ild_uids ' | Hide processes for other users |
| `1 hide_gids ' | Hide the process of another group |
| `2 hide_jail ' | hide the process in jail |
| `3 read_msgbuf ' | ban non-privileged users from reading the kernel buffer zone (generally viewed with `dmesg ') |
| `4 proc_debug ' | Disable unprivileged user process debug function |
| '5 randall_pid ' | PROCESS PID RANDOMIZATION |
| `6 clear_tmp ' | clear `/tpm ' on starter |
| `7 capable_syslogd ' | Disable Syslogd Network Socket (disable remote log) |
| `8 security_console ' | enable console password (root password also required in single user mode) |
| '9 disable_ddtrace ' | Ban DTrace destructive mode |


# Install solid

[Virtual Machine non-solidable to install] (. .gitbook/assets/install-14.2.png)

(https://cgit.freebsd.org/src/committee/?id=03c07bdc8b31))。

** This image is from the Virtual Machine Installation Interface**。

[The Physics may have some solids to install]

** This picture is from a physical machine installation interface (using a pick-up card)**


>** Warning**
>
> YOU'D BETTER CANCEL THE CHECK AT THIS POINT, THAT IS, NOT TO INSTALL ANY SOLIDS (WHICH IS ALSO PROBLEMATIC), OTHERWISE YOU'LL BE STUCK HERE INDEFINITELY BECAUSE OF THE NETWORK PROBLEM. IF YOU DON'T REMEMBER WHAT YOU NEED TO INSTALL, YOU CAN TAKE A LOOK AT IT WITH THE CODESPAN_0_。
>
>![ ] (. .gitbook/assets/1-install.png)
>
> ** This image is from a physical machine installation interface (using a pick-up card)**

# Create normal users

![.. ..gitbook/assets/ins30.png]

_CODESPAN_0_

To be created, press ** Return key** to select __CODESPAN_0; if no ordinary user is required, ~ root death squad~, use ** Direction key** to select __CODESPAN_1_。


>** Skills**
>
> The majority of login managers are default-ban root users. In other words, you may not be able to log on to the desktop with root without some change (see other chapters) in the default. ~ Although FreeBSD does not have a desktop under the default status, or it can also be directly __CODESPAN_0~。

![.. ..gitbook/assets/ins31.png]


Note**
>
>IF YOU WANT TO CREATE A NORMAL USER, PLEASE ADD IT TO __CODESPAN_0_GROUP (SEE ARROW POSITION)。


```sh
FreeBSD Installer
========================
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
Enter password: # Enter the password, the password does not appear on the screen, it will not be ****, nothing
Enter password again:
Lock out the account after creation
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



Other parameters keep the default settings unchanged. FreeBSD 14 and beyond, the default shell of all users is unified for __CODESPAN_0_。

__CODESPAN_0_,  **BACK KEYS** TO COMPLETE THE CREATION

IF YOU ENTER __CODESPAN_0_, PRESS ** RETURN KEY** TO CREATE A SECOND NORMAL USER。

# End installation

![.. ..gitbook/assets/ins32.png]

_CODESPAN_0_

Press ** Return key** to finish installation。

![.. ..gitbook/assets/ins33.png]

_CODESPAN_0_

Press ** Return key** to complete installation。

![.. ..gitbook/assets/ins34.png]

_CODESPAN_0_

Press ** Return key** to restart the newly installed system。



Welcome to FreeBSD

Restart to FreeBSD new system after installation:

![.. ..gitbook/assets/ins35.png]

After full start:

>** Skills**
>
>FreeBSD basic system does not have a graphical interface and Xorg is not installed, so this is the case。



![.. ..gitbook/assets/ins36.png]

ENTER THE USERNAME __CODESPAN_0_ AND THE PASSWORD __CODESPAN_1_ SET AT THE TIME OF INSTALLATION TO LOG IN TO THE SYSTEM。

>** Skills**
>
>THE PASSWORD IS NOT DISPLAYED ON THE SCREEN, IT'S NOT __CODESPAN_0, IT'S NOTHING, JUST ENTER IT BACK。

![.. ..getbook/assets/ins37.png]

# Fragmentation and unfinished business

- Unable to access installation interface

In the case of virtual machines, check your configuration

If a physics machine:

>Please check the following list in turn:
>
> - Are you a regular home computer
> - processor is intel or amd
> - Has the safe start (Secure Boot) in the BIOS closed
> - is the image downloaded from <https://freebsd.org>
> - DID YOU DOWNLOAD THE LATEST RELEASE MIRROR
> - DID YOU DOWNLOAD THE MIRROR SUFFIX NAME > CODESPAN_0
> - is the mirror verification (sha256) approved
> - DO YOU DOWNLOAD MIRRORS WITH _`amd64`
> - SEE CLEARLY __CODESPAN_0 ** ** NOT** `arm64` (FOR DEVELOPMENT BOARDS)
> - IS YOUR U-DRIVE EXPANDED
- Did you use Ventoy
> -Booking software please use [Rufus] (https://rufus.ie/zh/), not [Ventoy] (https://www.ventoy.net/cn/index.html)


If there is still a problem, please ask first in English in [Office Forums] (https://forums.freebsd.org/); if this does not work, the bug can be presented in other sections。

- Restarted and entered the installation interface

IN THE CASE OF A VIRTUAL MACHINE, PLEASE ACTIVELY EJECT/ DISCONNECT AN AUTOMATIC CONNECTION TO THE DVD STARTER AND RESTART IT; IN THE CASE OF A PHYSICAL MACHINE, REMOVE THE U-DISK OR POP-UP INSTALLED DISK AND RESTART IT。

- It's stuck in a service

In previous versions, services such as sendmail may be stuck on start-up for long periods, or static IP addresses need to be configured, but the system has been trying DHCP。

you can try to enter **ctrl**+**c** to interrupt the service to start the system。
