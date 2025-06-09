# Section 3.2 FreeBSD for Source

# FreeBSD package manager design concept

Those familiar with Linux may find that FreeBSD's package management program is in fact equivalent to the perfect combination of two major Linux distribution package managers:

- Arch Linux: Pacman, pkg.
- Gentoo Linux: Portage, which corresponds to Ports is itself a Ports imitation

I'm sorry.
|: --: |: | | | | | | |
|pkg is a traditional Linux-like package manager for the installation of binary software packages | Do not need binary to install software to unconfigure, `pkg ' is not installed by default, `pkg ' enter will prompt the installation of |
Source template for ~portsnap~ ~ | | | | | | | | | | | ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ In other words, this source [ebuild database] similar to Gentoo (https://mirrors.ustc.edu.cn/help/gentoo.html)** has been abandoned in FreeBSD 14 and subsequent editions, without the need for configuration** to be obtained by, inter alia, `git ' , `gitup ' and compressor packages `ports.tar.gz ' . Zenium
The package manager for |ports|Gentoo (order `emerge ' ) is derived from this. To help users compile and install software from source code. In other words, the [Distfiles Source] equivalent to Gentoo (https://mirrors.ustc.edu.cn/help/gentoo.html) | does not need source-code-based compilation software to unconfigure. Zenium
|update is used to update the basic system (kernel + user space) | is expected to be abandoned in FreeBSD 15 or 16 and replaced by [pkgbase] (https://wiki.freebsd.org/Pkgbase)
|kernel modules (kmods) | kernel core module source, to address possible non-compatibility problems between small versions [Possible resolution to the drum-kmold kennel mismatch after above above above from Baptist] (https://forums.freebsd.org/threads/possible-solution-to-the-drm-kmod-kernel-fishmatch-after-upgrade-fram-bapt.96058#post-68294), [CFT: repository for kennel Modeles] (https://lists.freebsd.org/archives/reports/2024-Deceb97.html)


>** Skills**
>
>This paper lists multiple mirror stations for one source, without all configurations, just choose one.

There are currently no official mirror stations in the country, all of which are unofficial.

Note**
>
>[NJU] (https://github.com/nju-lug/NJU-Mirror-Issue/issues/54) and 163 are synchronized directly upstream from USTC instead of FreeBSD.

#pkg source: pkg source provides binary packages

Sources within the country generally support only aarch64 (arm64) and amd64 structures.

The pkg source in FreeBSD is divided into two configuration files, system and user. ** Not recommended** to modify `/etc/pkg/FreeBSD.conf ' ~ but it's too much trouble, I usually change this document directly ~ because it will change as the basic system is updated.

I don't...

Not all sources have `quarterly ' and `latest ' , see <https://pkg.freebsd.org/>.


# # pkg for source

To get a scroll-up package, change `quarterly ' to `latest ' . The difference is found in the FreeBSD manual. Please note that the version `CURRENT ' is only `latest ' .

Use the command to modify the system level pkg source with last:

```sh '
# sed-i's'/quarterly/latest/g'/etc/pkg/FreeBSD.conf
````

I don't...

- Create user-level source directories and files:

```sh '
#mkdir-p/usr/local/etc/pkg/repos
#ee /usr/local/etc/pkg/repos/mirrors.conf
````

I don't...

- China University of Science and Technology Open Source Mirror Station (USTC)

>** Skills**
>
>Video course [005-FreeBSD14.2 Replace pkg with USTC mirror station] (https://www.bilibili.com/video/BV13ji2YLEkV)

Write the following:

```sh '
stc: {
url: "http://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/latest"
♪ I'm sorry ♪
FreeBSD: {enabled: no}
````

- Open Mirror Station, Nanjing University

Write the following:

```sh '
nju: {
url: "http://mirrors.nju.edu.cn/freebsd-pkg/${ABI}/latest"
♪ I'm sorry ♪
FreeBSD: {enabled: no}
````

- Web-enabled mirror stations

Write the following:

```sh '
163:
url: "http://mirrors.163.com/freebsd-pkg/${ABI}/latest",
♪ I'm sorry ♪
FreeBSD: {enabled: no}
````

#ports Source: Package Manager to compile and install software by source code

# # Download ports

This source is the source of downloads per se. Same as before `portsnap ' .

## Git method

_Other Organiser

```sh '
# pkg install #
````

or

```sh '
#cd/usr/ports/devel/git
# Make install clean
````

I don't...

Then:

```sh '
#get clear-filter=tree:0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git/usr/ports
````

Note**
>
>--depth1 ' will put a greater computing pressure on the server, using as much as possible the parameter `--filter=tree:0 ' .

Method of downloading compressed files

>** Warning**
>
>Use Ports by downloading the Port file. It is a one-time: Ports cannot be updated after. It is recommended that you prioritize the Git method.


```sh '
#fetch https://mirrors.nju.edu.cn/freebsd-ports/ports.tar.gz
````

Or...

```sh '
#fetch https://mirrors.ustc.edu.cn/freebsd-ports/ports.tar.gz
````

And...

```sh '
# tar-zxvf ports.tar.gz-C/usr/ # unpressure to path
# rm ports.tar.gz # delete archive
````

# # ports source

This source is the source of downloading the software in the ports.


> ** Warning**
>
> ports sources may not be complete. The rest is probably less than a tenth. See <https://github.com/ustclug/discussions/issues/408>.

Create or modify files:

```sh '
#ee /etc/make.conf
````

I don't...

- Open Mirror Station, Nanjing University


Write the following:

```sh '
MASTER_SISTE_OVERRIDE? =http://mirrors.nju.edu.cn/freebsd-ports/distriles/${DIST_SUBDIR}/
````

- Web-enabled mirror stations

Write the following:

```sh '
MASTER_SITE_OVERRIDE? =http://mirrors.163.com/freebsd-ports/distriles/${DIST_SUBDIR}/
````

- Open Source Software Mirror Station, China University of Science and Technology


Write the following:

```sh '
MASTER_SISTE_OVERRIDE? =http://mirrors.ustc.edu.cn/freebsd-ports/distriles/${DIST_SUBDIR}/
````

# kernel modules (kmods) kernel module source: FreeBSD 14.2 and higher (excluding 15.0-CURRENT)

New folder `/usr/local/etc/pkg/repos ' (i.e. `mkdir-p/usr/local/etc/pkg/repos ' ) and new document `/usr/local/etc/pkg/repos/FreeBSD-kmods.conf ':


FreeBSD official source

Writing:

# Quitely branch

```sh '
FreeBSD-kmods{
url: pkg+https://pkg.freebsd.org/${ABI}/kmods_quarterly_2
Signature_type: "fingerprint""S"
Fingerprints: "/usr/share/keys/pkg"
"srv"
I can't believe it.
♪ I'm sorry ♪
````

# # latest branch

```sh '
FreeBSD-kmods{
url: pkg+https://pkg.freebsd.org/${ABI}/kmods_latest_2
Signature_ type: "fingerprints"
Fingerprints: "/usr/share/keys/pkg"
"srv"
I can't believe it.
♪ I'm sorry ♪
````

Open Source Software Mirror Station, China University of Science and Technology


Writing:

# Quitely branch

```sh '
FreeBSD-kmods{
url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_quarterly_2
I can't believe it.
♪ I'm sorry ♪
````

# # latest branch

```sh '
FreeBSD-kmods{
url: https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/kmods_latest_2
I can't believe it.
♪ I'm sorry ♪
````


Versions that are not supported by security (please use them as appropriate)

>** Skills**
>
The >Open Source Mirror Station also provides a pkg binary source for expired versions of FreeBSD 11, 12. Useable.

Releases that are not supported by security are also available using binary sources. For example, `FreeBSD 9.2 ' :

First switch to available binary source

```sh '
#setenv PACKAGESITE http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
````

If shell's not csh, then:

```sh '
#export PACKAGESISITE = http://ftp-archive.freebsd.org/pub/FreeBSD-Archive/ports/amd64/packages-9.2-release/Latest
````

Example of installation: `bsdinfo ' is now installed.

```sh '
# pkg_add-r bsdinfo
Fetching http://ftp-archive.freebsd.org/pub/FreeBSD-archive/ports/amd64/packages-9.2-release/Latest/bsdinfo.tbz...Done.
````

Note**
>
>pkg is not available and would suggest that `diggests.txz ' and `repo.txz ' could not be found, as pkgng was not officially supported at that time and only `pkg_* ' commands were still supported.

# References

- [FreeBSD ports] (https://mirrors.ustc.edu.cn/help/freebsd-ports.html), USTC Mirrors
- [FreeBSD pkg] (https://mirrors.ustc.edu.cn/help/freebsd-pkg.html), USTC Mirrors
