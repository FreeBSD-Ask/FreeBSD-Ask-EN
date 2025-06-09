# Section 4.21 root login on the desktop

> ** Warning**
>
> As some users want root to log on to the desktop, write this chapter for a free spirit. Please note that the root account has the highest authority and that the wrong use of the root account is likely** to destroy the system** and therefore there are very high security risks** using its login graphical interface**. Please be careful with the following. We have no responsibility.

# GDM

GDM, the GNOME Display Manager, GNOME Display Manager.

Open `/usr/local/etc/pam.d/gdm-password ' , note `account requisite pam_securetty.so ' (i.e. add # # at the top)

Restart Service

```sh '
# Service gdm restart
````

# LightDM

LightDM, Light Display Manager, lightweight display manager.

Then change the profile:

- Edit `/usr/local/etc/lightdm/lightdm.conf ':

Pull down, find `greeter-show-manual-login=true ' remove the `#' in front. The business will appear repeatedly, for the first time, for your use, do not modify it! And it should keep pulling down.

- Edit `/usr/local/etc/pam.d/lightdm ':

Delete the line `account requisite pam_securetty.so ' (i.e. add # # at the top)

Restart Service

```sh '
♪ service lightdm restart
````

Yeah.

# SDDM

SDDM is the Simple Desktop Display Manager, a simple desktop display manager.

Change `/usr/local/etc/pam.d/sddm ' document: replace `login ' after `include ' with `system ' . There are four replacements required.

Restart Service

```sh '
♪ Service sddm restart
````

After that, root login sddm!


> ** Warning**
>
The > root account has the highest authority, and the error in using the root account may** damage the system**, and therefore there is a very high security risk** using its login graphical interface.
。