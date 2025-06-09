# Section 3.8 Update FreeBSD by source code

The basic idea is to get the source code for FreeBSD and then compile it. You can use git directly to replace the code, or you can download the txz compression file in the ISO mirror, or you can download the zip compression package for the current FreeBSD project on the gethub.

See Handbook for compilation process. Very simple.


>**svn to guit**
>
>FreeBSD Project fully migrated from SVN to Git in 2021, i.e. [https://git.freebsd.org] (https://git.freebsd.org)
>
> The way to access the source code has also changed and no longer uses svn.


# Get source code from Git


# # Install Git

```sh '
# pkg install #
````

Or:

````
#cd /usr/ports/devel/git/ & make install clean
````


# # Git proxy settings


- If `sh ' , `bash ' , `zsh ' :

Settings:

```sh '
#get config --global http.proxy http://192.168.X:7890
#get config-global https.proxy http://192.168.X:7890
````

Cancel:

```sh '
#get config-global-unset http.proxy
#get config-global-unset https.proxy
````

# Git pulls the source code

````
#get clean --depth 1 https://git.FreeBSD.org/src.git/usr/src
````

Or (GitHub is a mirror of src on FreeBSD.org, synchronized every 10 minutes)

````
#get line --depth 1 https://github.com/freebsd/freebsd-src/usr/src
````

References

- [Submitting GitHub Pull Requests to FreeBSD] (https://freebsdfoundation.org/our-work/journal/browser-based-edition/conformation-manage-2/submitting-github-pull-requests-to-freebsd/)


# # troubleshooting and unfinished business


- Git: `fatal: unable to update url base from redaction '

Use FreeBSD source without `.git '

# Gitup

```sh '
# pkg install giveup
````

Or:

````
#cd/usr/ports/net/gitup/ & make install clean
````

````
#gitup release # specific version needs to refer to current gitup configuration https://github.com/johnmehr/gitup/blob/main/gitup.conf
# guitup curent #
````

# # troubleshooting and unfinished business

- Git: `fatal: unable to access 'https://git.FreeBSD.org/src.git/:SSL certificate program: certificate is not yet valid '

It's probably the wrong time.

```sh '
#ntpdate-u cool.ntp.org #
````

# Retrieving source code from compressed packages (favourable but not up to date)

The method is simpler and faster.

FreeBSD 14.2 for example:

```sh '
#fetch https://download.freebsd.org/ftp/releases/amd/64/14.2-RELEASE/src.txz
# tar xvzf src.txz-C #
````

> ** Why unpressure to `/ '? **
>
> Because `/ ' will depress the source code to `/usr/src ' . If the above path is changed to `/usr/src ' , the source code is lifted to `/usr/src/usr/src ' . Because he's a condensed bag with a path.

>** Skills**
>
>If slow, switch to <https://mirrors.ustc.edu.cn/freebsd/releases/amd/64/14.2-RELEASE/src.txz>

# Start compiling

```sh '
# cd /usr/src # cut to work directory
# Make-j4 buildworld #
# make-j4 Kernel
# Reboot # restart to use the new kernel
# cd /usr/ src # cut back the job directory
# etcupdate-p #
# make installationworld #
# etcupdate-B #
Reboot
````

# # troubleshooting and unfinished business

- 'Conflicts remain from previous update, Aborting. '

Conflict resolution**

>** Skills**
>
> Unlike most modern Linux, [FreeBSD] (https://github.com/freebsd/freebsd-src/tree/main/contrib/nvi) (OpenBSD) `vi ' is *[nvi] (https://sites.google.com/a/bostic.com/keith-Bostic?authuser=0)* (rerealization of original **ex/vi**) and does not refer to any link sign to *vim*. Essentially no one can use it, and there is generally no need to study, so it is necessary to replace it with another text editor.
>
> ```sh '
> Export EDITOR=/usr/bin/ee # Switch vi to ee. For version or csh before FreeBSD 14:setenv EDITOR/usr/bin/ee
> export VISUAL=/usr/bin/ee # Switch vi to ee. Used for pre-FreeBSD 14 versions or csh: Setenv VISUAL/usr/bin/ee
> ````

```sh '
# etcupdate-B
Problems remain from previous update, abomining.

````

````
♪ conflict resolution ♪
Resolving compliance in '/etc/group':
Select: (p) postpone, (df) diff-full, (e) edit,
(h) Help for more options: e #e
♪ etcupdate-B
````

# ZFS related upgrades can be found in ZFS section

# References

- [FreeBSD Handbook] (https://handbook.bsdcn.org/).
- [etcupdate -- manage updates to system files not updated by installworld]
