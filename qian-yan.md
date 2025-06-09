# Foreword

# Target platform

The current version is compatible with FreeBSD 14.2-RELEASE and FreeBSD 15.0-CURRENT and, to the extent possible, downward。

Mainly targeted at x86-64 (amd64), Aarch64 (arm64) and as many other system platforms as possible。

Windows test environments are Windows 10, 11 and use the latest version of Windows as much as possible。

# pkg with ports

Because FreeBSD has two ways of installing software (but individual software does not support pkg installation): therefore, for convenience, as far as possible, a description of the two ways of installation has been included in this course. But I want you to understand that it's just for convenience, not for the use of ports or pkgs for installation or for the use of both。

>** Please note**
>
>ports are generally HeAD branches, and your pkg better stay on the same main line as the ports, i.e. choose __CODESPAN_0_. But you can also draw your own pkg for the Ports quarterly branch, such as ___CODESPAN_1_。

---|---

To install the software __CODESPAN_0, __CODESPAN_1 _ __ CODESPAN_2 _2 _ in ports, i.e. __ CODESPAN_3 __。

- Then you can first install binary packages in pkg, like most Linux usage, down to:

```sh
# pkg install yyy
```

This can also be done:

```sh
# pkg install xxx/yyy
```

Or put it this way:

```sh
# pkg ins yyy
```

- Then you can also install through Ports:

```sh
# cd /usr/ports/xxx/yyy
# make install clean
```

I'll keep popping out the window and asking you how to choose. If the default option is used, do so:

```sh
# cd /usr/ports/xxx/yyy
# make BATCH=yes install clean
```

If you want to complete all configurations at once:

```sh
# cd /usr/ports/xxx/yyy
# make config-recursive # 会一直问你，直到结束依赖
# make install clean
```


Command and symbol meaning in this book

___ CODESPAN_0 ON BEHALF OF __ CODESPAN_1_, WHICH IS ESSENTIALLY EQUIVALENT TO __ CODESPAN_2 __, __ CODESPAN_3 __ AND __ CODESPAN_4 __。

__CODESPAN_0, __CODESPAN_1_ REPRESENTS NORMAL USER ACCOUNT PRIVILEGES。

```sh
┌---------------┐        ┌--------------┐
│ 普通用户       │--su-→▶│   root 用户   │
│ ($ 或 % 提示符)│←------ │   (# 提示符)  │
└---------------┘  exit  └---------------┘
```

---|---

Note**
>
>Presents some attention。

>** Skills**
>
>tip some tricks。

>** Warning**
>
> Matters that cannot be completed or cause significant harm if they are not known, do not。

---|---

Chapters:

```
故障排除与未竟事宜
```

The aim is to leave the existing problems and improvements in the direction/proposals or riddles, with a view to the wisdom of future generations。

# Demand for users

The difficulty benchmark is based on the level of pass or above that general undergraduate students in computer science and technology can achieve。

# The book is located #

The book aims to provide an in-depth analysis of the FreeBSD operating system, bridging the gap between beginners and researchers。

# Bibliography

Related books: New changes are not significant. Unlike Linux, there are so many introductory books. For historical reasons, look at UNIX related books。


> ** Skills**
>
Many of the following books can be read free of charge through Twitter。


| Cover | Book Name | Author | ISBN | Press | Annotations |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [FreeBSD technology inner] (./.gitbook/assets/Unleashed.png) | FreeBSD technology inner | Brian Tiemann, Michael Urban | 9787111102010 | Mechanical Industry Press | THE 2002 BOOK IS STILL WORKING. SHOULD YOU SAY BSD HAS NO DEVELOPMENT, OR SHOULD HE BE STABLE? THIS BOOK RECOMMENDS CHAPTERS 1, 4, 8, 9, 10, 11, 12, 13 |
| [Unix & Linux University Academy] (./.gitbook/assets/unix3.png) | Unix & Linux University Curriculum | Harley Hahn | 9787302209560 | Qinghua University Press | Command Line Basis |
| [UNIX/Linux System Management Technical Manual (Rev. 5)] (./.gitbook/assets/unix4.png) | UNIX/Linux System Management Technical Manual (version 5) | Evi Nemeth, Garth Snyder, Trent R. Hein, Ben Whaley, Dan Mackin | 9787115532763 | People ' s Post and Telecommunications Press | COMMAND STEP AND UNIX BASIS |
| [FreeBSD operating system design and realization (second edition of original book)] (./.gitbook/assets/freebsd2rd.png) | FreeBSD operating system design and realization (version 2 of the original book) | Marshall McKusick, George Neville-Neil, Robert N.M. Watson | 9787111689973 | Mechanical Industry Press | The kernel was mainly explained. Light paper. How many chapters do you have to download on the Internet |
| [UNIX Programming Arts] (./.gitbook/assets/s11345267.png) | UNIX PROGRAMMING ARTS (TAOUP) | Eric Raymond | 9787121176654 | Electronic Industry Press | THE MAIN DISCUSSION WAS UNIX DESIGN PHILOSOPHY AND SOFTWARE ENGINEERING THEORY。 |
| [church and fair] (./.gitbook/assets/dajiaotang.png) | The Cathedral and the Fair | Eric S. Raymond | 978711452478 | Mechanical Industry Press | The history of the Open Source Campaign was mainly presented。 |
| [4.4 BSD operating system design and realization] (./.gitbook/assets/4 BSD.png) | 4.4 BSD OPERATING SYSTEM DESIGN AND ACHIEVEMENT | Marshall Kirk McKusick | 9787111366478 | Mechanical Industry Press | 4.4 BSD OPERATIONAL SYSTEM DESIGN AND ACHIEVEMENT |
| [In-depth understanding of FreeBSD device driver development] (./.gitbook/assets/qudong.png) | In-depth Understanding FreeBSD Device Driver Development | Joseph Kong | 9787111411574 | Mechanical Industry Press | FreeBSD Device Driver Development |
| [UNIX Environment Advanced Programming (Rev. 3)] (./.gitbook/assets/unix.png) | UNIX ADVANCED ENVIRONMENTAL PROGRAMMING (REV.3) | W. Richard Stevens, Stephen A. Rago | 9787115352118 | People ' s Post and Telecommunications Press | IN-DEPTH KNOWLEDGE OF PRACTICAL KNOWLEDGE OF PROGRAMMING INTERFACES DRIVING THE UNIX KERNEL |
| ! [UNIX Web programming volume 1: API (version 3)] (./.gitbook/assets/unix1.png) | UNIX WEB PROGRAMMING VOLUME 1: API (REV.3) | W. Richard Stevens, Bill Fenner, Andrew M. Rudoff | 9787115367198 | People ' s Post and Telecommunications Press | HOW TO PROGRAM THE NETWORK USING A PATCH API |
| [UNIX Web programming volume 2: Inter-process Communications (version 2)] (./.gitbook/assets/unix2.png) | UNIX NETWORK PROGRAMMING VOLUME 2: INTER-PROCEDURE COMMUNICATIONS (REV.2) | W. Richard Stevens | 9787115367204 | People ' s Post and Telecommunications Press | In-depth knowledge of various forms of inter-process communication. ** The original author of this book has no third edition |
| ! [In-depth understanding of UNIX system] (./.gitbook/assets/unixinternationals.png) | IN-DEPTH UNDERSTANDING THE UNIX SYSTEM | Uresh Vahalia | 978711491453 | Mechanical Industry Press | UNIX KERNEL BASE |
| [Unix quarter-century] (./.gitbook/assets/unix25.png) | One quarter of a century | Peter H. Salus | 9780201547771 | Addison-Wesley Legal | history book, translated in [this] (https://freebsd.gitbook.io/unix-er-shi-wu-nian) |
| ! [Unix Haunters Handbook] (./.gitbook/assets/unixno.png) | Unix Haters Handbook | Simon Garfinkel, Daniel Weise, Steven Strasssmann | 9781568842035 | IDG Books Worldwide, Inc. | history book, translated in [this] (https://book.bsdcn.org/unix-tong-hen-zhe-shou-ce) |

# Choose your book #

| Cover | Book Name | Author | ISBN | Press | Annotations |
| :---: | :---: | :---: | :---: | :---: | :---: |
| [UNIX Legend: History and Memory] (./.gitbook/assets/unixchuanqi.png) | UNIX LEGENDS — HISTORY AND MEMORY | Brian W. Kernighan | 9787115557179 | People ' s Post and Telecommunications Press | MAJOR TALK ABOUT THE HISTORY OF UNIX. WRITE ROUGHER。 |
| [Absolute FreeBSD, 3rd Evaluation: The Complete Guide to FreeBS] (./.gitbook/assets/AbsoluteBSD.png) | ***Absolute FreeBSD 3rd*** | Michael W. Lucas | 9781593278922 | No Statch Press | English version, no translation available. The term includes very basic elements. Remember, people with a computer base don't need to read。 |
