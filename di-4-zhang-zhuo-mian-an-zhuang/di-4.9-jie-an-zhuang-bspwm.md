# Section 4.9 bspwm

bspwm, said to be more in line with UNIX philosophy (see [bspwm Introduction] (https://zerovip.vercel.app/zh/63233), 7.2 Unix philosophy).

# Install bspwm

- Install by pkg

```sh '
# pkg install xgbspwm shhkd # pkg inkppppkppppppppppkpppppppppkppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppptppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppbpppppppppppppppppppppppppp
````

- Install through Ports:


```sh '
#cd/usr/ports/x11/xorg/ & make install clean
#cd /usr/ports/x11-wm/bspwm/ & make install clean
# cd/usr/ports/x11/sxhkd/ & make install clean
# cd /usr/ports/x11/rofi/ & make install clean
# cd /usr/ports/x11/kitty/ & make install clean
#cd /usr/ports/graphics/feh/ & make install clean
#cd /usr/ports/x11-wm/picom/ & make install clean
#cd /usr/ports/x11/polybar/ & make install clean
#cd/usr/ports/sysutils/dunst/ & make install clean
#cd /usr/ports/x11-fonts/wqy/ & make install clean
#cd/usr/ports/x11/lightdm/ & make install clean
#cd /usr/ports/x11/lightdm-gtk-greener/ & make install clean
#cd /usr/ports/devel/xdg-user-dirs/ & make install clean
````

Explanation:


Name of package Description of role
|: - - - - - |: | - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
`xorg 'X Windows
`bspwm ' | Lightweight flat window manager
`sxhkd '| A tool to bind shortcuts
`rofi ' | program starter to support application of startup, window switching, etc.
`kitty ' | terminal simulator
`feh ' | Desktop Background Change
`picom ' | Window Synth, Add Window Translucency, Shadow, Motion Equivalence
`polybar ' panel showing system information, application icons, etc.
`dunst ' Notification Manager
`lightdm ' |LightDM Display Manager to provide a graphical login interface
|lightdm-gtk-greeter`LightDM login interface plugin for GTK+, missing will not be able to start LightDM |
`wqy-fonts '
`xdg-user-dirs ' | to manage user directories such as desktops, downloads, etc.



> ** Hint**
>
>polybar suggests to replace it with another because it is not fully functional on freebsd. Suggest `chinese/tintin+++ 'to display systray icons


# Enable service

```sh '
# For service dbus able
````

# Create Profile

```sh '
$Mkdir~/.config
$ mkdir~/.config/bspwm
$ mkdir~/.config/sxhkd
$cp /usr/local/share/examples/bspwm/bspwmrc ~/.config/bspwm
$cp /usr/local/share/examples/bspwm/sxhkdrc ~/.config/sxhkd
$chmod+x~.config/bspwm/bspwmrc
````

Modify ~/.config/sxhkd/sxhkdrc '

```sh '
sub +Return
Hey, Kitty.

Super+space
I'm sorry.
````

# Set polybar to start scripts and profiles

```sh '
$ mkdir~/.config/polybar
$cp /usr/local/etc/polybar/config.ini ~/.config/polybar
````

Create ~/.config/polybar/launch.sh '

```sh '
#!/bin/sh
Okay, will-q-polybar.
I'm sorry.
````

Implementation

```sh '
$chmod+x~.config/polybar/launch.sh
````

# Set picom, polybar, dunst to start

```sh '
$ echo "picom &" > ~/.config/bspwm/bspwmrc
$ echo "$HOME/.config/polybar/launch.sh" > ~/.config/bspwm/bspwmrc
$ echo "dunst &" > ~/.config/bspwm/bspwmrc
````


# Start bspwm by startx

```sh '
$ ~.xinitrc
````

# Start bspwm by lightdm

- Create `/usr/local/share/xsessions/bspwm.desktop '

```sh '
#mkdir/usr/local/share/xsessions
#ee /usr/local/share/xsessions/bspwm.desktop #

[Desktop Entry]
Name=bspwm
Comment=Log in with bspwm
Exec=/usr/local/bin/bspwm
Type=Application
````

- Lightdm service

```sh '
♪ service lightdm able
````

# Some operations and settings

Windows+spaces: start application with rofi

Windows + Return: Start terminal (i.e. kitty)

More shortcuts to refer to ~/.config/sxhkd/sxhkdrc '

I don't...

- Set desktop background:

```sh '
$ feh-bg-center "$HOME/.local/share/wallpapers/wallpaper.jpg"
````

- Autoset after one execution:

~/.config/ bspwm/ bspwmrc ** Add before **

```sh '
$HOME/.fehbg &
````

# Show pictures

![.. ..gitbook/assets/bspwm.png]

The Chrome browser in the picture, the Thunar file manager, needs to be installed.

# References

- [Bspwm installation and configuration from scratch] (https://zhuanlan.zhihu.c)@m/p/568211941)
