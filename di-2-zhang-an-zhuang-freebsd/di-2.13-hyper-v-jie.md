Section 2.13 Install FreeBSD - Based on Hyper-V

# Hyper-V Profile

Hyper-V is a virtual machine developed by Microsoft for Windows, divided into __CODESPAN_0 and `Gen 2`_. Windows Home Edition does not support Hyper-V。

__CODESPAN_0 AND __CODESPAN_1..

| Hyper-V algebra | Hard Disk | Activate Guidance |
| :----------: | :--------: | :-------------------------------: |
| Gen 1 | IDE + SCSI | MBR ONLY |
| Gen 2 | SCSI ONLY | ONLY UEFI+SAFE STARTUP SUPPORT + PXE SUPPORT |

THE SYSTEM IS QUICKLY CREATED AS __CODESPAN_0_。

Note:**
>
Turn off security startup when > Gen 2 is used, otherwise the system cannot start! Click Settings: Click Secure - > Uncheck Enable Safe Start. As of 2025.2.1 FreeBSD does not support safe start-up。

| Hyper-V algebra | FreeBSD Version | Mouse | Keyboard | Remarks |
| :----------: | :----------: | :----------------------------------------------------------------: | :----: | :--------------------------------------------------------------------------------------------: |
| Gen 1 | 13.0 | Support | Not supported | I'm sorry |
| Gen 2 | 13.0 | [not supported] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=221074) | Support | `sysctl kern.evdev.rcpt_mask=6 ' |
| Gen 2 | 14.0 | Support | Support | See [source code] (https://cgit.FreeBSD.org/src/committee/?id=21f4e817de79d5de79bdf180d358ca5f48bf9) |


# Test environment

- Windows 11 23H2 Professional edition
- FreeBSSD 14.1-RELEASE(__CODESPAN_0_)
- Hyper-V Version: 0.0.22621.4249
- Use Second Generation Hyper-V

# Install Hyper-V

[Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Right click the Windows logo, right click the Terminal Administrator in the pop-up window, and enter the following:

```powershell
PS C:\Users\ykla> Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All 
是否立即重启计算机以完成此操作?
[Y] Yes  [N] No  [?] 帮助 (默认值为“Y”): 
# 此处按回车键确定重启完成 Hyper-V 的安装
```


# Create a virtual machine

[Hyper-V](. . . .gitbook/assets/hp2.png)

Right click the host name of the host and select New > Virtual Machine。



! [Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Click Next Page。


[Hyper-V] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Name, and then click Next Page。

[Hyper-V] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Select Second Generation. Then click " Next page " 。


! [Hyper-V] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Sets the memory size, and then click Next Page。

[Hyper-V](. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Set the network, and then click Next Page。


[Hyper-V] (.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Select the virtual hard drive name, size, storage location. Then click " Next page " 。


! [Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

CLICK BROWSING TO FIND DOWNLOADED __CODESPAN_0_, CHECK. THEN CLICK " NEXT PAGE " 。

[Hyper-V](. . . . .gitbook/assets/hp9.png)

Click Finish。

# Adjust the virtual machine

[Hyper-V](. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Click Settings

[Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Please close the safe start。

[Hyper-V](. ./ .gitbook/assets/hp12.png)

Check out the guest service. For information, see references。

[Hyper-V](..gitbook/assets/hp16.jpg)

You can choose to turn off " use autocheckpoints " , that is, off automatic snapshots. For information, see references。


# Install FreeBSD

[Hyper-V](.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Start the virtual machine。

[Hyper-V](. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 

Start installation。

[Hyper-V](. ./ .gitbook/assets/hp15.jpg)

Installation complete。

# Test desktop

The mouse, keyboard and keyboard are normal and sutureless. However, the desktop size cannot be adjusted。


[Hyper-V](./.gitbook/assets/hp.jpg)

The virtual machine must be shut down before it can be removed。

# References

- [Install Hyper-V on Windows] (https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v), Microsoft official tutorials, with many options
- [Hyper-V Integrated Services] (https://learn.microsoft.com/zh-cn/virtualization/hyper-v-on-windows/reference/internationalization-services) detailing various Hyper-V services
- [Use checkpoint to review the voluntary process to its previous status]
- [Selement between standing and protection points in Hyper-V] (https://learn.microsoft.com/zh-cn/windows-server/virtualization/hyper-v/manage/choose-between-standard-or-project-checkpoints-in-hyper-v)
- [FreeBSD13 Hyper-V Environment] (https://qiita.com/nanorkyo/items/d33e1befd4eb9c004fcd)
