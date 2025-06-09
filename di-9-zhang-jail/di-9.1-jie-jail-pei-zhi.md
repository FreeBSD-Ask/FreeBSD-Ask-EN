Section 9.1 Jail Configuration

# create jail directory

# Into FreeBSD basic system #

Programme I

```sh
# cd /usr/src
# make buildworld                      # 编译基本系统
# make installworld DESTDIR=/usr/jail/ # 安装到 jail
# make distribution DESTDIR=/usr/jail/ # 或者用
```

Programme II

Download __CODESPAN_0_or extract __CODESPAN_1_1_ from iso and depressurize to jail

```sh
# tar -xvf base.txz -C /usr/jail/
```

mounts the devfs filesystem. (not necessarily)

```sh
# mount -t devfs devfs /usr/jail/dev
```

# WRITE __CODESPAN_0_

```sh
# sysrc jail_enable="YES"
```

CREATE __CODESPAN_0_FILE (CAN WRITE __CODESPAN_1_, BUT THIS IS EASY TO MANAGE)

```sh
www {
host.hostname =www.example.org;         # 主机名
ip4.addr = 192.168.0.10;                # IP 地址
path ="/usr/jail";                      # jail 位置
devfs_ruleset = "www_ruleset";          # devfs ruleset
mount.devfs;                            # 挂载 devfs 文件系统到 jail
exec.start = "/bin/sh /etc/rc";         # 启动命令
exec.stop = "/bin/sh /etc/rc.shutdown"; # 关闭命令
}
```

# Management

View online Jail information list with __CODESPAN_0_

```sh
JID IP Address    Hostname   Path
3   192.168.0.10  www       /usr/jail/www
```

Central-British Contrast

| English | Chinese |
| :--------: | :-------: |
| JID | jail ID |
| IP Address | IP ADDRESS |
| Hostname | Host Name |
| Path | jail path |

# start and stop jail

```sh
# service jail start www
# service jail stop www
```

# login jail

```sh
# jexec 1 tcsh
```

# clean off jail

```sh
# jexec 3 /etc/rc.shutdown
```

# upgrade jail

```sh
# freebsd-update -b /here/is/the/jail fetch
# freebsd-update -b /here/is/the/jail install
```

# ping with the network

# turn on ping #

WRITING __CODESPAN_0_

```sh
allow.raw_sockets=1;
allow.sysvipc=1;
```

configure complete please restart jail。

- Example:

```sh
# jail -rc test
```

Network

CREATE __CODESPAN_0_ AND EDIT。

```sh
search lan
nameserver 223.5.5.5 #不要写路由器地址
nameserver 223.6.6.6 #不要写路由器地址
```

# Fragmentation and unfinished business

- Delete files without permission

```sh
# chflags -R noschg directory
```

- `Certificate verification failed for /C=US/O=Let's Encrypt/CN=E6
0020C1CD593C000:error:16000069: STORE routines:ossl_store_get0_loader_int:unregistered'

Checked and timed. Generally occurring in FreeBSD 14.1, 14.2 RELEASE。

Solutions:

```sh
# certctl rehash
```

RE-EXECUT __CODESPAN_0_JUST FINE。

Reason unknown, see

- [Bug 280031 - Cannot into `pkg ' due to 404 on pkg.freebsd.org] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=280031)
- [Cannot fitch (and install) `pkg '] (https://forums.freebsd.org/threads/cannot-fetch-and-install-pkg93976/)
