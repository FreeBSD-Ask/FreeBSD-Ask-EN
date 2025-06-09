# Section 3.9 Update FreeBSD with pkgbase

Now FreeBSD system upgrades are separated from third-party software upgrades (now using `freebsd-update ' ), and pkgbase is intended to combine them in a uniform use of `pkg ' commands (learning Linux?). Because only RELEASE, which is a first-level structure, is `freebsd-update ' available. As early as 2016, pkgbase was scheduled to go to FreeBSD 14 to replace `freebsd-update ' , but has now been postponed to 15. Another individual feels that `freebsd-update ' experience is very poor and very slow (net is irrelevant).

**pkgbase was originally designed to allow for the use of a binary tool for updating, for example, by stable, current and releasing. Now, stable, current can only be updated by fully compiling the source code. **

>** Warning**
>
There is a risk that all data may be lost! It is recommended that backup be done before the operation. **

# Download `pkgbasify ' script

Download `pkgbasify.lua ' script at [Github repository] (https://github.com/FreeBSDFD/pkgbasify).

# (optional) Configure software sources

FreeBSD official source pkgbase:

** Branch**
|: --: |: --: |: |
| (15.0-CURRENT) | Two times a day: 08:00, 20:00  < <https://pkg.freebsd.org/${ABI}/base_latest>
| (15.0-CURRENT) | Weekly: 20:00  <
Two times a day: 08:00, 20:00 <https://pkg.freebsd.org/${ABI}/base_latest>
Once a week: Sunday 20:00 <https://pkg.freebsd.org/${ABI}/base_weekly>
|relang/14.0 (RELEASE) | Two times a day: 08:00, 20:00  < <https://pkg.freebsd.org/${ABI}/base_release_0>
| Releng/14.1 (RELEASE) | Two times a day: 08:00, 20:00 < https://pkg.freebsd.org/${ABI}/base_release_1>
|Releng/14.2 (RELEASE)| Two times a day: 08:00, 20:00 < https://pkg.freebsd.org/${ABI}/base_release_2>

** The time of the above table has been converted to Beijing time, Eastern Region Time. The FreeBSD official mirror station time. **

If the official source downloads at a slow pace, it may be considered for domestic mirroring.

Modify the `create_base_repo_conf ' function in Lua script:

```lua
Fun action Create_base_repo_conf(path)
Assert (os.execute)
Local f < close> = assert (io.open (path, "w"))
Asert(f:write(string.format)[[[ ]
FreeBSD-base:
url: "%s",
"srv",
Signature_type: "fingerprints",
"/usr/share/keys/pkg",
I can't believe it.
♪ I'm sorry ♪
, base_repo_url()))
End
````

Replace the source information with any of the following mirror stations, such as:

```lua
Fun action Create_base_repo_conf(path)
Assert (os.execute)
Local f < close> = assert (io.open (path, "w"))
Asert(f):write([[[ ]]
FreeBSD-base:
url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_latest"
I can't believe it.
♪ I'm sorry ♪
)
End
````


Nanjing University Open Mirror Station NJU

```sh '
FreeBSD-base:
url: "https://mirrors.nju.edu.cn/freebsd-pkg/${ABI}/base_latest"
I can't believe it.
♪ I'm sorry ♪
````

Open Source Mirror Station, China University of Science and Technology

```sh '
FreeBSD-base:
url: "https://mirrors.ustc.edu.cn/freebsd-pkg/${ABI}/base_latest"
I can't believe it.
♪ I'm sorry ♪
````

# # Web-enabled mirror site 163

```sh '
FreeBSD-base:
url: "https://mirrors.163.com/freebsd-pkg/${ABI}/base_latest"
I can't believe it.
♪ I'm sorry ♪
````

# Run 'pkgbasify.lua '

```sh '
chmod+xpkgbasify.lua
/pkgbasify.lua
````

Note**
>
> I'm testing a pure system with no redundant configurations and third-party programs (except pkg) and only SSH services.


>** Warning**
>
There is a risk that all data may be lost! **

# References

- [wiki/PkgBase] (https://wiki.freebsd.org/PkgBase)

