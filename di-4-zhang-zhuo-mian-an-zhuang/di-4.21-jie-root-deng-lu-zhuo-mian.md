# section 4.21 root login on the desktop

> ** Warning**
>
> as some users want root to log on to the desktop, write this chapter for a free spirit. please note that the root account has the highest authority and that the wrong use of the root account is likely** to destroy the system** and therefore there are very high security risks** using its login graphical interface**. please be careful with the following. we have no responsibility。

# GDM

GDM, the GNOME Display Manager, GNOME Display Manager。

OPEN __CODESPAN_0, COMMENT __CODESPAN_1_

Restart Service

```sh
# service gdm restart
```

# LightDM

LightDM, Light Display Manager, lightweight display manager。

Then change the profile:

- EDIT __CODESPAN_0:

PULL DOWN AND FIND __CODESPAN_0_ TO REMOVE THE __CODESPAN_1_. THE BUSINESS WILL APPEAR REPEATEDLY, FOR THE FIRST TIME, FOR YOUR USE, DO NOT MODIFY IT! AND IT SHOULD KEEP PULLING DOWN。

- EDIT __CODESPAN_0:

COMMENT __CODESPAN_0_

Restart Service

```sh
# service lightdm restart
```

Yeah。

# SDDM

SDDM is the Simple Desktop Display Manager, a simple desktop display manager。

CHANGE ___CODESPAN_0_ FILE: REPLACE `login`_ WITH `system`_ AFTER `include`_. THERE ARE FOUR REPLACEMENTS REQUIRED。

Restart Service

```sh
# service sddm restart
```

after that, root login sddm


> ** Warning**
>
the > root account has the highest authority, and the error in using the root account may** damage the system**, and therefore there is a very high security risk** using its login graphical interface。
