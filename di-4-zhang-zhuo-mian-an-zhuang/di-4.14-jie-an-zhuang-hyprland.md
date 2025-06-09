# Section 4.14 Hyprland

Hyprland is a Wayland compositer that supports transparent windows, fuzzy, round corners, etc。

[hyprland on freebsd]

# Install Hyprland

- install with pkg:

```sh
# pkg ins hyprland waybar wofi qt6-base qt5-wayland qt6-wayland xdg-desktop-portal-hyprland hyprpicker swaybg mako nerd-fonts slurp grim swaylock kitty dolphin
```

- Or install with Ports:

```sh
# cd /usr/ports/x11-wm/hyprland/ && make install clean
# cd /usr/ports/x11/waybar/ && make install clean
# cd /usr/ports/x11/wofi/ && make install clean
# cd /usr/ports/devel/qt6-base/ && make install clean
# cd /usr/ports/graphics/qt5-wayland/ && make install clean
# cd /usr/ports/graphics/qt6-wayland/ && make install clean
# cd /usr/ports/x11/xdg-desktop-portal-hyprland/ && make install clean
# cd /usr/ports/x11/hyprpicker/ && make install clean
# cd /usr/ports/x11/swaybg/ && make install clean
# cd /usr/ports/x11/mako/ && make install clean
# cd /usr/ports/x11-fonts/nerd-fonts/ && make install clean
# cd /usr/ports/x11/slurp/ && make install clean
# cd /usr/ports/x11/grim/ && make install clean
# cd /usr/ports/x11/swaylock/ && make install clean
# cd /usr/ports/x11-fm/dolphin/ && make install clean
# cd /usr/ports/x11/kitty/ && make install clean
```


Note**
>
> automatically install dbus and wayland as a dependency。

- Explain:

| Package Name | Description of role |
|:-----------------------------|:--------------------------------------------------------------------------|
| `hyprland ' | Dynamic Wallland Synth |
| `waybar ' | GTK status bar for wloots synthesiser (e. g. Hyprland) |
| `wofi ' | program launcher (or use rofi, too, to understand) |
| `qt6-base ' | Base module for Qt 6 |
| `qt5-wayland ' | The Wayland support module for Qt 5 allows Qt 5 applications to run in the Wayland environment。 |
| `qt6-wayland ' | The Wayland Support Module for Qt 6 allows Qt 6 applications to run in the Wayland environment。 |
| `xdg-desktop-portal-hyprland ' | XDG Designtop Portal of Hyprland achieved by providing an interface with other applications |
| `hyprpecker ' | Colour Selector |
| `swaybg ' | Wallpaper Tool |
| `mako ' | Show Notifications |
| `nerd-fonts ' | icon font, which can be used to insert a pattern in the configuration file and display it in places like waybar |
| `slurp ' | Screen Selection Tool for Selection on Screen |
| `grim ' | Screenshot Tool |
| `swaylock ' | Lock Screen Tool |
| `kitty' | Terminal |
| `dolphin ' | File Manager |


# Start service

```sh
# service seatd enable
# service dbus enable
```

# First time on Hyprland

> ** Important**:
>
> If XDG_RUNTIME_DIR is not set to start the error tip, you can make the settings below. ** Here's the example of zsh as the default shell:**
>
> Write in __CODESPAN_0_: (If the default shell is sh, write to ~/.profile, echo $0 to show the default shell)
>
> ```sh '
>export XDG_RUNTIME_DIR=/var/run/user/__CODESPAN_0_
> ````
>
> AND THEN RESTART: __CODESPAN_0_
>
>
>Ctrl+Alt+F2 enter tty to execute __CODESPAN_0, which will generate a default profile at __CODESPAN_1_。

Configure


IF YOU NEED TO START AUTOMATICALLY, WRITE __CODESPAN_0_:

```sh
ck-launch-session Hyprland
```

If the default shell is sh, write to __CODESPAN_0... and specify the configuration file __CODESPAN_1_..
The focus of the Hyprland window differs from that of the traditional desktop, which is the window on which the mouse cursor is placed (it is " put " , which does not need to click), where the focus of the window is, without the shortcut of Alt+Tab。

## configure hyprland.conf

DOCUMENT LOCATION: __CODESPAN_0_

- Hyprland's default top will have a yellow strip warning sign. Profiles can comment on it, find this line and comment on __CODESPAN_0_
- Default with Windows logo key (Super key in UNIX, same below) as mod key (according to personal custom, also set to Alt key, etc.)_CODESPAN_0_
- Suspended windows and traditional desktop environments act in a manner similar to that in which you can drag to any position on the screen at will, and the window size can be adjusted with the mouse. The default configuration file is to hold down the mod key, and then the left mouse button is to hold the suspended window to drag the window to move, while the right button tow the window to adjust the size of the window. Sets the default suspended window: __CODESPAN_0_
- it is recommended to read the configuration file below, hyprland.conf, swaybg to set the wallpaper and to change the path to your own photo file。

5. TASK COLUMN: __CODESPAN_0_

EXAMPLE:

```sh
# 进入 Hyprland 后自动启动 fcitx5（已经注释掉，按照5.2章安装后自行取消注释即可）
#exec-once=fcitx5
# 设置壁纸，别忘了修改成自己壁纸文件的路径！！！
#exec-once=swaybg -i "$HOME/Pictures/Wallpapers/壁纸.jpg"
# 任务栏
exec-once=waybar
# swaylock 锁屏
exec-once=swayidle -w timeout 300 'swaylock'

♪ Please note not all available settings / options are set here.
For a full list, see the wiki

# autogenerated = 1。

#See https://wiki.hyprland.org/Configuring/Monitors/
== sync, corrected by elderman ==

#See https://wiki.hyprland.org/Configuring/Keywords/ for more

# With a file
# source=~/.config/hypr/myColors.conf

Some default env vars.
_Other Organiser

# For all cases, see https://wiki.hyprland.org/Configuring/Variables/
input {
kb_playout = us
kb_variant =
kb_model =
kb_options =
kb_rules =

    follow_mouse = 1

    touchpad {
        natural_scroll = no
    }

sensitivity is 0 #-1.0, 0 means no sexualization.
♪ I'm sorry ♪

_other organiser
#See https://wiki.hyprland.org/Configuring/Variables/ for more

    gaps_in = 5
    gaps_out = 20
    border_size = 2
    col.active_border = rgba(33ccffee) rgba(00ff99ee) 45deg
    col.inactive_border = rgba(595959aa)

= dwindle
♪ I'm sorry ♪

animations
= yes

    # Some default animations, see https://wiki.hyprland.org/Configuring/Animations/ for more

    bezier = myBezier, 0.05, 0.9, 0.1, 1.05

animation = window, 1, 7, my Bezier
= windowout, 1, 7, default, popin 80%
animation = border, 1, 10, default
animation = borderline, 1, 8
animation = fade, 1, 7, default
animation = workspaces, 1, 6
♪ I'm sorry ♪

dwindle
#See https://wiki.hyprland.org/Configuring/Dwindle-Layout/ for more
enabling is based to MainMod + P in the keybinds section below
♪ you probably want this ♪
♪ I'm sorry ♪

you're not gonna get me started
#See https://wiki.hyprland.org/Configuring/Variables/ for more
= off
♪ I'm sorry ♪

# Window rules
#See https://wiki.hyprland.org/Configuring/Window-Rules/ for more
windowrulev2=float, title:rofi.*
== sync, corrected by elderman == @elder_man
windowrulev2 = float, type: picture viewer


#See https://wiki.hyprland.org/Configuring/Keywords/ for more
$mainMod = SUPER
US$ShiftMod = SUPER_SHIFT
$altMod=SUPER_ALT
$alt=alt
US$Shift=SHIFT

#Example binds, see https://wiki.hyprland.org/Configuring/ Binds/ for more
= $mainMod, Q, exec, kitty #open terminal
bind = $mainMod, C, Killactive, # Close Window
bind = $mainMod, M, exit, # written off
bind = $mainMod, E, exec, toolin# File Manager
bind = $mainMod, V, togglefloating, # Switch to suspended window, drag
bind = $mainMod, R, exec, wife-show drun # Software starter, similar menu
bind = $mainMod, P, pseudo, # Focus Window (the window to which the cursor is directed) freely adjusts the size and position within the area where the flat window was originally occupied
bind = $mainMod, J, togglespit, # Regulates the direction of the focus window and the layout of the adjacent window, up and down, or left and right。
# I got a screenshot #
$screen_file=${HOME}/screen_shot_$(date + "%Y-%m-%d_%H-%M-%S".png
i'm sorry, I'm sorry
i'm sorry
bend=$Shift, Print, exec, Grim-g '$lorp'
it's just that, uh, you know, it's kind of like, uh..

# Move focus with MainMod #
=$mainMod, left, movefocus, l
== sync, corrected by elderman ==
=$mainmod, up, movefocus, u
=$mainMod, down, movefocus, d

# Switch workspaces with MainMod #
# toggle workspace meinmod+number keys, 1 to 0 corresponds to 10 workspaces。
=$mainMod, 1, workspace, 1
== sync, corrected by elderman ==
== sync, corrected by elderman ==
=$mainmod, 4, workspace, 4
=$mainmod, 5, workspace, 5
=$mainmod, 6, workspace, 6
=$mainMod, 7, workspace, 7
=$mainMod, 8, workspace, 8
=$mainMod, 9, workspace, 9
=$mainmod, 0, workspace, 10

# Move active window to a workspace with MainMod + SHIFT + [0-9]
# Move window to another workspace, e. g.mainmod+Shift+2 (win key +2 is viewing workspace 1)
== sync, corrected by elderman == @elder_man
== sync, corrected by elderman == @elder_man
=$mainMod SHIFT, 3, movetoworkspace, 3
=$mainMod SHIFT, 4, movetoworkspace,4
== sync, corrected by elderman == @elder_man
== sync, corrected by elderman == @elder_man
== sync, corrected by elderman == @elder_man
== sync, corrected by elderman == @elder_man
== sync, corrected by elderman == @elder_man
== sync, corrected by elderman == @elder_man

# Scroll through the existing workspace using plainMod + mouse wheel
=$mainMod, mouse_down, workspace, e+1
== sync, corrected by elderman == @elder_man

# Move/resize Windows with MainMod + LMB/RMB and Draging
== sync, corrected by elderman == @elder_man
== sync, corrected by elderman == @elder_man

```

# configure kitty.conf

DOCUMENT LOCATION: __CODESPAN_0_ EXAMPLE:

```sh
# Look and feel

# Color
#aclude... /obsidian.color.conf

# Font Settings
font_family Hassklug Nerd Font Mono
font_size 14.0
#font_features FiraCodeNerdFontCompleteM-Retina +ss02 +ss03 +ss04 +ss05 +ss07 +Zero

# Text Cursor Settings
cursor_blink_interval 2.0
cursor_stop_blinking_after 5.0

# Scrollback
scrollback_lines-1

# Mouse-related settings
copy when selected
mouse_side_wait 2.0 # hide mouse on time

# A hint #
it's not a bad idea
visual_bell_duration 0.3
bell_on_tab yes

# Tabs
tab_bar_edge top
tab_bar_style powerline
tab_powerline_style angled
#invited_tab_foreground #111
i'm sorry, but i'm sorry
active_tab_font_stylebar
#666
#inactive_tab_background #888
tab_bar_background #444
inactive_tab_font_style normal
tab_title_template"fmt.fg.gray"
"active_tab_title_template"

# Mechanics
input_delay 2
i don't know
allow_remote_control no
allow_hyperlinks no
xm-256color
macos_option_as_alt yes
macos_quit_wen_last_window_closed yes
stip_training_spaces smart
you know, update_check_interval 72
hind_window_descriptionstitlebar-only

# Shortcuts
i'm not sure if i'm going to do this

The deaths
@text tab pbcopy
map ctrl+shift+c copy_to_clipboard
_clipboard
map ctrl+alt+j scroll_page_up
map ctrl+alt+k scroll_page_down
i'm sorry

# Tab Management
{\chffffff}map ctrl+t new_tab_wd!neigbor
map alt+s next_tab
map alt+a previous_tab
map alt+q close_tab
map ctrl+s set_tab_title
map ctrl+ship+lift move_tab_backward
map ctrl+shift+right move_tab_forward
map alt+1 goto_tab1
map alt+2 goto_tab2
map alt+3 goto_tab 3
map alt+4 goto_tab 4
map alt+5 goto_tab 5
map alt+6 goto_tab 6
map alt+7 goto_tab7
map alt+8 goto_tab8
map alt+9 goto_tab9

# Text size adjustment
map ctrl+equal change
i'm sorry, miss ctrl+minus change
map ctrl+0 change

#include$US$.conf

```

## # configure waybar (taskbar)

the waybar configuration file directory contains a __CODESPAN_0_ folder in the home directory, containing a __CODESPAN_1 file, and a __CODESPAN_2_. Reference is made to the waybar folder using the example profile. An example profile requires the installation of a noto-enoji font to display it properly, or to change it to the icon you want。

EXAMPLE:

```json
{
    "position": "top",
    "layer": "top",
    "height": 16,
    "margin-top": 0,
    "margin-bottom": 0,
    "margin-left": 0,
    "margin-right": 0,
    "modules-left": ["custom/launcher", "wlr/workspaces", "custom/playerctl", "custom/playerlabel"],
    "modules-center": ["cpu", "memory", "disk"],
    "modules-right": ["tray", "custom/randwall", "network", "pulseaudio", "clock"],
	"clock": {
		"format": "⏰  {:%H:%M}",
		"tooltip": "true",
        	"tooltip-format": "<big>{:%Y %B}</big>\n<tt><small>{calendar}</small></tt>",
        	"format-alt": "🗓️  {:%y/%m/%d}"
	},


	"wlr/workspaces": {
        "active-only": false,
        "all-outputs": true,
        "disable-scroll": false,
        "on-scroll-up": "hyprctl dispatch workspace -1",
        "on-scroll-down": "hyprctl dispatch workspace +1",
		"format": "{icon}",
		"on-click": "activate",
		"format-icons": {
			"urgent": "",
			"active": "🔴",
			"default": "🔵",
    "sort-by-number": true
    },
    },

    "custom/playerctl": {
      "format": "{icon}",
      "return-type": "json",
      "max-length": 64,
      "exec": "playerctl -a metadata --format '{\"text\": \"{{artist}} - {{markup_escape(title)}}\", \"tooltip\": \"{{playerName}} : {{markup_escape(title)}}\", \"alt\": \"{{status}}\", \"class\": \"{{status}}\"}' -F",
      "on-click-middle": "playerctl play-pause",
      "on-click": "playerctl previous",
      "on-click-right": "playerctl next",
      "format-icons": {
        "Playing": "<span foreground='#E5B9C6'>󰒮 󰐌 󰒭</span>",
        "Paused": "<span foreground='#928374'>󰒮 󰏥 󰒭</span>"
      },
    },

    "custom/playerlabel": {
      "format": "<span>{}</span>",
      "return-type": "json",
      "max-length": 48,
      "exec": "playerctl -a metadata --format '{\"text\": \"{{artist}} - {{markup_escape(title)}}\", \"tooltip\": \"{{playerName}} : {{markup_escape(title)}}\", \"alt\": \"{{status}}\", \"class\": \"{{status}}\"}' -F",
      "on-click-middle": "playerctl play-pause",
      "on-click": "playerctl previous",
      "on-click-right": "playerctl next",
      "format-icons": {
        "Playing": "<span foreground='#E5B9C6'>󰒮 󰐌 󰒭</span>",
        "Paused": "<span foreground='#928374'>󰒮 󰏥 󰒭</span>"
      },
    },

"memory":
"format": "🌊,",
"format-alt": "Total",
"interval": 5
♪ I don't know ♪,

"cpu":
"format": "📟usage}",
"format-alt":,
"interval": 5
♪ I don't know ♪,

"disk": {
"format": "📦,",
"format-alt": "Total",
"interval": 5,
"path"..
♪ I don't know ♪,

	"network": {
        	//"format-ethernet": " {ifname}: {ipaddr}",
            "format-ethernet": " IP: {ipaddr}",
        	//"format-linked": " {ifname} (No IP)",
        	"format-disconnected": "󰤭",
        	//"format-alt": " {ifname}: {ipaddr}/{cidr}",
          "tooltip-format": "{essid}",
          "on-click-right": "nm-connection-editor"
	},

	"tray": {
		"icon-size": 16,
		"spacing": 5
	},

	"backlight": {
	"format": "{icon} {percent}%",
        "format-icons": ["", "", "", "", "", "", "", "", ""],
	},

"pulseudio":
"format": "i can't believe it.",
"format-muded": "p",
"format-icons":
"default"..
♪ I don't know ♪,
"scroll-step": 5,
♪ I don't know ♪,
"custom/launcher":
"format": "p",
"on-click": "wifi-how drun,",
"on-click-right": "wifi-how drun"
♪ I don't know ♪,
♪ I'm sorry ♪

```

EXAMPLE:

```css
* {
    border: none;
    border-radius: 0px;
    /*font-family: VictorMono, Iosevka Nerd Font, Noto Sans CJK;*/
    font-family: Cascadia Code, FontAwesome, Noto Sans CJK, Microsoft YaHei UI, HarmonyOS Sans;
    font-size: 14px;
    font-style: normal;
    min-height: 0;
}

windows#waybar
background: ragba (30, 30, 46, 0.5);
border-bottom: 1 px solid #282828;
#f4d9e1
♪ I'm sorry ♪

#workspaces #
#282828;
margin: 5px 5px 5px 5px 5px;
paddy: 0px 5px 0px 5px;
border-radius: 16px;
border: solid 0px #f4d9e1;
fort-right: normal;
fort-style: normal;
♪ I'm sorry ♪
#workspaces button
paddy: 0px 5px;
border-radius: 16px;
color: #928374;
♪ I'm sorry ♪

#workspaces button
#f4d9e1;
background-color: transfer;
border-radius: 16px;
♪ I'm sorry ♪

#workspaces button: cover #
#E6B9C6;
color: black;
border-radius: 16px;
♪ I'm sorry ♪

# custom-date, #clock, #battery, #pulseaudio, #network, # custom-randwall, # custom-launcher
i don't know;
paddy: 5px 5px 5px 5px 5px;
margin: 5px 5px 5px 5px 5px;
border-radius: 8px;
border: solid 0px #f4d9e1;
♪ I'm sorry ♪

#custom-date
#D3869B;
♪ I'm sorry ♪

#custom-power
color: #24283b;
#db4b4b;
border-radius: 5px;
margin-right: 10px;
margin-top: 5px;
margin-bottom: 5px;
margin-loft: 0px;
paddy: 5px 10px;
♪ I'm sorry ♪

#tray
#282828;
margin: 5px 5px 5px 5px 5px;
border-radius: 16px;
paddy: 0px 5px;
/*border-right: solid 1px #282738;*/
♪ I'm sorry ♪

#clock #
#E6B9C6;
#282828;
border-radius: 0px 0px 24px;
paddy-loft: 13px;
paddy-right: 15px;
margin-right: 0px;
margin-loft: 10px;
margin-top: 0px;
margin-bottom: 0px;
fort-right:;
/*border-left: solid 1px #282738;*/
♪ I'm sorry ♪


#battery
#9ece6a;
♪ I'm sorry ♪

#battery.charging
#9ece6a;
♪ I'm sorry ♪

#battery.warning:not (.charging)
#f7768e;
color: #24283b;
border-radius: 5px 5px 5px 5px 5px;
♪ I'm sorry ♪

#backlight
#24283b;
#db4b4b;
border-radius: 0px 0px 0px 0px;
margin: 5px;
margin-loft: 0px;
margin-right: 0px;
paddy: 0px 0px;
♪ I'm sorry ♪

#network
#f4d9e1;
border-radius: 8px;
margin-right: 5px;
♪ I'm sorry ♪

#pulseudio
#f4d9e1;
border-radius: 8px;
margin-loft: 0px;
♪ I'm sorry ♪

#pulseudio.muded
i don't know;
color: #928374;
border-radius: 8px;
margin-loft: 0px;
♪ I'm sorry ♪

# custom-randwall
#f4d9e1;
border-radius: 8px;
margin-right: 0px;
♪ I'm sorry ♪

#custom-launcher
#e5809e;
#282828;
border-radius: 0px 24px 0px 0px;
margin: 0px 0px 0px 0px;
paddy: 0 20px 0 13px;
/*border-right: solid 1px #282738;*/
font-size: 20px;
♪ I'm sorry ♪

#custom-launcher button: cover #
#FB4934;
color: transport;
border-radius: 8px;
margin-right: -5px;
margin-loft: 10px;
♪ I'm sorry ♪

#custom-playerctl
#282828;
paddy-loft: 15px;
dading-right: 14px;
border-radius: 16px;
/*border-left: solid 1px #282738;*/
/*border-right: solid 1px #282738;*/
margin-top: 5px;
margin-bottom: 5px;
margin-loft: 0px;
fort-right: normal;
fort-style: normal;
font-size: 16px;
♪ I'm sorry ♪

# custom-playerlabel
i don't know;
paddy-loft: 10 px;
paddy-right: 15px;
border-radius: 16px;
/*border-left: solid 1px #282738;*/
/*border-right: solid 1px #282738;*/
margin-top: 5px;
margin-bottom: 5px;
fort-right: normal;
fort-style: normal;
♪ I'm sorry ♪

#window #
#282828;
paddy-loft: 15px;
paddy-right: 15px;
border-radius: 16px;
/*border-left: solid 1px #282738;*/
/*border-right: solid 1px #282738;*/
margin-top: 5px;
margin-bottom: 5px;
fort-right: normal;
fort-style: normal;
♪ I'm sorry ♪

#custom-wf-recorder
paddy: 0 20px;
#e5809e;
#1E1E2E;
♪ I'm sorry ♪

#cpu #
#282828;
/*color: #FABD2D;*/
border-radius: 16px;
margin: 5px;
margin-left: 5px;
margin-right: 5px;
paddy: 0px 10px 0px 10px;
fort-right:;
♪ I'm sorry ♪

# memoory #
#282828;
/*color: #83A598;*/
border-radius: 16px;
margin: 5px;
margin-left: 5px;
margin-right: 5px;
paddy: 0px 10px 0px 10px;
fort-right:;
♪ I'm sorry ♪

#disk
#282828;
/*color: #8EC07C;*/
border-radius: 16px;
margin: 5px;
margin-left: 5px;
margin-right: 5px;
paddy: 0px 10px 0px 10px;
fort-right:;
♪ I'm sorry ♪

#custom-hyprappy
#282828;
/*color: #8EC07C;*/
border-radius: 16px;
margin: 5px;
margin-left: 5px;
margin-right: 5px;
paddy: 0px 11px 0px 9px;
fort-right:;
♪ I'm sorry ♪

```

configure

the swaylock profile is in __CODESPAN_0_, and the following is an example profile:

```sh
ignore-empty-password
font=Fira Sans Compressed

no, i'm not
timestr=%R
datestr=%a, %e of %B

screenshots

fade-in = 0.2

effect-blur=20x2
#effect-grayscale
effect-scale = 0.3

indicator
indicator-radius = 360
indicator-thickness=60
indicator-caps-lock

key-hl-color=228833

separator-color=000000000

inside-color=00000099
inside-clar-color=ffd20400
inside-caps-lock-color=009ddc00
inside-ver-color=d9d8d800
inside-wrong-color=ee2e2400

r-color=231f20D9
r-clar-color=231f20D9
ring-caps-lock-color=231f20D9
r-ver-color=231f20D9
ring-wrong-color=231f20D9

line-color = 10000000
line-clar-color=ffd2000
line-caps-lock-color=009ddc00
line-ver-color=d9d8d800
line-wrong-color=ee2e2400

text-clar-color=ffd20400
text-ver-color=d9d8d800
text-wrong-color=ee2e2400

bs-hl-color=ee2e24FF
#caps-lock-key-hl-color=ffd204FF
#caps-lcok-key-hl-color=ee2e24FF
#caps-lock-bs-hl-color=ee2e24FF
#disable-caps-lock-text
text-caps-lock-color=000000FF
````

# Fragmentation and unfinished business

IF YOU HAVE FAILED TO START, OR IF YOU HAVE BLACK SCREENS, CHECK IF YOU HAVE ADDED YOUR USER TO THE __CODESPAN_0_ GROUP, IF YOU HAVE INSTALLED A GRAPHIC CARD DRIVE, IF YOU HAVE SET THE ENVIRONMENT VARIABLE `XDG_RUNTIME_DIR`_ CORRECTLY, AND NO。

# References

- [ArchLinux Hyprland Construction Pointer North] (https://www.bilibili.com/read/cv22707313)
- [Configuration for Hyprland] (https://nth233.top/posts/2023-02-26-Hyprland%E9%85%E8D%E7%BD%AE)
