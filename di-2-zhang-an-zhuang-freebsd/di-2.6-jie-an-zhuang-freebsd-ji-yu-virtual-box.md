# Section 2.6 Install FreeBSD - Based on Virtual Box


# Download VirtualBox

ENTER THE PAGE TO CLICK ON THE RIGHT __CODESPAN_0_ TO DOWNLOAD:

[https://www.virtualbox.org] (https://www.virtualbox.org)

# Install Settings

The following presentations are based on Virtual Box 7.1.4 and Windows 11 24H2。

![.. ..gitbook/assets/vb1.png]

Select New。

![.. ..gitbook/assets/vb2.png]


Name type " FreeBSD " , the bottom few options are automatically completed。

![..gitbook/assets/vb3.png]

SETS THE MEMORY SIZE, THE NUMBER OF CPUS, AND OPENS THE EFI。

>** Skills**
>
>UEFI LOWER GRAPHIC CARD CAN ALSO BE DRIVEN NORMALLY. -2023.1.4 TEST


![...gitbook/assets/vb4.png]

Resizes the hard drive。

![.. ..gitbook/assets/vb4.5.png]

Open settings。

![.. ..gitbook/assets/vb5.png]

`VBoxSVGA` IS FINE WITH THE GRAPHIC CARD CONTROLLER。

>** Warning**
>
>DO NOT TRY TO TICK THE 3D BELOW, WHICH WILL ACTUALLY GIVE UP THE SELECTED __CODESPAN_0_。

![.. ..gitbook/assets/vb5.5.png]

Start installation

![.. .gitbook/assets/vb6.png]

![..gitbook/assets/vb7.png]

![...gitbook/assets/vb8.png]

Note**
>
>The lower version of the VirtualBox installation of FreeBSD will be completed by manual shutdown, unmounting/deleting the installed CD, or re-entering the installation interface。

Installed systems:

![...gitbook/assets/vb9.png]


# Network Settings

# # Method 1 Bridge

Bridges are the simplest way to connect the mainframe to the virtual machine and can be obtained with an IP address of a host in the same IP segment, or 192,168.31.123 if the host is 192,168.31.x。

![. . .gitbook/assets/VBbridge.png]

__CODESPAN_0_IS SUFFICIENT (FOR LONG-TERM ENTRY INTO FORCE `/etc/rc.conf`_ COULD BE ADDED `ifconfig_em0="DHCP"`_)。

IF NO NETWORK (INTERNET) IS AVAILABLE, PLEASE SET DNS AS __CODESPAN_0_. IF NOT, PLEASE LOOK AT THE REST OF THIS CHAPTER。

METHOD 2 NAT

The network set-up is complex and sometimes the bridge does not necessarily work. For the purpose of using a host (e.g. Windows 10) to control the FreeBSD system in a virtual machine, two webcards — one for the NAT network model and the other for the host mode only — are required. As shown in the figure:

![.. ..gitbook/assets/vbnat1.png]

![..gitbook/assets/vbnat2.png]

Use the command CODESPAN_0_ to see that if the second card __CODESPAN_1 __ does not get the ip address, please manually DHCP can get __CODESPAN_2 __ (can be added to __CODESPAN_3 __ for long-term validity)。

IF NO NETWORK (INTERNET) IS AVAILABLE, PLEASE SET DNS AS __CODESPAN_0_. IF NOT, PLEASE LOOK AT THE REST OF THIS CHAPTER。

# The card drive and booster

- install with pkg:

```sh
# pkg install virtualbox-ose-additions
```

Or use Ports:

```sh
# cd /usr/ports/emulators/virtualbox-ose-additions/
# make install clean
```

---|---

- View installation instructions:

```sh
root@ykla:/home/ykla # pkg info -D virtualbox-ose-additions
virtualbox-ose-additions-6.1.50.1401000:
On install:
VirtualBox Guest Additions are installed.
# VirtualBox 客户端增强功能已安装。

To be able and start the assigned services:

# Sysrc vboxguest_enable #
# Sysrc vboxservice_enable #
# enables the required service, using sysrc to add the starter。

To start the services, restart the system.
To start the service, please restart the system。

In some cases, a panic will access when the kennel module loads.
Having no more than one special CPU might miss the issue.
# In some cases, panic may occur when the kernel module is loaded. Limiting to a single nuclear virtual CPU could alleviate the problem。

For features such as window scaling and clipboard sharing, membership of
with username "jerry" as an example:

♪ pw groupmod wheel-m jerry
# to enable window zooming, clipboard sharing, users need to join the wheel group。
# example command adds the user jerry to the wheel group。

The settings dialogue for FreeBSSD examples use of the VMSVGA
while this might suit integrations of FreeBSD
without a desk environment (a common use case), it is not acceptable
where Guest Parties are involved.
# VirtualBox would suggest FreeBSD use VMSVGA graphic card controller。
# This is more appropriate for a free BSD system without desktops, but is not recommended in an environment where Guest Additions are installed。

Where are the plans

1. Prefer VBoxSVGA
# If Guest Additions have been installed, give priority to VBoxSVGA as a graphic card controller。

Do not allow 3D acquisition
i don't know, lose the offer for VBoxSVGA)
# Do not enable 3D acceleration, otherwise the VBoxSVGA settings will be ignored。

You may signore the yellow alert that includes use of VMSVGA.

# YOU CAN IGNORE THE YELLOW WARNING MESSAGE USING VMSVGA。
````

xorg can automatically identify the driver,** not ** manual configuration `/usr/local/etc/X11/xorg.conf` (test-tested manual configuration is more carded, five seconds at a time ...)。

- Start-up services:

```sh
# sysrc vboxguest_enable="YES"
# sysrc vboxservice_enable="YES"
```

- activate services, adjust privileges (in the case of normal users ykla):

```sh
# service vboxguest restart # 可能会提示找不到模块，但是不影响使用
# service vboxservice restart
# pw groupmod wheel -m ykla # 管理员权限
```

# Fragmentation and unfinished business

# EFI CAN'T SHUT DOWN PROPERLY #

EDIT __CODESPAN_0_, ADD

```sh
hw.efi.poweroff=0
```

AND THEN WE'LL RESTART, AND THEN WE'LL TURN IT OFF. THIS IS USING ACPI INSTEAD OF UEFI INTERFACES FOR SHUTDOWN OPERATIONS。

References

- [12.0-U8.1 - > 13.0-U2 Poweroff programme & resolution] (https://www.truenas.com/compunity/threads/12-0-u8-1-13-u2-poweroff-problem-solution.104813/)
- [EFI: VirtualBox command non-stop after subsequent regular shutdown of FreeBSD] (https://forums.freebsd.org/threads/efi-virtualbox-computer-non-stop-after-shutdown-of-freebsd848556)

# The mouse goes in #

PRESS __CODESPAN_0_ (ONE __CODESPAN_1_1_, EACH ON AND AROUND THE NORMAL KEYBOARD, FOR THE DEFAULT SETTING); PRESS __CODESPAN_2 + RIGHT __CODESPAN_3 __ IF THE AUTOMATIC ZOOM SCREEN NEEDS TO BE RESTORED OR IF THE MENU BAR CANNOT BE FOUND。

>** Skills**
>
> ON THE 108 KEYBOARD, THE __CODESPAN_0_ KEY IS BELOW __CODESPAN_1_。

## # UEFI FIRMWARE SETTINGS

CLICK __CODESPAN_0 TO ENTER THE UEFI SOLIDWARE SETTINGS OF THE VB VIRTUAL MACHINE REPEATEDLY。

