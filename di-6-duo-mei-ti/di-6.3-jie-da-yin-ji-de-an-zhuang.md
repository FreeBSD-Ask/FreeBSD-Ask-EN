Section 6.3 Printer

CUPS, full name Common Unix Printing System, supports printing protocols and printer devices, and allows printers to be shared on the network with IPP or SMB protocols。

Printers are connected through USB to the print server (i.e. FreeBSD). Print servers share printers on the Intranet for use. Other computers in the Intranet automatically search for printers in the Intranet by sending out a radio package。

This is a print server that can be found regularly through Android, Apple, Debian tests。


# Install CUPS (common UNIX printing system)

- install with pkg:

```sh
# pkg install cups cups-filters
```

- Or install with Ports:

```sh
# cd /usr/ports/print/cups/ && make install clean
# cd /usr/ports/print/cups-filters/ && make install clean
```

>** Skills**
>
> If you use the desktop environment, select __CODESPAN_0_ in the Ports Options interface to generate an application icon for adding and configure printers in the system。

Explanation:

| Package | Description of role |
|:----------------|:------------------------------------------|
| `cups ' | FOR CUPS SERVICE |
| `cups-filters ' | To support driver-free printers (i.e. IPP Everywhere protocol) |
| `dbus ' | Avahi needs as CUPS dependent auto-installation |
 | `awahi-app ' | As CUPS-dependent auto-installation, Avahi daemon, for auto-detection of printers in the Intranet |


>** Skills**
>
>This paper turns FreeBSD into a print server. If FreeBSD only wants to print as a print client with a USB connected printer and does not need to share, then awahi-app and dbus are not necessary

Note**
>
> If the printer does not support undriver-free printing, the corresponding driver needs to be installed

# Add service

```sh
# service dbus enable
# service avahi-daemon enable
# service cupsd enable
```

Once the service is activated, the other devices should be able to automatically identify the shared printer in the Intranet. Try printing the test page to test if you can print properly。

# Shared printing service to LAN

IF THIS IS NOT SET TO ALLOW ACCESS TO THE LOCAL AREA NETWORK, IT IS NOT POSSIBLE TO USE A MACHINE EXCEPT __CODESPAN_0_。

---|---

EDIT __CODESPAN_0_:

- It's available

```ini
Listen localhost:631
Listen /var/run/cups/cups.sock
```

Add (IP for your FreeBSD IP address):

```ini
Listen IP:631
```

- Again

```ini
# Restrict access to the server...
<Location />
  Order allow,deny
</Location>

Restrict access to the admin pages...
<Location/admin >
AuthType Default
Require user@SYSTEM
Order open, Denny
</Location >
````

For

```ini
# Restrict access to the server...
<Location />
  Allow from 192.168.0.0/24 # 要访问的 IP 所在网段
  Order allow,deny
</Location>

Restrict access to the admin pages...
<Location/admin >
Allow from 192.168.0.0/24 # IP session to visit
AuthType Default
Require user@SYSTEM
Order open, Denny
</Location >
````

THIS WAY THE CUPS MANAGEMENT PAGE CAN BE ACCESSED REMOTELY FROM THE LAN。

# Add Printer

ENTER __CODESPAN_0_ IN THE BROWSER, WHICH IS THE PRINTER'S MANAGEMENT PAGE。

![.. ..gitbook/assets/cup1.png]

CLICK __CODESPAN_0_ TO CREATE A PRINTER BY HINT。

You will be prompted to enter an account password using __CODESPAN_0 or __CODESPAN_1_ group user login (entry their account password in FreeBSD)。

![.. ..gitbook/assets/cup2.png]

CLICK __CODESPAN_0_ TO ADD A PRINTER。

![.. ..gitbook/assets/cup3.png]

The printer used in this paper is Brother HL L3228CDW。

![.. .gitbook/assets/cup4.png]

WHEN CREATING, PLEASE TICK __CODESPAN_0_。

![.. .gitbook/assets/cup5.png]

Select the model。

![.. ..gitbook/assets/cup6.png]

IF THE PRINTER IS FREE OF CHARGE, SELECT ___ CODESPAN_0; OTHERWISE THE RELEVANT DRIVER NEEDS TO BE INSTALLED AND THE CORRESPONDING MODEL SELECTED。

![...gitbook/assets/cup7.png]

Successfully added printer

![.. ..gitbook/assets/cup8.png]

# KDE DESKTOP ADD PRINTER

EQUIPMENT THAT NEEDS TO BE PRINTED DOES NOT REQUIRE ADDITIONAL OPERATION. THE PRINTING SERVER IS TYPICALLY AUTOMATICALLY FOUND AND AUTOMATICALLY ADDED TO THE PRINTER LIST, WHICH IS SELECTED WHEN PRINTING A FILE. FOR EXAMPLE, KDE DESKTOP:

![.. ..gitbook/assets/cup10.png]

![.. ..gitbook/assets/cup11.png]

# Print Test Page

Print test pages from the Debian machine from the Intranet:

![... ..gitbook/assets/cup12.jpg)

# Fault removal and unfinished business

- Printer-free

to confirm that the printer is free, you can search at <https://openprinting.github.io/printers/>. take the example of the printer used for this document:

![.. ..gitbook/assets/cup9.png]

HP Hp printer installed Port __CODESPAN_0_。

- What kind of test page is FreeBSD printing

To be tested。
