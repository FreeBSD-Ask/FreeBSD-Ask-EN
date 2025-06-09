Section 5.4 Five Input Method

IBus

Need to install configuration IBus, a little。


# # Install Rime input method


```sh
# pkg install zh-ibus-rime
```

Or:

```sh
# cd /usr/ports/chinese/ibus-rime/ 
# make install clean
```

THEN RUN THE INITIALISATION COMMAND __CODESPAN_0_ WITH __CODESPAN_1_INPUT METHOD:

![.. ..gitbook/assets/wubi3.png]

# # Configure Rime Input Method

A further 98 five-coded tables (__CODESPAN_0, __CODESPAN_1_) are copied under __CODESPAN_2_. Download address: [FreeBSD-98wubi-tales] (https://github.com/FreeBSD-Ask/98-input/)

MODIFY __CODESPAN_1_FILE UNDER __CODESPAN_1_: OPEN __CODESPAN_2_ TO FIND __CODESPAN_3_, AND ADD __CODESPAN_4_ (BEWARE TO INDENT) IN THE FIRST LINE BELOW, AND DELETE OTHER SCHEMES, AS FOLLOWS:

```sh
# Rime default settings
# encoding: utf-8

config_version: '0.40'

schema_list:
- schema: wubi98

...the rest is omitted..
````

Save exit redeployment Rime input method is sufficient。

![.. ..gitbook/assets/wubi4.png]

![..gitbook/assets/wubi5.png]

# Fcitx 5


# # Install Fcitx 5

```sh
# pkg install fcitx5 fcitx5-qt5 fcitx5-qt6 fcitx5-gtk2 fcitx5-gtk3 fcitx5-gtk4 fcitx5-configtool-qt5 fcitx5-configtool-qt6 zh-fcitx5-chinese-addons 
```

Fcitx 5 configurations are omitted。

# # Fcitx 5 Configure 98 5

First download the required documentation: <https://github.com/FreeBSD-Ask/98-input>。

- COPYING THE __CODESPAN_0_ FILE BELOW __CODESPAN_1_
- COPYING THE __CODESPAN_0 AND __CODESPAN_1_ ICONS TO __CODESPAN_2
- PUT THE __CODESPAN_0_SAURUS BELOW __CODESPAN_1_。
- RESTART __CODESPAN_0, WITH 98 INITIALS。

![.. ..gitbook/assets/wubi1.png]

![..gitbook/assets/wubi2.png]

---|---

APPENDIX: KING 98 FIVE METHODS TO GENERATE __CODESPAN_0_ LIBRARY, WITH THE FOLLOWING COMMANDS:

```sh
$ libime_tabledict 98wbx.txt 98wbx.main.dict
```

# Configure Rime with 86

First install and configure Fcitx 5. Configure from a cursor。

```sh
# pkg ins zh-fcitx5-rime zh-rime-essay zh-rime-wubi 
```

Or:

```sh
# cd /usr/ports/chinese/rime-wubi/
# cd /usr/ports/chinese/fcitx5-rime/ && make install clean
# cd /usr/ports/chinese/rime-essay/ && make install clean
```

The method for adding Rime is described above (the Rime input method is __CODESPAN_0_), which is omitted。

AMEND _`/usr/local/share/rime-data/default.yaml` TO READ AS FOLLOWS:

```
# Rime default settings
# encoding: utf-8

config_version: '0.40'

schema_list:
- yeah

...other omissions ..
````

# Profile

five input methods have been installed, and the profile of the rime is located as follows:

- Ibus

```sh
$ cd ~/.config/ibus/rime
```

- Fcitx5

```sh
$ cd ~/.local/share/fcitx5/rime
```

# # Modify the candidacy to 9 lines

__CODESPAN_0_ MUST GO TO THE ABOVE PROFILE DIRECTORY BEFORE THE FOLLOWING OPERATIONS ARE PERFORMED。

Method 1

```sh
$ rime_patch default menu
page_size: 9 # 输入后回车
^D # 按 ctrl+D
patch applied.
```

Of which:

-_CODESPAN_0_TO_CODESPAN_1_FILE
- __CODESPAN_0_ CORRESPONDING LEVEL I OPTION, __CODESPAN_1_ CORRESPONDING LEVEL II OPTION

Restart it。

Method 2

```sh
$ rime_patch default menu/page_size
9 # 输入后回车
^D # 按 ctrl+D
patch applied.
```

Restart it。

It is recommended that form II be used to set it up, which requires some knowledge of the configuration file format in a more complex setting。

# # Default English output

```sh
$ rime_patch wubi86 'switches/@1/reset'
1
^D
patch applied.
```

This applies the Patch to wubi86 input method (writing __CODESPAN_0_), most of the options are related to the input method, and only a few are global (writing __CODESPAN_1_)

Restart it。

# IBus

EDIT __CODESPAN_0, REPLACE __CODESPAN_1_ WITH __CODESPAN_2_REDEPLOYMENT OR RESTART。

![.. ..gitbook/assets/wubi6.png]

# It's broken

- This has moved to a common file, which normally changes only to the user configuration, which would affect the overall situation and would be easily restored if updated。

Pending。

# References

- [how to set the input box line display]
- [LOYOON-Tsaw/Rime_collections/] (https://github.com/LOYOon-Tsaw/Rime_collections/blob/master/Rime_description.md)
- [i'm sorry]
