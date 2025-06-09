# Section 6.2 Bluetooth

A webcard driven by iwm can install `comms/iwmbt-firmware` to drive bluetooth:

- install with pkg:

```sh
# pkg install iwmbt-firmware
```

- Install with Ports:

```sh
# cd /usr/ports/comms/iwmbt-firmware/ 
# make install clean
```

---|---

BLUETOOTH FOLLOWS THE USB BUS, USING __CODESPAN_0, AND CAN VIEW ALL EQUIPMENT, INCLUDING BLUETOOTH, E.G. __CODESPAN_1 -- IS BLUETOOTH, AND __CODESPAN_2_。

# The Wireless Bluetooth Mouse Settings

This is based on FreeBSD 13.0, Rotte m337。

```sh
# service hcsecd enable
# service bthidd enable
# service hcsecd start
# service bthidd start
```

ADD BLUETOOTH DEVICES USING __CODESPAN_0_。

BLUETOOTH MOUSE TO MATCH MODE, RUNNING __CODESPAN_0_, ADDING WITH HINT INFORMATION:

```sh
#  bluetooth-config scan
Scanning for new Bluetooth devices (Attempt 1 of 5) ... done.
Found 1 new bluetooth device (now scanning for names):
[ 1] 34:88:5d:12:34:56  "Bluetooth Mouse M336/M337/M535" (Logitech-M337)
Select device to pair with [1, or 0 to rescan]: 1

This protections humans interface services.
Set it up
````

# Fragmentation and unfinished business

- the logitech m337 pair will automatically be disconnected。

SOLUTION: DELETE ___ CODESPAN_0 FROM __ CODESPAN_1_LINE __ CODESPAN_2__. RESTART __CODESPAN_3_SERVICE_CODESPAN_4_。


