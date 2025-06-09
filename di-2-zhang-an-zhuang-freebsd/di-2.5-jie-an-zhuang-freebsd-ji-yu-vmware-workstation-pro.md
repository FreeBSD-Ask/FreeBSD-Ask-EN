# Section 2.5 Install FreeBSD - Based on VMware Workstation Pro


# Video tutorial

- [001-WIndows11 Install VMware17] (https://www.bilibili.com/video/BV1Qji2YLEGS)

Mirror Download

> ** Hint**
>
>Virtual Mirror (https://download.freebsd.org/releases/VM-IMAGES/14.2-RELEASE/amd64Latest/) can also be used for the freeBSD official build, requiring manual build-up of UFS and ZFS。
>
>VIEW IS GENERALLY USED FOR MIRRORS OF SIMILAR FILENAMES AND SUFFIXES, SUCH AS __CODESPAN_0, BUT __CODESPAN_1 _ _ IS NOT ONLY USED FOR U-RECORDING, AND VIRTUAL MACHINES ARE ALSO AVAILABLE, USING THE METHOD TO REFER TO SECTION 31.2。


# Configure virtual machines



[VMware Install FreeBSD] (..gitbook/assets/vm1.png)


[VMware Install FreeBSD] (..gitbook/assets/vm2.png)

[VMware Install FreeBSD] (..gitbook/assets/vm3.png)

Please make sure to choose " Install the operating system later " , otherwise the startup will be problematic。

[VMware Install FreeBSD] (..gitbook/assets/vm4.png)

Select Other, and then choose FreeBSD。

>** Skills**
>
> This step is really meaningless. Even the choice of Windows can be successfully launched. However, for a low version of FreeBSD, the Virtual Machine Enhancement Tool is not open and may be problematic。

[VMware Install FreeBSD] (..gitbook/assets/vm5.png)

VIRTUAL MACHINES OCCUPY A VERY LARGE AMOUNT OF DISK SPACE. IF YOU DON'T WANT C-DISPOSED, PLEASE ADJUST YOUR STORAGE POSITION。

[VMware Install FreeBSD] (..gitbook/assets/vm6.png)

PLEASE RESIZE THE MAXIMUM DISK. THE DEFAULT VALUE IS NOT REASONABLE. TO INSTALL A DESKTOP, THE MINIMUM IS GREATER THAN 20 G。

[VMware Install FreeBSD] (..gitbook/assets/vm7.png)

[VMware Install FreeBSD] (./.gitbook/assets/vm8.png)

[VMware Install FreeBSD] (. .gitbook/assets/vm9.png)

THE DEFAULT 256 M CAN START. BUT THIS IS NOT RECOMMENDED. I CAN'T GIVE 512 M EITHER。

[VMware Install FreeBSD] (./.gitbook/assets/vm10.png)

THE DEFAULT VALUE 1 CPU CAN START. BUT IT DOESN'T MAKE SENSE。

[VMware Install FreeBSD] (..gitbook/assets/vm11.png)

IN USE ISO IMAGE FILE, CLICK ON BROWSE TO FIND AND SELECT THE __CODESPAN_0_ FILE YOU DOWNLOADED。

[VMware Install FreeBSD] (..gitbook/assets/vm12.png)


>** Skills**
>
> FreeBSD can also support VMware cards driving UEFI. –2025.3.24


> ** Warning**
>
[Bug 250580 - VMware UEFI guests grash in private hardware after r366691] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=250580) FreeBSD 11/12 may not be operational in the UEFI environment of VMware. Tested 13.0 Normal startup。



[VMware Install FreeBSD] (. . .gitbook/assets/vm13.png)

[VMware Install FreeBSD](. . .gitbook/assets/vm14.png)

[VMware Install FreeBSD] (..gitbook/assets/vm15.png)


# Network Settings

Use NAT mode (default) and if you cannot connect to the host (physical machine), open VMware Edit - Virtual Network Manager, "Return Default Settings" until a configuration similar to the following figure appears:

Note**
>
>As tested, the bridge virtual machine is very slow to transmit files to the host。

>** Skills**
>
> If the Revert Default Settings do not work, there will always be only one single mode, please configure manually according to the chart。

>** Warning**
>
>NAT MODE "NAME" IS BOUND TO YOUR HOST __CODESPAN_1_1_, THE DEFAULT BOUND TO __CODESPAN_2_: IN OTHER WORDS, __CODESPAN_3_ "NAME" MUST BY DEFAULT BE ASSIGNED TO __CODESPAN_4_, AND THE OTHER NAME VIRTUAL MACHINES WILL NOT BE NETWORKED
>
[i've been working on freebsd]


[i've been working on freebsd]

Please do not set the above manually, and if CODESPAN_0 __ is kept in the virtual machine, restart the physics machine and turn on the virtual machine: VMware Edit - Virtual Network Manager, Revert Default Settings until the above configuration appears. (Please don't try to configure manually. It's not working.)

IF NO NETWORK IS AVAILABLE, PLEASE SET DNS AS __CODESPAN_0_. PLEASE SEE THE REST OF THIS CHAPTER。

IF DHCP CANNOT ALWAYS REACH IP AFTER CONFIGURATION OF THE BRIDGE, YOU CAN TRY MANUALLY TO REPLACE "BRIDGE TO AUTO" WITH THE CARD YOU CURRENTLY USE。

[i've been working on freebsd]

# Virtual machine enhancement tool and graphic card driver

Installation of card-driven and virtual machine enhancement tools, namely:

```sh
# pkg install xf86-video-vmware open-vm-tools xf86-input-vmmouse open-vm-kmod
```

Or..

```
# cd /usr/ports/x11-drivers/xf86-video-vmware/  && make install clean
# cd /usr/ports/emulators/open-vm-tools/ && make install clean
# cd /usr/ports/x11-drivers/xf86-input-vmmouse/  && make install clean
# cd /usr/ports/emulators/open-vm-kmod/ && make install clean
```

Note**
>
>You can do this if you don't use the desktop (still Port __CODESPAN_0_):
>
> ```sh '
>pkg install open-vm-tools-nox11
> ````

Upon installation, the automatic scaling of the screen can be achieved without any additional configuration。

Note**
>
the driver will also need to be installed under >wayland。

>** Skills**
>
> If the screen display is abnormal (too large), try to edit the virtual setup > hardware, device > monitor, specified monitor setup > maximum resolution for any monitor, set to host or slightly below host resolution。


# # Mouse integration (host virtual mouse switch)

Please install a graphic card drive and virtual machine enhancement tool first。

```sh
# sysrc moused_enable=YES
# Xorg -configure
# mv /root/xorg.conf.new /usr/local/share/X11/xorg.conf.d/xorg.conf
```

EDIT __CODESPAN_0_ TO AMEND THE FOLLOWING PARAGRAPH TO READ (OTHER PARTS DO NOT NEED TO BE MOVED, JUST LEAVE THEM AS THEY ARE):

```sh
Section "ServerLayout"
        Identifier     "X.org Configured"
        Screen          0  "Screen0" 0 0
        InputDevice    "Mouse0" "CorePointer"
        InputDevice    "Keyboard0" "CoreKeyboard"
        Option          "AutoAddDevices" "Off"  # 添加此行到此处
EndSection

* Reissued for technical reasons

Section "InputDevice"
Identifier "Mouse0"
Driver "vmmouse" # Modify Mouse to vmmouse
Option "Protocol" "auto"
"/dev/sysmouse"
Option "ZaxisMapping" "4 5 6 7"
EndSection

* Reissued for technical reasons
````

# # Share Folder

Please install virtual machine enhancements first。

# # set shared folders in the physics machine

[FreeBSD VMware Shared Folder]

Note**
>
> There's no reason to doubt that the name of the virtual machine is Windows 11 because it's Windows 11 and BSD's two-system virtual machine。

View the settings in the FreeBSD virtual machine:

```sh
root@ykla:/home/ykla # vmware-hgfsclient
123pan
```

## # load the use module

Load fuse, write __CODESPAN_0_:

```sh
fusefs_load="YES"
```

Mount

# # Mount manually #

Note**
>
> PLEASE EXCHANGE __CODESPAN_0_ FOR YOUR OWN PATH。

```sh
# vmhgfs-fuse .host:/123pan /mnt/hgfs
```

## Automount ##

EDIT ___CODESPAN_0_: WRITE:

Note**
>
> PLEASE EXCHANGE __CODESPAN_0_ FOR YOUR OWN PATH。

```sh
.host:/123pan      /mnt/hgfs    fusefs  rw,mountprog=/usr/local/bin/vmhgfs-fuse,allow_other,failok 0
```

Check (please do so, or if wrongly written, it will be stuck at the opening point):

```sh
# mount -al # 若无输出则正常
```

## # View shared folders

```sh
root@ykla:/home/ykla # ls /mnt/hgfs/
Downloads
root@ykla:/home/ykla # ls /mnt/hgfs/Downloads/
零跑
```

[FreeBSD VMware Shared Folder]

File matches。

References

- [Resolve Ubuntu shared hands on vmware (July 2022)] (https://www.cnblogs.com/MARcogo/p/16463460.html)
- [i'm sorry, use:] (https://forums.freebsd.org/threads/fuse-failed-to-open-use-device4454544), resolving `fuse: failed to open fuse device: No such file or directory`_
- [VMware shared hands] (https://forums.freebsd.org/threads/vmware-shared-funders.10318/), mount method references


# Fragmentation and unfinished business

> ** Note**
>
> The mouse usually becomes difficult to control when using Windows remote desktops or other XRDP tools to remote another Windows desktop and using the VMware virtual machine that operates on it. It's normal

- Every time you enter a graphical interface, the window expands exceptionally。

Adjust the maximum resolution of the virtual machine。

[VMware Install FreeBSD] (..gitbook/assets/vm16.png)

HARDWARE - DISPLAY - MONITOR - MAXIMUM RESOLUTION (M) OF ANY MONITOR, MODIFIED FROM THE DEFAULT MAXIMUM ___CODESPAN_0_(2K) TO OTHER SMALLER VALUES, OR A CUSTOM VALUE。

- No sound

If you still don't have a sound after loading the sound card, please close the volume to 100% and look again. Because the default sounds are almost invisible。

# appendix: bookcom accounts related

# # bookcom account registration

VMware has been acquired by Chase. ** It is therefore necessary to register and log in to the account number of any cartoon products currently downloaded. ** Any tutorial that does not have this domain name is currently invalid。

> **registration process for booking accounts**
>
> - open <https://support.broadcom.com/>
>
>! [open <https://support.broadcom.com/>] (..gitbook/assets/Register.png)
>
> - Click on “Register” at the top right corner (or open directly <https://profile.broadcom.com/web/registration>)
>
Enter your e-mail at the page Email Address (e-mail). If not, you can use your QQ number and then add a __CODESPAN_0 -- like your Q number is __CODESPAN_1 -- so your QQ mailbox is __CODESPAN_2..
>
Enter the text information on the picture (in fact, the authentication code) at the page " Enter text from image " . If you can't see it or know it, you can order the right CODESPAN
> click on Next (continue)
>
Open <https://wx.mail.qq.com/> if you use a mailbox generated by QQQ. Other mailboxes should be opened on their respective websites and, if you do not know, use the QQQbox。
>
>! [Registration] (..getbook/assets/Register2.png)
>
> - Fill in "Enter text from image" for the "Verification Code: 972980" in step five。
>
>! [Mailbox Administration Code]
>
>- Click " Verify & Continue " (confirm and continue)
>
>! [Enter email access code]
>
> - Complete registration
>
>! [Register referred] (. .gitbook/assets/comreg.png)
>
> - End registration process
>
>! [End of registration] (. ..gitbook/assets/dolater.png)


# # broadcom account login

> **broadcom account login process**
>
> - open <https://support.broadcom.com/>
>
> click on "Login" (login) (or open <https://support.broadcom.com/c/portal/login>)
>
>! [Login] (. . . .getbook/assets/loginbcm.png)
>
>-Username (username) is the mailbox you registered to. And then click Next
>
>! [Login](.. . .getbook/assets/loginbcm2.png)
>
>- Click Next
>
>! [Click Next] (..gitbook/assets/loginbcm3.png)
>
>- Click Login
>
>! [Click Login] (..gitbook/assets/loginbcm4.png)
>
>- Login Completed
>
>! [Post-entry interface]

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
>! [Click "VMware Workstation Pro"]
>
> - Click "Release" to select the top one, not necessarily the same as me。
>
>! [Click "Release"]
>
>** or skip the above steps and open them directly <https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware+Workstance+Pro>**
>
>! [Download Home Page]
>
> - FILL OUT THE RED __CODESPAN_0_ PROJECT AND DON'T WRITE IT YOURSELF。
>
>! [Additional information] (..gitbook/assets/downbcm5png)
>
> - Check the box on the left of "I agree to Terms and Conditions" to turn him into a rim。
>
>! [Consent to a history agreement] (..gitbook/assets/downbcm6.png)
>
> - Click on the cloud picture of the right arrow
>
>! [Download] (..gitbook/assets/downbcm7.png)



VMware Workstation Pro is currently available to individual users ** for free download, free use, free authorization. ** Please do not download from any third-party sites. ** Otherwise there will be some unknown consequences -- 90% of the problem is caused by it。


# # Open source/community products

All Open Source/Community products are integrated here for download。

For example: Community Network Driver for ESXi, ESXi Arm Employment。

Address: <https://community.broadcom.com/flings/home>. Any tutorial other than this domain is currently invalid。

# VMware Workplace Player (disused, not used)

VMware Workstation Player is currently out of service. And the function relative to VMware Workstation Pro is very missing. Not recommended, download without clicking <https://support.broadcom.com/group/ecx/productdownloads?subfamily=VMware%20Workstation%20Player>. Currently, all the courses that contain the software are old。
