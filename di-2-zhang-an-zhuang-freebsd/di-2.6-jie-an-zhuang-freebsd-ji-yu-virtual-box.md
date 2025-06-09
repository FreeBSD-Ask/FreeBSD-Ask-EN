# Section 2.6 Install FreeBSD - Based on Virtual Box


# Download VirtualBox

Enter the page and click `Download ' to download:

[https://www.virtualbox.org] (https://www.virtualbox.org)

# Install Settings

The following presentations are based on Virtual Box 7.1.4 and Windows 11 24H2.

![.. ..gitbook/assets/vb1.png]

Select New.

![.. ..gitbook/assets/vb2.png]


Name type " FreeBSD " , the bottom few options are automatically completed.

![..gitbook/assets/vb3.png]

Sets the memory size, the number of CPUs, and opens the EFI.

>** Skills**
>
>UEFI lower graphic card can also be driven normally. -2023.1.4 Test


![...gitbook/assets/vb4.png]

Resizes the hard drive.

![.. ..gitbook/assets/vb4.5.png]

Open settings.

![.. ..gitbook/assets/vb5.png]

The VBoxSVGA ' is fine with the graphic card controller.

>** Warning**
>
>Do not attempt to tick the 3D below, which would actually give up the selection `VBoxSVGA ' .

![.. ..gitbook/assets/vb5.5.png]

Start installation!

![.. .gitbook/assets/vb6.png]

![..gitbook/assets/vb7.png]

![...gitbook/assets/vb8.png]

Note**
>
>The lower version of the VirtualBox installation of FreeBSD will be completed by manual shutdown, unmounting/deleting the installed CD, or re-entering the installation interface.

Installed systems:

![...gitbook/assets/vb9.png]


# Network Settings

# # Method 1 Bridge

Bridges are the simplest way to connect the mainframe to the virtual machine and can be obtained with an IP address of a host in the same IP segment, or 192,168.31.123 if the host is 192,168.31.x.

![. . .gitbook/assets/VBbridge.png]

Once set, `#dhclient em0 ' is sufficient (ifconfig_em0= "DHCP" `for long-term effect can be added to `/etc/rc.conf ' ).

If no network (Internet) is available, please set DNS as `223.5.5 ' . If not, please look at the rest of this chapter.

Method 2 NAT

The network set-up is complex and sometimes the bridge does not necessarily work. For the purpose of using a host (e.g. Windows 10) to control the FreeBSD system in a virtual machine, two webcards — one for the NAT network model and the other for the host mode only — are required. As shown in the figure:

![.. ..gitbook/assets/vbnat1.png]

![..gitbook/assets/vbnat2.png]

Take a look at the command #ifconfig ' , and if the second card `em1 ' does not get the ip address, get DHCP manually: `#dhclient em1 ' is available (ifconfig_em1= "DHCP" can be added to `/etc/rc.conf ' for long-term effect).

If no network (Internet) is available, please set DNS as `223.5.5 ' . If not, please look at the rest of this chapter.

# The card drive and booster

- Install with pkg:

```sh '
# pkg install virtualbox-ose-additions
````

Or use Ports:

```sh '
#cd/usr/ports/emulators/virtualbox-ose-additions/
# Make install clean
````

I don't...

- View installation instructions:

```sh '
root@ykla:/home/ykla
virtualbox-ose-additions-6.1.50.1401,000:
On install:
Virtual Box Options are incorporated.
# VirtualBox client enhancement installed.

To be able and start the assigned services:

# Sysrc vboxguest_enable #
# Sysrc vboxservice_enable #
# Enables the required service, using sysrc to add the starter.

To start the services, restart the system.
To start the service, please restart the system.

In some cases, a panic will access when the kennel module loads.
Having no more than one special CPU might miss the issue.
# In some cases, panic may occur when the kernel module is loaded. Limiting to a single nuclear virtual CPU could alleviate the problem.

For features such as window scaling and clipboard sharing, membership of
With username "jerry" as an example:

♪ Pw groupmod wheel-m jerry
# To enable window zooming, clipboard sharing, users need to join the Wheel group.
# Example command adds the user Jerry to the Wheel group.

The settings dialogue for FreeBSSD examples use of the VMSVGA
While this might suit integrations of FreeBSD
Without a desk environment (a common use case), it is not acceptable
Where Guest Parties are involved.
# VirtualBox would suggest FreeBSD use VMSVGA graphic card controller.
# This is more appropriate for a free BSD system without desktops, but is not recommended in an environment where Guest Additions are installed.

Where are the plans?

1. Prefer VBoxSVGA
# If Guest Additions have been installed, give priority to VBoxSVGA as a graphic card controller.

Do not allow 3D acquisition
I don't know, lose the offer for VBoxSVGA)
# Do not enable 3D acceleration, otherwise the VBoxSVGA settings will be ignored.

You may signore the yellow alert that includes use of VMSVGA.

# You can ignore the yellow warning message using VMSVGA.
````

xorg can automatically identify the driver,** ** not required ** manual configuration `/usr/local/etc/X11/xorg.conf ' (tested manual configuration instead of a card and five seconds to click ...).

- Start-up services:

```sh '
# Sysrc vboxguest_enable #
# Sysrc vboxservice_enable #
````

- Activate services, adjust privileges (in the case of normal users ykla):

```sh '
# Service vboxguest present # may suggest that the module is not available, but does not affect its use
# For service vboxservice present
# pw groupmod sheel-m ykla
````

# Fragmentation and unfinished business

# EFI can't shut down properly #

Edit `/etc/sysctl.conf ', add

```sh '
ww.efi.poweroff=0
````

And then we'll restart, and then we'll turn it off. This is using ACPI instead of UEFI interfaces for shutdown operations.

References

- [12.0-U8.1 ->13.0-U2 Poweroff programme & resolution] (https://www.truenas.com/compunity/threads/12-0-u8-1-13-u2-poweroff-problem-solution.104813/)
- [EFI: VirtualBox computer non-stop after subcessful shutdown of FreeBSD] (https://forums.freebsd.org/threads/efi-virtualbox-computer-non-stop-after-accessful-shutdown-of-freebsd84856/)

# The mouse goes in #Press `ctrl ' on the right (one `ctrl ' on the right and one on the right) and press `home ' + right `ctrl ' if the automatic zoom screen needs to be restored or the menu bar cannot be found.

>** Skills**
>
> On the 108 keyboard, the `Home ' key is below `Scroll Lock ' .

## # UEFI firmware settings

The UEFI firmware setup to access the VB virtual machine by `Esc ' repeatedly.

。