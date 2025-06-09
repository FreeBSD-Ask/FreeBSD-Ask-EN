# Section 4.2 Visible Card Driver (NVIDIA)

>** Warning**
>
>For notebooks that do not have **Synthetic Card Straightway**, the Intel Nucleic Visible Drive (related Drm) must be installed!

# Install a card drive


Install with pkg:

```sh '
# pkg install nvidia-drm-kmod nvidia-settings
````

Or install with Ports;

```sh '
#cd /usr/ports/graphics/nvidia-drm-kmod/ & make install clean
# cd /usr/ports/x11/nvidia-settlings/ & make install clean
````


# Configure NVIDIA graphic cards

- Activate kernel module.

```sh '
# echo 'hw.nvidiadrm.modeset="1">/boot/loader.conf
# sysrc-f/etc/rc.conf kld_list+=nvidia-modset
````

>** Warning**
>
>Do not attempt to load `nvidia-drm.ko ' . It's useless and it's gonna get stuck.

- Generates the X11 profile. Attention, if normal displays no need for this and the next steps!

```sh '
Xorg - configure
#cp / root/xorg.conf.new/etc/X11/xorg.conf
````

>** Warning**
>
>Do not attempt to install and use Port `x11/nvidia-xconfig ' . It's useless and it's gonna get stuck.



# Installation of decodors

- Install with pkg:

```sh '
pkg install libva-vdpau-driver libvdpau libvdpau-va-gl
````

- Or install with Ports:

```sh '
#cd /usr/ports/multimedia/libva-vdpau-driver/ & make install clean
#cd /usr/ports/multimedia/libvdpau/ & make install clean
#cd /usr/ports/multimedia/libvdpau-va-gl/ & make install clean
````

The NVIDIA drive can then be used properly by restarting.

# View drive state

After restarting, you should be able to drive the graphic card.

- To view drive information (up-to-date every second):

```sh '
$nvidia-smi-L-1
````

- View KDE system parameters:

![..gitbook/assets/nvi2.png]


- Open a movie with MPV, and you can see that there's a significant increase in the amount of use (I'm up from 3M to hundreds of gigatons) and can watch it with SMPlayer.

![.. ..gitbook/assets/nvi1.jpg]


