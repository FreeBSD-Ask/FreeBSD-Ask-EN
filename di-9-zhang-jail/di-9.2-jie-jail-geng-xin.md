Section 9.2 Jail Update

if you want to manage more than one jail at the same time, you have to run each jail on its own once and for all. by creating a single template, all jail can share a basic environment, with their own writing space, without interference。

This paper will create the following directory structure:

- __CODESPAN_0 is a template, a common read-only part of all jail, which will be mounted on __CODESPAN_1 in this case。
- __CODESPAN_0 is a framework that facilitates the creation of jail and does not itself serve any jail。
- __CODESPAN_0 is the root directory run by jail __CODESPAN_1_, the mounted point of a read-only template, which is an empty directory。
- ___ CODESPAN_0 is the mount point of the ___ CODESPAN_1_ and is an empty directory。
- __CODESPAN_0 is the actual repository of the __CODESPAN_1 and will be mounted to `/jail/www/s`_。

If you want to create more than one Jail, create data directories and project directories again so that all jails share __CODESPAN_0_。

REQUIRE __CODESPAN_0_

- install with pkg

```sh
# pkg install cpdup
```

- Install with Ports:

```
# cd /usr/ports/sysutils/cpdup/ 
# make install clean
```

# Create Template Directory

```sh
# mkdir -p /jail/mroot
# 然后放入基本目录
# 将 ports 和源码放入模板
# git clone --filter=tree:0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /jail/mroot/usr/ports
# cpdup /usr/src /jail/mroot/usr/src # 需要提前获取源码，且要注意源码对应的版本要与 /jail/mroot 的版本相同
```

Connect the writeable part to the writeable directory position

```sh
# cd /jail/mroot # cd 到模板目录
# mkdir s        # 创建用来做链接的目录
# ln -s s/etc etc
# ln -s s/home home
# ln -s s/root root
# ln -s ../s/usr-local usr/local
# ln -s ../s/usr-X11R6 usr/X11R6
# ln -s ../../s/distfiles usr/ports/distfiles
# ln -s s/tmp tmp
# ln -s s/var var
```

# Create Frame Directory

```sh
# mkdir -p /jail/skel
# mkdir /jail/skel /jail/skel/home /jail/skel/usr-X11R6 /jail/skel/distfiles /jail/skel/portbuild
# 移动可写部分
# mv /jail/mroot/etc /jail/skel
# mv /jail/mroot/usr/local /jail/skel/usr-local
# mv /jail/mroot/tmp /jail/skel
# mv /jail/mroot/var /jail/skel
# mv /jail/mroot/root /jail/skel
```

installs the missing profile using etcupdate。

```sh
# etcupdate -s /jail/mroot/usr/src -d /jail/skel/var/db/etcupdate -D /jail/skel
```

CREATE COMMON PROFILE FOR __CODESPAN_0_

```sh
# echo “WRKDIRPREFIX?=  /s/portbuild” >> /jail/skel/etc/make.conf
```

# Create Data Directory

It's a copy of a frame

```sh
# cpdup /jail/skel /jail/files/www
```

# Create Project Directory

```sh
# mkdir /jail/www /jail/www/s
```

# create fstab

```sh
# ee /jail/www.fstab
# 将公共只读系统挂载到项目目录
/jail/mroot /jail/www nullfs ro 0 0
# 将项目数据目录挂载到项目目录
/jail/files/www /jail/www/s nullfs rw 0 0
```

# write jail.conf

```sh
# 全局部分

"/bin/sh/etc/rc";
exec.stop = "/bin/sh/etc/rc.shutdown";
i'm sorry, exec.clean;
(a) mount.devfs;
= 1;
= 1;
interface = "webcard address";

# Hostname can also be replaced by variables
hostname = "$name.domain.local";

# jail position, also variable
path = "/jail/$name";

#ip address
ip4.addr = 192,168.1.$ip;

# fstab position
mount.fstab = /jail/$name.fstab;

www {
$ip=2
# if you don't use fstab, use
#mount.fstab ="; # replace global
♪ I'm sorry ♪
````

