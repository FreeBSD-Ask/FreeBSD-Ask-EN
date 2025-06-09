# Section 5.5 Web browser

# Fire Fox Browser

# # Install normal versions (frequent updates)

- Install with pkg

```sh '
# Pkg install firebox
````

- Or use Ports.

```sh '
#cd /usr/ports/www/firefox
# Make install clean
````

# # Install long-support versions

- Install with pkg

```sh '
Pkg install firefox-esr
````

- Or use Ports.

```sh '
#cd/usr/ports/www/firefox-esr/
# Make install clean
````

Chromium

Chromium is not Chromium, but the order to commence in FreeBSD is `chrome ' .

I don't...

- Install with pkg

```sh '
# Pkg install choromium
````

- Or use Ports.

```sh '
#cd /usr/ports/www/chromium
# Make install clean
````

> ** Warning**
>
> To compile Chromium, you must have at least 12G memory, or an equivalent exchange partition + memory.

# Chrome (Linux Compatible)

- Install with pkg

```sh '
# Pkg install linux-chrome
````

- Or use Ports.

```sh '
#cd/usr/ports/www/linux-chrome/
# Make install clean
````



# Appendix: Chromium Synces with Google Account

>** Skills**
>
>There are items that even consider as currently removed components not clean enough, i.e. Port `www/ungoograd-chromium'. The software removes more non-transparent and Google-related elements.

- Because of its open source, Chromium's relationship with Google Crome is about the same as AOSP on Pixel UI. Chromium does not install download plugins directly from Google Chome 's online plug-in store, but manually installs crx from the local area (AutoSync browser plugins are added). There are no Google translation plugins, etc., and more of the difference between the two can be found (https://chromium.goglesource.com/chromium/src/+/master/docs/chromium_browser_vs_google_chrome.md)
- First, `Chromium ' is not `Google Chrome ' , which is the open source and free software published by The Chromium Project under [BSD 3-Clause "New" or "Revised" License] (https://github.com/chromium/chromium/blob/main/LICENSE), and Google LLC.

- Chromium deleted the default api of the previous login with the Chrome account after the release of [Chromium 89] (https://archlinux.org/news/chromium-losing-sync-support-in-early-march/).

Get to the point, you need to add the following two Google online forums (mail list) before you start getting token

- [Google Browner sign-in best account] (https://groups.google.com/u/0/a/chromium.org/g/google-browser-signin-testacounts)
- [Chromium-dev] (https://groups.google.com/a/chromium.org/g/chromium-dev)

![..gitbook/assets/join-chromium-dev-for-api1.png]

Because we just need access to the Chrome Google API, you have to close both mailing lists (i.e. “do not receive emails”), or you will be subjected to the actual bombing of the mailing list (which is very frequent).

![..gitbook/assets/join-chromium-dev-for-api2.png]

![..gitbook/assets/join-chromium-dev-for-api3.png]

When you add Google Browner sign-in test account, you may see a hint like "You have no right to access this " , which is normal.

[join-mail-list-for-google-api-error2] (./.gitbook/assets/join-chromium-list-2error.png)

Later, it was opened with a browser.

Note**
>
>The Google account that needs to be on the console is the same as the one that was added to the mailing list.

![..gitbook/assets/chromium-use-google-api-guide-0.png]

Click " My First Project " at the top left corner and select " New Item " at the top right corner of the popup window.

![..gitbook/assets/chromium-use-google-api-guide-02.png]

The name of the project is entered at all times and the organization defaults.

![..gitbook/assets/chromium-use-google-api-guide-03.png]

Click " My First Project" at the top left corner, and then select the item you just created in the pop-up window.

![./.gitbook/assets/chromium-use-google-api-guide-04.png]

Click on "API services" in the chart above, then "+ Enable API services"

![./.gitbook/assets/chromium-use-google-api-guide-04-1.png]

Search for 'chrome-sync'

![./.gitbook/assets/chromium-use-google-api-guide-06.png]


Click to enable 'Chrome Sync API '

![./.gitbook/assets/chromium-use-google-api-guide-05.png]

The following status will be shown later in the enabled API list

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

- Client ID `502882456359-okloi0a7k6vjodss69so97tmgv0jjj5.apps.googleusercontent.com '
- Client Key `GoCSPX-iKHEKZmP4w_zdq0Z8nwOqz6SF2_M`

Returns the "API" service, click "+ Create Certificate" and then click "API Key".

![..gitbook/assets/chromium-use-google-api-guide-17.png]

We got an API key (this is my, it's invalid, you have to create your own): `Aiza SyDVPYJQN9HTjAiD89y3xBDOG3oaxV5_E'

![.. ..gitbook/assets/chromium-use--google-api-guide-18.png)

Open the certificate and give an overview:

![./.gitbook/assets/chromium-use-google-api-guide-19.png]


Editor ~/.profile ' , add (this is for me, it's invalid, you have to create yourself):

Note**
>
>This text is only tested under the default shell sh + KDE 6. If you use different environments, welcome PR.

```sh '
Report GOOGLE_API_KEY=AizaSyDVpYvJQun9HTjAiD89y3xBDOG3oaxV5_E # Here fill in API key
Report GOOGLE_DEFAULT_CLIENT_ID=502882456359-okloi0a7k6vjodss69s97tmv0jjj5.apps.googleusercontent.com #
# Fill in the client key here
````

Then start over. Open Chromium again.

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

- [Chromium Sync-Learning to Pi] (https://www.learningtopi.com/sbc/chromium-sync)
- [For Chromium to resume login] (https://nyac.at/posts/google-sync-in-chromium)


# Fragmentation and unfinished business

## # Use a lot of performance when solving unknown errors in Chromium (add to the start parameter of the icon, the icon is a text file)

```sh '
Chrome-disk-cache-size=0-disable-gpu
````

