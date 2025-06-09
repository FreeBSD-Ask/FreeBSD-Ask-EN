# Use of Section 3.3 gitup

>** Skills**
>
>FreeBSD 14.0 has been deleted from the portsnap and replaced with guit, as described here.

`gitup ' , i.e. updating the guit.

# Install gitup

- Install with pkg:

```sh '
# pkg install giveup
````

- Or install with Ports:

```sh '
#cd/usr/ports/net/gitup/
# Make install clean
````

# Use gitup

```sh '
♪ Giveup ports ♪
# giveup release #
````

# Inner Git mirror station

```sh '
#cp/usr/local/etc/gitup.conf.sample/usr/local/etc/gitup.conf
````

Edit, `/usr/local/etc/gitup.conf ' , with the following amendments (with 123 to be revised in three cases):

```ini '
# FreeBSD
# I don't know
# Delibert conversion options for gitup.conf.
_Other Organiser
"defaults":
"host": "mirrors.ustc.edu.cn", #1 changed to this.
"port": 443,
# "proxy_host": ""
# "proxy_port": 0,
# "proxy_username": ""
# "proxy_password": ""
# "source_address": ""
"low_memory": false,
"display_depth": 0,
"verbosity": 1,
"work_directory": "/var/db/gitup",
♪ I don't know ♪

"ports":
"repository_path": "/freebsd-ports/ports.git", #2 changed to this
"branch": "main",
"target_directory": "/usr/ports",
"ignores":[,]
♪ I don't know ♪

"quarterly":
"repository_path": "/freebsd-ports/ports.git", #3 changed to this
"branch": "quarterly",
"target_directory": "/usr/ports",
"ignores":[,]
♪ I don't know ♪

"release": {
"Repository_path": "/src.git,"
"branch": "releng/13.2,
"target_directory": "/usr/src",
"ignores":
"sys/[^]+/conf",
I don't know.
♪ I don't know ♪

"stable":
"Repository_path": "/src.git,"
"branch": "stable/13",
"target_directory": "/usr/src",
"ignores":
"sys/[^]+/conf",
I don't know.
♪ I don't know ♪

"current":
"Repository_path": "/src.git,"
"branch": "main",
"target_directory": "/usr/src",
"ignores":
"sys/[^]+/conf",
I don't know.
♪ I'm sorry ♪
♪ I'm sorry ♪
````

Ports:

```sh '
# Giveup ports
````

# Fragmentation and unfinished business

- Too slow (if no mirror station): Set HTTP proxy

The `gitup ' agent is not dependent on the system agent, but is determined separately by its configuration document `/usr/local/etc/gitup.conf ' .

Example:

```sh '
"proxy_host": "192.168.27.1",
"proxy_port": 7890,
````

- Detailed debugging output:

```sh '
# giveup-v2 ports
````

- ♪ There are too many files to return-please re-cline the returntory: Argument list too long ♪

```sh '
# rm-rf/usr/ports
# Giveup ports
````

Empty the directory is sufficient to remove the hint `rm: /usr/ports/:Device busy ' .

# Reference Link

- [gitup -- A multiimalist, dependency-free programme to clean/pull Git repos-itories.] (https://www.freebsd.org/cgi/man.cgi?query=gitup&sektion=1&manpath=freebsd-release-ports),man
- [net/gitup] (https://www.freshports.org/net/gitup)
- [johnmehr/gitup] (https://github.com/johnmehr/gitup), developer's network
