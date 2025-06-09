SECTION 4.1 VISIBLE CARD-DRIVEN (INTEL, AMD)

>** Warning**
>
> DO NOT USE __CODESPAN_0, WHICH CAUSES UNNECESSARY ERRORS AND PROBLEMS。

# Fragmentation and unfinished business

[No driver installed] (..gitbook/assets/noqudong.png)

No graphic card driver installed。

---|---


# Show card support

For FreeBSD 13, compiled using __CODESPAN_0_, the support is the same as Linux 5.10. AMD can support R7 4750U。

FreeBSD 14.1-RELEASE, 14-STABLE (OSVERSION > 1400508), compiled and used __CODESPAN_0_, in support of the same as Linux 6.1. The 12th generation of Alder Lake-N (e.g. N100) can be supported through practical testing. Subsequent editions of the 13 generations and others are being tested without conditions。

FreeBSD 15 CURRENT, compiled and used __CODESPAN_0_, supported by Linux 6.6。

>** Skills**
>
> You can query the OSVERSION equivalent version and Git submission in the final chapter of the port developer 's manual。
>
>LOOK AT THIS MACHINE OSVERSION:
>
> ```sh '
@uname-U
>150019
> ````

>** Warning**
>
>A new system source code may need to be retrieved every time a dot or large version is upgraded, and the installation of a graphic card-driven module may need to be recompiled to successfully complete the upgrade, rather than being stuck to the black screen: or you use " module source " 。


# Install Intel / AMD card driver

Note**
>
> When using Gnome, you may not be able to enter the desktop again if you lock the screen/sillscreen automatically. See [Bug 25549-x11/gdmdosn't show the login scheme] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=255049)。

Note**
>
> When using Ports, Drm needs to have a current version of the system source code in __CODESPAN_0, which can be used to update the chapter of the system. If you were installed in other sections of the reference book, then your system would probably already have a source code and no more source code。


# FreeBSD 13.X

```sh
# cd /usr/ports/graphics/drm-510-kmod
# make BATCH=yes install clean
```

Or (please use Ports if you have any questions)

```sh
# pkg install drm-510-kmod
```

# FreeBSD 14.X

>** Skills**
>
> for pkg installation, please configure the core module source for kernels (kmods) by reference to other chapters of this book。

```sh
# cd /usr/ports/graphics/drm-61-kmod
# make BATCH=yes install clean
```

Or (please use Ports if you have any questions)

```sh
# pkg install drm-61-kmod
```

FreeBSD 15.0

```sh
# cd /usr/ports/graphics/drm-66-kmod
# make BATCH=yes install clean
```

Note**
>
> This older graphic card, like HD 4000 of the Intel Triple Processor, does not need to be installed in the traditional BIOS mode, but there is a potential under UEFI (FreeBSD 13.0 and later without the problem) and this DRM graphic card driver needs to be installed。

# Configure Intel / AMD card

Please proceed as follows:

# Intel core card

```sh '
# sysrc-f/etc/rc.conf kld_list+=i915kms
````

# AMD #

- IF IT'S AN AMD CARD AFTER HD7000, ADD `amdgpu` (MOST PEOPLE SHOULD USE THIS, IF NO CHANGE __CODESPAN_1_)

    ```sh
    # sysrc -f /etc/rc.conf kld_list+=amdgpu
    ```

- IF IT'S HD-7000, ADD __CODESPAN_0

    ```sh
    # sysrc -f /etc/rc.conf kld_list+=radeonkms
    ```

# # troubleshooting and unfinished business

Note**
>
>In case of any problem, use Ports to recompile the installation. Especially when the version is upgraded。

- CODESPAN_0_

the reminder does not match the kernel version. please upgrade the system or use ports to compile the installation。

![..getbook/assets/amd_error.png]

# Video hard-on

# Intel video hard fix

if this section is not configured, the software will not run! directly "paragraph error"。

- install with pkg:

```sh
# pkg install libva-intel-media-driver
```

- Or install with Ports:

```sh
# cd /usr/ports/multimedia/libva-intel-media-driver/ 
# make install clean
```

# # AMD VIDEO HARD FIX

- install with pkg

```sh
# pkg ins mesa-gallium-va mesa-gallium-vdpau
```

- Or install with Ports:

```sh
# cd /usr/ports/graphics/mesa-gallium-va/ && make install clean
# cd /usr/ports/graphics/mesa-gallium-vdpau/ && make install clean
```

---|---

This may also be necessary:

WRITE __CODESPAN_0_ (PLEASE CREATE)

```ini
Section "Device"
  Identifier "AMDgpu"
  Driver "amdgpu"
  Option "TearFree" "on"
EndSection
```

And then you can test it with __CODESPAN_0. Please install mpv on your own。

# Brightness reconciliation

Common

- For general computers:

```sh
# sysrc -f /boot/loader.conf  acpi_video="YES"
```

- For Thinkpad:

```sh
# sysrc -f /boot/loader.conf  acpi_ibm_load="YES"
# sysrc -f /boot/loader.conf  acpi_video="YES"
```

# INTEL/AMD

__CODESPAN_0_enacted from FreeBSD 13。

```sh
# backlight          # 打印当前亮度
# backlight decr 20  # 降低 20% 亮度
# backlight +        # 默认调整亮度增加 10%
# backlight -        # 默认调整亮度减少 10%
```

IF THE ABOVE-MENTIONED OPERATION DOES NOT WORK, CHECK WHAT EQUIPMENT EXISTS UNDER THE PATH __CODESPAN_0_。

- EXAMPLE (A COPY WON'T WORK, SELF __CODESPAN_0_ LOOK AT):

```sh
# backlight -f /dev/backlight/amdgpu_bl00 - 10
# backlight -f /dev/backlight/backlight0 - 10  
```

References

- [well, backlight-consultation backlighthardware]
- this part of the tutorial was tested for renoir graphic cards:

# Fragmentation and unfinished business

- if there is a problem with using a graphic card, contact the author directly: [https://github.com/freebsd/drm-kmod/issues] (https://github.com/freebsd/drm-kmod/issues)
- IF THERE IS A PROBLEM WITH THE SCREEN NOT LIT AT THE TIME OF AWAKENING, ADD __CODESPAN_1 TO RESET THE DISPLAY ADAPTER AT THE TIME OF AWAKENING。
- IF THE NORMAL USER IS NOT A MEMBER OF ___CODESPAN_0_, THEN JOIN __CODESPAN_1_。

# References

- Detailed support for graphic cards is available [ ] (https://wiki.freebsd.org/Graphics)
