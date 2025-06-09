# Section 3.1 FreeBSD mirror station status

Status

the main problem is that rsync is not officially open in any way and that it does not accept the official secondary mirror application for the mirror station。

According to the information currently available, the FreeBSD project ceased public disclosure by May 2015. [Adds are not available public imrors of packages and possible works.] (https://reviews.freebsd.org/R9:3418e47d2f6cd8d04ac934f38d136ba910105a8). The reasons given were:

{\cHFFFFFF}{\cH00FFFF}{\cH00FF00} Due to very high requirements of bandwidth, stage and acceptance of the FreeBSD; Project has developed not to allow public imrors of packages.
>
>The FreeBSD project decided not to allow public mirror packages due to the high bandwidth, storage and management requirements。

That's a reason for not knowing。

---|---

2025 Replies received:

On Fri, 28 Feb 2025, at 17:45, ykla wrong:
How to Mirror pkg and update from official Mirror sites?
>
As we returned on special occasions before: pkg and freebsd-update need Machines under our control with internet compliance to the rest of our system.
>
That then turned into a voluntary mine and the conversion went nowhere.

Translation:

friday, 28 february 2025, at 17:45, ykla wrote:
how can pkg mirrors and system updates be made through official mirror sites
>
>as we have responded many times before: pkg and freebsd-update functions need to be supported by physical servers under our control (** note: here the other side points to root privileges**) and these servers need to be networked with our clusters。
>
A proposal to provide a Nanjing machine was made earlier, but discussions stalled after the successor programme was changed to virtual. We cannot use virtual machine programmes and need real hardware (** note: each other points to naked metals**), physical storage media and physical network transmission links。

---|---

There are currently no FreeBSD official mirror stations in mainland China。

Repeated contacts, such as mailing lists, did not occur twice, approximately five times, of which three responded and two did not. Its main response is “Expressed regret, but the Taiwan region already has a mirror”. In addition to the fact that there is no direct indication of how to mirror the image, and in particular to the Linux Users Association of the Chinese University of Science and Technology (of which other mirror stations, such as the TUNA Association of Tsinghua University, did not address it), it was mentioned that FreeBSD was also unresponsive。

This is the case in the domestic network environment, where a proxy approach to speed-up is essential, but it is the core imperative for the development of FreeBSD that no one can be required to have the same level of access to easy and accessible network services. Attention is drawn to the fact that mirror stations are infrastructure, as it says, “If you want to be rich, fix the road”, and if the roads to FreeBSD are not accessible, they are all thorny. Here is a call to reach out to the official friends of FreeBSD and first to solve this fundamental problem。

open unofficial assue mirror application:

USTC:

- <https://github.com/ustclug/mirrorrequest/issues/172>
<https://github.com/ustclug/mirrorrequest/issues171>

unofficial issue mirror application currently closed:

TUNA: <https://github.com/tuna/issues/issues/16>

# The official mirror basics

- the root privileges of the server, which are not granted by the open-source mirror station in the country
- IPv6 and CN2 networks, which are also lacking in the country
- BGP NETWORK
- SUFFICIENT STORAGE SPACE (APPROXIMATELY 50 TB) AND 1G BANDWIDTH
- The above five computers。
- Documentation issues — specialized companies/social organizations are required to file cn.FreeBSD.org
- The biggest problem, no money

Details can be seen:

- Single mirrors: <https://wiki.freebsd.org/Teams/clusteradm/tiny-mirror>
- Complete mirror: <https://wiki.freebsd.org/Teams/clusteradm/generic-mirror-layout>

# Unofficial mirror station

FreeBSD does not have official mirror stations in mainland China; there are official mirror stations in Taiwan, China。

FreeBSD currently has a number of unofficial mirror stations in the mainland:

- USTC (pkg ports only) <https://mirrors.ustc.edu.cn>
- <https://mirror.bjtu.edu.cn> contact: <https://t.me/bjtumiror>
- net 163 mirror stations (ports pkg only)
- Open Source Mirror Station, Nanjing University: no effective contact, no responsible person。

FreeBSD official contact:

- [@FreeBSD.org] (mailto:miror-admin@FreeBSD.org)
- [freebsd-hubs@freebsd.org] (mailto: freebsd-hubs@freebsd.org), this mailing list appears to be dead and no one has responded and sent mail。
