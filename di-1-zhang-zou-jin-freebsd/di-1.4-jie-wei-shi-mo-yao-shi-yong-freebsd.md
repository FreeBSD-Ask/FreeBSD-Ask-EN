# Section 1.4 Why use FreeBSD?


# The reason for choosing FreeBSD # # FreeBSD can look for the right middle of a changing world

- ** FreeBSD can look for the right middle of a changing world**

If you want to choose one that's the same as Windows, Android, and that doesn't affect the day-to-day system with a big update, instead of fighting the system every day, FreeBSD is trustworthy.

The vast majority, or almost all, of Linux ' s configurations and system components are ** changing **, particularly when there are large variations. And Linux is still in the middle of a destructive change.

CentOS, Debian is just ** within the life cycle**, but there is no consistency or stability in the large version. And because ** has not changed for a long time**, the large version** has changed** and will only become more eccentric and unmoveable**. And since Linux has never been designed to distinguish between basic systems and third-party user software, the cost of such systems** remains constant throughout the life cycle** is that no software version will change, change or change.

This means:

1. If you need to keep up to date the software version or the development of your work. So you're almost always dealing with failures associated with operating systems, not focusing on your own development or services or solving your own practical problems.

You're fighting the system almost every day to fix this hard-on hammer because he's always taking off. Instead of really nailing it. It's only because of Systemd that Bug can't be finished for many lifetimes, and you basically don't have to work every day, and you're fighting with these things.

2 Unless your Linux environment has never been upgraded or replaced with a patch, because the means of production and the environment are fixed and non-changed and do not want to be updated or have no reason to spend money, the upgrading and upgrading are simply abandoned. In fact, most Linux was used before. So there seems to be no problem. But there are huge security risks and common failure points. And sooner or later you'll have to upgrade unless you're broke. It's just a matter of time. But because you chose Linux, it would be impossible to upgrade, and almost all the configurations and dependencies are changing, even non-existent, and it is common to change, only to start over. Your stability will no longer exist.

Even if you ** don't want to change,** those unskilled people and the whole market will force you to change,** you'll have to change.** For example, can you still use your Flash now?

# Common reason for choosing FreeBSD

- ** You like to use it, you don't. It's too long to look at it, no? Repeat this entry**
- In Buddhists, because of fate. There is no place for all things, and there is no place for us to meet, and there is no place for them. All kinds of people.
- Christianly, it's the Lord's guidance. God is born in this eternal present. You look like you're making your own choice, and you're actually the main arrangement.
- From Hegel, it's a rebuttal. FreeBSD is a direct descendant of UNIX, and Linux is just a simulator, and many of the agreements were born to UNIX, so you were destined to come here.
- From my point of view, the search for stability and innovation in the software requires both a binary source and the ability to compile and install. I could not find Linux systems except FreeBSD. (~VoidLinux? ~)
- BSD III authorization agreements: free distribution allowed. GPL and BSD agreements, what is real freedom? The GPL, at best, ensures his freedom by limiting it. Learning BSD, like learning philosophy, is not about learning for a certain precise knowledge per se, but about learning for freedom (since most people see BSD as no longer having so-called practical value). So at this point, it can be said that, in their view, BSD is fundamentally different from other operating systems -- that BSD is really free.
- FreeBSD is an open source of practice from the College and a committed practitioner of UNIX philosophy.
- The Linux release, which is far from fragmentation, frees users of difficult choices from suffering.
- BSD is a complete OS, not a kernel. The kernel and basic systems are maintained as a whole as a project. This is what's wrong with all Linux systems. The absence of the concept and distinction of a de facto basic system could result in a series of intuitive violations.
- The Linux community has become a dirty muddy, both kernel development and user group. - See literary stories.

# Technical reasons for choosing FreeBSD

- The basic system profile is separated from the third-party software profile. You don't encounter such strange things as the use of rpm commands to unload glibc, leading to the destruction of the system. FreeBSD's package manager does not interfere with the basic system.
- Not locking down software versions, such as the software that Linux relies on. All software will be rolled up. These non-rolled versions of the linux software are basically locked to death on that version and will not be updated with any functional versions. The scrolling version has another set of stability problems. All BSD versions share a single port, only a very small part of the software and the system version is bound hard, and the rest can be rolled up. Moreover, because of the existence of the basic system, third-party software hardly affects the stability of the system. Linux cannot find a balance between software upgrades and system stability.
- Document is complete, FreeBSD doc is equal to src, regardless of height.
- There are fewer security holes than Linux.
- Common failure points in products and structures can be avoided.
- Almost 2-year release cycle, 4-year maintenance cycle that gives FreeBSD stability.
- Through BSD Ports, you can compile and install software and freely configure it.
- ZFS file system can be configured as `\ partition. ZFS is hailed as the most powerful file system.
- Jail and byhve virtualization, without the need to deploy bottom virtualization and save system resources.
- Traditional BSD INIT guides you from stymd persecution.
- DTrace frame and GEOM storage frame.
- Linux Binary Compatibility Layer, which runs Linux software as long as it supports CentOS or Ubuntu/Debian. And the software runs faster than Linux.
- Audit of security incidents.
- Unlike the Linux-drived kernel, the FreeBSD-drive is largely linked to kernel decomposition.
- Linux kernel development is a pretty closed process. (https://www.kernel.org/doc/html/latest/proceeding/submitting-tches.html), with only a few people able to participate in direct submission. FreeBSD, in keeping with the idea of free development for all, is currently [you can submit your code directly on Github] (https://github.com/freebsd/freebsd-src/pulls) or a registered account number at <https://reviews.freebsd.org/> to make a large-scale change.
See also [Linux kernel coding style] (https://www.kernel.org/doc/html/latest/process/coding-style.html). FreeBSD, on the other hand, has a code style used in Kernighan & Ritchie 's C program design language.
- As a result of Ports, FreeBSD's old system source is still in service, instead of the same as Linux once EoL has no software source available.

References

- [Submitting GitHub Pull Reviews to FreeBSD] (https://freebsdfoundation.org/our-work/journal/browser-based-edition/configration-development-2/submitting-github-pull-requests-to-freebsd/), translated into FreeBSD on [GitHub] (https://github.com/taophilosophy/freebsd-journal-cn/blob/main/2024-05/zai-github-shang-xiang-freebsd-ti-jiao.md)
- [Contributions Guidings for GitHub] (https://github.com/freebsd/freebsd-src/blob/main/CONTRIBUTTING.md)


# Choose the social meaning of FreeBSD

# GNU and Open Source Campaign has come to an end

- Linux Kernel is decided by Linus alone: “[Linus Torvalds] is the final adjudicator who decides whether to change access to the Linux kernel. ] (https://www.kernel.org/doc/html/latest/translations/zh_CN/process/submitting-pacters.html)” and FreeBSD is ultimately decided collectively by a two-year core team.


>** Thinking issues**
>
> Evidently: The current absence of desktop parts on FreeBSD is due in large part to their over-reliance on Linux-specific function libraries, such as the `iproute2 ' package containing `ip ' commands. More reason is that these desktops or components and systemd are tied in depth or are forced to rely at all, such as `NetworkManager ' . And Samba developers say, "We use Linux, we develop for Linux, all others please subtches." People in the FreeBSD community call it “Linuxism/Linux Discrimination”, and you will see this word again in the links quoted in the literary chapter, and some people are proud of it.
。>
We have no idea what the consequences of such behaviour are, but there are more and more such procedures, and there is a tendency to become mainstream, and even most developers do not consider compatibility in the development of programs, such as `todesk ' . Even Java lost his portability. Why didn't Eclipse on FreeBSD update for almost two years? This is precisely because of such [bundling problems] (https://git.eclipse.org/r/c/platform/eclipse.platform.swt/+/163641). `systemmd-boot ' has even recently replaced `grub2 ' , and Linux will be unified for the foreseeable future. The program (which is expected to run on Linux) no longer has any portability.
>
Maybe Linux's open source is at the end. "You can continue to build your wheels, but you can't run any program if you don't comply with my system." Now FreeBSD faces this dilemma, and it will be for everyone.
>
The fact that Linux has completely turned his back on the philosophy and ideas from which he started is beyond doubt.
>
Is that true? What do you think?

- FreeBSD is chosen to keep a fire seed after Linux is controlled by the systemmd and the business company behind it. Large operating systems, capable of replacement, have only FreeBSD operating systems.
- FreeBSD is chosen to retain the next truly open operating system. It can keep the open-source business going and practice the true UNIX philosophy, not to take the wrong path and close the road.

(https://freebsdfoundation.blogspot.com/2014/11/freebsd-foundation-announces-general.html)


Last week, I donated $1 million to the FreeBSD Foundation, which supports the Open Source Operating System FreeBSD. FreeBSD helped millions of programmers follow their passions and get creative. I am the beneficiary. In the late 1990s, I started using FreeBSD, when I was in financial straits and living in government-provided housing. In a way, FreeBSD helped me out of poverty -- the important reason I can get into Yahoo! The reason they use FreeBSD, which is my preferred operating system. Years later, when Brian and I started creating whatsApp, we still used FreeBSD to support our server operation, and so today.
>
I've published this donation in the hope that more people will see the useful work done by the FreeBSD Foundation and inspire others to support FreeBSD. We will all benefit if FreeBSD can continue to provide opportunities for people like me to lift more migrant children out of poverty and help more start-ups to create successful, if not transformative, results.
>
> _whatsApp Original CEO and founder Jan Koum

In fact, this is not a hammer, and [2020] (https://freebsdfoundation.org/our-donors/donors/?donationYear=2018), [2019] (https://freebsdfoundation.org/our-donors/donors/?donationYear=2019), [2020] (https://freebsdfoundation.org/our-donors/donors/?donaryyear=2018) and (https://freebsdfoundation.org/donors/donors/?donors??donationYear=2020year=20202020year=20year=20year=2018yearyear=2018), [20.[2022] Contributions of more than $250,000 per year.

# Honest and credible #

A system like FreeBSD that works quietly backstage to be forgotten by its users may well be an antique, and if there are a few blue screen errors every day, Kernel Panic, or an “internal error”, `You are in emergency mode', `BusyBox (initramfs)', `grub recue', etc., reminds users of their existence. Isn't it? Those windows, the 3Q war, the scrumptious ads, the 100-degree pedestals and the national operating system, the anti-fraud software from Green Dames to Andre's mobile phone, have been successful.

Most of the companies currently using Linux as a dedicated equipment operating system, or building their own commercial products on the basis of other GPL software, do not comply strictly with the GPL protocol to issue their codes. And for domestic companies, they don't even know what the GPL is, they just think it's free. The products of companies that are forced to open the GPL are not worth using. There have also been incidents of the retrofitting of open source software brands. By comparison, companies using FreeBSD are at least more honest, reliable and trustworthy. And it really makes the BSD code for people — even if one thinks that FreeBSD has fallen west of the Sun — despite the fact that these people have lived under the light of FreeBSD.

References

Wang Bo FreeBSD's Future in China. Quoted from FreeBSD 2nd edition, Mechanical Industry Press, 2002, ISBN 9787111102861


# I know more

- There is an official version of the Foundation, see [Why You Should Use FreeBSD] (https://book.bsdcn.org/fan-yi-wen-zhang-cun-dang/2024-nian-11-yu/why).
- The real motivation behind [systemd] (https://freebsd.gitbook.io/translated-articles/the-real-motization-behind-systemd)
- [systemd is not safe anywhere] (https://freebsd.gitbook.io/translated-articles/systemd-isnt-safe-to-run-anywhere)
- [GPL] (https://freebsd.gitbook.io/translated-articles/the-problems-with-the-gpl)
- [Why should you move everything from Linux to BSD] (https://freebsd.gitbook.io/translated-articles/why-you-should-migrate-every-from-linux-to-bsd)
- [New Ports Submitter: Oel Bodenmann (jbo@freebsd.org)] (https://book.bsdcn.org/freebsd-za-zhi-jian-zhong-wen-ban/2023-1112/xin-de-port-ti-jiao-zhe-oel-bodenmann-jboreebsd.org)
