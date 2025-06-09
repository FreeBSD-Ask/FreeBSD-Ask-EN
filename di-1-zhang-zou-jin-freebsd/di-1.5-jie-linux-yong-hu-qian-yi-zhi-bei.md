# Section 1.5 Linux User Migration Guide

# FreeBSD is different from Linux

- FreeBSD is still using the old BSD init instead of system; BSD init is not the same as the traditional SysVinit - BSD has no running level (runlevel) and __CODESPAN_0_, all controlled by rc。

When running init as a user process, you can simulate AT&T System V UNIX - that is, super-user can specify the level of operation required in the command line: init sends a specific signal to the original (PID 1)init process to perform the corresponding operation and achieve a similar function. See [init] (https://man.freebsd.org/cgi/man.cgi?query=init&sektion=8&manpath=freebsd-release-ports). For example, the implementation of ___CODESPAN_0_ in FreeBSD remains a shutdown。

| Run Level | Signal | Operational description |
|:----------:|:------------|:--------------------------------------|
| CC BY-NC-ND 2.0 | SIGUSR1 | Stop the system running。 |
| CC BY-NC-ND 2.0 | SIGUSR2 | Stop the system and turn off the power。 |
| CC BY-NC-ND 2.0 | SIGWINCH | Stop the system, turn off the power and restart。 |
| One | SIGTERM | Enter single-user mode。 |
| Six | SIGINT | Restart the computer。 |
| c | SIGTSTP | Stops further login。 |
| q | SIGHUP | rescan terminal equipment files (ttys (5))。 |


- FreeBSD all user shell defaults are sh (14 prior root is csh, common user is sh), not bash (toggle to bash or zsh if you like)

- FreeBSD basic system contains virtually no software that is incompatible with the BSD protocol。

>** Thinking issues**
>
>-FreeBSD is committed to GNU, which means that basic systems do not use software such as glibc and GCC。
>
> Do you think BSD has been going to GNU, or Linux has been to GNU

- Strict separation of FreeBSD user and system profiles, i.e. complete separation of kernel and basic systems from third-party applications
- FreeBSD is maintained as a complete operating system, not as a kernel and user space; that is, if you want to use FreeBSD, there is only one freeBSD option
- FreeBSD does not have a free command and does not support the installation of this package (freeBSD is no longer using procfs), and the text editor attached to the FreeBSD basic system is __CODESPAN_0 and __CODESPAN_1 (not a soft link to vi, which is real nvi); __CODESPAN_2 __, but __CODESPAN_3 __)。


References

- [Linux Institutionalization init system, Part 1: sysvinit Part 2: Upstart Part 3: System] (https://www.cnblogs.com/MYSQLZOUQI/p/5250336.html), for archiving, in original language
[i'm sorry, but i don't know what you're talking about]
- [Comparison of init systems] (https://wiki.gentoo.org/wiki/Comparison_of_init_systems)
- [GPL Software in FreeBSD Base] (https://wiki.freebsd.org/GPLinBase), GPS software in FreeBSD Basic System


# FreeBSD's flaws

- FreeBSD is based on the philosophy of slow is fast, fast is slow, both in the community and by developers. It is because of this idea that many things are not rushed and that there is more time to look at everything. But this is a post-industrialization era, and many people think that “fast-to-fast” is just an outdated software engineering theory, preferring agility. ~ We really need to take some time to slow down and look at ourselves, whether knowledge or self. It may not be a waste of time to do nothing. {\i1 \cH30D3F4}
- FreeBSD systems are generally not sufficiently modern and do not have what modern operating systems should be. It's worse in the embedded。
- FreeBSD does not provide users with a basic desktop system
- FreeBSD has a poor driver
- FreeBSD has very few developers: this means that your Bug may not be able to solve it for a long time and not all packages can keep up to date
- relatively little information on FreeBSD
- Many software, such as NetworkManager, could not be transplanted and components of the desktop environment could not be perfected because Systemd was not compatible with operating systems other than Linux
- Because of the basic objectives and design problems of the FreeBSD project, the FreeBSD basic system does not contain some software and commands that are commonly used in Linux, such as __CODESPAN_0, __CODESPAN_1_. Some can be installed on their own, others cannot
- Two file systems for FreeBSD, ZFS and UFS, can only be expanded and not reduced
- FreeBSD lacks a top-level application design, and even docker-like technology Jail on the ground floor has not developed; FreeBSD virtualization technology Byhve is difficult to use。

---|---

Many of Linux ' s commonly used concepts were actually originally derived from BSD, such as packagings, distributions。

— [What's a Linux container] (https://www.redhat.com/zh/topics/containers/shenmeshi-linux-rongqi)

The concept now known as packaging technology, which originally appeared in 2000 as FreeBSD jail, could make FreeBSD partitions into several subsystems (also known as Jail). Jail was developed as a safe and secure environment, which system administrators can share with multiple users within or outside the enterprise. In 2001, the implementation of the isolation environment entered the Linux area through the Jacques Gélinas VServer project. After completing this basic work on multiple controlled user spaces in Linux, the Linux packaging began to form and eventually developed into the present. In 2008, Docker came to the stage through dotClaud technology with the same name。

# Basic comparison

| Operating systems | Release/life cycle (main edition) | Primary package manager (command) | Licences (main) | Tool Chain | shell | Desktop |
| :----------: | :---------------------------------------------------------------------------: | :--------------------------------------------------------------------: | :----------------------------------------------------------: | :----: | :--------: | :----------: |
| Ubuntu | [2 years/10 years] (https://ubuntu.com/about/release-cycle) | [apt] (https://ubuntu.com/server/docs/package-manage) | [GNU] (https://ubuntu.com/legal/international-policy-policy) | gcc | bash | Gnome |
| Gentoo Linux | Scroll Update | [Portage (emerge)] (https://wiki.gentoo.org/wiki/Portage) | GNU | gcc | bash | Optional |
| Arch Linux | Scroll Update | [pacman] (https://wiki.archlinux.org/title/pacman) | GNU | gcc | bash | Optional |
| RHEL | [3 up to 12 years] (https://access.redhat.com/zh_CN/support/policy/updates/errata) | [RPM (Yum, dnf)] (https://www.redhat.com/sysadmin/how-manage-packages) | GNU | gcc | bash | Gnome |
| FreeBSD | [approximately 2/4 years] (https://www.freebsd.org/security/) | pkg/ports | BSD | i don't know, clang | csh/sh | Optional |
| Windows | [unfixed] (https://docs.microsoft.com/zh-cn/lifecycle/faq/windows) | Optional | Monochrome | Optional | powershell | Windows Desktop |
| MacOS | 1 year/approximately 5 years | None | [early] (https://www.apple.com/legal/sla/) | i don't know, clang | zsh | Aqua |


# Command replacement/software substitution

As Linux is also widely used as a GNU tool, it can be run on FreeBSD as long as it is not theoretically dependent on a specific Linux function library。

| Linux command/GNU software | BSD Port/command | Description of role | Remarks |
| :-----------------: | :-------------------: |  :---------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `lsusb ' | `sysutils/usbutils ' | SHOW USB INFO | `cat / var/run/dmesg ' |
| `lspci ' | `sysutils/pciutils ' | SHOW PCI INFORMATION | `cat / var/run/dmesg ' |
| `lsblk ' | `sysutils/lsblk ' | Show disk usage | I'm sorry |
| `free ' | 'sysutils/freecolor ' | Show memory usage | FreeBSD did not provide the `free ' order because it relied on Linux characteristics and was provided by the package `procps ' . `free ' , where there is a need, may be used as `https://github.com/j-eck/free '  |
| `lscpu ' | `sysutils/lscpu ' | Show processor information | I'm sorry |
| glibc | bsdlibc | C LIBRARY | I'm sorry |
| GCC | LLVM + Clang | Compiler, Compile Chain Tool | `devel/gcc ' |
| `vim ' | `editos/vim/` | Text Editor | FreeBSD `vi ' is not softly connected to `vim ' but early `nvi ' |
| `wget ' | `ftp/wget ' | Downloader | system default download tool is 'fetch ' |
| bash | `shells/bash ' | shell | the system default shell is `sh ' (nonsoft connection). you can change it yourself。 |
| NetworkManager | `net-mgmt/networkmgr ' | Network Connection Tool | NetworkManager relies on `systemd '  |
| `lsmod ' | `kldstat ' | List loaded kernel modules | I'm sorry |
| `race ' | `truss ' | Tracking system calls | I'm sorry |
| `modprobe ' | load kernel module: `kldload ' ; unmount kernel module: `kldunload ' | Load kernel module, unmount kernel module | I'm sorry |
