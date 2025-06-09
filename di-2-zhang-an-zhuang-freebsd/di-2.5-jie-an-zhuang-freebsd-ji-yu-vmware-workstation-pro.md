# Section 2.5 Install FreeBSD - Based on VMware Workstation Pro


# Video tutorial

- [001-WIndows11 Installation VMware17] (https://www.bilibili.com/video/BV1Qji2YLEGS)

Mirror Download

> ** Hint**
>
>The virtual machine can also use the officially constructed [virtual machine mirrors] of FreeBSD (https://download.freebsd.org/releases/VM-IMAGES/14.2-RELEASE/amd64/Latest/), requiring manual build-up, with an optional UFS and ZFS.
>
>The virtual machine generally uses mirrors of similar file names and suffixes such as `FreeBSD-14.2-RELEASE-amd64-disc1.iso ' , but `FreeBSD-14.2-RELEASE-amd64-memstick.img ' is not only for U-booking purposes, but also for use in virtual machines, for which reference is made to section 31.2.


# Configure virtual machines



[VMware Installs FreeBSD] (..gitbook/assets/vm1.png)


[VMware Installed FreeBSD] (..gitbook/assets/vm2.png)

[VMware Installs FreeBSD] (..gitbook/assets/vm3.png)

Please make sure to choose " Install the operating system later " , otherwise the startup will be problematic.

[VMware Installs FreeBSD] (..gitbook/assets/vm4.png)

Select Other, and then choose FreeBSD.

>** Skills**
>
> This step is really meaningless. Even the choice of Windows can be successfully launched. However, for a low version of FreeBSD, the Virtual Machine Enhancement Tool is not open and may be problematic.

[VMware Installs FreeBSD] (..gitbook/assets/vm5.png)

Virtual machines occupy a very large amount of disk space. If you don't want C-disposed, please adjust your storage position.

[VMware Installs FreeBSD] (..gitbook/assets/vm6.png)

Please resize the maximum disk. The default value is not reasonable. To install a desktop, the minimum is greater than 20 G.

[VMware Installed FreeBSD] (..gitbook/assets/vm7.png)

[VMware Installs FreeBSD] (..gitbook/assets/vm8.png)

[VMware Installs FreeBSD] (..gitbook/assets/vm9.png)

The default 256 M can start. But this is not recommended. I can't give 512 M either.

[VMware Installs FreeBSD] (./.gitbook/assets/vm10.png)

The default value 1 CPU can start. But it doesn't make sense.

[VMware Installs FreeBSD] (..gitbook/assets/vm11.png)

Click to browse and select the `-RELEASE-amd64-disc1.iso ' file you downloaded in the ISO image file.

[VMware Installs FreeBSD] (..gitbook/assets/vm12.png)


>** Skills**
>
> FreeBSD can also support VMware cards driving UEFI. –2025.3.24


> ** Warning**
>
[Bug 250580 - VMware UEFI guests crash in VMware after r366691] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=250580) FreeBSD 11/12 may not be activated in the UEFI environment of VMware. Tested 13.0 Normal startup.



[VMware Installs FreeBSD] (..gitbook/assets/vm13.png)

[VMware Installs FreeBSD] (..gitbook/assets/vm14.png)

[VMware Installs FreeBSD] (./.gitbook/assets/vm15.png)


# Network Settings

Use NAT mode (default) and if you cannot connect to the host (physical machine), open VMware Edit - Virtual Network Manager, "Return Default Settings" until a configuration similar to the following figure appears:

Note**
>
>As tested, the bridge virtual machine is very slow to transmit files to the host.

>** Skills**
>
> If the Revert Default Settings do not work, there will always be only one single mode, please configure manually according to the chart.

>** Warning**
>
>NAT mode 'name 'is bound to `VMware Network VMwork VMnet8 ' in your host 'The Control Panel \Network and Internet\Net ' . The default bind is `8 ' : in other words, the `NAT mode `name' must by default be designated as `VMnat8 ' in the following figure, and no network will exist on the other name virtual machine!
>
>! [vmware network on freebsd] (..gitbook/assets/VMnat8.png)


[vmware network on freebsd]

Please do not set the above manually, if inside the virtual machine is always hinting at 'no link ' , please restart the physics machine and turn on the virtual machine: VMware Edit - Virtual Network Manager, Revert Default Settings until the above configuration appears. (Please don't try to configure manually. It's not working.)

If no network is available, please set DNS as `223.5.5 ' . Please see the rest of this chapter.

If DHCP cannot always reach IP after configuration of the bridge, you can try manually to replace "bridge to auto" with the card you currently use.

[vmware network on freebsd]

# Virtual machine enhancement tool and graphic card driver

Installation of card-driven and virtual machine enhancement tools, namely:

```sh '
# pkg install xf86-video-vmware open-vm-tools xf86-input-vmmuse open-vm-kmod
````

Or...

````
#cd /usr/ports/x11-drivers/xf86-video-vmware/ & make install clean
#cd /usr/ports/emulators/open-vm-tools/ & make install clean
#cd /usr/ports/x11-drivers/xf86-input-vmmuse/ & make install clean
#cd /usr/ports/emulators/open-vm-kmod/ & make install clean
````

Note**
>
>This can be done if you do not use the desktop (still Port `emulators/open-vm-tools '):
>
> ```sh '
>pkg install open-vm-tools-nox11
> ````

Upon installation, the automatic scaling of the screen can be achieved without any additional configuration.

Note**
>
The driver will also need to be installed under >wayland.

>** Skills**
>
> If the screen display is abnormal (too large), try to edit the virtual setup > hardware, device > monitor, specified monitor setup > maximum resolution for any monitor, set to host or slightly below host resolution.


# # Mouse integration (host virtual mouse switch)

Please install a graphic card drive and virtual machine enhancement tool first.

```sh '
# Sysrc moussed #
Xorg - configure
#mv / root/xorg.conf.new/usr/local/share/X11/xorg.conf.d/xorg.conf
````

Edit `/usr/local/share/X11/xorg.conf.d/xorg.conf ' to amend the following paragraph to read (other parts do not need to be moved, leave them as they are):

```sh '
Section "ServerLayout"
Identifier "X.org Configured"
Screen 0 "Screen0" 0
InputDevice "Mouse0" "CorePointer"
InputDevice "Keyboard0" "CoreKeyboard"
Option "AutoAddDevies" "Off" # Add this line here
EndSection

* Reissued for technical reasons.

Section "InputDevice"
Identifier "Mouse0"
Driver "vmmouse" # Modify Mouse to vmmouse
Option "Protocol" "auto"
"/dev/sysmouse"
Option "ZaxisMapping" "4 5 6 7"
EndSection

* Reissued for technical reasons.
````

# # Share Folder

Please install virtual firstMachine enhancement tool.

# # set shared folders in the physics machine

[FreeBSD VMware Shared Folders] (..gitbook/assets/hgfs1.png)

Note**
>
> There's no reason to doubt that the name of the virtual machine is Windows 11 because it's Windows 11 and BSD's two-system virtual machine.

View the settings in the FreeBSD virtual machine:

```sh '
#vmware-hgfsclient
123 Pan
````

## # load the use module

Load fuse, write `/boot/loader.conf ':

```sh '
Fusefs_load=YES
````

Mount

# # Mount manually #

Note**
>
> Please replace `123 Pan ' with your own path.

```sh '
# vmhgfs-fuse.host:/123pan/mnt/hgfs
````

## Automount ##

Edit `/etc/fstab/`: Write:

Note**
>
> Please replace `123 Pan ' with your own path.

```sh '
.host: /123pan /mnt/hgfs fusefs rw, mountprog=/usr/local/bin/vmhgfs-fuse, allow_other, failok 0
````

Check (please do so, or if wrongly written, it will be stuck at the opening point):

```sh '
# Mount-al #
````

## # View shared folders

```sh '
Root@ykla:/home/ykla#ls/mnt/hgfs/
Downloads
Root@ykla:/home/ykla#ls/mnt/hgfs/Downloads/
Zero.
````

...! [FreeBSD VMware Shared Folders] (./.gitbook/assets/hgfs2.png)

File matches.

References

- [Resolution on vmware Ubuntu shared folders (July 2022)] (https://www.cnblogs.com/MARCOGO/p/16463460.html), for a holistic approach
- [use: paid to open use data] (https://forums.freebsd.org/threads/fuse-failed-to-open-use-device444), `use: paid to open use device: No such file or directory'
- [VMware sharered figures] (https://forums.freebsd.org/threads/vmware-shared-funders.10318/), mount method references here


# Fragmentation and unfinished business

> ** Note**
>
> The mouse usually becomes difficult to control when using Windows remote desktops or other XRDP tools to remote another Windows desktop and using the VMware virtual machine that operates on it. It's normal!

- Every time you enter a graphical interface, the window expands exceptionally.

Adjust the maximum resolution of the virtual machine.

[VMware Installed FreeBSD] (./.gitbook/assets/vm16.png)

Hardware - Display - Monitor - Maximum Resolution (M) of Any Monitor, modified from the default maximum of `2560 x 1600 `(2K) to other smaller values, or custom value.

- No sound.

If you still don't have a sound after loading the sound card, please close the volume to 100% and look again. Because the default sounds are almost invisible.

# Appendix: Bookcom accounts related

# # bookcom account registration

VMware has been acquired by Chase. ** It is therefore necessary to register and log in to the account number of any cartoon products currently downloaded. ** Any tutorial other than this domain (`broadcom.com ' ) is currently invalid.

> **Registration process for booking accounts**
>
> - Open <https://support.broadcom.com/>
>
>! [Open <https://support.broadcom.com/>] (..getbook/assets/Register.png)
>
> - Click on “Register” at the top right corner (or open directly <https://profile.broadcom.com/web/registration>)
>
Enter your e-mail at the page Email Address (e-mail). If not, you can use your QQ number and then add a `@q.com' -- like your QQ number is `121211111', and your QQ mailbox is `1212111111@ qq.com '
>
Enter the text information on the picture (in fact, the authentication code) at the page " Enter text from image " . `Enter text from image ' to the right if you can't see or know.
> click on Next (continue)
>
Open <https://wx.mail.qq.com/> if you use a mailbox generated by QQQ. Other mailboxes should be opened on their respective websites and, if you do not know, use the QQQbox.
>
>! [Registration] (.../.gitbook/assets/Register2.png)
>
> - Fill in "Enter text from image" for the "Verification Code: 972980" in step five.
>
>! [Mailbox certifier] (..gitbook/assets/mail.png)
>
>- Click " Verify & Continue " (confirm and continue)
>
>! [Input the mailbox authentication code] (..gitbook/assets/Verify.png)
>
> - Complete registration
>
>! [Registration completed] (..gitbook/assets/comreg.png)
>
> - End registration process
>
>! [end of registration] (..gitbook/assets/dolater.png)


# # Broadcom account login

> **Broadcom account login process**
>
> - Open <https://support.broadcom.com/>
>
> click on "Login" (login) (or open <https://support.broadcom.com/c/portal/login>)
>
>! [Book] (..gitbook/assets/loginbcm.png)
>
>-Username (username) is the mailbox you registered to. And then click Next.
>
>! [Book] (..gitbook/assets/loginbcm2.png)
>
>- Click Next
>
>! [click next] (..gitbook/assets/loginbcm3.png)
>
>- Click Login
>
>! [click login] (.. .getbook/assets/loginbcm4.png)
>
>- Login Completed
>
>! [post-entry interface] (..gitbook/assets/afterlogin.png)

# VMware Workstation Pro Download (Recommended)

> **VMware Working Pro Download Process**
>
> - Click on the top right-hand icon (first on the left of the name) to select " VMware Cloud Foundation " (VMware Cloud computing base)
>
>![ ] (..gitbook/assets/downbcm1.png)
>
>- Click My Downloads on the right
>
>![ ] (..gitbook/assets/downbcm0png)
>
> - Flip down, click "VMware Workstation Pro"
>
>! [click on "VMware Workration Pro" (./.gitbook/assets/downbcm2.png)
>
> - Click "Release" to select the top one, not necessarily the same as me.
>
>! [click on “Release”) (.../.gitbook/assets/downbcm3.png)
>
>** or skip the above steps and open them directly <https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware+Workstance+Pro>**
>
>! [download homepage] (..getbook/assets/downbcm4.png)
>
> - Fill out the red `* ' project and don't do it yourself, preferably not copy me.
>
>! [Additional information] (..getbook/assets/downbcm5png)
>
> - Check the box on the left of "I agree to Terms and Conditions" to turn him into a rim.
>
>! [Agree to a licence agreement] (..gitbook/assets/downbcm6.png)
>
> - Click on the cloud picture of the right arrow
>
>! [download] (.. .getbook/assets/downbcm7.png)



VMware Workstation Pro is currently free for individual users **Download, free of charge, free of charge. ** Please do not download from any third-party sites. ** Otherwise there will be some unknown consequences -- 90% of the problem is caused by it.


# # Open source/community products

All Open Source/Community products are integrated here for download.

For example: Community Network Driver for ESXi, ESXi Arm Employment.

Address: <https://community.broadcom.com/flings/home>. At present, any tutorial (`community.broadcom.com ' ) other than this domain is not valid.

# VMware Workplace Player (disused, not used)

VMware Workstation Player is currently out of service. And the function relative to VMware Workstation Pro is very missing. Not recommended, download without clicking <https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Player>. Currently, all the courses that contain the software are old.
。