# SECTION 7.1 HTTP AGENT

V2ray or clash opens to allow LAN connection. You can then configure the following。

- view used shell

```sh
$ echo $SHELL
```

# HTTP_PROXY PROXY

# IF __CODESPAN_0, __CODESPAN_1 _ OR __CODESPAN_2 _

Note**
>
>ENVIRONMENTAL VARIABLE HTTP_PROXY MUST BE UPPERCASE! IT'S NOT WORKING

- Settings:

```sh
# export HTTP_PROXY=http://192.168.X.X:7890
```

>** Warning**
>
>ALL __CODESPAN_0_IN THIS PAPER IS NOT AN ACTUAL PARAMETER, WHICHEVER IS THE ACTUAL, THE COPY PASTE WILL NOT BE EFFECTIVE

- Cancel:

```sh
# unset HTTP_PROXY
```


# IF USING __CODESPAN_0_

Settings:

```sh
# setenv http_proxy http://192.168.X.X:7890
```

Cancel:

```sh
# unsetenv http_proxy
```

# Git Agent

See section on Update through Source Code。

# Browser Configuration Agent

chromium does not itself have a profile such as __CODESPAN_0_. There is no environment variable parameter to specify the default proxy server. However, you can add start-up parameters (options)。

For example:

```sh
--proxy-server="<IP 地址>:<端口>"
```

Example:

```sh
$ chrome --proxy-server="127.0.0.1:1234" (终端启动)
```

default is the http protocol if your proxy is using sock:

```sh
--proxy-server="socks://<IP 地址>:<端口>"
```

socksv4:

```sh
--proxy-server="socksv4://<IP 地址>:<端口>"
```

- enable chromium to use the proxy by default in a graphical interface:

Finds the desktop file that your desktop environment created for Chromium, usually at __CODESPAN_0_。

```sh
$ ee chromium-browser.desktop # 使用你喜欢的编辑器打开上述目录下的 chromium desktop 文件
```

FIND __CODESPAN_0_ THIS LINE ADDS THE PARAMETERS YOU NEED AT A LATER STAGE。

```sh
Comment[zh_CN]=Google web browser based on WebKit
Comment=Google web browser based on WebKit
Encoding=UTF-8
Exec=chrome %U
GenericName[zh_CN]=
......
```

Example:

```sh
Exec=chrome %U --proxy-server="192.168.2.163:20172"
```

# # Separately as Firefox Configuration Agent

This section is not repeated because Firefox has a module for the GUI Configuration Agent in the browser > Network Settings tab for Windows GNU/linux Macos and all BSD clients。

[FF-Porxy]

# # References

- [FreeBSD Manual Pages: Chromium] (https://man.freebsd.org/cgi/man.cgi?query=chrome&appos=0&sektion=0&manpath=FreeBSD+13.2-RELEASE+and+Ports&arch=default&format=html)
- [FreeBSD Forums: choromium solutions page doesn't exist] (https://forums.freebsd.org/threads/chromium-proxy-settlings-page-doesnt-exist31927/)
