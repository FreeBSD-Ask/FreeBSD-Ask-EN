Section 6.1 Sound cards

# Sound Settings

soundcard drive snd_hda default is loaded. The default kernel does not contain the corresponding kernel module manually loaded.

View the current soundcard device with the following command:

```sh '
$cat /dev/sndstat
Installed papers:
pcm 0: < NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm1: < NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm2: < NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm 3: < NVIDIA (0x0083) (HDMI/DP 8ch)> (play)
pcm 4: < Realtek ALC892 (Rear Analog 5.1/2.0)> (play/rec)
pcm 5: <realtek ALC892 (Front Analog)> (play/rec)
p.c. 6: <realtek ALC892 (Rear Digital)> (play)
No deviations incorporated from usersspace.
````

Behind is the default device with default is the ass. If the software's audio is used and the output is default, the audio is exported from this device.

FreeBSD most of the software is audio output driven by ass. Some defaults are pulseaudio (e.g. firefox) and these software settings look at the last hint.

The following commands modify the output device. The last number is the corresponding pcm back.

```sh '
$ sysctl hw.snd.default_unit=5
````

OS MIXER:

|GUI Environment
|: -: | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | : | | | | | | | | | | | | | | : | | | | | | | | | | | | | | | | | | | |
|kde5
Gtk
| Non-graphic audio/mixertui

# Fault removal and unfinished business

Some sound cards need to be self-compiled for reference [Open Sound System for FreeBSD] (http://www.opensund.com/freebsd.html).

But ass has some shortcomings, using `obs-studio ' cannot record ass output. Record only ass input. It is possible to simulate a device in an official forum.

However `obs-studio ' can record the sound of the pulseudio output.

So some software can use pulseadio as an output. Audio output of software using pulseudio controls the audio output device without commands above. Pulseudio will send audio to the corresponding device according to its own settings, so it needs to be controlled by a pulseudio mixer.

In kde5, the audio controller below the belt, the switch is controlled pulseudio.

Some of the officially packaged multimedia software supports pulseaudio, but most of the corresponding compilation options for these software are not open. If you need an audio output of the recording software, you can open the ports compile options for yourself. Set pulseudio in the software as an audio drive output on it.

。