# Section 3.2 FreeBSD for Source

# FreeBSD package manager design concept

Those familiar with Linux may find that FreeBSD's package management program is in fact equivalent to the perfect combination of two major Linux distribution package managers:

- Arch Linux: Pacman, pkg
- Gentoo Linux: Portage, which corresponds to Ports is itself a Ports imitation

| Source | Annotations | Remarks |
|:---:|:---|:---|
| pkg | A traditional Linux-like package manager to install binary packages | do not need binary installation software to unconfigure, `pkg ' is not installed by default, enter `pkg ' returns will prompt installation |
| ~ portsnap ~ | Pulls the source code template for Ports (it does not contain the source code, but only some description files and patches). In other words, this source is similar to Gentoo's [ebuild database] (https://mirrors.ustc.edu.cn/help/gentoo.html) | ** Used for free BSD 14 and subsequent editions without configuring** to `git ' , `gitup ' and compressor pack `ports.tar.gz '。 |
| i don't know | This is the origin of Gentoo ' s package manager Portage (order `emerge ' ). To help users compile and install software from source code. In other words, it's equivalent to Gentoo's [Distfiles Source] (https://mirrors.ustc.edu.cn/help/gentoo.html) | The source-code-based compilation software is not required。 |
| oh, update | For updating basic systems (kernel + user space) | It is expected to be abandoned in FreeBSD 15 or 16 and replaced with [pkgbase] (https://wiki.freebsd.org/PkgBase) |
| kernel modeles (kmods) | KERNEL MODULE SOURCE TO ADDRESS POSSIBLE ABI INCOMPATIBILITY BETWEEN SMALL VERSIONS | See [Possible resolution to the drum-kmold Kessmatch after above above above above from Baptist] (https://forums.freebsd.org/threads/possible-solut-to-the-drm-kmod-kernel-mismastch-offer-upgrade-fom-bapt.9608/#post-682984), [CFT: repository for Kernel media] (https://lists.freebsd.org/archives/freebsd-ports/2024-December/006997.html) |


>** Skills**
>
>This paper lists multiple mirror stations for one source, without all configurations, just choose one。

There are currently no official mirror stations in the country, all of which are unofficial。

Note**
>
>[NJU] (https://github.com/nju-lug/NJU-Mirror-Issue/issues/54) and 163 are synchronized directly upstream from USTC instead of FreeBSD。

#pkg source: pkg source provides binary packages

sources within the country generally support only aarch64 (arm64) and amd64 structures。

The pkg source in FreeBSD is divided into two configuration files, system and user. ** Not recommended** to modify __CODESPAN_0~ but it's too much trouble, I usually change this document directly, because it changes with the basic system。

---|---

Not all sources have __CODESPAN_0 and __CODESPAN_1, see <https://pkg.freebsd.org/>。


# # pkg for source

To get a scroll-up package, modify __CODESPAN_0 to __CODESPAN_1_. The difference is found in the FreeBSD manual. Please note that version __CODESPAN_2_ only __CODESPAN_3_。

use the command to modify the system level pkg source with last:

```sh
# sed -i '' 's/quarterly/latest/g' /etc/pkg/FreeBSD.conf
```

---|---

- Create user-level source directories and files:

```sh
# mkdir -p /usr/local/etc/pkg/repos
# ee /usr/local/etc/pkg/repos/mirrors.conf
```

---|---

- CHINA UNIVERSITY OF SCIENCE AND TECHNOLOGY OPEN SOURCE MIRROR STATION (USTC)

>** Skills**
>
>See video course [005-FreeBSD14.2 Place pkg from USTCmirror status] (https://www.bilibili.com/video/BV13ji2YLEkV)

Write the following:

```sh
ustc: {
url: "http://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest",
}
FreeBSD: { enabled: no }
```

- Open Mirror Station, Nanjing University

Write the following:

```sh
nju: {
url: "http://mirrors.nju.edu.cn/freebsd-pkg/${ABI}/latest",
}
FreeBSD: { enabled: no }
```

- Web-enabled mirror stations

Write the following:

```sh
163: {
url: "http://mirrors.163.com/freebsd-pkg/${ABI}/latest",
}
FreeBSD: { enabled: no }
```

#ports source: package manager to compile and install software by source code

# # download ports

This source is the source of downloads per se. It's equal to the previous ___CODESPAN_0_。

## Git method

_other organiser

```sh
# pkg install git
```

or

```sh
# cd /usr/ports/devel/git
# make install clean
```

---|---

Then:

```sh
# git clone  --filter=tree:0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git /usr/ports
```

Note**
>
>__CODESPAN_0_ WILL PUT A GREAT DEAL OF COMPUTING PRESSURE ON THE SERVER, USING AS MUCH AS POSSIBLE __CODESPAN_1_。

Method of downloading compressed files

>** Warning**
>
>Use Ports by downloading the Port file. It is a one-time: Ports cannot be updated after. It is recommended that you prioritize the Git method。


```sh
# fetch https://mirrors.nju.edu.cn/freebsd-ports/ports.tar.gz
```

Or..

```sh
# fetch https://mirrors.ustc.edu.cn/freebsd-ports/ports.tar.gz
```

And..

```sh
# tar -zxvf ports.tar.gz -C /usr/ # 解压至路径
# rm ports.tar.gz # 删除存档
```

# # ports source

this source is the source of downloading the software in the ports。


> ** Warning**
>
> ports sources may not be complete. the rest is probably less than a tenth. see <https://github.com/ustclug/discussions/issues/408>。

Create or modify files:

```sh
# ee /etc/make.conf
```

---|---

- Open Mirror Station, Nanjing University


Write the following:

```sh
MASTER_SITE_OVERRIDE?=http://mirrors.nju.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

- Web-enabled mirror stations

Write the following:

```sh
MASTER_SITE_OVERRIDE?=http://mirrors.163.com/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

- Open Source Software Mirror Station, China University of Science and Technology


Write the following:

```sh
MASTER_SITE_OVERRIDE?=http://mirrors.ustc.edu.cn/freebsd-ports/distfiles/${DIST_SUBDIR}/
```

# kernel modules (kmods) kernel module source: FreeBSD 14.2 and higher (excluding 15.0-CURRENT)

NEW FOLDER __CODESPAN_0 (I.E. __CODESPAN_1_), AND NEW FILE __CODESPAN_2_:


FreeBSD official source

Writing:

# quitely branch

```sh
FreeBSD-kmods {
	url: pkg+https://pkg.freebsd.org/${ABI}/kmods_quarterly_2
	signature_type: "fingerprints"
	fingerprints: "/usr/share/keys/pkg"
	mirror_type: "srv"
	enabled: yes
}
```

# # latest branch

```sh
FreeBSD-kmods {
	url: pkg+https://pkg.freebsd.org/${ABI}/kmods_latest_2
	signature_type: "fingerprints"
	fingerprints: "/usr/share/keys/pkg"
	mirror_type: "srv"
	enabled: yes
}
```

Open Source Software Mirror Station, China University of Science and Technology


Writing:

# quitely branch

```sh
FreeBSD-kmods {
	url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_2
	enabled: yes
}
```

# # latest branch

```sh
FreeBSD-kmods {
	url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest_2
	enabled: yes
}
```


Versions that are not supported by security (please use them as appropriate)

>** Skills**
>
The >Open Source Mirror Station also provides a pkg binary source for expired versions of FreeBSD 11, 12. Useable。

RELEASES THAT ARE NOT SUPPORTED BY SECURITY ARE ALSO AVAILABLE USING BINARY SOURCES. THE FOLLOWING IS THE EXAMPLE OF ___CODESPAN_0_:

First switch to available binary source

```sh
# setenv PACKAGESITE http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
```

if shell's not csh, then:

```sh
# export PACKAGESITE=http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
```

EXAMPLE OF INSTALLATION: __CODESPAN_0_ IS NOW INSTALLED。

```sh
root@ykla:~ # pkg_add -r bsdinfo
Fetching http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest/bsdinfo.tbz... Done.
```

Note**
>
>pkg is not available, and a reminder will not be found that __CODESPAN_0 and `repo.txz`_, as pkgng was not officially supported at the time, and only __CODESPAN_2_ commands were still supported。

# References

- [FreeBSD ports] (https://mirrors.ustc.edu.cn/help/freebsd-ports.html), USTC Mirrors
- [FreeBSD pkg] (https://mirrors.ustc.edu.cn/help/freebsd-pkg.html), USTC Mirrors
