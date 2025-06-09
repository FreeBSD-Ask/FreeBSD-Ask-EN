Section 2.13 Install FreeBSD - Based on Hyper-V

# Hyper-V Profile

Hyper-V is a virtual machine developed by Microsoft for Windows, divided into `Gen 1 ' and `Gen 2 ' . Windows Home Edition does not support Hyper-V.

The distinction between `Gen 1 ' and `Gen 2 ' is as follows:

|Hyper-V algebra | hard disk | start guide |
|: -: |: |: |: |: | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
Gen 1 + SCSI Only MBR
|Gen 2| Only SCSI | Only UEFI + Security Start Support + PXE Support

The system is quickly created as `Gen 2 ' .

Note:**
>
Turn off security startup when > Gen 2 is used, otherwise the system cannot start! Click Settings: Click Secure - > Uncheck Enable Safe Start. As of 2025.2.1 FreeBSD does not support safe start-up.

|Hyper-V algebra |FreeBSD version | Mouse | Keyboard | Remarks |
|: - -: |: |: |: | | | | | | | | | | | | | | | : | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
|Gen 1| 13.0| Support | does not support |/ |
|Gen 2 | 13.0 | [not supported] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=221074) | Support | Need to modify parameters `sysctl kern.evdev.rcpt_mask=6`
|Gen 2 | 14.0 | Support | Support | Reference to [source code] (https://cgit.FreeBSD.org/src/committee/?id=21f4e817de79d5de79bbdd380d358ca5f48bf9)


# Test environment

- Windows 11 23H2 Professional edition
- FreeBSD 14.1-RELEASE (`FreeBSD-14.1-RELEASE-amd64-disc1.iso ' )
- Hyper-V Version: 0.0.22621.4249
- Use Second Generation Hyper-V

# Install Hyper-V

[Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Right click the Windows logo, right click the Terminal Administrator in the pop-up window, and enter the following:

``Powershell '
PS C: \uses\ykla>Enable-WindowsOpportalFeature-Online-FeatureName Microsoft-Hyper-V-All
Is the computer restarted immediately to complete this operation?
[Y] Yes [N] No [?] Help (default value "Y"):
# Press the Return key here to make sure you restart the Hyper-V installation
````


# Create a virtual machine

[Hyper-V](. . . .gitbook/assets/hp2.png)

Right click the host name of the host and select New > Virtual Machine.



! [Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Click Next Page.


[Hyper-V] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Name, and then click Next Page.

[Hyper-V] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Select Second Generation. Then click " Next page " .


! [Hyper-V] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Sets the memory size, and then click Next Page.

[Hyper-V](. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Set the network, and then click Next Page.


[Hyper-V] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Select the virtual hard drive name, size, storage location. Then click " Next page " .


! [Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Click " Browse " to find downloaded `FreeBSD-14.1-RELEASE-amd64-disc1.iso ' , selected. Then click " Next page " .

[Hyper-V](. . . . .gitbook/assets/hp9.png)

Click Finish.

# Adjust the virtual machine

[Hyper-V](. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Click Settings

[Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Please close the safe start.

[Hyper-V](. ./ .gitbook/assets/hp12.png)

Check out the guest service. For information, see references.

[Hyper-V](..gitbook/assets/hp16.jpg)

You can choose to turn off " use autocheckpoints " , that is, off automatic snapshots. For information, see references.


# Install FreeBSD

[Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Start the virtual machine.

[Hyper-V](. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

Start installation.

[Hyper-V](. ./ .gitbook/assets/hp15.jpg)

Installation complete.

# Test desktop

The mouse, keyboard and keyboard are normal and sutureless. However, the desktop size cannot be adjusted.


[Hyper-V](./.gitbook/assets/hp.jpg)

The virtual machine must be shut down before it can be removed.

# References

- Installation of Hyper-V on Windows (https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v), Microsoft Official Courses, with options
- [Hyper-V Integrated Services] (https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/reference/information-services) detailing various Hyper-V services
- [Returning the virtual machine to its previous state using the checkpoint] (https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/user-guide/checkpoints?source=recommenations&tabs=hyper-v-manager%2Cpowershell)
- [Selection between standard and production checkpoints in Hyper-V] (https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/manage/choose-between-standard-or-project-checkpoints-in-hyper-v)
- [FreeBSD13 を Hyper-V Environment にイ qiita.com/nanorkyo/items/d33e1befd4eb9c004fcd]
