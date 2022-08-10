# s-runner

I use this little program mostly for competitive programming, but it can be used for whatever you want.
I don't like to have the binaries of my programs in the same directory as the source codes (I often try to open those binaries with vim). So to avoid having to type `g++ -lm --std=c++17 foo.cpp -o /tmp/foo && /tmp/foo < /tmp/foo.in` every time, I created this.

## Usage
Help:
```
usage: s [-h] [-r] [-f] [-i INPUTS [INPUTS ...]] [-cf CODEFORCES] path

s-runner by joaomarcosth9

positional arguments:
  path                  path to the source code file

options:
  -h, --help            show this help message and exit
  -r, --run             run the executable after compiling (default: False)
  -f, --fast            compile with less debugging flags (cpp only) (default: False)
  -i INPUTS [INPUTS ...], --inputs INPUTS [INPUTS ...]
                        input files (should be located at /tmp/) (default: None)
  -cf CODEFORCES, --codeforces CODEFORCES
                        codeforces problem URL for automatic testing (default: None)
```

Examples:

``` 
s foo.cpp                         # Just compile to /tmp/foo
s foo.cpp -r                      # Compile and run
s foo.cpp -r -i foo.in            # Compile and run with /tmp/foo.in as input
s foo.cpp -r -i foo.in bar.in     # Compile and run with /tmp/foo.in and /tmp/bar.in as input
s Watermelon.cpp -cf https://codeforces.com/problemset/problem/4/A     # Compile and run with CF testcases as input
```
