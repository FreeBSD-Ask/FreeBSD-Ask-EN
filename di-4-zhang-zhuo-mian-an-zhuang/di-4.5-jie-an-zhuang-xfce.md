Section 4.5 Xfce

Xfce aims to develop a lightweight but fully functional desktop. Xfce's Logo is a mouse (https://docs.xfce.org/faq#what_does_it_mean), and there have been feedbacks from bugs who claim that Xfce's screen wallpaper caused their computer screens to be scratched by cats ([joke\] The default desktop startup screen domain to monitor!] (https://bugzilla.xfce.org/show_bug.cgi?id=12117)).

# Install xfce4

- Install by pkg

```sh '
# pkg install xorg lightdm-gtk-greeter xqy-fonts xdg-user-dirs xfce4-goodieslightdm-gtk-greeter-settings
````

- or install through ports

```sh '
#cd/usr/ports/x11/xorg/ & make install clean
# cd /usr/ports/x11-wm/xfce4 & make effective clean
#cd /usr/ports/x11/xfce4-goodies/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd/usr/ports/x11/lightdm/ & make install clean
#cd /usr/ports/x11/lightdm-gtk-greener/ & make install clean
#cd /usr/ports/x11/lightdm-gtk-greener-settings/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
#cd /usr/ports/x11/xfce4-goodies/ & make install clean
````

- Explain.

Name of package Description of role
|: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
`xorg 'X Windows
`lightdm ' | Lightweight Display Manager
GTK+ login interface plugin for `lightdm-gtk-greenter ' | LightDM
`xfce 'xfce Desktop Environment
`wqy-fonts '
`xdg-user-dirs' manages user home directory
Additional components and plugins for `xfce4-goodies ' | XFCE
|lightdm-gtk-greiter-settings`equipment configuration LightDM GTK+ login interface without a graphical tool that will not be able to start |


# 'startx'

```sh '
$eho "/usr/local/etc/xdg/xfce4/xinitrc" ~/.xinitrc
````

Or...

```sh '
$ echo "/usr/local/etc/xdg/xfce4/xinitrc" ~/.xsession
````


# Start service

```sh '
# For service dbus able
♪ service lightdm able
````

# Set the Chinese interface

Edit `/etc/login.conf ' : find `default:\, amend `:lang=C.UTF-8 ' to `:lang=zh_CN.UTF-8 ' .

Refresh database:

```sh '
#cap_mkdb/etc/login.conf
````

# Picture appreciation #

[FreeBSD installation Xfce] (..gitbook/assets/xfce1.png)

[FreeBSD installation Xfce] (..gitbook/assets/xfce2.png)

[FreeBSD installation Xfce] (./.gitbook/assets/xfce3.png)

# Global menu (optional)

Installation:

```sh '
# pkg install xfce4-appmenu-plugin-appmenu-gtk-module appmenu-registrar
````

or:

```sh '
#cd /usr/ports/x11/xfce4-appmenu-plugin/ & make install clean
#cd /usr/ports/x11/gtk-app-menu/ & make install clean
#cd/usr/ports/x11/appmenu-registrar/ & make install clean
````

View installation to describe, install description configuration:

```sh '
$ xfconf-query-c xsettings-p/Gtk/ShellShowsMenubar-n-t bool-s true
$ xfconf-query-c xsettings-p/Gtk/ShellShowsAppmenu-n-t bool-s true
It's like "appmenu-gtk-module."
````

# Software recommendations

The xfce email client for FreeBSD is recommended as `mail/violence ' , which can be used with `xfce4-mailwatch-plugin ' , `security/gnome-keyring ' .

There is also a desktop plugin called `x11/xfce4-verve-plugin ' . You can check the content of the web page, in conjunction with setting up smart bookmarks. You can search for what you want by setting a man manual for FreeBSD.


# XTerm Terminal Dynamic Title

# sh #

Edit ~/.shrc ' , writing:

```sh '
If [-t 1]; then
While: do
%s\007' "$PWD"
I'm sorry.
IFS = read-r cmd; then
Break
F
%s\007' "$cmd"
"$cmd."
Don't do that.
I don't know.
F
````

# csh #

Edit ~/.cshrc ' , writing:

```sh '
If ($? TERM & $TERM = ~ xterm*) then
= 'hostname '
== sync, corrected by elderman == @elder_man
I don't know, endif.
````

# tcsh

Edit ~/.tcshrc ' , writing:

```sh '
Switch ($TERM)
Case xterm*:
setprompt="%({\033]0;%n@m:%~007}%#"
Breaksw
Difault:
Set prompt=%#
Breaksw
I'm sorry.
````

# bash #

Edit ~/.bashrc ' , writing:

```sh '
Case $TERM in
I'm sorry.
PS1 = "[033] 0;\u@h:\w\bash\$"
;
*)
PS1 is "bash."
;
That's it.
````

# zsh #

Edit ~/.zshrc ' , writing:

```sh '
butload-Uz add-zsh-hook

funaction xterm_title_precmd()
print-Pn -- '\e '2;%n@m %a '
["$TERM"== 'screen'*] & & print-Pn- ' \e_ 005{% @ \ \ \ \ \ \ \
♪ I'm sorry ♪

function xterm_title_preexec()
print -Pn -- '\e '2; %n@m@ # # # & print-n -- "${q)1}a"
["$TERM"= = 'sc]] & {print-Pn- ' \e_005{ %m\005{ \b4}005{} # # & & print-n -- '${1}1};}
♪ I'm sorry ♪

If[[[["$TERM"=(Eterm*alacretty*aterm*foot*gnom*konsole*kterm*putty*rxvt*scscreen*wezterm*tmux*xterm*]]
Add-zsh-book-Uz pred xterm_title_precmd
The Uz preexec xterm_title_preexec
F
````

References

- [6.1 Dynamic settings not working (https://docs.oracle.com/cd/E1963-01/817-1951/6mhl08aii/index.html), bash configuration from here
- [Wamphyre/BSD-XFCE] (https://github.com/Wamphyre/BSD-XFCE) with reference collections
- [Zsh - Arch Linux Chinese wiki] (https://wiki.archlinuxcn.org/wiki/Zsh), Zsh configuration from here

# Fragmentation and unfinished business

Further developments are needed to demonstrate the current process, and only s seems to be possible.

。