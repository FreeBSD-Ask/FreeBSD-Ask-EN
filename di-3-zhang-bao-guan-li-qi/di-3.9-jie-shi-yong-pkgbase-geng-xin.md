# Section 3.9 Update FreeBSD with pkgbase

Now FreeBSD system upgrades are separated from third-party software upgrades (now using __CODESPAN_0), and pkgbase is intended to combine them in a uniform use of __CODESPAN_1 for command management (learning Linux?). Because it's only RELEASE, which has a first-level structure, that can be used. As early as 2016, pkgbase was scheduled to be replaced by CODESPAN_3 by FreeBSD14, but has now been postponed to 15. The other person felt that the experience was very poor and very slow。

**pkgbase was originally designed to allow for the use of a binary tool for updating, for example, by stable, current and releasing. Now, stable, current can only be updated by fully compiling the source code. **

>** Warning**
>
There is a risk that all data may be lost! It is recommended that backup be done before the operation. **

# DOWNLOAD __CODESPAN_0_ SCRIPT

Download from [Github repositiry] (https://github.com/FreeBSDfoundation/pkgbasify) __CODESPAN_0_script。

# (optional) Configure software sources

FreeBSD official source pkgbase:

| ** Branch** | ** Frequency of update** | **URL ADDRESS** |
| :---: | :---: | :--- |
| main (15.0-CURRENT) | Twice a day: 08:00, 20:00 | <https://pkg.freebsd.org/${ABI}/base_latest> |
| main (15.0-CURRENT) | Weekly: Sunday 20:00 | <https://pkg.freebsd.org/${ABI}/base_weekly> |
| stable/14 | Twice a day: 08:00, 20:00 | <https://pkg.freebsd.org/${ABI}/base_latest> |
| stable/14 | Weekly: Sunday 20:00 | <https://pkg.freebsd.org/${ABI}/base_weekly> |
| releng/14.0 (RELEASE) | Twice a day: 08:00, 20:00 | <https://pkg.freebsd.org/${ABI}/base_release_0> |
| releng/14.1 (RELEASE) | Twice a day: 08:00, 20:00 | <https://pkg.freebsd.org/${ABI}/base_release_1> |
| releng/14.2 (RELEASE) | Twice a day: 08:00, 20:00 | <https://pkg.freebsd.org/${ABI}/base_release_2> |

** The time of the above table has been converted to Beijing time, Eastern Region Time. The FreeBSD official mirror station time. **

If the official source downloads at a slow pace, it may be considered for domestic mirroring。

Modify the __CODESPAN_0_ function in the Lua script:

```lua
function create_base_repo_conf(path)
	assert(os.execute("mkdir -p " .. path:match(".*/")))
	local f <close> = assert(io.open(path, "w"))
	assert(f:write(string.format([[
FreeBSD-base: {
  url: "%s",
  mirror_type: "srv",
  signature_type: "fingerprints",
  fingerprints: "/usr/share/keys/pkg",
  enabled: yes
}
]], base_repo_url())))
end
```

Replace the source information with any of the following mirror stations, such as:

```lua
function create_base_repo_conf(path)
	assert(os.execute("mkdir -p " .. path:match(".*/")))
	local f <close> = assert(io.open(path, "w"))
	assert(f:write([[
FreeBSD-base: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_latest",
  enabled: yes
}
]]))
end
```


NANJING UNIVERSITY OPEN MIRROR STATION NJU

```sh
FreeBSD-base: {
  url: "https://mirrors.nju.edu.cn/freebsd-pkg/${ABI}/base_latest",
  enabled: yes
}
```

OPEN SOURCE MIRROR STATION, CHINA UNIVERSITY OF SCIENCE AND TECHNOLOGY

```sh
FreeBSD-base: {
  url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_latest",
  enabled: yes
}
```

# # Web-enabled mirror site 163

```sh
FreeBSD-base: {
  url: "https://mirrors.163.com/freebsd-pkg/${ABI}/base_latest",
  enabled: yes
}
```

# RUN __CODESPAN_0_

```sh
chmod +x pkgbasify.lua
./pkgbasify.lua
```

Note**
>
> I'm testing a pure system with no redundant configurations and third-party programs (except pkg) and only SSH services。


>** Warning**
>
There is a risk that all data may be lost! **

# References

- [wiki/PkgBase] (https://wiki.freebsd.org/PkgBase)

