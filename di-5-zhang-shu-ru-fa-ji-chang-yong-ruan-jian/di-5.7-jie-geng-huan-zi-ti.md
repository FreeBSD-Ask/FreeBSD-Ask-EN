# Section 5.7 Change font

First extracts all font files of __CODESPAN_1 and __CODESPAN_2_. (MacOS fonts need special processing, although all appear to be formatted __CODESPAN_3_)

Creates a new directory for a new font that is easy to manage:

```sh
# mkdir -p /usr/local/share/fonts/WindowsFonts
```

COPY THE FONT FILE TO __CODESPAN_0_。

```sh
# chmod -R 755 /usr/local/share/fonts/WindowsFonts #刷新权限
# fc-cache
```
