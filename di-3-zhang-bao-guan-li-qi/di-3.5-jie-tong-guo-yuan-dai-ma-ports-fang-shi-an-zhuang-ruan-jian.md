Section 3.5 Installing software by source code through Ports

The collection of the relevant files or folders of a software (fixing files, checking codes, Makefile, etc.) is Port, which is Ports Collaction, or Ports。

NetBSD and OpenBSD also use Ports (not common)。

> ** Note**
>
> ports and pkg can be used at the same time, and most people do. but it is important to note that the source of pkg must be the last, otherwise there will be problems of dependence (e.g. ssl). the source of the last is later than the ports on the main line (compiled from it), so even the latset source may have the above problems, so if there is a problem, unload the package installed at the pkg and re-enact the ports。

>** Skills**
>
>ports download path is __CODESPAN_0_。


# use ports compression

The use of compressor bags has successfully circumvented the philosophical question of whether there is a chicken or an egg (to install Git but without Ports and without pkg)。

# # download ports compression

- NJU:

```sh
# fetch https://mirrors.nju.edu.cn/freebsd-ports/ports.tar.gz
```

- OR USTC

```sh
# fetch https://mirrors.ustc.edu.cn/freebsd-ports/ports.tar.gz
```

- Or FreeBSD, official

```sh
# fetch https://download.freebsd.org/ftp/ports/ports/ports.tar.gz
```

# # unpressure ports compression


```sh
# tar -zxvf ports.tar.gz -C /usr/ # 解压至路径
# rm ports.tar.gz # 删除存档
```


# Use Git to get Ports

# # Install Git

- install with pkg:

```sh
# pkg install git
```

# Pull the Ports repository (USTC) light clone

```sh
# git clone --filter=tree:0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports
```

# Pull the Ports repository (FreeBSD official)

```sh
# git clone --filter=tree:0 https://git.FreeBSD.org/ports.git /usr/ports
```

# # Full pull of Ports repository (FreeBSD official) and specify branch

```sh
# git clone https://git.FreeBSD.org/ports.git /usr/ports
```

View all branches:

```sh
# cd /usr/ports/ # 切换到 git 项目
# git branch -a
* main # * 代表当前分支
  remotes/origin/2014Q1

	……省略…………

remotes/origin/2025Q1
remotes/orgin/HEAD - >origin/main
remotes/origin/main
````

SWITCH TO __CODESPAN_0_ BRANCH:


```sh
root@ykla:/usr/ports # git switch 2025Q1
正在更新文件: 100% (14323/14323), 完成.
分支 '2025Q1' 设置为跟踪 'origin/2025Q1'。
切换到一个新分支 '2025Q1'
```

View local branch:

```sh
root@ykla:/usr/ports # git branch
* 2025Q1
  main
```

It's been switched for success。


# # Sync Update Ports Git


```sh
root@ykla:/ # cd /usr/ports/ # 切换目标目录
root@ykla:/usr/ports # git pull # 同步更新上游 Ports
```

If the hint has been modified locally, discard local changes and update:

```sh
root@ykla:/usr/ports # git checkout . # 放弃本地修改
root@ykla:/usr/ports # git pull
```

# # troubleshooting and unfinished business


```sh
fatal: unable to access 'https://mirrors.ustc.edu.cn/freebsd-ports/ports.git/': SSL certificate problem: certificate is not yet valid
```

First check time:

```sh
# date
Fri May 31 12:09:26 UTC 2024
```

Time error. Time to read:


```sh
# ntpdate -u pool.ntp.org
 5 Oct 08:39:16 ntpdate[3276]: step time server 202.112.29.82 offset +10960053.088901 sec
```

Inspection time:

```sh
# date
Sat Oct  5 08:39:21 UTC 2024
```

# USE __CODESPAN_0_QUERYING SOFTWARE PATH

Like

```sh
# whereis python
```

Output

```sh
python: /usr/ports/lang/python
```



# See dependency

Installed:

```sh
root@ykla:~ # pkg info -d screen
screen-4.9.0_6:
	indexinfo-0.3.1
```

Not installed:

```sh
root@ykla:/usr/ports/sysutils/htop # make all-depends-list
/usr/ports/ports-mgmt/pkg
/usr/ports/devel/pkgconf
/usr/ports/devel/kyua
……省略一部分……
```


look where python's ports are

```sh
# whereis python
# python: /usr/ports/lang/python
```

# install python3

```sh
# cd /usr/ports/lang/python
# make BATCH=yes clean
```

OF WHICH `BATCH=yes` MEANS THAT IT IS COMPILED USING DEFAULT PARAMETERS。

# How to set all the dependencies needed

```sh
# make config-recursive
```

# how to install dependency using pkg

Do not use Ports to compile dependency, only Ports to compile software packages:

```sh
# make install-missing-packages
```

EXAMPLE:

```sh
root@ykla:~ # cd /usr/ports/chinese/fcitx
root@ykla:/usr/ports/chinese/fcitx # make install-missing-packages
Updating FreeBSD repository catalogue...
FreeBSD repository is up to date.
Updating FreeBSD-base repository catalogue...
FreeBSD-base repository is up to date.
All repositories are up to date.
Updating database digests format: 100%
The following 2 package(s) will be affected (of 0 checked):

New packs to be INSTRAW:
[FreeBSD]
enchant2: 2.2.15_5 [FreeBSD]

Number of packs to be included: 2

94 KiB to be downloaded.

[y/N]:
````

# how to remove the current port and the profile on which it relies

```sh
# make rmconfig-recursive
```

# How to download all required packages once and for all

```sh
# make BATCH=yes fetch-recursive
```

#ports compiled software can also be converted to pkg packages

```sh
# pkg create nginx
```

# Update FreeBSD package/Port

Synchronize Ports Git first。

Lists the obsolete Port software:

```sh
root@ykla:/usr/ports # pkg version -l '<'
chromium-127.0.6533.99             <
curl-8.9.1_1                       <
ffmpeg-6.1.2,1                     <
vlc-3.0.21_4,4                     <
w3m-0.5.3.20230718_1               <
```

Below is a breakdown of 2 upgrade tools mentioned in FreeBSD:

# # 1 portmaster (recommended)

Update:

```sh
# cd /usr/ports/ports-mgmt/portmaster && make install clean
# portmaster -a #自动升级所有软件
# portmaster screen #升级单个软件
```

If you don't want to answer the question to solve your dependency, you can use options like BATCH=yes __CODESPAN_0_:

```sh
# portmaster -a -G --no-confirm
```

# # See dependency #

```sh
root@ykla:/usr/ports/ports-mgmt/portmaster # portmaster sysutils/htop  --show-work

== sync, corrected by elderman == @elder_man

Starting check for all relationships
== sync, corrected by elderman == @elder_man

Installed devel/autoconf
Installed devel/automake
== sync, corrected by elderman ==
== sync, corrected by elderman ==
== sync, corrected by elderman ==
== sync, corrected by elderman ==
````

# 2 portupgrade

```sh
# cd /usr/ports/ports-mgmt/portupgrade && make install clean
# portupgrade -ai #自动升级所有软件，i 会挨个确认
# portupgrade -R screen #升级单个软件
# portupgrade -a --batch		#不要问，只做，等同于  BATCH=yes
```

References

- [portmaster-manage your ports without external data or language]
- [i don't know if i'm going to be able to do that, but i'm going to have to do it]


FreeBSD USE

- How to specify a Ports compiled version

For example, Python's current default compilation is 3.9, to be replaced by 3.11:

```sh
# echo "DEFAULT_VERSIONS+= python=3.11  python3=3.11" >> /etc/make.conf
```

>If only one parameter is set, then it is normal to have a warning, see [Bug] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=243034)
>
> ```sh '
>/
>
{\cHFFFFFF}{\cH00FFFF} PYTHON_DEFAULT must be a version present in PYTHON2 {\cHFFFFFF} or PYTHON3_DEFAULT,
If you want more Python flovors, set BUILD_All_PYTHON_FLAVORS in your make.conf
> ````


The complete list is available at <https://cgit.freebsd.org/ports/tree/Mk/bsd.default-versions.mk>

# # References

- [Ports/DEFAULT_VERSIONS] (https://wiki.freebsd.org/Ports/DEFAULT_VERSIONS)
- [Python] (https://wiki.freebsd.org/Python)


- how to block the whole thing

```sh
# echo "OPTION_UNSET+= MYSQL" >> /etc/make.conf
```

# FreeBSD ports multi-line

WRITES THE FOLLOWING TO __CODESPAN_0, WITHOUT CREATING __CODESPAN_1_。

```ini
FORCE_MAKE_JOBS=yes
MAKE_JOBS_NUMBER=4
```

Linux, like Gentoo, is generally a direct __CODESPAN_0 or __CODESPAN_1, __CODESPAN_2_ is the core number。

__CODESPAN_0 IS THE CORE NUMBER OF THE PROCESSOR (OR THE LINEAR NUMBER。

Query by command:

```sh
root@ykla:/home/ykla # sysctl kern.smp.cpus
kern.smp.cpus: 16
```

Or:

```sh
root@ykla:/home/ykla # sysctl hw.ncpu 
hw.ncpu: 16
```

THE OUTPUT VALUE IS __CODESPAN_0_。

INTEL'S PROCESSOR IS SEARCHING __CODESPAN_0_ FOR THE NUMBER OF THREADS THAT CAN BE SEARCHED ON THE INTERNET。

- On a case-by-case basis, an alias acceleration can be set: (not permanent, FreeBSD 14 effective without default)

```sh
# alias ninja='ninja -j4'
```

# # References

- [Easy way to get cpu feet] (https://forums.freebsd.org/threads/easy-way-to-get-cpu-features105533), where commands for the number of CPU lines are derived。

# SET MEMORY TO __CODESPAN_0_

```sh
# ee /etc/fstab
```

Writing:

```sh
tmpfs /tmp tmpfs rw 0 0
```

__CODESPAN_0_RELAUNCH IS FINE。

# # References

- [tmpfs-in-mumory file system] (https://man.freebsd.org/cgi/man.cgi?tmpfs(5))


# ccache #

>** Warning**
>
>use ccache may result in translation failure! the first compilation will not only be accelerated but will also be slower than it is when it is repeated. it's an act of space for time。


# ccache3

install with pkg:

```sh
root@ykla:~ # pkg install ccache
```

- Install with Ports:

```
# cd /usr/ports/devel/ccache/ 
# make install clean
```

- View soft links:

```sh
root@ykla: # ls -al  /usr/local/libexec/ccache
total 56
drwxr-xr-x   3 root wheel 15 Sep 20 02:02 .
drwxr-xr-x  18 root wheel 49 Sep 20 01:39 ..
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 CC -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 c++ -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 cc -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 clang -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 clang++ -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 clang++15 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 02:02 clang++18 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 clang15 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 02:02 clang18 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 cpp13 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 g++13 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21 Sep 20 00:29 gcc13 -> /usr/local/bin/ccache
drwxr-xr-x   2 root wheel 15 Sep 20 02:02 world
```

---|---

- AMEND _`/etc/make.conf` TO ADD THE FOLLOWING LINE:

```sh
WITH_CCACHE_BUILD=yes
```

- SETS THE MAXIMUM 10GB CACHE TO COMPILE:

```sh
root@ykla:/usr/ports/devel/ccache4 # ccache -M 10G  
Set cache size limit to 10.0 GB
root@ykla:/usr/ports/www/chromium # ccache -s
cache directory                     /root/.ccache
primary config                      /root/.ccache/ccache.conf
secondary config      (readonly)    /usr/local/etc/ccache.conf
cache hit (direct)                     0
cache hit (preprocessed)               0
cache miss                             0
cache hit rate                      0.00 %
cleanups performed                     0
files in cache                         0
cache size                           0.0 kB
max cache size                      10.0 GB
```

- After some time as Ports compiled:

```sh
root@ykla:~ # ccache -s
cache directory                     /root/.ccache
primary config                      /root/.ccache/ccache.conf
secondary config      (readonly)    /usr/local/etc/ccache.conf
stats updated                       Fri Sep 20 02:05:35 2024
cache hit (direct)                    20
cache hit (preprocessed)              17
cache miss                           918
cache hit rate                      3.87 %
called for link                      121
called for preprocessing              26
compile failed                       115
preprocessor error                    66
bad compiler arguments                15
autoconf compile/link                523
no input file                         71
cleanups performed                     0
files in cache                      2305
cache size                           0.0 kB
max cache size                      10.0 GB
```

# ccache4

the latest version is ccache4:

install with pkg:

```sh
# pkg install ccache4
```

Or install with Ports:

```sh
# cd /usr/ports/devel/ccache4/
# make install clean
```

- View soft links:

```sh
root@ykla:~ # ls -al  /usr/local/libexec/ccache    total 55
drwxr-xr-x   3 root wheel 13  9月 20 02:29 .
drwxr-xr-x  20 root wheel 54  9月 20 02:29 ..
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 c++ -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 cc -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 CC -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 clang -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 clang++ -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 clang++15 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 clang15 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 cpp13 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 g++13 -> /usr/local/bin/ccache
lrwxr-xr-x   1 root wheel 21  9月 20 02:29 gcc13 -> /usr/local/bin/ccache
drwxr-xr-x   2 root wheel 13  9月 20 02:29 world
```

---|---

- AMEND _`/etc/make.conf` TO ADD THE FOLLOWING LINE:

```sh
WITH_CCACHE_BUILD=yes
```

- SETS THE MAXIMUM 20GB CACHE TO COMPILE:

```sh
root@ykla: # ccache -M 20G  
Set cache size limit to 20.0 GB
```

- After some time as Ports compiles, check the compilation cache:

```sh
root@ykla:/ # ccache -s
Cacheable calls:   558 /  579 (96.37%)
  Hits:            110 /  558 (19.71%)
    Direct:        110 /  110 (100.0%)
    Preprocessed:    0 /  110 ( 0.00%)
  Misses:          448 /  558 (80.29%)
Uncacheable calls:  21 /  579 ( 3.63%)
Local storage:
  Cache size (GB): 0.0 / 20.0 ( 0.11%)
  Hits:            110 /  558 (19.71%)
  Misses:          448 /  558 (80.29%)
```

View the current profile:

```sh
root@ykla:~ # ccache -p 
(default) absolute_paths_in_stderr = false
(default) base_dir =
(default) cache_dir = /root/.cache/ccache
……省略一部分……
```

References

- [ccache-howto-freebsd.txt.in] (https://github.com/freebsd/freebsd-ports/blob/main/devel/cache/files/cache-howto-freebsd.txt.in)
- [ccache-a fast C/C+compiller Cache] (https://man.freebsd.org/cgi/man.cgi?query=cache&sektion=1&n=1)

# Multi-wire download

# axel #

Installation:

```sh  
# pkg install axel
```

Or..

```sh
# cd /usr/ports/ftp/axel/
# make install clean
```

CREATE OR EDIT __CODESPAN_0_ FILES AND WRITE THE FOLLOWING LINES:

```sh
FETCH_CMD=axel
FETCH_BEFORE_ARGS= -n 10 -a
FETCH_AFTER_ARGS=
DISABLE_SIZE=yes
```

# wget2

```sh
# cd /usr/ports/www/wget2/ && make install clean
```

CREATE OR EDIT __CODESPAN_0_ FILES AND WRITE THE FOLLOWING LINES:

```sh
FETCH_CMD=wget2
FETCH_BEFORE_ARGS= -c -t 3 -o 10
FETCH_AFTER_ARGS=
DISABLE_SIZE=yes
```

__CODESPAN_0_ INTERMITTENT
- __CODESPAN_0_ NUMBER OF RETRIES 3
- __CODESPAN_0_ ENABLES 10 THREADS TO DOWNLOAD。

>** Skills**
>
THIS PARAMETER MAY BE TOO CONSERVATIVE. HOWEVER, IT IS IMPORTANT TO NOTE THAT MANY SERVERS DO NOT SUPPORT MORE THREADS FOR SIMULTANEOUS DOWNLOADS. IT ALSO PUTS A LOT OF PRESSURE ON THE SERVER。

References

- [i don't know, reports-contributed applications] (https://man.freebsd.org/cgi/man.cgi?query=ports&sektion=7), the source of CODESPAN_0, and also the source of parameter `BATCH`_。

