Section 3.6 Installing software via DVD

# Mount DVD to `/dist ' directory

- Directly mount local ISO:

```sh '
# mdconfig / home/ykla/FreeBSD-14.2-RELEASE-amd64-dvd1.iso #
md0
# mkdir-p/dist
# Mount-t cd9660 /dev/md0 /dist # cannot directly mount ISO, wrongly report
````

- Direct use of DVD devices (e.g. ISO mirrors mounted directly through virtual machines):

Watch ISO mount:

```sh '
# Gpart show

...leave the useless disk...

=>9 2356635 cd0 MBR (4.5G)
9 2356635 - free - (4.5G)
````

A `cd0 ' can be seen, and the size matches.

```sh '
# mkdir -p /dist # create mount point
# Mount-t cd9660/dev/cd0/dist # Mount ISO
#ls /list/ # check for mount
..cshrc bin lib net root var
I'm not sure if you're gonna be able to do that.
.rr_moved dev media proc tmp
I don't know what you're talking about.
````

# # troubleshooting and unfinished business

**/dist** If the directory is changed to another, the environment variable method is not valid because `packages/repos/FreeBSD_install_cdrom.conf ' cannot be modified.

# Install DVD software using 'bsdconfig ' (currently invalid)

Let's start with the way above.

```sh '
# bsdconfig
````

`3 Packages ' —> `1 CD/DVD Install from a FreeBSD CD/DVD '

`No pkg (8) data found! '

# Install DVD software directly using environment variables

Test installation:

```sh '
# env REROS_DIR=/dist/packages/poss pkg install xorg
Updating FreeBSD_install_cdrom repository catalogue...
FreeBSSD_cdrom repositiry is up to date.
All returns are up to date.
Checking integration... done.
The following 1 package will be affected:

New packs to be INSTRAW:
Xorg: 7.7_3

Number of packs to be involved: 1

[y/N]:
````

To list available software in DVD:

```sh '
# env EREPOS_DIR=/dist/packages/poss pkg rquery "%n"
````

# Switch source to DVD

Create DVD source

```sh '
#cp /list/packages/repos/FreeBSD_install_cdrom.conf/etc/pkg/
````

# # Test installation

```sh '
# pkg install xorg
Updating FreeBSD_install_cdrom repository catalogue...
FreeBSSD_cdrom repositiry is up to date.
All returns are up to date.
Checking integration... done.
The following 1 package will be affected:

New packs to be INSTRAW:
Xorg: 7.7_3

Number of packs to be involved: 1

[y/N]:
````

# References

- [Product Details] (https://www.freebsdmal.com/cgi-bin/fm/bsdvd10.1)
- [HOWTO: Install binary package without internet accesss] (https://forums.freebsd.org/threads/howtoinstall-binary-package-without-internet-acces.60723/)
