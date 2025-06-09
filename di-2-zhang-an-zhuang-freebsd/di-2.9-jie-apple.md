# Section 2.9 Install FreeBSD - Based on Apple M1 & Parallels Design 20


This is based on Apple M1 (macOS 14.7), Parallels Desktop 20.1.3-55743。

FreeBSD 15.0 CURRENT GUI (not automatically scaled), keyboard, mouse in Parallels Desktop 20。

Note**
>
[i'm sorry to bother you] (https://reviews.freebsd.org/D42158) was not merged into FreeBSD 14. Therefore, 14 cannot be installed and is reported as an error in the installation interface, see [Virtualizing FreeBSD 14 CURRENT on MacOS M2 Via Parallels 19] (https://forums.freebsd.org/threads/virtualizing-freebsd-14-current-on-macos-m2-via-parallels-1993266/). So only 15 or more can be installed。

# Install

[Parallels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd1.png)

Select " Install Windows, Linux or MacOS through image files " , and continue。

[Parallels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd2.png)

Click " Manual Selection " , and continue。

[Paralels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd3.png)

Click Select File..。

[Parallels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd4.png)

Select the FreeBSD mirror。

>** Warning**
>
>This is based on Apple M1, so the FreeBSD structure you chose should be aarch64

[Parallels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd5.png)

It's called " Unable to detect the operating system" and simply click "continue " 。

[Parallels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd6.png)

The operating system selects " Other " 。

[Paralels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd7.png)

>** Skills**
>
>Paralels Desktop 20 default setup is sufficient and generally does not need to adjust the hardware configuration and is UEFI. You can set yourself up at this step if you need it。

[Paralels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd8.png)

Starts the installation of FreeBSD。

[Parallels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd9.png)

Turn on the FreeBSD。

[Parallels Desktop 20 Install FreeBSD 15.0] (..gitbook/assets/pd10.png)

The desktop is normal when manually installed。

# Solve the problem of not moving the mouse

- Solve the problem of the FreeBSD mouse in Parallels Desktop by adding __CODESPAN_0_:


```sh
ums_load="YES"
```


References

[Issue(s) growing FreeBSD 12.2 aarch64 on Parallels Desktop on Apple Silicon] (https://forums.freebsd.org/threads/issue-s-booting-freebsd-12-2-aarch64-on-parallels-desktop-on-apple-silicon.786544). ]

# Virtual Machine Tool

Installation:

```sh
# pkg install parallels-tools
```

If the prompt is not found:

```sh
# cd /usr/ports/emulators/parallels-tools/ 
# make install clean
```

Note**
>
>For a Ports compile installation, a source code for the current system is required at __CODESPAN_0_。

# Unfinished #

Question: This virtual machine tool does not appear to have been updated for a long time, nor does it have any visible substantive effect. So what is it for

References

- [photo by Paballels-tools Parallels Desktop Tools for FreeBSD] (https://www.freshports.org/emulators/parallels-tools/)
