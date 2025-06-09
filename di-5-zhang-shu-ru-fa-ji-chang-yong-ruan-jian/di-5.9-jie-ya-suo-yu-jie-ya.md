Section 5.9 Compression and decompression

# zip

>** Skills**
>
>zip or non-English characters is a normal thing. Because of the different codes, the general national operating system (UOS, Ubuntukylin) has been patched. As to why this patch didn't go upstream, someone who knew was welcome to PR。

# # install zip

- use pkg

```sh
# pkg install zip
```

- use ports

```sh
# cd /usr/ports/archivers/zip/
# make install clean
```

# zip compression and decompression



- unpressure

zip unpressures the basic system with __CODESPAN_0_, without installation。

```sh
$ zip test.zip test # 压缩成 zip 文件
```

- compressed to zip

```
$ unzip test.zip # 解压 zip 文件到当前路径
$ unzip test.zip -d /home/ykla/test # 解压到指定路径，-d 即 directory，目录的意思
```

# tar

BASIC SYSTEM WITH __CODESPAN_0_, WITHOUT INSTALLATION。

tar, or “tape archive”, was originally stored on tape。

>** Thinking issues**
>
THE ARCHIVE PACKAGE IS THE COLLECTION OF __CODESPAN_0_ FILES (PACKAGING MULTIPLE FILES/DIRECTORS INTO A SINGLE FILE THAT CAN BE EASILY STORED). THE SIMPLE __CODESPAN_1_ OPERATION IS PACKED AND NOT COMPRESSED. THE ESSENCE OF COMPRESSION IS TO REDUCE THE SIZE OF THE DOCUMENT BY AN ALGORITHM, NOT TO TARGET THE DIRECTORY. SO THE COMMON COMPRESSION SOFTWARE IS ESSENTIALLY A FILE OF THE DIRECTORIES BEFORE THEY ARE COMPRESSED。
>
How do you understand the relationship between archiving and compression

# unpressure tar #



```sh
$ tar -xvf test.tar # 解压 tar 格式文件、包括不限于 test.tar.bz2、test.tar.gz、test.tar.xz：
$ tar -xvf test.tar -C /home/ykla/mytest # 解压到指定路径
```

- __CODESPAN_0_:Extract
- __CODESPAN_0_:verbose Quiet mode: output details
-__CODESPAN_0_:file specified file
- __CODESPAN_0:_CODESPAN_1_, I.E. SPECIFY THE PATH

# # compress into tar

```sh
$ tar -cvf test.tar test # 压缩成 tar 格式文件。-c 即 Create，创建；
$ tar -zcvf test.tar.gz test # 压缩成 gzip 格式文件。-z 即 gzip
$ tar -jcvf test.tar.bz2 test # 压缩成 bzip2 格式文件。参数 -j 即 bzip2，请注意大小写
$ tar -Jcvf test.tar.xz test # 压缩成 xz 格式文件。参数 -J 即 xz，请注意大小写
```

# xz

THE BASIC SYSTEM IS SELF-CONTAINED AND IS NEITHER INSTALLED。

## UNCOMPRESS __CODESPAN_0_

```sh
$ unxz -k test.tar.xz  # 解压并保留原文件，参数 -k 即 keep（保留），下同
$ unxz test.tar.xz     # 解压并删除原文件
```

# # COMPRESS ___ CODESPAN_0_

```sh
$ xz -k test.txt  # 压缩并保留原文件
$ xz test.pdf     # 压缩并删除原文件
```

# 7z

Under the FreeBSD operating system, the 7z command is used by downloading __CODESPAN_0_。

# # install 7-zip

- use pkg:

```
# pkg install 7-zip
```

- By Ports:

```
# cd /usr/ports/archivers/7-zip/
# make install clean
```

Example:

- compress 7z

```sh
$ 7z a test.7z test # 压缩成 7z 文件。-a 就是 add，即把要压缩的文件添加到 test.7z
```

- decompress 7z

```
$ 7z x test.7z # 解压 7z 文件
$ 7z x test.7z -o /home/ykla/下载/test # 解压到指定路径。-o 即 Output，指定输出路径
```

# rar

rar is a common compression tool on Windows。

# install rar #

- through pkg;

```sh
# pkg ins rar unrar
```

- By Ports:

```sh
# cd /usr/ports/archivers/rar/ && make install clean
# cd /usr/ports/archivers/unrar/ && make install clean
```

# use rar #

- compressed to rar

```
$ rar a archive.rar test # -a 即 add，把文件添加到 archive.rar 的意思
```

- unpressure, rar

```sh
$ unrar x archive.rar # 解压到当前路径。参数 -x 即 Extract，解压的意思
$ unrar x archive.rar /home/ykla/桌面/test/ # 解压缩到指定目录
```

# zstd

Zstd, basic system, no need for installation. [Add support for zstd-compressed user and Kennel core dumps.]

# # compress into zstd

- compress single files with zstd

```sh
$ zstd test.pdf
```

- use zstd compression folders

zstd does not support compressed folders (see [How can I contact a director?] (https://github.com/facebook/zstd/issues/1526)) and needs to be packed in tar:

>** Thinking issues**
>
>zstd why not support compressed folders? what are the possibilities。

```sh
$ tar -cf test.tar /home/ykla/test/ # 先压缩成 tar。参数 -f 即 file（文件）
```

AND COMPRESS __CODESPAN_0 TO __CODESPAN_1_1_

```sh
$ zstd -o test.tar.zst test.tar # 参数 -o 代表 file，文件
```

# unpressure zstd

- Extract to current path

```sh
$ zstd -d test.tar.zst
```

Note**
>
>THE DEPRESSURE IS __CODESPAN_0, AND __CODESPAN_1_ WILL NEED TO BE USED AGAIN。

- Depress to specified path

```sh
$ zstd -d test.tar.zst -o /home/ykla/mytest # 参数 -d 即 decompress（解压缩）
```

Note**
>
>THE DEPRESSURE IS __CODESPAN_0, AND __CODESPAN_1_ WILL NEED TO BE USED AGAIN。
