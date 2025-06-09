# Section 2.11 Qemu install RISC-V FreeBSD (based on x86 Windows)

Qemu is an open source virtual machine for a pure software simulation that supports the simulation of different systems structures.



This paper is based on Windows 11 24H2 (Physics) X86-64, FreeBSD 14.2 RELEASE RISC-V (Virtual Machine), qemu 20241220.

Qemu

Qemu Download Address:

[QEMU Binaries for Windows (64 bit)] (https://qemu.wiilnetz.de/w64), click on the bottom bottom penultimate file. The text was written as `qemu-w64-setup-20241220.exe ' . Size 174M.

Install Qemu on Windows after download.

# RISC-V FreeBSD disk mirror

RISC-V FreeBSD disk mirror (for example, FreeBSD 14.2 RELEASE):

<https://download.freebsd.org/releases/VM-IMAGEs/14.2-RELEASE/riscv64/Latest/FreeBSD-14.2-RELEASE-riscv-riscv64-zfs.raw.xx>

Uncompressed backup after download.

# OpenSBI

Access to OpenSBI (RISC-V Open Source Manager Binary Interface), functionally similar to BIOS.

I don't...

Install OpenSBI:

```sh '
# Pkg install opensbi
````

Or:

```sh '
#cd/usr/ports/sysutils/opensbi/
# Make install clean
````

Look where `fw_jump.elf ' is:

```sh '
# /etc/periodic/weekly/310.locate #
# local fw_jump.elf
/usr/local/share/opensbi/lp64/generic/firmware/fw_jump.elf
````

Extract `fw_jump.elf ' to Windows under backup.

# U-Boot

Get U-Boot, functionally similar to Grub2.

I don't...

Installation:

```sh '
# pkg install u-boot-qemu-riscv64
````

Or:

```sh '
#cd /usr/ports/sysutils/u-boot-qemu-riscv64
# Make install clean
````

View `u-boot ' location:

```sh '
# /etc/periodic/weekly/310.locate #
# local u-boot.bin
#locate u-boot.bin
/usr/local/share/u-boot/u-boot-qemu-riscv64/u-boot.bin
````

Extract `u-boot.bin ' to Windows under standby.

Configure Qemu

New text file on desktop `qemu.bat ' ,

Writing

``Powershell '
cd /d "C: \Program Files\qemu"
. qemu-system-riskv64.exe
- That's right.
-Smp four.
- Cpu rv64.
- I'm 4G.
-Device virtio-blk-device, drive-drive
-Drive file = "C: \ers\ykla\Desktop\freeBSD-14.2-RELEASE-riscv-riskv64-zfs.raw", if=none,id=hd ^
-Device virtio-net-device.
== sync, corrected by elderman == @elder_man
^
- "C:rs\ykla\desktop\u-boot.bin"
-Append "root = LABEL = rootfs"
-Nogramic.
````

Overview:

- ^ is equivalent to the back slash under Windows.
- `smp 'for CPU Number
- `cpu ' Designates CPU structures
- 'm ' Specifies memory size
- `hostfwd=tcp 'Map Local Port

above, replace `C:\Users\ykla\Desktop\ ' with your own path.

Run the script just fine.

[Qemu install FreeBSD] (./.gitbook/assets/qemu1.png)

Enter the username `root ' to return, no password by default.

Since running in PowerShell and CMD can create a variety of gills (e.g. `ee ' command, or press **TAB**).

But the mirror defaults that ssh is not configured with normal users, and direct ssh is unconnected.

I don't...

- Create an ordinary user (note to add to the Wheel group):

```sh '
# adduser
Username: ykla
Full name:
Uid (Leave empty for default):
Login group [ykla]:
Login group is ykla. Invite ykla into other groups?
[default]:
Shell (sh csh tcsh nologin):
Home directory [/home/ykla]:
Home directory missions:

[yes/no]
Once an empty password?
[yes/no]:
Enter password:
Enter password again:
Lock out the account after crime?
Username: ykla
Password: *****
Full Name:
Uid: 1001
ZFS dataset: zroot/ home/ ykla
Class:
Groups: ykla sheel
Home: /home/ykla
Home Mode:
Shell: /bin/sh
Locked: no
[yes/no]
(Zroot/home/ykla).
IFO:
Add another user?
Goodbye!
````

- Configure sshd:

```sh '
root@freebsd: ~ #service sshd available # Add starter
/etc/rc.conf
root@freebsd: #service sshd start #start sshd service
Generating RSA most key.
3072 SHA256: kXxPXoTuyVXz+KG7eE3J3NH+3rbMXQg6pW+1d9RGLM root@freebsd (RSA)
Setting up ECDSA most key.
256 SHA256: fCNrjiI5KPXvM29hxSVjRPL0NKGceijgYucUJttOuo root@freebsd (ECDCSA)
Generaling ED25519 host key.
256 SHA256: o6DJs5xfC9gUJP0Yjmr4iL9J77nebJnvmlUXBUPyQY root@freebsd (ED25519)
Checking on sshd communication.
Starting sshd.
````

- Then you can connect through ssh on Windows:

``Powershell '
ssh ykla@localhost: 8022
````

# Fragmentation and unfinished business

- Graphical cannot be shown

Pending

# References

- [Create FreeBSD video course using qemu. Run the VM using xhyve.]a3afa112df7de4912aafc249ec82f) with some amplification methods
- There are some conceptual interpretations and overall frameworks on QEMU for Windows x64 (https://naiv.fun/Ops/83.html)
- [RISC-V Integration Review] (https://smist08.wordpress.com/203/04/28/risk-v-migration-revisioned/), from which various parameters are derived.
。