# Section 6.5 Audio player

# Audacious

Install Audacious

- install with pkg:

```sh
# pkg install audacious audacious-plugins
```

Note**
>
> __CODESPAN_0_ IS NOT INSTALLED, __CODESPAN_1_ MASTER PROGRAM CANNOT BE OPENED。

- Or install with Ports:

```sh
# cd /usr/ports/multimedia/audacious/ && make install clean
# cd /usr/ports/multimedia/audacious-plugins/ && make install clean
```

# With #

- TEST __CODESPAN_0 (DUBE AC-4 CODE), __CODESPAN_1 , __CODESPAN_2 __ (AVS2/AVS3 CODE) MUSIC:

Audacious only supports ___CODESPAN_0_, not __CODESPAN_1_, `.av3a`。

(.. . . . . . . . . . . . . . . . . . . 

VLC

For example, installation, see other sections. FreeBSD __CODESPAN_0_ Default encoding does not open support for libuavs3d (AVS2/AVS3). I don't know how。

VLC tested to play ac4 (m4a):

![.. .gitbook/assets/vlc3.png]

PLAY DSD WITH MPD

Music Player Daemon (MPD) is a flexible, powerful and scalable music player system that operates on a computer and is controlled by various clients. The main MPD functions include: support for various audio formats, client-server architecture, playlist management, support for streaming media, cross-platform support, etc。

Ready

SUPPORTS A SOUNDCARD OR DAC, A DSD AUDIO FILE。

The following is based on FreeBSD 14.0, external DACs using Heidelberg R3 (soundcard settings are basically similar) and using an ass drive。

# Install

```sh
# pkg install musicpd
```

Or..

```sh
# cd /usr/ports/audio/musicpd/
# make install clean
```

Hardware Settings

View soundcard information

```sh
# cat /dev/sndstat
pcm0: <Realtek ALC269 (Analog 2.0+HP/2.0)> (play/rec) default
pcm1: <Intel Cougar Point (HDMI/DP 8ch)> (play)
pcm2: <USB audio> (play)
No devices installed from userspace.
```

Here's the pcm2, the corresponding device file CODESPAN_0, which will be used below。

THE MEANING OF THE RELEVANT HARDWARE PARAMETERS CAN BE SEEN FROM __CODESPAN_0, WITH THE FOLLOWING THREE KEY EXTRACTS:

```sh
dev.pcm.2.bitperfect: bit-perfect playback/recording (0=disable, 1=enable)
dev.pcm.2.play.vchanrate: virtual channel mixing speed/rate
dev.pcm.2.play.vchanmode: vchan format/rate selection: 0=fixed, 1=passthrough, 2=adaptive
```

THE FOLLOWING SETTINGS (CAN WRITE TO __CODESPAN_0_PERMANENT SETTINGS):

```sh
# sysctl dev.pcm.2.bitperfect=1
# sysctl dev.pcm.2.play.vchanrate=352800
# sysctl dev.pcm.2.play.vchanmode=1
```

- because of the ass drive, muscipd only uses dop transfer mode, dop mode requires bitperfect
- Sample rate (vchanrate), DSD sampling rate is a multiple of 44.1khz, so do not set a multiple of 48khz or there will be noises, and if possible, the highest, in this case 352.8khz。
-0 (fixed): under this model, audio devices use fixed sampling rates and formats to process multiple audio streams. 1 (passthrough): in this mode, the audio device maintains, to the extent possible, the original sampling rate and format of the input audio stream. 2 (adaptive): in this mode, the audio device automatically adapts and converts the sampling rate and format of the audio stream as required。

>** Skills**
>
> Available sampling rates can be viewed with __CODESPAN_0_. When non-dsd files are played, it is appropriate to have the same (or integer) sampling rate for audio files as for audio files, so that the loss of the sound from re-sampling can be avoided. The sampling rate is not as high as possible and can be tried several times to find the best。

```sh
# dmesg|grep -i pcm2
pcm2 on uaudio0
# dmesg|grep -i uaudio0
uaudio0 on uhub0
uaudio0: <HiBy R3, class 239/2, rev 2.00/ff.ff, addr 1> on usbus1
uaudio0: Play[0]: 384000 Hz, 2 ch, 32-bit S-LE PCM format, 2x4ms buffer. (selected)
uaudio0: Play[0]: 352800 Hz, 2 ch, 32-bit S-LE PCM format, 2x4ms buffer.
uaudio0: Play[0]: 192000 Hz, 2 ch, 32-bit S-LE PCM format, 2x4ms buffer.
uaudio0: Play[0]: 176400 Hz, 2 ch, 32-bit S-LE PCM format, 2x4ms buffer.
uaudio0: Play[0]: 96000 Hz, 2 ch, 32-bit S-LE PCM format, 2x4ms buffer.
uaudio0: Play[0]: 88200 Hz, 2 ch, 32-bit S-LE PCM format, 2x4ms buffer.
uaudio0: Play[0]: 48000 Hz, 2 ch, 32-bit S-LE PCM format, 2x4ms buffer.
uaudio0: Play[0]: 44100 Hz, 2 ch, 32-bit S-LE PCM format, 2x4ms buffer.
uaudio0: Play[0]: 32000 Hz, 2 ch, 32-bit S-LE PCM format, 2x4ms buffer.
uaudio0: No recording.
uaudio0: No MIDI sequencer.
pcm2 on uaudio0
uaudio0: No HID volume keys found.
```

# # Basic Settings

musicpd profile is __CODESPAN_0_。

Some of the default directories inside are:

```ini
/var--> mpd --
               |-> music
               |-> .mpd --> playlists
```

These directories need to be built on their own

```sh
# mkdir -p /var/mpd/music
# mkdir -p /var/mpd/.mpd/playlists
# chown -R mpd:mpd /var/mpd
# chmod 777 /var/mpd/music
```

the third line sets the directory to the user mpd all, otherwise there may be a permission problem. the fourth line is used to store music files, setting 777 to facilitate the addition and deletion of files, so that you can set yourself up as appropriate。

Amend _`/usr/local/etc/musicpd.conf`, add a section after the section entitled "Default OS Security Services":

```ini
audio_output {
        type            "oss"
        name            "OSS Device（dop mode）"
        device          "/dev/dsp2"     # 指定使用的设备，不需要把 dac 或声卡等设置为默认设备，dsp2 专用于播放音乐，默认设备做自己的事就行
        dop             "yes"           # 开启 dop 模式
}
```

Note: Multiple output devices can be specified, and the specified output devices can be turned off on and off among various clients


enable musicpd service

```sh
# sysrc musicpd_enable=YES
# service musicpd start
```

# The client uses #

You can use ncmpc (character interface), MaximumMPD (iphone) and so on。

pc end GUI recommends canta (__CODESPAN_0_)

Command line suggests the installation of mpc(__CODESPAN_0_) suitable for binding the global shortcut for the desktop environment



