Section 6.3 Printer

CUPS, full name Common Unix Printing System, supports printing protocols and printer devices, and allows printers to be shared on the network with IPP or SMB protocols.

Printers are connected through USB to the print server (i.e. FreeBSD). Print servers share printers on the Intranet for use. Other computers in the Intranet automatically search for printers in the Intranet by sending out a radio package.

This is a print server that can be found regularly through Android, Apple, Debian tests.


# Install CUPS (common UNIX printing system)

- Install with pkg:

```sh '
# Pkg install cups cups-filters
````

- Or install with Ports:

```sh '
#cd/usr/ports/print/cuts/ & make install clean
#cd /usr/ports/print/cuts-filters/ & make install clean
````

>** Skills**
>
> If you use the desktop environment, select `x11 ' in the Ports Options interface to generate an application icon for adding and configure printers in the system.

Explanation:

| Package | Effect statement |
|: - - - - - |: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
`cups ' for CUPS services
`cups-filters ' | to support a driver-free printer (i.e. IPP Everywhere protocol) |
|dbus |avahi needs as CUPS dependent on auto-installation
|awahi-app` | as CUPS relies on auto-installation, Avahi daemon for auto-discoverium for printers in the Intranet


>** Skills**
>
>This paper turns FreeBSD into a print server. If FreeBSD only wants to print as a print client with a USB connected printer and does not need to share, then awahi-app and dbus are not necessary

Note**
>
> If the printer does not support undriver-free printing, the corresponding driver needs to be installed

# Add service

```sh '
# For service dbus able
# With service aahi-daemon capable #
♪ Service cupsd enough
````

Once the service is activated, the other devices should be able to automatically identify the shared printer in the Intranet. Try printing the test page to test if you can print properly.

# Shared printing service to LAN

If this LAN access is not allowed, machines other than `localhost ' cannot be used.

I don't...

Edit `/usr/local/etc/cups/cupsd.conf':

- It's available.

```ini '
Listen localhost: 631
Listen/var/run/cups/cups.sock
````

Add (IP for your FreeBSD IP address):

```ini '
Listen IP:631
````

- Again.

```ini '
Restrict access to the server...
<Location/ >
Order open, Denny.
</Location >

Restrict access to the admin pages...
<Location/admin >
AuthType Default
Require user@SYSTEM
Order open, Denny.
</Location >
````

For

```ini '
Restrict access to the server...
<Location/ >
Allow from 192.168.0.0/24 # IP session to visit
Order open, Denny.
</Location >

Restrict access to the admin pages...
<Location/admin >
Allow from 192.168.0.0/24 # IP session to visit
AuthType Default
Require user@SYSTEM
Order open, Denny.
</Location >
````

This way the CUPS management page can be accessed remotely from the LAN.

# Add Printer

Enter `http://IP:631 ' in the browser, the address is the printer ' s management page.

![.. ..gitbook/assets/cup1.png]

Click `Adminization-Add Prince ' to create printer by hint.

It is sufficient to enter the account number password using `root ' or `wheel ' user login (entry their account password in FreeBSD).

![.. ..gitbook/assets/cup2.png]

Click `Add Prince ' to add a printer.

![.. ..gitbook/assets/cup3.png]

The printer used in this paper is Brother HL L3228CDW.

![.. .gitbook/assets/cup4.png]

When creating, please tick `Share This Prince ' .

![.. .gitbook/assets/cup5.png]

Select the model.

![.. ..gitbook/assets/cup6.png]

If the printer is free of charge, select `Generic IPP Everywhere Prince (en) ' ; otherwise the associated driver needs to be installed and the corresponding model selected.

![...gitbook/assets/cup7.png]

Successfully added printer!

![.. ..gitbook/assets/cup8.png]

# KDE Desktop Add Printer

Equipment that needs to be printed does not require additional operation. The printing server is typically automatically found and automatically added to the printer list, which is selected when printing a file. For example, KDE desktop:

![.. ..gitbook/assets/cup10.png]

![.. ..gitbook/assets/cup11.png]

# Print Test Page

Print test pages from the Debian machine from the Intranet:

![... ..gitbook/assets/cup12.jpg)

# Fault removal and unfinished business

- Printer-free.

To confirm that the printer is free, you can search at <https://openprinting.github.io/printers/>. Take the example of the printer used for this document:

![.. ..gitbook/assets/cup9.png]

HP HP printer installed Port `print/hplip '

- What kind of test page is FreeBSD printing?

To be tested.
。