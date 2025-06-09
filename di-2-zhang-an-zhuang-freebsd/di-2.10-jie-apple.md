# Section 2.10 Install FreeBSD - Based on Apple M1 & VMware Fusion Pro

This document is based on MacOS 15.3.1, VMware Fusion Pro 13.6.2, FreeBSD 15.0, UEFI (default). Tested 14.2-RELEASE.

Note**
>
> If you use MacOS 14, there may be a failure that the keyboard cannot enter.

# Download FreeBSD

As Apple M1 is arm structure, please download a mirror with the words `aarch64 ' . ** Not ** Add `amd64'.

# Configure virtual machines

![.. .gitbook/assets/Fusion1.png]

Select the FreeBSD mirror to download.

![..gitbook/assets/Fusion2.png]

The default memory is too small. Click "Custom Settings"

![..gitbook/assets/Fusion3.png]

Click Processor and Memory

![..gitbook/assets/Fusion4.png]

Modifys the number of processors memory size. `4096MB ' is 4G.

# Start installation

![.. .gitbook/assets/Fusion5.png]

![..gitbook/assets/Fusion6.png]


# Configure the desktop

No virtual machine enhancement tool is required.

![..gitbook/assets/Fusion7.png]

![..gitbook/assets/Fusion8.png]

![..gitbook/assets/Fusion9.png]

The desktop cannot pull.

# Fragmentation and unfinished business

# Solve the problem of not moving the mouse #

Edit `/boot/loader.conf ' , add:

```sh '
You know, hw.usb.usbhid.enable=1
"YES."
````

Yeah.

References

- [Mouse does not work in VMWARE Fusion and Freebsd 142] (https://forums.freebsd.org/threads/mouse-does-not-work-in-vmware-fusion-and-freebsd-14-2-966563)
