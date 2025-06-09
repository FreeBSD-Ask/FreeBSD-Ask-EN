# Section 7.1 HTTP Agent

V2ray or clash opens to allow LAN connection. You can then configure the following.

- View used shell

```sh '
$eho $Shell
````

# HTTP_PROXY Proxy

# If using `sh ' , `bash ' or `zsh '

Note**
>
>Environmental Variable HTTP_PROXY must be uppercase! It's not working!

- Settings:

```sh '
#export HTTP_PROXY=http://192.168.X:7890
````

>** Warning**
>
>All `192.168.X:7890 ' in this paper are not actual parameters, whichever is practical, and a copy pasting will not be effective!

- Cancel:

```sh '
# Unset HTTP_PROXY
````


# If using 'csh ' #

Settings:

```sh '
#setenv http_proxy http://192.168.X:7890
````

Cancel:

```sh '
# Unsetenv http_proxy
````

# Git Agent

See section on Update through Source Code.

# Browser Configuration Agent

Chromium itself does not have a profile such as ~/.config ' . There is no environment variable parameter to specify the default proxy server. However, you can add start-up parameters (options).

For example:

```sh '
--proxy-server= "I.P. Address: Port"
````

Example:

```sh '
$ crome-proxy-server= "127.0.0.1:1234" (end start)
````

Default is the http protocol if your proxy is using sock:

```sh '
--proxy-server="socks"
````

Socksv4:

```sh '
--proxy-server="socksv4"
````

- Enable Chromium to use the proxy by default in a graphical interface:

Finds the desktop file that your desktop environment created for Chromium, usually at ~/.local/share/applications/ '.

```sh '
$ee chromium-browser. desktop# Use your favorite editor to open chromium desktop files in the above directory
````

Found `Exec=chrome %U' This line adds the parameters you need at a later stage.

```sh '
Comment
Comment =Google webbrowser based on WebKit
Encoding=UTF-8
Exec=chrome %U
GenericName [zh_CN]=
I don't know.
````

Example:

```sh '
Exec = chrome %U-proxy-server = "192.168.2.163:20172"
````

# # Separately as Firefox Configuration Agent

This section is not repeated because Firefox has a module for the GUI Configuration Agent in the browser > Network Settings tab for Windows GNU/linux Macos and all BSD clients.

[FF-Porxy]

# # References

- [FreeBSD Manual Pages: Chromium] (https://man.freebsd.org/cgi/man.cgi?query=chrome&appos=0&sektion=0&manpath=FreeBSD+13.2-RELEASE+and+Ports&arch=default&format=html)
- [FreeBSD FORUMs: chromium program settings page doesn't exist] (https://forums.freebsd.org/threads/chromium-proxy-settings-page-doesnt-exist31927/)
