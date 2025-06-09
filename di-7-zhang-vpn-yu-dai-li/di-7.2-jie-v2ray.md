# Section 7.2 V2ray

# install v2ray

- install with pkg:

```sh
# pkg install v2ray
```

- Or install with Ports:

```
# cd /usr/ports/net/v2ray/
# make install clean
```

---|---

- you can also install xray-core:

```sh
# pkg install xray-core
```

- Or install with Ports:

```
# cd /usr/ports/security/xray-core/ 
# make install clean
```

the two proxy configurations are essentially the same, and the configuration documents can be found in the respective official document, and xray is well able to refer to the v2ray configuration。

# Start software

If there is a pre-existing proxy client to export the configuration of the client ' s node, copy it to FreeBSD, assuming the exported file is named __CODESPAN_0_, then execute:

```sh
$ v2ray -c config.json
```

---|---

- if xray-core is used, execute:

```sh
$ xray -c config.json
```

The software should be working by now。

# Configure software agents

THIS IS WHEN YOU CAN OPEN __CODESPAN_0, FIND THE CORRESPONDING __CODESPAN_1... ATTRIBUTE, __CODESPAN_2... IS AN ARRAY, EACH OF WHICH REPRESENTS THE ENTRY INTERFACE CONFIGURATION, WITH AN ADDRESS AND PORT NUMBER, AND A PROXY. SETS THE CORRESPONDING ADDRESS AND PORT NUMBER HERE WITHIN THE SOFTWARE THAT YOU WANT。

For example, one of the entry interfaces, CODESPAN_1 , CODESPAN_2 , CODESPAN_3 , CODESPAN_4 , CODESPAN_5 , can be found in the browser setting, the Web-Agent Server, and the http proxy address set to __CODESPAN_6 , the port is __CODESPAN_7 . Same-socks proxy can also refer to this method setting。

MOST SOFTWARE AGENTS ARE SET DIFFERENTLY. THE CONFUSION IS SUCH THAT DESKTOP SOFTWARE NEEDS TO HAVE ITS OWN PROXY. TERMINAL COMMANDS ARE EASIER IF THEY REQUIRE A PROXY. MOST TERMINAL COMMANDS LOOK FOR THE THREE ENVIRONMENTAL VARIABLES __CODESPAN_0, __CODESPAN_1 AND __CODESPAN_2_, WITH THE CORRESPONDING AGENT BASED ON THE VALUES OF THESE THREE ENVIRONMENTAL VARIABLES。

the following commands apply to sh, bash, zsh:

```sh
$ export HTTP_PROXY="http://127.0.0.1:10809" # 设置 http 代理
$ export HTTPS_PROXY="http://127.0.0.1:10809" # 设置 https 代理
$ export ALL_PROXY="socks5://127.0.0.1:10808" # 设置 socks 代理
```

when the settings are complete, the web page is viewed in the fox browser, and the log of the v2ray output is observed, and the browser traffic is seen to be gone. terminal commands also leave the agent, but some of the commands set the agent according to the environment variable. please find out how the corresponding software is set。

# Agent diversion

Some sites do not need proxy servers, such as those in-country, local sites, etc. This requires a diversion of flows, some of which require agency, and some of which require a straight line。

Opens the config.json and finds the corresponding routing attribute, which has a rules sub- attribute that is used to configure v2ray traffic diversion. Rules can be configured with a ip attribute or domain attribute for each rule. The proxy traffic is a web site, and ip, if the ip or web site matches one of the rules, v2ray will forward the flow to the corresponding outbounds position, e.g. outbonds, with tag being proxy, direct (direct), block. So you can just put the pip that you want to divert into the corresponding rules. Reference is made here to the corresponding v2ray document. In fact, when exporting the profile on the v2ray client, the corresponding diversion rules are defaulted。

v2ray has also given two resource files __CODESPAN_0, __CODESPAN_1_, __ CODESPAN_2_, which are stored on various web sites, __ CODESPAN_3_, and each ip. The resource file path can be searched automatically for __CODESPAN_5 and __CODESPAN_6_ files under the path by setting the environment variable __CODESPAN_4_, v2ray. For xray is to set the resource path using __CODESPAN_7。

for example, the settings below the direct-link rules set the cn web site direct connection in geosite:

```json
      {
        "domain": [
          "geosite:cn"
        ],
        "outboundTag": "direct",
        "type": "field"
      },
```

the v2ray community gives a web site directly to the cn site that is less complete and less classified, and can search for community-organized geosite, geoip files on gethub, which also detail white list configuration patterns and blacklist configuration patterns。
