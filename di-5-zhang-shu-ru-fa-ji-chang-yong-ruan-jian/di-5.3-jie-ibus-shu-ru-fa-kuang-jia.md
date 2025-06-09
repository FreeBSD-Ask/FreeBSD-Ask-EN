# Section 5.3 IBus Input Method Framework

IBus is "Inteligent Input Bus" (intelligent input bus).

IBus

- Install with pkg:

```sh '
# Pkg install ibus zh-ibus-pinyin
````

- Or install with Ports:

````
#cd /usr/ports/textproc/ibus/ & make install clean
# cd /usr/ports/chinese/bus-libpini/ & make install clean
````

of which `zh-ibus-pinyin ' is the spelling method

There are other options.

- `chinese/bus-cangjie ' warehouse input method
- `chinese/bus-chewing '
- `chinese/bus-rime ' rime input engine (otherwise)
- `chinese/bus-table-chinese ' contains five input methods, including silos

# Configure Environment Variables

1. Sddm lightdm gdm can all write A group configuration in '~/.xfile '
2. Lightdm gdm can write A group configuration in ~/.profile '
3. Sddm can write configurations in user login shell profiles

I don't...

-sh: ~/.profile 'writing group A configuration
-bash: ~/.bash_profile ` or ~/.profile ' for group A configuration
-zsh: ~/.zprofile 'writing group A configuration
-csh: ~/.cshrc 'for group B configuration

Login after write-off, and then click on the ibus icon to add your own input method, then you can use it without any configuration, including Sdm/xfce/freebsd132/sh. However, the IBus tip should be added to the corresponding shell file:

- Group A (in sh, bash, zsh):

```sh '
I'm sorry.
I'm sorry.
QT_IM_MODULE=ibus
@im=ibus
I'm sorry.
"-daemonyze-xim"
````

- Group B (in csh):

```sh '
I don't know what you're talking about.
I'm sorry, I'm sorry.
QT_IM_MODULE ibus
@im=ibus
This post is part of our special coverage Syria Protests 2011.
"-daemonyze-xim"
````

# IBus Settings

```sh '
This post is part of our special coverage Egypt 2011.
````

I don't...

IBus has a requirement for coding (which requires `UTF-8 ' ), but no requirement for the area (e.g. `C.UTF-8 ' or `zh_CN.UTF-8 ' ).

[ibus](./.gitbook/assets/ibus-fr-ch-ok.png)

