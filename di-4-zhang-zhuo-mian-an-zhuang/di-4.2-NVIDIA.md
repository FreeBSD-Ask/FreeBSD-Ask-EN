# SECTION 4.2 VISIBLE CARD DRIVER (NVIDIA)

>** Warning**
>
>for notebooks that do not have **synthetic card straightway**, the intel nucleic visible drive (related drm) must be installed

# Install a card drive


install with pkg:

```sh
# pkg install nvidia-drm-kmod nvidia-settings
```

Or install with Ports

```sh
# cd /usr/ports/graphics/nvidia-drm-kmod/ && make install clean
# cd /usr/ports/x11/nvidia-settings/ && make install clean
```


# CONFIGURE NVIDIA GRAPHIC CARDS

- Activate kernel module

```sh
# echo 'hw.nvidiadrm.modeset="1"' >> /boot/loader.conf
# sysrc -f /etc/rc.conf kld_list+=nvidia-modeset
```

>** Warning**
>
> DO NOT ATTEMPT TO LOAD __CODESPAN_0_. IT'S USELESS AND IT'S GONNA GET STUCK。

- GENERATES THE X11 PROFILE. ATTENTION, IF NORMAL DISPLAYS NO NEED FOR THIS AND THE NEXT STEPS

```sh
# Xorg -configure 
# cp /root/xorg.conf.new /etc/X11/xorg.conf
```

>** Warning**
>
> Do not attempt to install and use Port __CODESPAN_0_. It's useless and it's gonna get stuck。



# Installation of decodors

- install with pkg:

```sh
pkg install libva-vdpau-driver libvdpau libvdpau-va-gl
```

- Or install with Ports:

```sh
# cd /usr/ports/multimedia/libva-vdpau-driver/ && make install clean
# cd /usr/ports/multimedia/libvdpau/ && make install clean
# cd /usr/ports/multimedia/libvdpau-va-gl/ && make install clean
```

THE NVIDIA DRIVE CAN THEN BE USED PROPERLY BY RESTARTING。

# View drive state

After restarting, you should be able to drive the graphic card。

- To view drive information (up-to-date every second):

```sh
$ nvidia-smi -L -1 
```

- VIEW KDE SYSTEM PARAMETERS:

![..gitbook/assets/nvi2.png]


- Open a movie with MPV, and you can see that there's a significant increase in the amount of use (I'm up from 3M to hundreds of gigatons) and can watch it with SMPlayer。

![.. ..gitbook/assets/nvi1.jpg]


