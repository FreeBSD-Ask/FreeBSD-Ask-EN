# Foreword

# Target platform

The current version is compatible with FreeBSD 14.2-RELEASE and FreeBSD 15.0-CURRENT and, to the extent possible, downward.

Mainly targeted at x86-64 (amd64), Aarch64 (arm64) and as many other system platforms as possible.

Windows test environments are Windows 10, 11 and use the latest version of Windows as much as possible.

# pkg with ports

Because FreeBSD has two ways of installing software (but individual software does not support pkg installation): therefore, for convenience, as far as possible, a description of the two ways of installation has been included in this course. But I want you to understand that it's just for convenience, not for the use of ports or pkgs for installation or for the use of both.

>** Please note**
>
> Ports are generally HEAD branches, and your pkg is best kept on the same main line as the ports, i.e. all choose `latest ' . But you can also draw your own pkg Quarterly Ports branch such as `2025Q1 ' .

I don't...

The software `yyy ' , `yyy ' is `xx/yyy ' in ports, i.e. the path is `/usr/ports/xx/yyy ' .

- Then you can first install binary packages in pkg, like most Linux usage, down to:

```sh '
# Pkg install yyyyy
````

This can also be done:

```sh '
# pkg install xx/yyyy
````

Or put it this way:

```sh '
♪ Pkg in yyyyy
````

- Then you can also install through Ports:

```sh '
#cd /usr/ports/xx/yyyy
# Make install clean
````

I'll keep popping out the window and asking you how to choose. If the default option is used, do so:

```sh '
#cd /usr/ports/xx/yyyy
# Make BATCH=yes important clean
````

If you want to complete all configurations at once:

```sh '
#cd /usr/ports/xx/yyyy
# Make config-recursive # will ask you until the end of dependency
# Make install clean
````


Command and symbol meaning in this book

`# on behalf of operations under `root ' is substantially equivalent to `su ' , `sudo ' and `doas ' .

`$ ' , `% ' represents normal user account privileges.

```sh '
┌ - - - - ┐ ┌ ┐ ┐
│ Common user │su-root user │
│ ($ or % hint) │← - - │ (# hint) │
└--------
````

I don't...

Note**
>
>Presents some attention.

>** Skills**
>
>tip some tricks.

>** Warning**
>
> Matters that cannot be completed or cause significant harm if they are not known, do not.

I don't...

Chapters:

````
Fragmentation and unfinished business
````

The aim is to leave the existing problems and improvements in the direction/proposals or riddles, with a view to the wisdom of future generations.

# Demand for users

The difficulty benchmark is based on the level of pass or above that general undergraduate students in computer science and technology can achieve.

# The book is located #

The book aims to provide an in-depth analysis of the FreeBSD operating system, bridging the gap between beginners and researchers.

# Bibliography

Related books: New changes are not significant. Unlike Linux, there are so many introductory books. For historical reasons, look at UNIX related books.


> ** Skills**
>
Many of the following books can be read free of charge through Twitter.


The cover, the book name, the author, the ISBN Press, the description of the book.
|: --: |: |: |: |: |: |: |: |: |: |: |: |: | |: | |: | |
(./.gitbook/assets/Unleashed.png) Should you say BSD has no development, or should he be stable? The book recommends Chapters 1, 4, 8, 9, 10, 11, 12, 13
(./.gitbook/assets/unix3.png)
| [UNIX/Linux system management technical manual (version 5)] (. / .gitbook/assets/unix4.png) | UNIX/Linux system management technical manual (version 5) | Evi Nemeth, Garth Snyder, Trent R. Hein, Ben Whaley, Dan Mackin | 9787115532763 | People's Post and Telecommunications Press | Command Progress and UNIX Foundation
| Marshall McKusick, George Neville-Neil, Robert N. M. Watson | 97871111689973 | Mechanical Industry Press Light paper. How many chapters do you have to download on the Internet? Zenium
|! [UNIX Programming Arts] (./.gitbook/assets/s11345267.png) Zenium
| (./.gitbook/assets/dajiaotang.png) Zenium
(./.gitbook/assets/4BSD.png)
|! (. .gitbook/assets/qudong.png)
| (. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
|! [UNIX Web Programming Volume 1 < API (3rd ed. > ) (. . .gitbook/assets/unix1.png) | UNIX Web Programming Volume 1 < API Networking 3 > | W. Richard Stevens, Bill Fenner, Andrew M. Rudoff | 9787115367198 | People ' s Mail and Telecommunications Publishing House | How to use an API for web programming
|! [UNIX Network Programming Volume 2: Inter-process Communications (Rev. 2)] (. . .gitbook/assets/unix2.png) | UNIX Network Programming Volume 2: Inter-process Communications (Rev. 2) | W. Richard Stevens | 9787115367204 People ' s Post and Telecommunications Press |) | In-depth understanding of the various forms of inter-process communication. ** The original author of this book has no third edition.
Uresh Vahalia | 978711491453 | Mechanical Industry Press | UNIX |
|! [Unix quarter-century] (./.gitbook/assets/unix25.png) | Unix quarter-century | Peter H. Salus | 978020154771| Addison-Wesley Commercial | History, translation in [here] (https://freebsd.gitbook.io/unix-er-shi-wu-nian) |
|! [Unix Handbook for Haters] (. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . I don't know.

# Choose your book #

| Cover | Book name | Author | ISBN Press Note |
|: --: |: |: |: |: |: |: |: |: |: |: |: |: | |: | |: | |
|! [UNIX legends: history and memories] (. . .gitbook/assets/unixchuanqi.png) | UNIX legends — history and memories | Brian W Kernighan | 9787115555779 | People's Post and Telecommunications Press | mainly tells the history of UNIX. Write rougher. Zenium
[Absolute FreeBSD, 3rd Edition: The Complete Guide to FreeBS] (. .gitbook/assets/AbsoluteBSD.png) |Absolute FreeBSD 3rd*** Michael W. Lucas | 9781593278922 No Starch Press | English version, currently untranslated. The term includes very basic elements. Remember, people with a computer base don't need to read. Zenium
