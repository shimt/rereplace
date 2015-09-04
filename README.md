rereplace
=========

rereplace is a string replacement tool which uses a regular expression.  
Since it was tired from mass-producing an one line sed script tutorial, it created.  

## Description

This is is a string replacement tool which uses a regular expression.  

* input is STDIN and an output is STDOUT.
* PATTERN and REPLACEMENT can also be read from a files.

```console:before
cat textfile.txt | sed -re 's/^([^\t\n]*)\t([^\t\n]*)\t([^\t\n]*)\t([^\t\n]*)$/\1,\4/g'
```

```console:after1
cat textfile.txt | rereplace.py '^([^\t\n]*)\t([^\t\n]*)\t([^\t\n]*)\t([^\t\n]*)$' '\1,\4'
```

```console:after2
cat > pattern.txt <<EOB
(?x)
^
([^\t\n]*)\t
([^\t\n]*)\t
([^\t\n]*)\t
([^\t\n]*)
$
EOB
echo -n '\1,\2' > replacement.txt
cat textfile.txt | rereplace.py @pattern.txt @replacement.txt
```

## Requirement

Python 3.x

## Usage

```console:help
usage: rereplace.py [-h] [--re-ascii] [--re-debug] [--re-ignorecase]
                    [--re-locale] [--re-multiline] [--re-dotall]
                    [--re-verbose] [--multiline]
                    PATTERN REPLACEMENT

regex replacing tool

positional arguments:
  PATTERN
  REPLACEMENT

optional arguments:
  -h, --help           show this help message and exit
  --multiline          enable multi-line mode (read all the lines into a
                       memory)

regex matching flags:
  --re-ascii, -a       re.ASCII
  --re-debug           re.DEBUG
  --re-ignorecase, -i  re.IGNORECASE
  --re-locale, -l      re.LOCALE
  --re-multiline, -m   re.MULTILINE
  --re-dotall, -s      re.DOTALL
  --re-verbose, -x     re.VERBOSE
```

## Install

copy rereplace.py. or `python3 setup.py install` or `python3 setup.py py2exe` (require py2exe)

## Licence

MIT
