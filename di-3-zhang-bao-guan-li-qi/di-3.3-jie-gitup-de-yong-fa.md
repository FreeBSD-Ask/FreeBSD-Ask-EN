# use of section 3.3 gitup

>** Skills**
>
>FreeBSD 14.0 has been deleted from the portsnap and replaced with guit, as described here。

`gitup`, which is to update the guit。

# install gitup

- install with pkg:

```sh
# pkg install gitup 
```

- Or install with Ports:

```sh
# cd /usr/ports/net/gitup/
# make install clean
```

# use gitup

```sh
# gitup ports 	# 获取 latest 的 ports
# gitup release # 获取 release 版本的源代码
```

# Inner Git mirror station

```sh
# cp /usr/local/etc/gitup.conf.sample /usr/local/etc/gitup.conf
```

EDIT, ___ CODESPAN_0_, WITH THE FOLLOWING MODIFICATIONS (WITH A TOTAL OF 123 TO BE MODIFIED):

```ini
# $FreeBSD$
#
# Default configuration options for gitup.conf.
{
	"defaults" : {
		"host"           : "mirrors.ustc.edu.cn",  #①改动成这样
		"port"           : 443,
#		"proxy_host"     : "",
#		"proxy_port"     : 0,
#		"proxy_username" : "",
#		"proxy_password" : "",
#		"source_address" : "",
		"low_memory"     : false,
		"display_depth"  : 0,
		"verbosity"      : 1,
		"work_directory" : "/var/db/gitup",
	},

	"ports" : {
		"repository_path"  : "/freebsd-ports/ports.git",  #②改动成这样
		"branch"           : "main",
		"target_directory" : "/usr/ports",
		"ignores"          : [],
	},

	"quarterly" : {
		"repository_path"  : "/freebsd-ports/ports.git",  #③改动成这样
		"branch"           : "quarterly",
		"target_directory" : "/usr/ports",
		"ignores"          : [],
	},

	"release" : {
		"repository_path"  : "/src.git",
		"branch"           : "releng/13.2",
		"target_directory" : "/usr/src",
		"ignores"          : [
			"sys/[^\/]+/conf",
		],
	},

	"stable" : {
		"repository_path"  : "/src.git",
		"branch"           : "stable/13",
		"target_directory" : "/usr/src",
		"ignores"          : [
			"sys/[^\/]+/conf",
		],
	},

"current":
"repository_path": "/src.git,",
"branch": "main",
"target_directory": "/usr/src",
"ignores":
"sys/[^]+/conf",
I don't know,
♪ I'm sorry ♪
♪ I'm sorry ♪
````

ports:

```sh
# gitup ports
```

# Fragmentation and unfinished business

- TOO SLOW (IF NO MIRROR STATION): SET HTTP PROXY

THE AGENT OF ___CODESPAN_0_ DEPENDS NOT ON THE SYSTEM AGENT, BUT ON ITS CONFIGURATION DOCUMENT __CODESPAN_1_。

EXAMPLE (DELETE __CODESPAN_0_ FIRST AND REPLACE:

```sh
"proxy_host" : "192.168.27.1",
"proxy_port" : 7890,
```

- Detailed debugging output:

```sh
# gitup -v2 ports
```

- {\cHFFFFFF}{\cH00FFFF}

```sh
# rm -rf /usr/ports
# gitup ports
```

EMPTY THE DIRECTORY AND RE-RAISE IT, AND YOU CAN IGNORE THIS HINT。

# Reference Link

- [well, I'd like to ask you a question, Mr. Git.]
- [this post is part of our special coverage global voices 2011]
- [photo by johnmehr/gitup] (https://github.com/johnmehr/gitup)
