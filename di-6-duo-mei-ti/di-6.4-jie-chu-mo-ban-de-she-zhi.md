Section 6.4 Touchboard

FreeBSD supports i2c and USB touchboard by default。

# Turn off the touchboard

Find touchboard:

```sh
ykla@ykla-mi:~ $ xinput list
⎡ Virtual core pointer                    	id=2	[master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer              	id=4	[slave  pointer  (2)]
⎜   ↳ Windows pointer                         	id=6	[slave  pointer  (2)]
⎣ Virtual core keyboard                   	id=3	[master keyboard (2)]
    ↳ Virtual core XTEST keyboard             	id=5	[slave  keyboard (3)]
    ↳ Windows keyboard                        	id=7	[slave  keyboard (3)]
```

SEE __CODESPAN_0_ IS THE TOUCHBOARD, OFF: (LAST __CODESPAN_1_OPEN; __CODESPAN_2_ OFF)

```sh
ykla@ykla-mi:~ $ xinput set-prop 6 "Device Enabled" 0
```

References

- [FreeBSD possible off] (https://qiita.com/fygar256items/35100d43b096470631d6)

# Fn key settings


- [AdJusting acpi_video rights includes on FreeBSD] (https://www.davidschlachter.com/misc/freebsd-acpi_video-thinkpad-display-brightness)
