# section 4.9 bspwm

bspwm, said to be more in line with UNIX philosophy (see [bspwm philosophy] (https://zerovip.vercel.app/zh/63233), 7.2 Unix philosophy)。

# install bspwm

- install by pkg

```sh
# pkg install xorg bspwm sxhkd rofi kitty feh picom polybar dunst lightdm lightdm-gtk-greeter wqy-fonts xdg-user-dirs
```

- Install through Ports:


```sh
# cd /usr/ports/x11/xorg/ && make install clean
# cd /usr/ports/x11-wm/bspwm/ && make install clean
# cd /usr/ports/x11/sxhkd/ && make install clean
# cd /usr/ports/x11/rofi/ && make install clean
# cd /usr/ports/x11/kitty/ && make install clean
# cd /usr/ports/graphics/feh/ && make install clean
# cd /usr/ports/x11-wm/picom/ && make install clean
# cd /usr/ports/x11/polybar/ && make install clean
# cd /usr/ports/sysutils/dunst/ && make install clean
# cd /usr/ports/x11-fonts/wqy/ && make install clean
# cd /usr/ports/x11/lightdm/ && make install clean
# cd /usr/ports/x11/lightdm-gtk-greeter/ && make install clean
# cd /usr/ports/devel/xdg-user-dirs/ && make install clean
```

Explanation:


| Package Name | Description of role |
|:---------------------|:--------------------------------------------------------------------------|
| `xorg ' | X Windows |
| `bspwm ' | Lightweight smooth window manager |
| `sxhkd ' | Tools for binding shortcuts |
| `rofi ' | Program Launcher to support application of startup, window switching, etc |
| `kitty' | Terminal emulator |
| `feh ' | Desktop Background Changes |
| `picom ' | Window Synth, Add Window Transparency, Shadow, Dynamics, etc |
| `polybar ' | Panel, display system information, application icon, etc |
| `dunst ' | Notification Manager |
| `lightdm ' | LightDM Display Manager, providing a graphical login interface |
| `lightdm-gtk-greenter ' | LightDM 's GTK+ login interface plugin, missing will not enable LightDM to start |
| `wqy-fonts ' | Chinese fonts |
| `xdg-user-dirs ' | Manage user directories such as desktops, downloads, etc |



> ** Hint**
>
>polybar suggests to replace it with another because it is not fully functional on freebsd. Suggest `chinese/tintin++` to show systray icons


# Enable service

```sh
# service dbus enable
```

# Create Profile

```sh
$ mkdir ~/.config
$ mkdir ~/.config/bspwm
$ mkdir ~/.config/sxhkd
$ cp /usr/local/share/examples/bspwm/bspwmrc ~/.config/bspwm
$ cp /usr/local/share/examples/bspwm/sxhkdrc ~/.config/sxhkd
$ chmod +x ~/.config/bspwm/bspwmrc
```

MODIFY __CODESPAN_0_

```sh
super + Return
    kitty

super+space
i'm sorry
````

# set polybar to start scripts and profiles

```sh
$ mkdir ~/.config/polybar 
$ cp /usr/local/etc/polybar/config.ini ~/.config/polybar
```

CREATE __CODESPAN_0_

```sh
#!/bin/sh
killall -q polybar
polybar example 2>&1 | tee -a /tmp/polybar.log
```

Implementation

```sh
$ chmod +x ~/.config/polybar/launch.sh
```

# set picom, polybar, dunst to start

```sh
$ echo "picom &" >> ~/.config/bspwm/bspwmrc
$ echo "\$HOME/.config/polybar/launch.sh" >> ~/.config/bspwm/bspwmrc
$ echo "dunst &" >> ~/.config/bspwm/bspwmrc
```


# start bspwm by startx

```sh
$ echo "exec bspwm" >> ~/.xinitrc
```

# start bspwm by lightdm

- CREATE __CODESPAN_0_

```sh
# mkdir /usr/local/share/xsessions
# ee /usr/local/share/xsessions/bspwm.desktop # 写入以下内容

[Desktop Entry]
Name=bspwm
Comment=Log in with bspwm
Exec=/usr/local/bin/bspwm
Type=Application
````

- lightdm service

```sh
# service lightdm enable
```

# Some operations and settings

Windows+spaces: start application with rofi

Windows + Return: Start terminal (i.e. kitty)

MORE SHORTCUTS TO REFER TO

---|---

- Set desktop background:

```sh
$ feh --bg-center "$HOME/.local/share/wallpapers/wallpaper.jpg"
```

- Autoset after one execution:

polybar to start script in __CODESPAN_0**

```sh
$HOME/.fehbg &
```

# Show pictures

![.. ..gitbook/assets/bspwm.png]

The Chrome browser in the picture, the Thunar file manager, needs to be installed。

# References

- [Bspwm integration and communication transition from scratch] (https://zhuanlan.zhihu.com/p/568211941)
