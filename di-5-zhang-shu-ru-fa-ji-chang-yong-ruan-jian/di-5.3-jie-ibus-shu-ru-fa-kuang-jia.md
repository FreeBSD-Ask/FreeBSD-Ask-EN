# Section 5.3 IBus Input Method Framework

IBus is "Inteligent Input Bus" (intelligent input bus)。

IBus

- install with pkg:

```sh
# pkg install ibus zh-ibus-pinyin
```

- Or install with Ports:

```
# cd /usr/ports/textproc/ibus/ && make install clean
# cd /usr/ports/chinese/ibus-libpinyin/ && make install clean
```

OF WHICH __CODESPAN_0_IS SPELL INPUT METHOD

There are other options

- __CODESPAN_0_SILOTON INPUT METHOD
- __CODESPAN_0_COOL
- __CODESPAN_0_rime input engine (otherwise)
- `chinese/ibus-table-chinese` CONTAINS FIVE DIFFERENT INPUT METHODS, INCLUDING SILOS, ETC

# Configure Environment Variables

Sddm lightdm gdm can write A group configuration in __CODESPAN_0_
2. Lightdm gdm can write A group configuration in __CODESPAN_0_
3. sddm can write configurations in user login shell profiles

---|---

-sh: __CODESPAN_0_ Write A group configuration
-bash: __CODESPAN_0 or __CODESPAN_1_for group A configuration
-zsh: __CODESPAN_0_ Write A group configuration
-csh: __CODESPAN_0_ Write B Group Configuration

Login after write-off, and then click on the ibus icon to add your own input method, then you can use it without any configuration, including Sdm/xfce/freebsd132/sh. However, the IBus tip should be added to the corresponding shell file:

- Group A (in sh, bash, zsh):

```sh
export XIM=ibus
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
export XIM_PROGRAM="ibus-daemon"
export XIM_ARGS="--daemonize --xim"
```

- Group B (in csh):

```sh
setenv XIM ibus
setenv GTK_IM_MODULE ibus
setenv QT_IM_MODULE ibus
setenv XMODIFIERS @im=ibus
setenv XIM_PROGRAM ibus-daemon
setenv XIM_ARGS "--daemonize --xim"
```

# IBus Settings

```sh
$ ibus-setup
```

---|---

IBus has a requirement for coding (which requires __CODESPAN_0), but no requirement for the area (e.g. __CODESPAN_1 or __CODESPAN_2/__)。

[i'm sorry] (. .gitbook/assets/bus-fr-ch-ok.png)

