# Section 7.2 V2ray

# Install v2ray

- Install with pkg:

```sh '
# pkg install v2ray
````

- Or install with Ports:

````
#cd/usr/ports/net/v2ray/
# Make install clean
````

I don't...

- You can also install xray-core:

```sh '
# pkg install xray-core
````

- Or install with Ports:

````
#cd/usr/ports/security/xray-core/
# Make install clean
````

The two proxy configurations are essentially the same, and the configuration documents can be found in the respective official document, and xray is well able to refer to the V2ray configuration.

# Start software

If there is a pre-existing proxy client to export the client ' s node configuration, copy it to FreeBSD, assuming the exported file is called `config.json ' and then execute:

```sh '
V2ray-c config.json
````

I don't...

- If xray-core is used, execute:

```sh '
That's right.
````

The software should be working by now.

# Configure software agents

This is when `config.json ' can be opened, and the corresponding `inborns ' attribute can be found, `inbounds ' is an array in which each element represents the configuration of the entry interface, has an address and port number, and is proxy. Sets the corresponding address and port number here within the software that you want.

For example, one of the entry interfaces `protocol ' is `http ' , `listen ' is `127.0.0.1 ' , `port ' is `10809 ' . If there is a need for a fire fox browser walker, it can be found in the browser setting, the network-agent server, setting the http proxy address is set to `127.0.0.1 ' and the port is `10809 ' . Same-socks proxy can also refer to this method setting.

Most software agents are set differently. The confusion is such that desktop software needs to have its own proxy. Terminal commands are easier if they require a proxy. Most terminal commands look for the three environmental variables `HTTP_PROXY ' , `HTTPS_PROXY ' , and `ALL_PROXY ' , with the corresponding agent based on the values of the three environmental variables.

The following commands apply to sh, bash, zsh:

```sh '
$export HTTP_PROXY="http://127.0.0.1:10809"# Set up http proxy
# Set up https proxy
$ export ALL_PROXY="socks5://127.0.0.1:10808"#Socks proxy
````

When the settings are complete, the web page is viewed in the Fox Browser, and the log of the v2ray output is observed, and the browser traffic is seen to be gone. Terminal commands also leave the agent, but some of the commands set the agent according to the environment variable. Please find out how the corresponding software is set.

# Agent diversion

Some sites do not need proxy servers, such as those in-country, local sites, etc. This requires a diversion of flows, some of which require agency, and some of which require a straight line.

Opens the config.json and finds the corresponding routing attribute, which has a rules sub- attribute that is used to configure v2ray traffic diversion. Rules can be configured with a ip attribute or domain attribute for each rule. The proxy traffic is a web site, and ip, if the ip or web site matches one of the rules, v2ray will forward the flow to the corresponding outbounds position, e.g. outbonds, with tag being proxy, direct (direct), block. So you can just put the pip that you want to divert into the corresponding rules. Reference is made here to the corresponding v2ray document. In fact, when exporting the profile on the v2ray client, the corresponding diversion rules are defaulted.

v2ray also gave `geosite.dat ' , `geoip.dat ' two resource documents, `geosite.dat ' , which are maintained on various web sites, and `geoip.dat ' which are maintained on each ip. Resource file path, which can automatically search for `geosite.dat ' and `geosite.ip ' files under the path by setting the environment variable `V2RAY_LOCATION_ASSET ', v2ray. For xray, the resource path is set using the `Xray_LOCATION_ASSET ' environment variable.

For example, the settings below the direct-link rules set the cn web site direct connection in geosite:

```json '
_Other Organiser
"domain":
"geosite:cn"
I don't know.
"outbound Tag": "direct,"
"type": "field"
♪ I don't know ♪
````

The v2ray community gives a web site directly to the cn site that is less complete and less classified, and can search for community-organized geosite, geoip files on gethub, which also detail white list configuration patterns and blacklist configuration patterns.
。