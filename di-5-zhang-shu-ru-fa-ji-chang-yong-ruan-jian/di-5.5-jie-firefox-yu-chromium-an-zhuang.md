# Section 5.5 Web browser

# Fire Fox Browser

# # Install normal versions (frequent updates)

- install with pkg

```sh
# pkg install firefox
```

- Or use Ports

```sh
# cd /usr/ports/www/firefox
# make install clean
```

# # Install long-support versions

- install with pkg

```sh
pkg install firefox-esr
```

- Or use Ports

```sh
#cd /usr/ports/www/firefox-esr/
# make install clean
```

Chromium

Chromium is not chrome, but the start order in FreeBSD is __CODESPAN_0_。

---|---

- install with pkg

```sh
# pkg install chromium
```

- Or use Ports

```sh
# cd /usr/ports/www/chromium
# make install clean
```

> ** Warning**
>
> To compile Chromium, you must have at least 12G memory, or an equivalent exchange partition + memory。

# Chrome (Linux Compatible)

- install with pkg

```sh
# pkg install linux-chrome
```

- Or use Ports

```sh
# cd /usr/ports/www/linux-chrome/ 
# make install clean
```



# Appendix: Chromium Synces with Google Account

>** Skills**
>
> There are items that even consider as currently removed components not clean enough, i.e. Port __CODESPAN_0_. The software removes more non-transparent and Google-related elements。

- Because of its open source, Chromium's relationship with Google Crome is about the same as AOSP on Pixel UI. Chromium does not install download plugins directly from Google Chome 's online plug-in store, but manually installs crx from the local area (AutoSync browser plugins are added). There are no Google translation plugins, etc. [View this page] (https://chromium.goglesource.com/chromium/src//master/docs/chromium_browser_vs_google_chrome.md)
- First, CODESPAN_0 is not CODESPAN_1 __, the former being the Open Source and Free Software published by the Chromium Project under [BSD 3-Clause "New" or "revised" License] (https://github.com/chromium/chromium/blob/main/LICENSE) and the latter being Google LLC。

- Chromium deleted the default api of the previous login with the Chrome account after the release of [Chromium 89] (https://archlinux.org/news/chromium-losing-sync-support-in-early-march/)。

Get to the point, you need to add the following two Google online forums (mail list) before you start getting token

- [Google Browner sign-in best account]
- [Chromium-dev] (https://groups.google.com/a/chromium.org/g/chromium-dev)

![..gitbook/assets/join-chromium-dev-for-api1.png]

Because we just need access to the Chrome Google API, you have to close both mailing lists (i.e. “do not receive emails”), or you will be subjected to the actual bombing of the mailing list (which is very frequent)。

![..gitbook/assets/join-chromium-dev-for-api2.png]

![..gitbook/assets/join-chromium-dev-for-api3.png]

When you add Google Browner sign-in test account, you may see a hint like "You have no right to access this " , which is normal。

[join-mail-list-for-google-api-error2] (./.gitbook/assets/join-chromium-list-2error.png)

Open with a browser (https://console.cloud.google.com/)

Note**
>
>The Google account that needs to be on the console is the same as the one that was added to the mailing list。

![..gitbook/assets/chromium-use-google-api-guide-0.png]

Click " My First Project " at the top left corner and select " New Item " at the top right corner of the popup window。

![..gitbook/assets/chromium-use-google-api-guide-02.png]

The name of the project is entered at all times and the organization defaults。

![..gitbook/assets/chromium-use-google-api-guide-03.png]

Click " My First Project" at the top left corner, and then select the item you just created in the pop-up window。

![./.gitbook/assets/chromium-use-google-api-guide-04.png]

CLICK ON "API SERVICES" IN THE CHART ABOVE, THEN "+ ENABLE API SERVICES"

![./.gitbook/assets/chromium-use-google-api-guide-04-1.png]

search for 'chrome-sync'

![./.gitbook/assets/chromium-use-google-api-guide-06.png]


Click to enable 'Chrome Sync API '

![./.gitbook/assets/chromium-use-google-api-guide-05.png]

THE FOLLOWING STATUS WILL BE SHOWN LATER IN THE ENABLED API LIST

![./.gitbook/assets/chromium-use-google-api-guide-07.png]

Select " Outlook Permission Request Page " :

![./.gitbook/assets/chromium-use-google-api-guide-08.png]

Create external application:

![./.gitbook/assets/chromium-use-google-api-guide-09.png]

![./.gitbook/assets/chromium-use-google-api-guide-10.png]

![./.gitbook/assets/chromium-use-google-api-guide-11.png]

![./.gitbook/assets/chromium-use-google-api-guide-12.png]

Create as follows:

![./.gitbook/assets/chromium-use-google-api-guide-13.png]

Click on the Client to create the OAuth client ID "Application type is " Desktop Application " :

![./.gitbook/assets/chromium-use-google-api-guide-14.png]

Create as follows:

![./.gitbook/assets/chromium-use-google-api-guide-15.png]

Click to create Desktop Client 1

![..gitbook/assets/chromium-use-google-api-guide-16.png]

We got it (me, it's not working, you have to create yourself):

- CLIENT ID _CODESPAN_0_
- CLIENT KEY __CODESPAN_0_

RETURNS THE "API" SERVICE, CLICK "+ CREATE CERTIFICATE" AND THEN CLICK "API KEY"。

![..gitbook/assets/chromium-use-google-api-guide-17.png]

WE GOT AN API KEY. _CODESPAN_0_

![./.gitbook/assets/chromium-use-google-api-guide-18.png]

Open the certificate and give an overview:

![./.gitbook/assets/chromium-use-google-api-guide-19.png]


EDIT __CODESPAN_0, JOIN. (THIS IS MINE, IT'S INVALID, YOU HAVE TO CREATE YOUR OWN:

Note**
>
>This text is only tested under the default shell sh + KDE 6. If you use different environments, welcome PR。

```sh
export GOOGLE_API_KEY=AIzaSyDVpYvJQUn9HTjAiD89y3xBDOG3oaxV5_E # 这里填 API 密钥
export GOOGLE_DEFAULT_CLIENT_ID=502882456359-okloi0a7k6vjodss69so97tmqmv0jjj5.apps.googleusercontent.com # 这里填客户端 ID
export GOOGLE_DEFAULT_CLIENT_SECRET=GoCSPX-iKHEKZmP4w_zdq0Z8nwOqz6SF2_M # 这里填客户端密钥
```

Then start over. Open Chromium again。

Click On Synchronization:

![./.gitbook/assets/chromium-use-google-api-guide-20.png]

Enter your own account:

![./.gitbook/assets/chromium-use-google-api-guide-21.png]

Enter your own account password:

![..gitbook/assets/chromium-use-google-api-guide-22.png]

![..gitbook/assets/chromium-use-google-api-guide-23.png]

Can not open message

![..gitbook/assets/chromium-use-google-api-guide-24.png]

References

- [Chromium Synch-Learning to Pi] (https://www.learningtopi.com/sbc/chromium-sync)
- [Restore login for Chromium] (https://nyac.at/posts/google-sync-in-chromium)


# Fragmentation and unfinished business

## # use a lot of performance when solving unknown errors in chromium (add to the start parameter of the icon, the icon is a text file)

```sh
chrome --disk-cache-size=0 --disable-gpu
```

