Section 6.1 Sound cards

# Sound Settings

soundcard drive snd_hda default is loaded. the default kernel does not contain the corresponding kernel module manually loaded。

View the current soundcard device with the following command:

```sh
$ cat /dev/sndstat
Installed devices:
pcm0: <NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm1: <NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm2: <NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm3: <NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm4: <Realtek ALC892 (Rear Analog 5.1/2.0)> (play/rec) default
pcm5: <Realtek ALC892 (Front Analog)> (play/rec)
pcm6: <Realtek ALC892 (Rear Digital)> (play)
No devices installed from userspace.
```

behind is the default device with default is the ass. if the software's audio is used and the output is default, the audio is exported from this device。

FreeBSD most of the software is audio output driven by ass. Some defaults are pulseaudio (e.g. firefox) and these software settings look at the last hint。

the following commands modify the output device. the last number is the corresponding pcm back。

```sh
$ sysctl hw.snd.default_unit=5
```

os mixer:

| GUI ENVIRONMENT | Name |
| :------: | :-------------: |
| kde5 | audio/dsbmixer |
| gtk | audio/gtk-mixer |
| Non Graphical | audio/mixertui |

# Fault removal and unfinished business

Some sound cards need to be self-compiled for reference [Open Sound System for FreeBSD] (http://www.opensund.com/freebsd.html)。

But ass has some disadvantages, using __CODESPAN_0_can't record ass output. Record only ass input. In the official forum, you can simulate a device。

But __CODESPAN_0_can record the sound of the pulseadio output。

so some software can use pulseadio as an output. audio output of software using pulseudio controls the audio output device without commands above. pulseudio will send audio to the corresponding device according to its own settings, so it needs to be controlled by a pulseudio mixer。

in kde5, the audio controller below the belt, the switch is controlled pulseudio。

some of the officially packaged multimedia software supports pulseaudio, but most of the corresponding compilation options for these software are not open. if you need an audio output of the recording software, you can open the ports compile options for yourself. set pulseudio in the software as an audio drive output on it。

