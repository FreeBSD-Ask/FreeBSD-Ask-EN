Section 9.2 Jail Update

If you want to manage more than one jail at the same time, you have to run each jail on its own once and for all. By creating a single template, all jail can share a basic environment, with their own writing space, without interference.

This paper will create the following directory structure:

- `/jail/moot ' is a template, a common read-only part of all jail, which will be mounted on `/jail/www ' in this case.
- `/jail/skel ' is the framework that facilitates the creation of jail and is not in itself used for any jail.
- `/jail/www ' is the root directory run by jail `www ' and the mounted point of the read-only template, which is itself an empty directory.
- `/jail/www/s ' is the mount point for the written part of jail `www ' and is an empty directory.
- `/jail/files/www ' is the physical location of the scribble part of jail `www ' and will be mounted on `/jail/www/s ' .

If more than one Jail is to be created, then recreate the data directory and the project directory so that all Jail will share `/jail/moot ' .

Need to install 'cpdup '

- Install with pkg

```sh '
# Pkg install cpdup
````

- Install with Ports:

````
#cd/usr/ports/sysutils/cpdup/
# Make install clean
````

# Create Template Directory

```sh '
#mkdir-p/jail/moot
# Then put it in the basic directory
# Put ports and source code in the template
#get clear-filter=tree: 0 https://mirrors.ustc.edu.cn/freebsd-ports/ports.git/jail/moot/usr/ports
#cpdup /usr/src /jail/moot/usr/src # needs to get the source code in advance and be careful that the version corresponding to the source code is the same as the version of /jail/moot
````

Connect the writeable part to the writeable directory position

```sh '
# cd /jail/moot # cd to template directory
# mkdir s # create a directory to link
# In-s s/etc etc
In-ss/home home
In-s/ root root
# In-s ../s/usr-local usr/local
# In-s .. ../s/usr-X11R6 Usr/X11R6
# In-s ../ .././s/distriles usr/ports/distriles
In-s s/tmp tmp
In-s s/var var
````

# Create Frame Directory

```sh '
# mkdir-p/jail/skel
#mkdir/jail/skel /jail/skel/home/jail/skel/usr-X11R6/jail/skel/distriles/jail/skel/portbuild
# Move to write
#mv/jail/moot/etc/jail/skel
#mv/jail/moot/usr/local/jail/skel/usr-local
#mv/jail/moot/tmp/jail/skel
#mv/jail/moot/var/jail/skel
#mv/jail/moot/root/jail/skel
````

Installs the missing profile using etcupdate.

```sh '
#etcupdate - /jail/moot/usr/src-d/jail/skel/var/db/etcupdate -D/jail/skel
````

Create a common profile for `make '

```sh '
#echo “WRKDIRPREFIX? =/s/portbuild” > /jail/skel/etc/make.conf
````

# Create Data Directory

It's a copy of a frame.

```sh '
#cpdup/jail/skel/jail/files/www
````

# Create Project Directory

```sh '
#mkdir/jail/www/jail/www/s
````

# Create fstab

```sh '
#ee /jail/www.fstab
# Mount a public read-only system to the project directory
/jail/moot /jail/wwwnullfsro0
# Mount project data directories to project directories
/jail/files/www/jail/www/snullfsrw00
````

# Write jail.conf

```sh '
# Global

"/bin/sh/etc/rc";
Exec.stop = "/bin/sh/etc/rc.shutdown";
I'm sorry, exec.clean;
(a) Mount.devfs;
= 1;
= 1;
Interface = "Webcard address"

# Hostname can also be replaced by variables
hostname = "$name.domain.local";

# Jail position, also variable
Path = "/jail/$name";

#ip address
ip4.addr = 192,168.1.$ip;

# fstab position
Mount.fstab = /jail/$name.fstab;

www {
$ip=2
# If you don't use fstab, use
#mount.fstab ="; # replace global
♪ I'm sorry ♪
````

