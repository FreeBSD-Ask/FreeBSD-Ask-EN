# Section 6.5 Audio player

# Audacious

Install Audacious

- Install with pkg:

```sh '
# Pkg install auspicious #
````

Note**
>
> Unable to open the `Audacious ' master without `audious-plugins ' .

- Or install with Ports:

```sh '
#cd /usr/ports/multimedia/audacious/ & make important
#cd /usr/ports/multimedia/audacious-plugins/ & make install clean
````

# With #

- Test of `.m4a` (Dube AC-4 code), `.flac ' , `.av3a ' (AVS2/AVS3 code) music:

Audacioous supports only `.flac ' and not `.m4a ' , `.av3a ' .

(.. . . . . . . . . . . . . . . . . . . .

VLC

For example, installation, see other sections. FreeBSD `ffmpeg ' default code did not open support for libuavs3d (AVS2/AVS3). I don't know how.

VLC tested to play ac4 (m4a):

![.. .gitbook/assets/vlc3.png]

Play DSD with MPD

Music Player Daemon (MPD) is a flexible, powerful and scalable music player system that operates on a computer and is controlled by various clients. The main MPD functions include: support for various audio formats, client-server architecture, playlist management, support for streaming media, cross-platform support, etc.

Ready

Supports a soundcard or DAC, a DSD audio file.

The following is based on FreeBSD 14.0, external DACs using Heidelberg R3 (soundcard settings are basically similar) and using an ass drive.

# Install

```sh '
# pkg install musicpd
````

Or...

```sh '
#cd/usr/ports/udio/musicpd/
# Make install clean
````

Hardware Settings

View soundcard information

```sh '
#cat /dev/sndstat
pcm0: <realtek ALC269 (Analog 2.0+HP/2.0)> (play/rec)
pcm1: <Intel Couga Point (HDMI/DP 8ch)> (play)
pcm2: < USB audio> (play)
No deviations incorporated from usersspace.
````

This is pcm 2, the corresponding equipment file `/dev/dsp2 ' , which will be used below.

The meaning of the relevant hardware parameters can be seen in `sysctl-d dev.pcm.2 ' , with the following three key extracts:

```sh '
dev.pcm.2.bitperfect: bit-perfect playback/recording (0=disable, 1=enable)
dev.pcm.2. Play.vchanrate: virtual channel mixing
dev.pcm.2.play.vchanmode: vchan format/rate self-section: 0=fixed, 1=passthrough, 2=adaptive
````

The following settings (can write to `syscl.conf 'permanent settings):

```sh '
# syscldev.pcm2.bitperfect=1
# syscl dev.pcm2.play.vchanrate=352,800
# syscl dev.pcm2.play.vchanmode=1
````

- Because of the ass drive, muscipd only uses dop transfer mode, dop mode requires bitperfect
- Sample rate (vchanrate), DSD sampling rate is a multiple of 44.1khz, so do not set a multiple of 48khz or there will be noises, and if possible, the highest, in this case 352.8khz.
-0 (fixed): Under this model, audio devices use fixed sampling rates and formats to process multiple audio streams. 1 (passthrough): In this mode, the audio device maintains, to the extent possible, the original sampling rate and format of the input audio stream. 2 (adaptive): In this mode, the audio device automatically adapts and converts the sampling rate and format of the audio stream as required.

>** Skills**
>
> Available sampling rates can be viewed in `dmesg ' . When non-dsd files are played, it is appropriate to have the same (or integer) sampling rate for audio files as for audio files, so that the loss of the sound from re-sampling can be avoided. The sampling rate is not as high as possible and can be tried several times to find the best.

```sh '
♪ Dmesg grep-i pct2
P and 2 on uaudio0
♪ I don't know ♪
uudio0 on uhub0
uudio0: <Hiby R3, class 239/2, rev 2.00/ff.ff, addr 1 > on usbus1
uudio0: Play[0]: 384000 Hz, 2 c, 32-bit S-LE PCM format, 2x4ms buffer. (selected)
uudio0: Play[0]: 352,800 Hz, 2 c, 32-bit S-LE PCM format, 2x4ms buffer.
uudio0: Play[0]: 192000 Hz, 2 c, 32-bit S-LE PCM format, 2x4ms buffer.
uudio0: Play[0]: 176400 Hz, 2 c, 32-bit S-LE PCM format, 2x4ms buffer.
uudio0: Play[0]: 96,000 Hz, 2 c, 32-bit S-LE PCM format, 2x4ms buffer.
uudio0: Play[0]: 88200 Hz, 2 c, 32-bit S-LE PCM format, 2x4ms buffer.
uudio0: Play[0]: 48,000 Hz, 2 c, 32-bit S-LE PCM format, 2x4ms buffer.
uudio0: Play[0]: 44100 Hz, 2 c, 32-bit S-LE PCM format, 2x4ms buffer.
uudio0: Play[0]: 32000 Hz, 2 c, 32-bit S-LE PCM format, 2x4ms buffer.
No reporting.
No MIDI security.
P and 2 on uaudio0
No HID volume keys found.
````

# # Basic Settings

musicpd profile is `/usr/local/etc/ musicpd.conf '.

Some of the default directories inside are:

```ini '
/var-- mpd--
Mosic
.mpd-
````

These directories need to be built on their own.

```sh '
#mkdir-p/var/mpd/music
#mkdir-p / var/mpd/.mpd/playlists
# Down-R mpd:mpd/var/mpd
#chmod777/var/mpd/music
````

The third line sets the directory to the user mpd all, otherwise there may be a permission problem. The fourth line is used to store music files, setting 777 to facilitate the addition and deletion of files, so that you can set yourself up as appropriate.

Amend the section `/usr/local/etc/musicpd.conf ' to add a section after the section "Default OSS Device " :

```ini '
Audio_output
type "oss"
Name "OSS Data"
Design "/dev/dsp2" # specified devices do not need to set dac or soundcards as default devices, dsp2 for music, and default devices do their own things
Dop "yes" # Open dop mode
♪ I'm sorry ♪
````

Note: Multiple output devices can be specified, and the specified output devices can be turned off on and off among various clients


Enable musicpd service

```sh '
# Sysrc musicpd_enable
# With service music started
````

# The client uses #

You can use ncmpc (character interface), MaximumMPD (iphone) and so on.

pc end GUI recommends cantata (`pkg install cantata ')

Command line suggests the installation of mpc (`pkg install musicpc '), suitable for binding the global shortcut for the desktop environment



