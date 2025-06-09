Section 9.1 Jail Configuration

# Create jail directory

# Into FreeBSD basic system #

Programme I

```sh '
# cd /usr/src
# make builtworld
# make installworld DESTDIR=/usr/jail/ # install to jail
# Make distribution #
````

Programme II

Download `base.txz 'or extract 'baes.txz ' from iso and depressurize to jail

```sh '
#tar-xvf base.txz-C/usr/jail
````

Mounts the devfs filesystem. (not necessarily)

```sh '
# Mount-t Devfs /usr/jail/dev
````

# # Write '/etc/rc.conf '

```sh '
# Sysrc jail_enable #
````

Create `jail.conf ' files (can write `rc.conf ' but this is easy to manage)

```sh '
www {
host. hostname =www.example.org;#hostname
ip4.addr = 192.168.0.10; #IP address
path = "/usr/jail"; #jail position
== sync, corrected by elderman ==
Mount.devfs; # Mount Devfs file system to jail
Exec.start = "/ bin/sh/etc/rc"; # Start command
exec.stop = "/bin/sh/etc/rc.shutdown"; #Close command
♪ I'm sorry ♪
````

# Management

View online Jail information list with `jls '

```sh '
JID IP Address Hostname Path
3192.168.0.10 www/usr/jail/www
````

Central-British Contrast

English
|: -: |: | | |
JID Jail ID
IP Address IP Address
Hostname hostname
Path to Path Jail

# Start and stop jail

```sh '
# Service jail start www
# Service jail stop www
````

# Login jail

```sh '
# jexec 1 tcsh
````

# Clean off jail

```sh '
# jexec 3 / etc/rc.shutdown
````

# Upgrade jail

```sh '
#freebsd-update-b/here/is/the/jail fix
#freebsd-update-b/here/is/the/jail
````

# ping with the network

# Turn on ping #

Writing `/etc/jail.conf '

```sh '
Allow.raw_sockets=1;
Allow.sysvipc=1;
````

Configure complete please restart jail.

- Example:

```sh '
# Jail-rc test
````

Network

Create `/etc/resolv.conf ' and edit.

```sh '
I'm sorry.
Nameserver 223.5.5.5
Nameserver 223.6.6.6.6 #do not write a router address
````

# Fragmentation and unfinished business

- Delete files without permission

```sh '
♪ Cheflags-R noschg directory
````

- `Certificate verification failed for /C=US/O=Let's Encrypt/CN=E6
0020C1CD593C000:error:16000069: STORE routines:ossl_store_get0_loader_int:unregistered'

Checked and timed. Generally occurring in FreeBSD 14.1, 14.2 RELEASE.

Solutions:

```sh '
# Certctl rehash
````

Re-execut `pkg ' is sufficient.

Reason unknown, see

- [Bug 280031 - Cannot install `pkg`due to 404 on pkg.freebsd.org] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=280031)
- [Cannot fitch (and install) `pkg '] (https://forums.freebsd.org/threads/cannot-fetch-and-install-pkg93976/)
