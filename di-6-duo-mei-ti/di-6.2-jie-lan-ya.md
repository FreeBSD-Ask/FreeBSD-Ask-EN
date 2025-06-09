# Section 6.2 Bluetooth

An iwm-driven webcard can install `comms/ iwmbt-firmware ' to drive Bluetooth:

- Install with pkg:

```sh '
# Pkg install iwmbt-firmware
````

- Install with Ports:

```sh '
#cd/usr/ports/comms/iwmbt-firmware/
# Make install clean
````

I don't...

Bluetooth follows the USB bus, using `usbconfig ' to view all equipment, including bluetooth, e.g. `gen 1.5 ' is bluetooth, iwmbtfw -d gen 1.5 ' .

# The Wireless Bluetooth Mouse Settings

This is based on FreeBSD 13.0, Rotte m337.

```sh '
# With service hcsed available
# With service bound enough
# Service hcsecd start
# For service bthidd start
````

Use the `bluetooth-config ' tool to add bluetooth devices.

Bluetooth mouse to pair mode, running `#bluetooth-config scan ' , adding with hint information:

```sh '
# Bluetooth-config scan
Scanning for new Bluetooth studies
Found 1 new bluetooth data (now scanning for names):
[1] 34:88:5d:12:34:56 "Bruetooth Mouse M337/M535" (Logitech-M337)
Secrecy deviation with [1, or 0 to restcan]:

This protections humans interface services.
Set it up?
````

# Fragmentation and unfinished business

- The logitech m337 pair will automatically be disconnected.

Solutions: Delete `bd_addr ' row `xx:xx:xx:xx:xx:xx:xx ' in `/var/db/bthidd.hids '. Restart 'bthidd 'service '#service bthidd restart '.


。