# s-runner

Kinda useless, it's just commands simplification.

I use this little program mostly for competitive programming, but it can be used for whatever you want.
I don't like to have the binaries of my programs in the same directory as the source codes (I often try to open those binaries with vim). So to avoid having to type `g++ -lm --std=c++17 foo.cpp -o /tmp/foo && /tmp/foo < /tmp/foo.in` every time, I created this.

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
s foo.cpp                  # Just compile
s foo.cpp -r               # Compile and run
s foo.cpp -r -i foo.in     # Compile and run with /tmp/foo.in as input
```
