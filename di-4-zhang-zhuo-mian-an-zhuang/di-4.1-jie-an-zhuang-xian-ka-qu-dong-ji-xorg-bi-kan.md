Section 4.1 Visible card-driven (Intel, AMD)

>** Warning**
>
>Do not use `sysutils/desktop-insteller ' , which causes unnecessary errors and problems.

# Fragmentation and unfinished business

! [Drive not installed] (..gitbook/assets/noqudong.png)

No graphic card driver installed.

I don't...


# Show card support

For FreeBSD 13, compiled using `drm-510-kmod ' , support is the same as Linux 5.10. AMD can support R7 4750U.

FreeBSD 14.1-RELEASE, 14-STABLE (OSVERSION > 1400508), compiled and used `drm-61-kmod ' in support of the same as Linux 6.1. The 12th generation of Alder Lake-N (e.g. N100) can be supported through practical testing. Subsequent editions of the 13 generations and others are being tested without conditions.

FreeBSD 15 CURRENT, compiled and used `drm-66-kmod ' , in support of the same as Linux 6.6.

>** Skills**
>
> You can query the OSVERSION equivalent version and Git submission in the final chapter of the port developer 's manual.
>
>Look at this machine OSVERSION:
>
> ```sh '
@uname-U
>150019
> ````

>** Warning**
>
>A new system source code may need to be retrieved every time a dot or large version is upgraded, and the installation of a graphic card-driven module may need to be recompiled to successfully complete the upgrade, rather than being stuck to the black screen: or you use " module source " .


# Install Intel / AMD card driver

Note**
>
> When using Gnome, you may not be able to enter the desktop again if you lock the screen/sillscreen automatically. See [Bug 255049 - x11/gdm doesn't show the login scene] (https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=255049).

Note**
>
> When using Ports, Drm needs to have a current version of the system source code in `/usr/src ' that can be consulted to update the chapter of the system. If you were installed in other sections of the reference book, then your system would probably already have a source code and no more source code.


# FreeBSD 13.X

```sh '
#cd /usr/ports/gram-510-kmod
# Make BATCH=yes important clean
````

Or (please use Ports if you have any questions)

```sh '
# pkg install drum-510-kmod
````

# FreeBSD 14.X

>** Skills**
>
> For pkg installation, please configure the core module source for kernels (kmods) by reference to other chapters of this book.

```sh '
#cd /usr/ports/gram-61-kmod
# Make BATCH=yes important clean
````

Or (please use Ports if you have any questions)

```sh '
# pkg install drum-61-kmod
````

FreeBSD 15.0

```sh '
#cd/usr/ports/gram-66-kmod
# Make BATCH=yes important clean
````

Note**
>
> This older graphic card, like HD 4000 of the Intel Triple Processor, does not need to be installed in the traditional BIOS mode, but there is a potential under UEFI (FreeBSD 13.0 and later without the problem) and this DRM graphic card driver needs to be installed.

# Configure Intel / AMD card

Please proceed as follows:

# Intel core card

```sh '
# sysrc-f/etc/rc.conf kld_list+=i915kms
````

# AMD #

- Add `amdgpu ' (most people should use this, if no change `radeonkms ') if HD-7000 is later

```sh '
# sysrc-f/etc/rc.conf kld_list+=amdgpu
````

- If it's HD-7000, add `kld_list= 'radeonkms'.

```sh '
# sysrc-f/etc/rc.conf kld_list+=radeonkms
````

# # troubleshooting and unfinished business

Note**
>
>In case of any problem, use Ports to recompile the installation. Especially when the version is upgraded.

- 'KLD XXX.ko depends on kelnel -'

The reminder does not match the kernel version. Please upgrade the system or use ports to compile the installation.

![..getbook/assets/amd_error.png]

# Video hard-on

# Intel video hard fix

If this section is not configured, the software will not run! Directly "paragraph error".

- Install with pkg:

```sh '
# pkg install libva-intel-media-driver
````

- Or install with Ports:

```sh '
#cd/usr/ports/multimedia/libva-intel-media-driver/
# Make install clean
````

# # AMD video hard fix

- Install with pkg

```sh '
# pkg in mesa-gallium-va mesa-gallium-vdpau
````

- Or install with Ports:

```sh '
#cd /usr/ports/graphics/mesa-gallium-va/ & make install clean
#cd /usr/ports/graphics/mesa-gallium-vdpau/ & make install clean
````

I don't...

This may also be necessary:

`/usr/local/etc/X11/xorg.conf.d/20-amdgpu-tearfree.conf ' (please create)

```ini '
Section "Device"
Identifier "AMDgpu"
Driver "amdgpu."
Option "TearFree" "on"
EndSection
````

It can then be tested with `mpv-hwdec xx.mp4 ' . Please install mpv on your own.

# Brightness reconciliation

Common

- For general computers:

```sh '
# sysrc-f/boot/loader.conf acpi_video=YES
````

- For Thinkpad:

```sh '
# sysrc-f/boot/loader.conf acpi_ibm_load=YES
# sysrc-f/boot/loader.conf acpi_video=YES
````

# Intel/AMD

`backlight ' introduced from FreeBSD 13.

```sh '
# backlight #
# Backlight decr 20 #
# backlight + # default adjustment brightness increase 10%
# backlight - # default light change 10%
````

If the above operation does not work, check what equipment exists under the path `/dev/backlight ' .

- Example (a copy won't work, self `ls /dev/backlight ' look at):

```sh '
# Backlight-f/dev/backlight/amdgpu_bl00-10
# Backlight-f/dev/backlight/backlight0-10
````

References

- [backlight -- configuration backlight hardware] (https://man.freebsd.org/cgi/man.cgi?backlight)
- This part of the tutorial was tested for renoir graphic cards:

# Fragmentation and unfinished business

- If there is a problem with using a graphic card, contact the author directly: [https://github.com/freebsd/drm-kmod/issues] (https://github.com/freebsd/drm-kmod/issues)
- If there is an awakening problem, the `hw.acpi.reset_video= "1" can be added to `/boot/loader.conf ' to reset the display adaptor when awakening.
- General users who are not members of the `wheel ' group are requested to join the `video ' group.

# References

- The details of the graphic support are available [wiki/Graphics] (https://wiki.freebsd.org/Graphics)
