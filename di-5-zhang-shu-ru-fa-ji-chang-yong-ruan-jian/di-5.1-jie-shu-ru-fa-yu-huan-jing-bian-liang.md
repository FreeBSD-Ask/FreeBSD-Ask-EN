Section 5.1 Localized environment variable

# The path to an active profile

1. sddm lightdm gdm may be written in ~/.xprofile ' ;
2. Lightdm gdm may be written in ~/.profile ' ;
Sddm can be written in the user login shell profile;

I don't...

~/.profile`
-bash: ~/.bash_profile ` or ~/.profile `
-zsh: '~/.zprofile '
- csh: ~/.cshrc '

# Localized associated variables

The following variables are used to localize the control environment, most of which are defined by POSIX.

The `LC_* ' series of variables is the environmental variable used in the `Unix ' operating system for localization (i.e., internationalization and localization). These variables control the text character encoding, date and time format, currency symbols, language, etc. Some of the common variables are:

- `LC_COLLATE ' : rules defining the sorting of strings.
- `LC_CTYPE ' : Defines character sets and character type judgement rules, such as letters, numbers, points, etc.
- `LC_Monetary ' : definition of currency format and currency symbol.
- `LC_MESAGES ' : Defines the language in which the information is exported while the program is running.
- `LC_NUMERIC ' : Defines numerical formats such as decimal points and thousands separator.
- `LC_TIME ' : Define date and time format.
- `LC_ADRESS ': Defines the format of the address.
- `LC_NAME ' : Format for defining a person ' s name.
- `LC_PAPER ' : Define paper size and print format.
- `LC_TELEPHONE ' : Defines the format of the telephone number.
- `LC_MEASUREMENT ' : Defines the format of measurement units.
- `LC_IDENTICATION ' : Format for defining document characteristics.

Special:

- `LC_All ': By setting this variable, the values of all other `LC_* ' variables can be covered at the same time.
- `LANG ' : to set the default language and character set. It is usually used to provide area settings when no other `LC_* ' variable settings are available. If the `LANG ' and `LC_* ' variables are set simultaneously: `LC_* ' variables will override the corresponding settings in the `LANG ' variable.
- `LANGUAGE ' : The language environment used to set the current system affects the behaviour of many programs, such as date format, digital format, character encoding, etc. Specifically, this environmental variable is usually automatically read by some programs and, depending on its value, determines which language and localization settings should be used. If this variable is not set, the program may use the default system language environment or other environment variables (e.g. `LC_AL', `LC_MESSAGES ', etc.) to determine the language environment.

By using these variables, users can easily adapt the language and localization settings of the operating system to different geographic and linguistic environments.

- The current value of the above variables can be determined using the `local ' command, such as:

```sh '
$locale
LANG=C.UTF-8
LC_CTYPE= "C.UTF-8"
LC_COLLATE= "C.UTF-8"
LC_TIME= "C.UTF-8"
LC_NUMERIC = "C.UTF-8"
LC_Monetary = "C.UTF-8"
LC_MSAGES = "C.UTF-8"
LC_All
````

- So Chinese culture can be different.

1. Culture in a simple interface simply sets `LC_MESAGES ' as ``zh_CN.UTF-8' (validated under SDDM/Xfce).
2. More commonly, the three environmental variables `LANG ' , `LC_ALL '  and `LANGUAGE ' are set to `zh_CN.UTF-8 ' .
3. English-only environment, with Chinese input.

I don't...

Why are all three environmental variables `LANG ' , `LC_ALL ' , `LANGUAGE ' set to 'zh_CN.UTF-8 ' ? It is mainly the developers who use different variables when writing the program, for greater compatibility.

I don't...

The first set-up only affects interfaces, tips, etc., but has no impact on other format outputs (refer to an overview of the `LC_* ' series of variables) e.g. (sh).

```sh '
$locale
LANG=C.UTF-8
LC_CTYPE= "C.UTF-8"
LC_COLLATE= "C.UTF-8"
LC_TIME= "C.UTF-8"
LC_NUMERIC = "C.UTF-8"
LC_Monetary = "C.UTF-8"
LC_MSAGES=zh_CN.UTF-8
LC_All
$Date
Fri Apr 21 21:14:43 UTC 2023
$ export LC_TIME=zh_CN.UTF-8
$Date
Friday, 21 April 2023 2115 hours 07 seconds UTC
````

By default:

- `LC_TIME ' environmental variable is `C.UTF-8 ' ;
- `date ' command output `Fri Apr 21 21:14:43 UTC 2023 ' ;
- `LC_TIME ' environment variable set to `zh_CN.UTF-8 ' ;
- The `date ' command output is `Friday, 21 April 2023 2115 hours 07 seconds UTC ' .

Note**
>
>Maintenance of the English-language output of the `date ' order is sometimes important for some scripts (this is only one case, and other special needs, etc.). This is also the case with other information controlled by the `LC_* ' variable.
。