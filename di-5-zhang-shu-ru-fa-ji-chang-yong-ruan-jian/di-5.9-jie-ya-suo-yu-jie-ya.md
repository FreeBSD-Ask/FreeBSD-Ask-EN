Section 5.9 Compression and decompression

# zip

>** Skills**
>
>zip or non-English characters is a normal thing. Because of the different codes, the general national operating system (UOS, Ubuntukylin) has been patched. As to why this patch didn't go upstream, someone who knew was welcome to PR.

# # Install zip

- Use pkg

```sh '
# Pkg install zip
````

- Use ports

```sh '
#cd/usr/ports/archivers/zip/
# Make install clean
````

# zip compression and decompression



- Unpressure.

If the zip is depressed, the basic system is self-contained `unzip ' without installation.

```sh '
$zip test.zip test# Compress into zip file
````

- Compressed to zip

````
$ unzip test.zip# unpressure zip file to current path
$ unzip test.zip-d/home/ykla/test# unpressure to specified path,-d means directory
````

# tar

Basic systems are self-contained `tar ' without installation.

tar, or “tape archive”, was originally stored on tape.

>** Thinking issues**
>
The >>archiving package is the `0 ' file collection (packaging multiple files/directories into a single file for easy storage). Simple `tar ' operations are packed and not compressed. The essence of compression is to reduce the size of the document by an algorithm, not to target the directory. So the common compression software is essentially a file of the directories before they are compressed.
>
How do you understand the relationship between archiving and compression?

# Unpressure tar #



```sh '
$tar-xvf test.tar# unpressure tar format, including not limited to test.tar.bz2, test.tar.gz, test.tar.xx:
$tar-xvf test.tar-C/ home/ykla/mytest# unpressure to specified path
````

- `x ':Extract
- `v ' :verbose verbose means output details
- 'f ':file specified file
- `C ': `cd ' meaning, i.e., specify the path

# # Compress into tar

```sh '
$tar-cvf test.tar test# Compress into a tar file. - Create, created;
$tar-zcvf test.tar.gz test# Compress to gzip format. -z is gzip.
$tar-jcvf test.tar.bz2 test# Compress into bzip2 format. Parameter -j is bzip2, note case
$tar-Jcvf test.tar.xx test# Compress to xz format. Parameter -J, xz, note case
````

# xz

The basic systems are self-contained `xz ' , `unxz ' and are likewise not installed.

# # unxz #

```sh '
$unxx-k test.tar.xx# unpressure and preserve original file, argument-k keep (reserved), same
$ unxz test.tar.xx# unpressure and delete original file
````

# # Compress into `xx '

```sh '
$ xz-k test.txt# Compress and keep the original file
$ xz test.pdf # Compress and delete the original file
````

# 7z

Under the FreeBSD operating system, the 7z command is used by downloading `archivers/7-zip ' .

# # Install 7-zip

- Use pkg:

````
# pkg install 7-zip
````

- By Ports:

````
#cd/usr/ports/archivers/7-zip/
# Make install clean
````

Example:

- Compress 7z

```sh '
$7z a test.7z test # compress to 7z file. A-a is add, which is adding the file to compression to test.7z.
````

- Decompress 7z

````
$7z x test.7z # free 7z file
$7z x test.7z-o/home/ykla/ download/test# depress to the specified path. -o is Outlook, specify output path
````

# Rar

Rar is a common compression tool on Windows.

# Install rar #

- Through pkg;

```sh '
♪ Pkg in rar unrar
````

- By Ports:

```sh '
# cd /usr/ports/archivers/rar/ & make install clean
#cd /usr/ports/archivers/unrar/ & make install clean
````

# Use rar #

- Compressed to rar

````
$ rar a ARchive. rar test #-a -- add, add file to ARchive. rar
````

- Unpressure, rar.

```sh '
$ unrar x archive.r# unpressure to the current path. Parameter - x, Extract, depression
$ unrar x archive.rr/home/ykla/ desktop/ test/# uncompress to specified directory
````

# zstd

Zstd, basic system, no need for installation. (https://svnweb.freebsd.org/base?view=review&vision=329240)

# # Compress into zstd

- Compress single files with zstd

```sh '
$ zstd test.pdf
````

- Use zstd compression folders

zstd does not support compressed folders (see [How can I compress a directory?] (https://github.com/facebook/zstd/issues/1526)) and needs to be packed in tar:

>** Thinking issues**
>
>zstd Why not support compressed folders? What are the possibilities.

```sh '
$ tar-cf test.tar/home/ykla/test/# compress to tar. Parameter -f is file(file)
````

Then compress `test.tar ' into `test.tar.zst '

```sh '
$ zstd-o test.tar.zst test.tar# argument-o for file,
````

# Unpressure zstd

- Extract to current path.

```sh '
That's right.
````

Note**
>
>The decompression is `test.tar ' , which needs to be repeated with `tar ' .

- Depress to specified path.

```sh '
$zstd -d best.tar.zst -o/home/ykla/mytest# argument -d is decompress
````

Note**
>
>The decompression is `test.tar ' , which needs to be repeated with `tar ' .
。