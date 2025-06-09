Section 4.5 Xfce

Xfce aims to develop a lightweight but fully functional desktop. Xfce's Logo is only [Rats] (https://docs.xfce.org/faq#what_does_it_mean), and there was feedback from bug who claimed that Xfce's screen wallpaper caused his computer screen to be scratched by a cat because it was a mouse ([joke\] The default desktop startup screen domain to monitor!] (https://bugzilla.xfce.org/show_bug.cgi?id=12117)。

# install xfce4

- install by pkg

```sh
# pkg install xorg lightdm lightdm-gtk-greeter xfce wqy-fonts xdg-user-dirs xfce4-goodies lightdm-gtk-greeter-settings
```

- or install through ports

```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11-wm/xfce4 && make install clean # 注意有个 4
# cd /usr/ports/x11/xfce4-goodies/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/lightdm/ && make install clean
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean
# cd /usr/ports/x11/lightdm-gtk-greeter-settings/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean 
# cd /usr/ports/x11/xfce4-goodies/ && make install clean
```

- Explain

| Package Name | Description of role |
|:-------------------------------|:------------------------------------|
| `xorg ' | X Windows |
| `lightdm ' | Lightweight Display Manager LightDM |
| `lightdm-gtk-greenter ' | GTK+ login interface plugin for LightDM |
| `xfce ' | Xfce Desktop Environment |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manage user home directory |
| 'xfce4-goodies ' | XFCE ADDITIONAL ASSEMBLIES AND PLUGINS |
| `lightdm-gtk-greener-settings ' | Configure the graphic tool for the LightDM GTK+ login interface, without which it will not be possible to start |


# CODESPAN_0__

```sh
$ echo "/usr/local/etc/xdg/xfce4/xinitrc" > ~/.xinitrc
```

Or..

```sh
$ echo "/usr/local/etc/xdg/xfce4/xinitrc" > ~/.xsession
```


# Start service

```sh
# service dbus enable
# service lightdm enable
```

# Set the Chinese interface

EDIT __CODESPAN_0: FIND __CODESPAN_1_, AND MODIFY __CODESPAN_2_ TO __ ___ CODESPAN_3_。

Refresh database:

```sh
# cap_mkdb /etc/login.conf
```

# Picture appreciation #

FreeBSD inclusion Xfce (..gitbook/assets/xfce1.png)

[FreeBSD integration Xfce] (..gitbook/assets/xfce2.png)

[FreeBSD integration Xfce]

# Global menu (optional)

Installation:

```sh
# pkg install xfce4-appmenu-plugin appmenu-gtk-module appmenu-registrar
```

or:

```sh
# cd /usr/ports/x11/xfce4-appmenu-plugin/ && make install clean
# cd /usr/ports/x11/gtk-app-menu/ && make install clean
# cd /usr/ports/x11/appmenu-registrar/ && make install clean
```

View installation to describe, install description configuration:

```sh
$ xfconf-query -c xsettings -p /Gtk/ShellShowsMenubar -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/ShellShowsAppmenu -n -t bool -s true
$ xfconf-query -c xsettings -p /Gtk/Modules -n -t string -s "appmenu-gtk-module"
```

# Software recommendations

The xfce email client for FreeBSD recommended __CODESPAN_0, which can be used together with __CODESPAN_1 and __CODESPAN_2_。

There is also a desktop plugin called ___CODESPAN_0_. You can check the content of the web page, in conjunction with setting up smart bookmarks. You can search for what you want by setting a man manual for FreeBSD。


# XTerm Terminal Dynamic Title

# sh #

EDIT __CODESPAN_0_, WRITING:

```sh
if [ -t 1 ]; then       
  while :; do
    printf '\033]0;%s\007' "$PWD"   
    printf '\n$ '
    if ! IFS= read -r cmd; then
      break
    fi
    printf '\033]0;%s\007' "$cmd"
    eval "$cmd"
  done
  exit
fi
```

# csh #

EDIT __CODESPAN_0_, WRITING:

```sh
if ( $?TERM && $TERM =~ xterm* ) then
    set host = `hostname`      
    alias postcmd 'rehash; printf -- "\033]2\;%s\007" "${user}@${host}: ${cwd}"
endif
```

# tcsh

EDIT __CODESPAN_0_, WRITING:

```sh
switch ($TERM)
case xterm*:
    set prompt="%{\033]0;%n@%m: %~\007%}%# "
    breaksw
default:
    set prompt="%# "
    breaksw
endsw 
```

# bash #

EDIT __CODESPAN_0_, WRITING:

```sh
case $TERM in
         xterm*)
             PS1="\[\033]0;\u@\h: \w\007\]bash\\$ "
             ;;
         *)
             PS1="bash\\$ "
             ;;
     esac
```

# zsh #

EDIT __CODESPAN_0_, WRITING:

```sh
autoload -Uz add-zsh-hook

funaction xterm_title_precmd()
print-Pn -- '\e '2;%n@m %a '
["$TERM"== 'screen'*] & & print-Pn- ' \e_ 005{% @ \ \ \ \ \ \ \
♪ I'm sorry ♪

function xterm_title_preexec()
print -Pn -- '\e '2; %n@m@ # # # & print-n -- "${q)1}a"
["$TERM" = 'screen'*]] & {print-Pn- ' \e_\ 00 00 00 \ \ \ # # # # # & & print-n -- \ (q)}
♪ I'm sorry ♪

if[[[["$TERM"=(Eterm*alacretty*aterm*foot*gnom*konsole*kterm*putty*rxvt*scscreen*wezterm*tmux*xterm*]]
add-zsh-book-Uz pred xterm_title_precmd
the Uz preexec xterm_title_preexec
f
````

References

- [6.1 Dynamic head not working] (https://docs.oracle.com/cd/E1963-01/817-1951/6mhl08aii/index.html), bash configuration from here
- [Wamphyre/BSD-XFCE] (https://github.com/Wamphyre/BSD-XFCE) with reference collections
- [Zsh - Arch Linux]

# Fragmentation and unfinished business

further developments are needed to demonstrate the current process, and only s seems to be possible。

