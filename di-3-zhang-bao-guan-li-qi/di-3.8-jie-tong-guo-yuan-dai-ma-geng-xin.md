# Section 3.8 Update FreeBSD by source code

The basic idea is to get the source code for FreeBSD and then compile it. You can use git directly to replace the code, or you can download the txz compression file in the ISO mirror, or you can download the zip compression package for the current FreeBSD project on the gethub。

See Handbook for compilation process. Very simple。


>**svn to guit**
>
>FreeBSD Project fully migrated from SVN to Git in 2021, i.e. [https://git.freebsd.org] (https://git.freebsd.org)
>
> the way to access the source code has also changed and no longer uses svn。


# Get source code from Git


# # Install Git

```sh
# pkg install git
```

Or:

```
# cd /usr/ports/devel/git/ && make install clean
```


# # Git proxy settings


- IF ___CODESPAN_0, __CODESPAN_1, __CODESPAN_2:

Settings:

```sh
# git config --global http.proxy http://192.168.X.X:7890
# git config --global https.proxy http://192.168.X.X:7890
```

Cancel:

```sh
# git config --global --unset http.proxy
# git config --global --unset https.proxy
```

# Git pulls the source code

```
# git clone --depth 1 https://git.FreeBSD.org/src.git /usr/src 
```

Or (GitHub is a mirror of src on FreeBSD.org, synchronized every 10 minutes)

```
# git clone --depth 1 https://github.com/freebsd/freebsd-src /usr/src
```

References

- [Submitting GitHub Pull Priorities to FreeBSD] (https://freebsdfoundation.org/our-work/journal/browser-based-edition/conformation-development-2/submitting-github-pull-requests-to-freebsd/)


# # troubleshooting and unfinished business


- Git:_CODESPAN_0_

Use FreeBSD source without __CODESPAN_0_

# Gitup

```sh
# pkg install gitup
```

Or:

```
# cd /usr/ports/net/gitup/ && make install clean
```

```
# gitup release # 具体版本需要参考当前 gitup 配置 https://github.com/johnmehr/gitup/blob/main/gitup.conf
# gitup current # 获取 current 源代码
```

# # troubleshooting and unfinished business

- Git:_CODESPAN_0_

It's probably the wrong time

```sh
# ntpdate -u pool.ntp.org # 当时间相差较大时必须使用该命令，其他命令不会生效
```

# Retrieving source code from compressed packages (favourable but not up to date)

The method is simpler and faster。

FreeBSD 14.2 for example:

```sh
# fetch https://download.freebsd.org/ftp/releases/amd64/14.2-RELEASE/src.txz
# tar xvzf src.txz  -C /
```

>** WHY UNPRESSURE TO ___CODESPAN_0_? **
>
> BECAUSE __CODESPAN_0_ WILL DEPRESS THE SOURCE CODE TO __CODESPAN_1_. IF THE ABOVE PATH IS CHANGED TO ___CODESPAN_2_, THE SOURCE CODE WILL BE DEPRESSED TO __CODESPAN_3_. BECAUSE HE'S A CONDENSED BAG WITH A PATH。

>** Skills**
>
>If slow, switch to <https://mirrors.ustc.edu.cn/freebsd/releases/amd/64/14.2-RELEASE/src.txz>

# Start compiling

```sh
# cd /usr/src          # 切到工作目录
# make -j4 buildworld  # 编译世界
# make -j4 kernel      # 编译并安装内核
# reboot               # 重启以使用新内核
# cd /usr/src          # 切回工作目录
# etcupdate -p         # 进行必要的配置文件合并  
# make installworld    # 安装世界 
# etcupdate -B         # 合并更新
# reboot               # 重启以完成更新流程
```

# # troubleshooting and unfinished business

- CODESPAN_0_

Conflict resolution**

>** Skills**
>
> Unlike most modern Linux, [FreeBSD] (https://github.com/freebsd/freebsd-src/tree/main/contrib/nvi) (OpenBSD) __CODESPAN_0 is *[nvi] (https://sites.google.com/a/bostic.com/keith-hostic?authuser=0)* (rerealization of original **ex/vi**) and does not refer to any link symbol to *vim*. Essentially no one can use it, and there is generally no need to study, so it is necessary to replace it with another text editor。
>
> ```sh '
> Export EDITOR=/usr/bin/ee # Switch vi to ee. For version or csh before FreeBSD 14:setenv EDITOR/usr/bin/ee
> export VISUAL=/usr/bin/ee # Switch vi to ee. Used for pre-FreeBSD 14 versions or csh: Setenv VISUAL/usr/bin/ee
> ````

```sh
root@ykla:~ # etcupdate -B     
Conflicts remain from previous update, aborting.

```

```
# etcupdate resolve          # 解决冲突
Resolving conflict in '/etc/group':
Select: (p) postpone, (df) diff-full, (e) edit,
        (h) help for more options: e # 输入 e 解决冲突
# etcupdate -B 
```

# ZFS RELATED UPGRADES CAN BE FOUND IN ZFS SECTION

# References

- [FreeBSD Handbook] (https://handbook.bsdcn.org/)。
[i'm sorry, but i'm sorry, but i'm sorry, but i'm sorry.]
