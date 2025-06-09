# Section 1.5 Linux User Migration Guide

# FreeBSD is different from Linux

- FreeBSD still uses the old BSD init instead of system; BSD init is not the same as the traditional SysVinit - BSD has no running level (runlevel) and no `/etc/inittab ', all controlled by rc.

When running init as a user process, you can simulate AT&T System V UNIX - that is, super-user can specify the level of operation required in the command line: init sends a specific signal to the original (PID 1)init process to perform the corresponding operation and achieve a similar function. See [init] (https://man.freebsd.org/cgi/man.cgi?query=init&sektion=8&manpath=freebsd-release-ports). For example, the implementation of `init 0 ' in FreeBSD remains a shutdown.

| Run level | Signal | Operational instructions |
|: -: |: | | | | | | | | | | | | | | | | | | | |
| 0 | SIGUSR1 | stop system running. Zenium
| 0 | SIGUSR2 | stop system running and shut down power. Zenium
| 0 | SIGWINCH | stops system running, shuts down power and restarts. Zenium
|1 | SIGTERM | into single-user mode. Zenium
|6 | SIGINT| restarts the computer. Zenium
c | SIGSTP | prevents further login. Zenium
Re-scanning terminal equipment files (ttys (5)). Zenium


- FreeBSD all user shell defaults are sh (14 prior root is csh, common user is sh), not bash (toggle to bash or zsh if you like);

- FreeBSD basic system contains virtually no software that is incompatible with the BSD protocol.

>** Thinking issues**
>
>-FreeBSD is committed to GNU, which means that basic systems do not use software such as glibc and GCC.
>
> Do you think BSD has been going to GNU, or Linux has been to GNU?

- Strict separation of FreeBSD user and system profiles, i.e. complete separation of kernel and basic systems from third-party applications;
- FreeBSD is maintained as a complete operating system, not as a kernel and user space; that is, if you want to use FreeBSD, there is only one freeBSD option;
- FreeBSD does not have free commands and does not support the installation of this package (FreeBSD no longer uses procfs), and FreeBSD basic system contains text editors with `ee ' and `vi ' (not vi with a soft link to vim, which is real nvi); there is no preloading of `wget ' but `etch ' .


References

- [Substantial analysis of Linux initialization init system, part 1: sysvinit part 2: UpStart part 3: Systemd] (https://www.cnblogs.com/MYSQLZOUQI/p/5250336.html), for archiving, in original language
- [init -- process control initiation] (https://man.freebsd.org/cgi/man.cgi?query=init)
- [Comparison of init systems] (https://wiki.gentoo.org/wiki/Comparison_of_init_systems)
- [GPL Software in FreeBSD Base] (https://wiki.freebsd.org/GPLinBase), GPS software in FreeBSD Basic System


# FreeBSD's flaws

- FreeBSD is based on the philosophy of slow is fast, fast is slow, both in the community and by developers. It is because of this idea that many things are not rushed and that there is more time to look at everything. But this is a post-industrialization era, and many people think that “fast-to-fast” is just an outdated software engineering theory, preferring agility. ~ We really need to take some time to slow down and look at ourselves, whether knowledge or self. It may not be a waste of time to do nothing. {\i1 \cH30D3F4}
- FreeBSD systems are generally not sufficiently modern and do not have what modern operating systems should be. It's worse in the embedded.
- FreeBSD does not provide users with a basic desktop system;
- FreeBSD has a poor driver;
- FreeBSD has very few developers: this means that your Bug may not be able to solve it for a long time and not all packages can keep up to date;
- relatively little information on FreeBSD;
- Many software, such as NetworkManager, could not be transplanted and components of the desktop environment could not be perfected because Systemd was not compatible with operating systems other than Linux;
- Because of the basic objectives and design problems of the FreeBSD project, FreeBSD basic systems do not contain some software and commands commonly used in Linux, such as `lspci ' and `free ' . Some can be installed on their own, others cannot;
- Two file systems for FreeBSD, ZFS and UFS, can only be expanded and not reduced.
- FreeBSD lacks a top-level application design, and even docker-like technology Jail on the ground floor has not developed; FreeBSD virtualization technology Byhve is difficult to use.

I don't...

Many of Linux ' s commonly used concepts were actually originally derived from BSD, such as packagings, distributions.

- [What is Linux container? (https://www.redhat.com/zh/topics/containers/shenmeshi-linux-rongqi)

The concept now known as packaging technology, which originally appeared in 2000 as FreeBSD jail, could make FreeBSD partitions into several subsystems (also known as Jail). Jail was developed as a safe and secure environment, which system administrators can share with multiple users within or outside the enterprise. In 2001, the implementation of the isolation environment entered the Linux area through the Jacques Gélinas VServer project. After completing this basic work on multiple controlled user spaces in Linux, the Linux packaging began to form and eventually developed into the present. In 2008, Docker came to the stage through dotClaud technology with the same name.

# Basic comparison

| Operating system | Release/life cycle (main version) | Primary package manager (command) | Licence (main) | Tool chain | shell | Desktop |
|: --: --: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
| Ubuntu | [2 years/10 years] (https://ubuntu.com/about/release-cycle) | [apt] [https://ubuntu.com/server/docs/package-manage] | (https://ubuntu.com/legal/international-policy-policy) |gcc |bash | Gnome |
|Gentoo Linux|Scroll Update [Portage(emerge)]
ZeniumArch Linux | Scroll Update [Pacman]
| RHEL | [3 maximum 12 years] (https://access.redhat.com/zh_CN/support/policy/updates/errata) [RPM(yum, dnf)] (https://www.redhat.com/sysadmin/how-manage-packages)
FreeBSD [approximately 2/4 years] (https://www.freebsd.org/security/) Pkg/ports |BSD lang csh/sh
(https://docs.microsoft.com/zh-cn/lifecycle/faq/windows)
| | | | | | | | | | | | | (https://www.apple.com/legal/sla/) | clang zsh | Aqua |


# Command replacement/software substitution

As Linux is also widely used as a GNU tool, it can be run on FreeBSD as long as it is not theoretically dependent on a specific Linux function library.

|Linux command/GNU software |BSD Port/ Command function statement |Note |
|: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
`lsusb ' `sysutils/usbutils ' | displays USB information | used roughly
`lspci ' | sysutils/pciutils ' | displays PCI information | in rough use of `cat / var/run/dmesg ' |
`lsblk ' | sysutils/lsblk '| Show disk usage |/ |
`free ' | sysutils/freecolor ' | shows memory usage | FreeBSD does not provide `free ' orders because it relies on Linux characteristics and is provided by package `procps ' . `free ' , where `free ' is required, may be used as `https://github.com/j-eck/free ' , other alternative orders are `vmstat ' .
`lscpu ' `sysutils/lscpu ' Display Processor Information / |
glibc bsdlibc
GCC |LLVM + Clang | Compiler, Compile Chain Tool
`vim ' | editos/vim/ ' | text editor `vi ' is not softly connected to `vim ' but early `nvi ' |
`wget ' |ftp/wget ' | Downloader | Default download tool for the system is 'fetch '
| `shells/bash `shell | shell | default shell is `sh ' (non-soft connection). You can change it yourself. Zenium
NetworkManager `net-mgmt/networkmgr ' Network connection tool |NetworkManager relies on `systemmd ' and cannot directly transplant |
|lsmod '| `kldstat '| lists loaded kernel modules |/ |
`race ' , `truss ' , call / |
|modprobe ' | Load kernel module: `kldload ' ; unmount kernel module: `kldunload ' | Load kernel module, unload kernel module |/|
