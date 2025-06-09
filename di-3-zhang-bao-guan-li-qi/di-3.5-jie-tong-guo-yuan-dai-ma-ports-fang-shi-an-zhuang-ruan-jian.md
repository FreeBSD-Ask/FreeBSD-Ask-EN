Section 3.5 Installing software by source code through Ports

The collection of the relevant files or folders of a software (fixing files, checking codes, Makefile, etc.) is Port, which is Ports Collaction, or Ports.

NetBSD and OpenBSD also use Ports (not common).

> ** Note**
>
> ports and pkg can be used at the same time, and most people do. But it is important to note that the source of pkg must be the last, otherwise there will be problems of dependence (e.g. ssl). The source of the last is later than the ports on the main line (compiled from it), so even the latset source may have the above problems, so if there is a problem, unload the package installed at the pkg and re-enact the ports.

>** Skills**
>
>ports download path is `/usr/ports/distriles/'.


# Use ports compression

The use of compressor bags has successfully circumvented the philosophical question of whether there is a chicken or an egg (to install Git but without Ports and without pkg).

# # Download ports compression

- NJU:

```sh '
#fetch https://mirrors.nju.edu.cn/freebsd-ports/ports.tar.gz
````

- Or USTC.

```sh '
#fetch https://mirrors.ustc.edu.cn/freebsd-ports/ports.tar.gz
````

- Or FreeBSD, official.

```sh '
#fetch https://download.freebsd.org/ftp/ports/ports/ports.tar.gz
````

# # unpressure ports compression


```sh '
# tar-zxvf ports.tar.gz-C/usr/ # unpressure to path
# rm ports.tar.gz # delete archive
````


# Use Git to get Ports

# # Install Git

- Install with pkg:

```sh '
# pkg install #
````

# Pull the Ports repository (USTC) light clone

```sh '
#get clear-filter=tree:0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git/usr/ports
````

# Pull the Ports repository (FreeBSD official)

```sh '
#get clear-filter=tree:0 https://git.FreeBSD.org/ports.git/usr/ports
````

# # Full pull of Ports repository (FreeBSD official) and specify branch

```sh '
#get clear https://git.FreeBSD.org/ports.git/usr/ports
````

View all branches:

```sh '
# cd /usr/ports/ # switch to git item
♪ Let's get out of here ♪
* Main *
Remotes/origin/2014Q1

... omitted...

Remotes/origin/2025Q1
Remotes/orgin/HEAD - >origin/main
remotes/origin/main
````

Switch to Branch `2025Q1 ':


```sh '
Root@ykla:/usr/ports
Updating document: 100% (14323/1423), completed.
Branch '2025Q1' is set to track 'origin/2025Q1'.
Switch to a new branch '2025Q1'
````

View local branch:

```sh '
#get Branch
:: 2025Q1
I don't know.
````

It's been switched for success.


# # Sync Update Ports Git


```sh '
root@ykla:/ #cd/usr/ports/ #toggle destination directory
root@ykla:/usr/ports
````

If the hint has been modified locally, discard local changes and update:

```sh '
Root@ykla:/usr/ports #get checkout. #forget local changes
Root@ykla:/usr/ports
````

# # troubleshooting and unfinished business


```sh '
Fatal: unable to access 'https://mirrors.ustc.edu.cn/freebsd-ports/ports.git/:SSL technical programme: certain is not yet valid
````

First check time:

```sh '
♪ date
Fri May 31 12:09:26 UTC 2024
````

Time error. Time to read:


```sh '
# Ntpdate-u pool.ntp.org
5 Oct 08:39: 16 ntpdate [3276]: step time server 202.12.29.82 confset +10960053.088901 sec
````

Inspection time:

```sh '
♪ date
Sat Oct 5 08:39:21 UTC 2024
````

# Use `whereis ' query software path

Like

```sh '
♪ Where's python
````

Output

```sh '
python: /usr/ports/lang/python
````



# See dependency

Installed:

```sh '
Root@ykla: #pkginfo-d screen
Screen-4.9.0_6:
indexinfo-0.3.1
````

Not installed:

```sh '
#make all-depends-list
/usr/ports/ports-mgmt/pkg
/usr/ports/devel/pkgconf
/usr/ports/devel/kyua
. . . . . . . . . . .
````


Look where Python's ports are

```sh '
♪ Where's python
# python: /usr/ports/lang/python
````

# Install python3

```sh '
#cd /usr/ports/lang/python
# Make BATCH=yes clean
````

Where `BATCH=yes ' is meant to be compiled using default parameters.

# How to set all the dependencies needed

```sh '
# Make config-recursive
````

# How to install dependency using pkg

Do not use Ports to compile dependency, only Ports to compile software packages:

```sh '
# Make install-missing-packages
````

Example:

```sh '
Root@ykla:~cd/usr/ports/chinese/fcitx
Root@ykla:/usr/ports/chinese/fcitx #make install-missing-packages
Updating FreeBSD repository catalogue...
FreeBSD report is up to date.
Updating FreeBSD-base repository catalogue...
FreeBSD is up to date.
All returns are up to date.
Updating data categories format: 100%
The following 2 pack(s) will be affected:

New packs to be INSTRAW:
[FreeBSD]
Enchant2: 2.2.15_5 [FreeBSD]

Number of packs to be included: 2

94 KiB to be downloaded.

[y/N]:
````

# How to remove the current port and the profile on which it relies

```sh '
# Make rmconfig-recursive
````

# How to download all required packages once and for all

```sh '
# Make BATCH=yes fix-recursive
````

#ports compiled software can also be converted to pkg packages

```sh '
♪ Pkg create nginx
````

# Update FreeBSD package/Port

Synchronize Ports Git first.

Lists the obsolete Port software:

```sh '
#pkg version-l '<
Chomium-127.0.6533.99 <
Curl-8.9.1_1 <
ffmpeg-6.1.2, 1 <
vlc-3.0.21_4,4 <
w3m-0.5.3.20230718_1 <
````

Below is a breakdown of 2 upgrade tools mentioned in FreeBSD:

# # 1 portmaster (recommended)

Update:

```sh '
# cd /usr/ports/ports-mgmt/portmaster & make install clean
# portmaster-a # auto-upgrad all software
# Portmaster screen
````

`-a-G-no-confirm':

```sh '
# Portmaster-a-G-no-confirm
````

# # See dependency #

```sh '
Root@ykla:/usr/ports/ports-mgmt/portmaster

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

```sh '
# cd /usr/ports/ports-mgmt/portupgrad & make install clean
# portupgrade-ai # auto-upgrad all the software, i'll be confirmed each time
# portupgrade-R clean #
# portupgrade-a-batch #
````

References

- [portmaster -- manage your ports without external data or language]
- [portupgrade, portinstall -- tools to upgraded packages or in-stall new ones via ports or packages]


FreeBSD USE

- How to specify a Ports compiled version?

For example, Python's current default compilation is 3.9, to be replaced by 3.11:

```sh '
# echo "DEFAULT_VERSIONS+= python=3.11 python3=3.11" >/etc/make.conf
````

>If only one parameter is set, then it is normal to have a warning, see [Bug] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=243034)
>
> ```sh '
>/!
>
{\cHFFFFFF}{\cH00FFFF} PYTHON_DEFAULT must be a version present in PYTHON2 {\cHFFFFFF} or PYTHON3_DEFAULT,
If you want more Python flovors, set BUILD_All_PYTHON_FLAVORS in your make.conf
> ````


The complete list is available at <https://cgit.freebsd.org/ports/tree/Mk/bsd.default-versions.mk>.

# # References

- [Ports/DEFAULT_VERSIONS] (https://wiki.freebsd.org/Ports/DEFAULT_VERSIONS)
- [Python] (https://wiki.freebsd.org/Python)


- How to block the whole thing.

```sh '
# Echo "OPTION_UNSET+=MYSQL" > /etc/make.conf
````

# FreeBSD ports multi-line

The following is written in `/etc/make.conf ' without a new one for `touch ' .

```ini '
FORCE_MAKE_JOBS=yes
MAKE_JOBS_NUMBER=4
````

Linux, like Gentoo, is generally a direct `-jx ' or `jx+1 ' , `x ' is the core number.

`4 ' is the core number of processors (or the linear number?

Query by command:

```sh '
Root@ykla:/home/ykla
I'm sorry.
````

Or:

```sh '
#sysctl hw.ncpu
hw.ncpu: 16
````

The output value is the `MAKE_JOBS_NUMBER ' value.

Intel's processor is searching for the `CPU model +ARK ' and the number of lines available on the Intel Network.

- On a case-by-case basis, an alias acceleration can be set: (not permanent, FreeBSD 14 effective without default)

```sh '
# Alias ninja #
````

# # References

- [Easy way to get cpu views] (https://forums.freebsd.org/threads/easy-way-to-get-cpu-features 10553), where commands for the number of CPU lines are derived.

# Set memory to `tmp '

```sh '
# ee / etc/fstab
````

Writing:

```sh '
tmpfs /tmptmpfs rw 0 0
````

`reboot ' can be restarted.

# # References

- [tmpfs --in-mumory file system] (https://man.freebsd.org/cgi/man.cgi?tmpfs(5))


# ccache #

>** Warning**
>
>Use ccache may result in translation failure! The first compilation will not only be accelerated but will also be slower than it is when it is repeated. It's an act of space for time.


# ccache3

Install with pkg:

```sh '
# pkg install ccache
````

- Install with Ports:

````
#cd/usr/ports/devel/cache/
# Make install clean
````

- View soft links:

```sh '
Root@ykla: #ls-al/usr/local/libexec/cache
Total 56
Drewcr-xr-x 3 root sheel 15 Sep 20 02:02.
Drwxr-x 18 root sheel 49 Sep 20 01:39...
/usr/local/bin/cache
lrwxr-xr-x 1 root wheel 21 Sep 20:29 c+- /usr/local/bin/cache
/usr/local/bin/cache
/usr/local/bin/cache
lrwxr-xr-x 1 root sheel 21 Sep 20:00 29 clang++ - /usr/local/bin/cache
lrwxr-xr-x 1 root wheel 21 Sep 20:00 29 clang++15 - /usr/local/bin/cache
lrwxr-xr-x 1 root wheel 21 Sep 20 02:02 clang++18 - /usr/local/bin/cache
lrwxr-xr-x 1 root wheel 21 Sep 20:00 29 clang15 - /usr/local/bin/cache
lrwxr-xr-x1 root/usr/local/bin/cache
/usr/local/bin/cache
lrwxr-xr-x 1 root wheel 21 Sep 20:00 29 g+13 - /usr/local/bin/cache
lrwxr-xr-x 1 root wheel 21 Sep 20:00 29 gcc13 - /usr/local/bin/cache
Drwxr-xr-x 2 root sheel 15 Sep 20 02:02 world
````

I don't...

- Amend `/etc/make.conf ' to add the following line:

```sh '
WITH_CCACHE_BUILD=yes
````

- Sets the maximum 10GB cache to compile:

```sh '
Root@ykla:/usr/ports/devel/cache4
Set size limit to 10.0 GB
Root@ykla:/usr/ports/www/chromium#cache-s
Cache directory / root/.cache
Primary config / root/.cache/ccache.conf
/usr/local/etc/cache.conf
Cache hit (direct) 0
Cache hit (prepressed) 0
Cache miss 0
Cache hit rate 0.00%
"Cleanups perform 0"
No, no, no.
..cache size 0.0 kB
GB 10.
````

- After some time as Ports compiled:

```sh '
# ccache-s
Cache directory / root/.cache
Primary config / root/.cache/ccache.conf
/usr/local/etc/cache.conf
stats raised Fri Sep 20 02:05:35 2024
Cache hit (direct) 20
Cache hit (preprocessed) 17
Cache miss 918.
Cache hit rate 3.87%
Called for link 121
Called for pre-empting 26
I'm sorry, but I'm sorry.
I'm sorry, preprocessor error 66
I'm sorry, bad compiller arguments 15
Autuconf company/link 523
No, no input file 71
"Cleanups perform 0"
I'm sorry, friends in Cache 2305.
..cache size 0.0 kB
GB 10.
````

# ccache4

The latest version is ccache4:

Install with pkg:

```sh '
# pkg install ccache4
````

Or install with Ports:

```sh '
#cd/usr/ports/devel/cache4/
# Make install clean
````

- View soft links:

```sh '
#ls-al/usr/local/libexec/cache total 55
It's not like we're in the middle of nowhere.
Drewcr-xr-x 20 root media 54 September 20 02:29...
lrwxr-xr-x 1 root wheel September 21 20 02:29 c++- /usr/local/bin/cache
/usr/local/bin/cache
lrwxr-xr-x 1 root Wheel September 21 20 02:29 CC->/usr/local/bin/cache
/usr/local/bin/cache
lrwxr-xr-x 1 root wheel September 21 20 02:29 clang++ - >/usr/local/bin/cache
lrwxr-xr-x 1 root wheel 20 02:29 clang++15 - /usr/local/bin/cache
lrwxr-xr-x 1 root Wheel September 21 20 02:29 clang15->/usr/local/bin/cache
/usr/local/bin/cache
lrwxr-xr-x 1 root wheel 20 02:29 g++13 - /usr/local/bin/cache
/usr/local/bin/cache
Drewxr-xr-x 2 root Wheel 13 September 20 02:29 world
````

I don't...

- Amend `/etc/make.conf ' to add the following line:

```sh '
WITH_CCACHE_BUILD=yes
````

- Sets the maximum 20GB cache to compile:

```sh '
# ccache-M 20G
Set size limit to 20.0 GB
````

- After some time as Ports compiles, check the compilation cache:

```sh '
# ccache-s
Cacheable calls: 558 / 579 (96.37%)
Hits: 110 / 558 (19.71%)
Direct: 110 / 110 (100.0%)
Preprocessed: 0 / 110 (0.00 per cent)
Notes: 448 / 558 (80.29%)
Uncacheable calls: 21 / 579 (3.63%)
Local story:
Cache size (GB): 0.0 / 20.0 (0.11%)
Hits: 110 / 558 (19.71%)
Notes: 448 / 558 (80.29%)
````

View the current profile:

```sh '
# ccache-p
(default)
(default) base_dir =
(default) Cache_dir = /root/.cache/cache
. . . . . . . . . . .
````

References

- [ccache-howto-freebsd.txt.in] (https://github.com/freebsd/freebsd-ports/blob/main/devel/cache/files/cache-howto-freebsd.txt.in)
- [ccache-a fast C/C+]+ compiller carche] (https://man.freebsd.org/cgi/man.cgi?query=cache&sektion=1&n=1)

# Multi-wire download

# Axel #

Installation:

```sh '
# pkg install Axel
````

Or...

```sh '
#cd/usr/ports/ftp/axel/
# Make install clean
````

New or edit `/etc/make.conf ' files, with the following lines:

```sh '
FETCH_CMD=axel
FETCH_BEFORE_ARGS=n10-a
FETCH_AFTER_ARGS
DISABLE_SIZE=yes
````

# wget2

```sh '
# cd /usr/ports/www/wget2/ & make install clean
````

New or edit `/etc/make.conf ' files, with the following lines:

```sh '
FETCH_CMD=wget2
FETCH_BEFORE_ARGS=-c-t 3-o 10
FETCH_AFTER_ARGS
DISABLE_SIZE=yes
````

- `-c ' intermittently;
- `-t 3 ` Number of retests 3;
- `-o 10 ' enable 10 threads to download.

>** Skills**
>
This parameter > `10 ' may be too conservative. However, it is important to note that many servers do not support more threads for simultaneous downloads. It also puts a lot of pressure on the server.

References

- [ports-contributed applications] (https://man.freebsd.org/cgi/man.cgi?query=ports&sektion=7), the source of `FETCH_CMD ' and also of the parameter `BATCH ' .

。