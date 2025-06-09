# Section 1.1 Course of operating system: UNIX, Unix-like, Linux & FreeBSD

# What's UNIX?

Previously, UNIX was an operating system. The final result is a C-language rewrite. — Bell Laboratories from `AT&T' (American Telephone & Telegraph, United States Telegraph).

It is now a standard norm**, a paragraph** legal trademark**. ** Philosophy,** a software engineering principle. **

I don't...

Check the registration of UNIX trademarks at the United States Patent and Trademark Office:

(.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

I don't...

UNIX Authentication Query Web site: [The Open Group of United Nations Office on Drugs and Crime] (http://www.opengroup.org/openbrand/register)

[The Open Group of Financial Authorities]


Now, we can know that authentication UNIX needs:

1. [Subject to a single UNIX norm] (https://www.opennggroup.org/openbrand/register/xym0.htm)
Payment certification


As you can see, often, the certified UNIX operating system has Apple MacOS. That is, from a trademark point of view, MacOS can be called a standard UNIX operating system. {\i1 \cH30D3F4}So, the man who installed UNIX can go to the black apple

>** Skills**
>
>macOS/iOS et al. relation to BSD
>
>MacOS/iOS based on BSD is clear from history and reality, but not entirely based on a section BSD:macOS/iOS should be understood as an independent BSD operating system - the same as OpenBSD, NetBSD and FreeBSD. See (https://book.bsdcn.org/fan-yi-wen-zhang-cun-dang/2024-nian-11-yue/apple)
>
>So it seems to be a fight between Andre and Apple, but it is a fight between Linux and BSD. > {\i1 \cH30D3F4}Maybe it's the cathedral and the market. {\i1 \cH30D3F4}


## # UNIX Introduction to philosophy and software engineering principles

### # traditional Unix philosophy (with UNIX programming art at its core)

>** Thinking issues**
>
Those who do not understand Unix are destined to recreate it, poor.
>
> > [Henry Spencer] (https://www.nasa.gov/history/alsj/henry.html)
>
>author Henry Spencer does not explicitly criticize which operating system, so you think this is more appropriate for which common operating system? Why?

The Unix philosophy is derived from the development of the UNIX operating system by Ken Thompson. Unix Philosophy says, "Keep it simple, stupid":


- Xiaomei.
- A program only does one thing.
- Prototype first.
- Portability before efficiency
- No binary.
- Silence is gold.
- Avoid only user interfaces (avoid no command line, only GUI)

References

UNIX Programming Arts, Eric Raymond, ISBN: 9787121176654, Electronic Industry Press.
- Linux/Unix Design Thoughts, Mike Gancarz, 9787115266927, People's Post and Telecommunications Press. (Expressed)
- [The Open Group Standards Products] (https://www.opengroup.org/standardprocess/certification.html)

# A quarter of the twenty-first century Unix Philosophy

Technology has proved to be fast becoming obsolete. That's why many people today think it's pointless to talk about Unix, about Unix philosophy. Because they're really out of date, and the simpleness of Unix philosophy is reduced to purely technical, which is the biggest misreading of Unix philosophy. It is also the driving force behind the difficult path of the philosophy of suffering.

The true Unix philosophy is by no means the ancestral law of the old-fashioned above. The essence of the Unix philosophy is people-centred, and the true Unix philosophy is a humanism. In different times, Unix philosophy should be interpreted differently, but in the final analysis it is a humanitarian — we want to promote the human subjectivity. Unix was born for fun, for space travel, and Linux was created for “Just For Fun”: it is self-evident that it is to adapt computers to people, not to force people to adapt to so-called computer rules, and to blow up badly designed ideas.

The path to Jane is reflected in the Western philosophy of Okham's razor, which is “no more entities, if not necessary”. This, to a certain extent, also inspires the idea of the phenomenon, and we should exclude from our minds some self-made ideas, leaving only what we can feel directly — that is, back to the thing itself.

We now go back to the operating system itself, to the computer itself, which should not be an additional burden, but should serve people — like FreeBSD's slogan “The Power to Service”.

Therefore, the modern Unix philosophy should not be “avoiding only the user interface”, but rather “avoiding only the command line”. Each procedure should report on its own operational progress, preferably with a progress note (whether or not it really represents progress) and the use of parameters to silence the above-mentioned behaviour, but acquiescence should not be called silence as gold — how many times do you yearn to see a progress note instead of nothing, even if the card is dead? ChatGPT is undoubtedly the biggest rebellion against "small or fair" and "one program only one thing." People need what they need.

# Unix's history

# Mutlics #

The MTSS, introduced by MIT in 1964, was the most creative operating system at the time, with an efficient CTSS, and MIT researchers decided to make a better version. They started designing Multics. Mutlics means multi-road reuse information and computing services.

Multics, which aims to create strong new software and new hardware that is more powerful than shoulder IBM 7094, invited two companies to help. General Electric of the United States is responsible for the design and production of computers with brand-new hardware characteristics that can better support time and multi-user systems, and since Bell Laboratory developed its own operating systems early in computer development, MIT invited Bell Laboratory to develop Multics in conjunction with General Electric of the United States.

Ultimately, the development of Multics was in jeopardy, and Multics designed a lot of programs and functions, often stuffing in a lot of different things, making the system too complex. In 1969, because it was considered to be an information-processing tool at the Bell Laboratory, it was no longer able to provide the laboratory with the objective of computing services, and its design was too expensive. In April of the same year, the Bell Laboratory withdrew from the Multitics project, leaving MIT and General Electric of the United States for further development.

# # UNICS #

After Bell Laboratories withdrew from the Multics development project, the project member Kenneth Lane Thompson found a CDC PDP-7 computer, which was not very powerful, had only 4KB memory, but had a nice graphic interface, Thompson used him to write a game *Space Travel* (Stellar Travel), and PDP-7 had a problem with disk rotation far below the rate of computer reading and writing, and in order to solve that problem Thompson wrote disk scheduling algorithms to increase the total disk throughput.

>** Skills**
>
>Stellar Travel has been transplanted and can now be played directly on the web site where the project is located [Cport of Ken Thompson's Space Travel] (https://github.com/mohd-akram/st) and on-line at [Space Travel] (https://akr.am/st/).
>
{\i1 \cH30D3F4}It's simple, but I don't know how to play

How do you test this new algorithm? To load data on disk, Thompson needs to write a batch-writing program.

He needs to write three programs, one every week: an editor who creates the code, converts the code to a machine language compiler that can run the PDP-7, and adds " Outer kernel — the operating system is complete."

When the new PDP-7 operating system was not developed much, Thompson discussed it with several colleagues, when the new system had no name and was named “UniclS” (United Information and Communications, non-renewal information and computer services), which was finally changed to **UNIX**, which is more easily remembered.


# What's Unix-like?

Unix-like is class Unix, i.e. all operating systems that meet UNIX standards, are generally compliant with POSIX norms and are not certified as UNIX as described in section I.

In other words, except Windows, most of the world ' s operating systems are basically called Unix-like, which includes Linux and FreeBSD.

What's Linux?

Linux is inspired by Minix, a micro-kernel operating system designed for teaching.

>** Skills**
>
> Now, almost every Intel processor runs Minix.
>
Maybe MinixIt's the most popular operating system in the world.

UNIX standard SUS contains the POSIX standard, which is an overset. Linux met the POSIX standard but did not perform [POSIX authentication] (http://get.posixcertified.ieee.org/).

In essence Linux is a copy or clone of UNIX (like the relationship between humans and robots).

Linux's name is Linux's father Linus Torvalds.

# narrow # Linux is the core

[Linux Kernel] (https://www.kernel.org/) Project 1990;

# # Broad Linux is GNU/Linux

GNU/ Linux = Linux Kernel + GNU + Package Manager

> [Chimera Linux] (https://chimera-linux.org/) **

Linux is known as GNU/Linux;

[GNU Project] 1984 - GNU's not Unix, from GNU, you can see Linux is not directly related to UNIX.

Specifically:

- GNU/Linux issue = Ubuntu, RHEL, Deepin, OpenSUSE...
- Ubuntu = Linux Kernel + apt/dpkg + Gnome
- OpenSUE = Linux Kernel + libzypp/rpm + KDE

> ** Note**
>
> If you still do not understand, it is recommended that you try it in person [Gentoo] (https://www.gentoo.org/downloads/(sage3) or [Slackware] (http://www.slackware.com/), it is not clear that you can try it [Gentoo(stage1)] (https://wiki.gentoo.org/wiki/Stage_file) or [LFS] (https://www.linuxframscratch.org/lfs/).
>
These operations are complex and require experience and basic knowledge.


# What's FreeBSD?

FreeBSD is not Linux. FreeBSD is not a clone of UNIX.

![.. ..gitbook/assets/nolinux.png]

I don't...

The term FreeBSD consists of two parts, namely “Free” and “BSD”.

BSD was originally developed by the University of California Berkeley, meaning `Berkeley Software Distribution ' (Berkeley Software Release).

Free is the meaning of Liberty and free.

FreeBSD is 19 June. FreeBSD Foundation and Community celebrates FreeBSD's birthday on this day. — [Join us to secure FreeBSD Day!] (https://freebsdfoundation.org/freebsd-day/)

# # UNIX Ship: FreeBSD isn't UNIX?

This issue is far from as clear as it could have been imagined. I have seen a number of discussants, even those who went through their old days, who have difficulty answering or clarifying. Or simply, the BSD does not have any UNIX authentication, and does not have a legal trademark to end the subject; even worse, it simply says in general terms that FreeBSD is a continuation and an orthodox successor to UNIX, and that it is “no name”; it is also argued that BSD is UNIX, just as Linux is UNIX.

These different answers are due to the fact that the problem is not a purely technical problem that can simply be analysed with legal trademark attribution or code inheritance. What is at stake is a profound introspective philosophical question — should we not walk into the same river twice or once? (As for similar issues, such as grain piles and balding, interested readers can refer to SEP entries “[Identity Over Time]” (https://plato.stanford.edu/entries/disarmament-time)” and “[Solites Paradox] (https://plato.stanford.edu/entries/sorites-paradox/)”). What is the answer to this question, actually, is a reflection of your philosophy and your scientific and technological perspective.

> **Tensius ship**
>
The safe return of Tessius and Athens youth was carried by a sailboat of 30 oars, which the Athensians kept until the time of Dmitry Faldius. Over and over again, they have broken down old and decayed plates and replaced them with solid new ones. Since then, the ship has become an example often cited by philosophers in their arguments about the development of things, one considering it to be the same ship and the other arguing that it is no longer the same ship.
>
>- [Gold Greece] Prutak. Greek Roman Eminent Persons [M]. Translator: Editor-in-Chief of Huang Hongxiang / Rongzhen/ Wu Pen Peng, 1st ed., Business Books, 1990-11. Page 23 (23).

The BSD operating system is not a replica, but an open source derivative of the AT&T research UNIX operating system and an ancestor of modern UNIX® System V. Before 4.4BSD, BSD was fully known as BSD UNIX.

Initially, Unix was an operating system developed by `AT&T ' to obtain source code but not open source. In the late 1970s, the Computer Systems Research Group of the University of Berkeley (CSRG) began an in-depth study of Unix and developed a large number of user space programs for it, resulting in a new system called BSD (Berkeley Software Distribution, Berkeley software package). Over time, the BSD system has evolved to include many innovations, such as the TCP/IP Barracks. Although the Unix kernel has evolved in several versions, in the 1990s, the AT&T code from the Net/2 version of the Unix kernel was completely replaced as a system without proprietary codes. The BSD system evolved into 4.2 BSD, BSD 4.4-lite ... and then 386 BSD.

In the process, the relationship between BSD and AT&T changed and eventually led to legal controversy, leading to the fragmentation of the BSD system. In 1993, the BSD core code split into two main projects: NetBSD and FreeBSD. OpenBSD was carved from NetBSD in 1996; DragonFlyBSD was carved from FreeBSD in 2003.
。