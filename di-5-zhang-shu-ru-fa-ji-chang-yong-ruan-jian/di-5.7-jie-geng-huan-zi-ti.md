# Section 5.7 Change font

First extracts all '.ttf ' and '.ttc ' font files from Windows `C:\Windows\Fonts '. (MacOS fonts require special processing, although all appear to be formatted `.ttf ')

Creates a new directory for a new font that is easy to manage:

```sh '
#mkdir-p/usr/local/share/fonts/WindowsFonts
````

Copy the font file to `WindowsFonts '.

```sh '
#chmod-R755 /usr/local/share/fonts/WindowsFonts # refresh permission
# fc-cache
````
