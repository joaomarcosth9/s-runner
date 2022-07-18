# s-runner

Just a commands simplification.

I use this little program mostly for competitive programming, but it can be used for whatever you want.

Help:
```
usage: s [-h] [-r] [-i INPUTFILE] path

s-runner by joaomarcosth9

positional arguments:
  path                  path to the source code file

optional arguments:
  -h, --help            show this help message and exit
  -r, --run             compile and run the file (default: False)
  -i INPUTFILE, --inputfile INPUTFILE
                        inputfile name (should be located at /tmp/) (default: None)
```

Examples:

```
s A.cpp # Just compile
s B.cpp -r # Compile and run
s C.cpp -r -i C.in # Compile and run with /tmp/C.in as input
```
