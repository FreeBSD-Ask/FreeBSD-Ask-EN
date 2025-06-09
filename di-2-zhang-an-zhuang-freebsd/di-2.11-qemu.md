# Section 2.11 Qemu install RISC-V FreeBSD (based on x86 Windows)

Qemu is an open source virtual machine for a pure software simulation that supports the simulation of different systems structures。



This paper is based on Windows 11 24H2 (Physics) X86-64, FreeBSD 14.2 RELEASE RISC-V (Virtual Machine), qemu 20241220。

Qemu

Qemu Download Address:

[QEMU Binaries for Windows (64 bit)] (https://qemu.wiilnetz.de/w64), click on the bottom bottom penultimate file. __CODESPAN_0_. Size 174M。

Install Qemu on Windows after download。

# RISC-V FreeBSD disk mirror

RISC-V FreeBSD disk mirror (for example, FreeBSD 14.2 RELEASE):

<https://download.freebsd.org/releases/VM-IMAGEs/14.2-RELEASE/riscv64/Latest/FreeBSD-14.2-RELEASE-riscv-riscv64-zfs.raw.xx>

Uncompressed backup after download。

# OpenSBI

Access to OpenSBI (RISC-V Open Source Manager Binary Interface), functionally similar to BIOS。

---|---

Install OpenSBI:

```sh
# pkg install opensbi
```

Or:

```sh
# cd /usr/ports/sysutils/opensbi/ 
# make install clean
```

LOOK AT THIS

```sh
# /etc/periodic/weekly/310.locate # 刷新数据库
# locate fw_jump.elf
/usr/local/share/opensbi/lp64/generic/firmware/fw_jump.elf
```

Extract __CODESPAN_0_to Windows under backup。

# U-Boot

Get U-Boot, functionally similar to Grub2。

---|---

Installation:

```sh
# pkg install u-boot-qemu-riscv64
```

Or:

```sh
# cd /usr/ports/sysutils/u-boot-qemu-riscv64/ 
# make install clean
```

VIEW __CODESPAN_0_POSITION:

```sh
# /etc/periodic/weekly/310.locate # 刷新数据库
# locate u-boot.bin
root@ykla:/home/ykla # locate u-boot.bin
/usr/local/share/u-boot/u-boot-qemu-riscv64/u-boot.bin
```

Extract __CODESPAN_0_to Windows under backup。

Configure Qemu

CREATE A NEW TEXT FILE ON THE DESKTOP __CODESPAN_0_

Writing

```powershell
cd /d "C:\Program Files\qemu"
.\qemu-system-riscv64.exe ^
    -machine virt ^
    -smp 4 ^
    -cpu rv64 ^
    -m 4G ^
    -device virtio-blk-device,drive=hd ^
    -drive file="C:\Users\ykla\Desktop\FreeBSD-14.2-RELEASE-riscv-riscv64-zfs.raw",if=none,id=hd ^
    -device virtio-net-device,netdev=net ^
    -netdev user,id=net,hostfwd=tcp::8022-:22 ^
    -bios "C:\Users\ykla\Desktop\fw_jump.elf" ^
    -kernel "C:\Users\ykla\Desktop\u-boot.bin" ^
    -append “root=LABEL=rootfs” ^
    -nographic
```

Overview:

- ___ CODESPAN_0 __ corresponds to the back slash under Windows。
-_CODESPAN_0_NUMBER OF CPUS
-__CODESPAN_0_SPECIFY CPU ARCHITECTURE
-__CODESPAN_0_SPECIFY MEMORY SIZE
- __CODESPAN_0_MAP LOCAL PORT

ABOVE, REPLACE __CODESPAN_0_ WITH YOUR OWN PATH。

Run the script just fine。

[Qemu Install FreeBSD] (./.gitbook/assets/qemu1.png)

ENTER THE USERNAME __CODESPAN_0_ TO RETURN TO THE CAR, WITH NO PASSWORD BY DEFAULT。

Since running in PowerShell and CMD can create a variety of obscurities (e. g. __CODESPAN_0_, or press **TAB**)。

but the mirror defaults that ssh is not configured with normal users, and direct ssh is unconnected。

---|---

- create an ordinary user (note to add to the wheel group):

```sh
root@freebsd:~ # adduser 
Username: ykla
Full name:
Uid (Leave empty for default):
Login group [ykla]:
Login group is ykla. Invite ykla into other groups? []: wheel  # 请在此处输入 wheel，否则无法 su
Login class [default]:
Shell (sh csh tcsh nologin) [sh]:
Home directory [/home/ykla]:
Home directory permissions (Leave empty for default):

[yes/no]
Once an empty password
[yes/no]:
Enter password:
Enter password again:
Lock out the account after crime
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
iFO:.
Add another user
Goodbye!
````

- configure sshd:

```sh
root@freebsd:~ # service sshd enable # 添加启动项
sshd enabled in /etc/rc.conf
root@freebsd:~ # service sshd start # 启动 sshd 服务
Generating RSA host key.
3072 SHA256:kXxPXoTuyVXz+KG7eE3J3NH+3rlbMXQg6pW+1d9RGLM root@freebsd (RSA)
Generating ECDSA host key.
256 SHA256:fCNrjiI5KPXvM29hxSVjRPL0NKGceijgYucUJttOIuo root@freebsd (ECDSA)
Generating ED25519 host key.
256 SHA256:o6DJs5xfC9gUJP0Yjmr4iL9J77nebJnvmlUExBUPyQY root@freebsd (ED25519)
Performing sanity check on sshd configuration.
Starting sshd.
```

- Then you can connect through ssh on Windows:

```powershell
ssh ykla@localhost:8022
```

# Fragmentation and unfinished business

- Graphical cannot be shown

Pending

# References

- [The VM using xyve.]
- [Build RISSC-V interpretation on QEU for Windows x64] (https://naiv.fun/Ops/83.html), with some conceptual interpretation and overall framework
- [RISC-V Application Review] (https://smist08.wordpress.com/2023/04/28/risk-v-migration-revisioned/), from which various parameters are derived。
