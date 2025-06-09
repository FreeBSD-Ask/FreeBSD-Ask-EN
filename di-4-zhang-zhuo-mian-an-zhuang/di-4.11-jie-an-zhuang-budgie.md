# Section 4.11 Budgie

Budgie is the default desktop for Solus Linux。

# Install

- install with pkg:

```sh
# pkg install budgie wqy-fonts
```

- Or install with Ports:

```sh
# cd /usr/ports/x11/budgie && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
```

>** Skills**
>
> will automatically install lightdm。

- Explain:

| Package Name | Description of role |
|:------------------|:--------------------------|
| `budgie ' | Desktop Environment |
| `wqy-fonts ' | Chinese fonts |

# View installation hints

```sh
root@ykla:/home/ykla # pkg info -D budgie
budgie-10.8:
On install:
Copy 'xprofile' into your home directory:
  cp /usr/local/share/examples/budgie/xprofile ~/.xprofile
# 将示例配置文件 xprofile 复制到你的主目录，用于设置桌面环境启动时的用户环境变量。

More Information, https://codeberg.org/olivierd/freebsd-ports-budgie/wiki
# More information can be found on the official wiki page。

If you want to launch new session from a console
cp /usr/local/share/examples/budgie/xinitrc~/.xinitrc
# if you want to start a session directly from the console (without login manager), copy the example xinitrc to the main directory。
````

# CONFIGURE __CODESPAN_0_

```sh
$ cp /usr/local/share/examples/budgie/xprofile ~/.xprofile
$ cp /usr/local/share/examples/budgie/xinitrc ~/.xinitrc
```

# CONFIGURE __CODESPAN_0_

EDIT __CODESPAN_0_, ADD:

```sh
proc           /proc       procfs  rw  0   0
```

# Service management

```sh
# service dbus enable
# service lightdm enable
```

# Chinese Environment

ADD UNDER __CODESPAN_0_:

```sh
lightdm_env="LC_MESSAGES=zh_CN.UTF-8" 
```

---|---

EDIT __CODESPAN_0: FIND __CODESPAN_1_, AND MODIFY __CODESPAN_2_ TO __ ___ CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```

# Desktop appreciation

../.gitbook/assets/budgie1.png

../.gitbook/assets/budgie2.png

The wallpaper is the default. Photo taken from the Gulf of Singapore。

../.gitbook/assets/budgie3.png

# References

- [Establishment] (https://codeberg.org/olivierd/freebsd-ports-budgie/wiki/Installation) This paper is mainly supplemented by this but is tested without the need to configure __CODESPAN_0。
