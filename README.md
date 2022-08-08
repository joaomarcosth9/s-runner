# s-runner

Kinda useless, it's just commands simplification.

I use this little program mostly for competitive programming, but it can be used for whatever you want.
I don't like to have the binaries of my programs in the same directory as the source codes (I often try to open those binaries with vim). So to avoid having to type `g++ -lm --std=c++17 foo.cpp -o /tmp/foo && /tmp/foo < /tmp/foo.in` every time, I created this.

Tip: add a symlink `ln -s ~/<path_to_script>/s.py /usr/bin/s`

Help:
```
usage: s [-h] [-r] [-i INPUTS [INPUTS ...]] path

s-runner by joaomarcosth9

positional arguments:
  path                  path to the source code file

options:
  -h, --help            show this help message and exit
  -r, --run             run the executable after compiling (default: False)
  -i INPUTS [INPUTS ...], --inputs INPUTS [INPUTS ...]
                        input files (should be located at /tmp/) (default:
                        None)
```

Examples:

``` 
s foo.cpp                    # Just compile to /tmp/foo
s foo.cpp -r                 # Compile and run
s foo.cpp -r -i foo          # Compile and run with /tmp/foo as input
s foo.cpp -r -i foo bar      # Compile and run with /tmp/foo and /tmp/bar as input
```
