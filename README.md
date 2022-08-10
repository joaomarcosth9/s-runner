# s-runner
I use this little program mostly for competitive programming, but it can be used for whatever you want.
I don't like to have the binaries of my programs in the same directory as the source codes (I often try to open those binaries with vim). So to avoid having to type `g++ -lm --std=c++17 foo.cpp -o /tmp/foo && /tmp/foo < /tmp/foo.in` every time, I made this.

**New feature:** [Automatic codeforces testing](#codeforces-testing)

- [1. Usage](#usage)
- [2. Install](#install)
- [3. Uninstall](#uninstall)
- [4. Notes](#notes)

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
## Examples:
``` 
> s foo.cpp                         # Just compile to /tmp/foo
> s foo.cpp -r                      # Compile and run
> s foo.cpp -r -i foo.in            # Compile and run with /tmp/foo.in as input
> s foo.cpp -r -i foo.in bar.in     # Compile and run with /tmp/foo.in and /tmp/bar.in as input
```
### Codeforces testing
```
> s wm.cpp -cf codeforces.com/problemset/problem/4/A    # Compile and run with CF testcases as input
# It also accepts full urls (with https://...) 
```
## Install
Requirements:
- Git
- Python3
  - bs4 (BeautifulSoup)
  - requests
```
pip install -r https://raw.github.com/joaomarcosth9/s-runner/main/requirements.txt
bash -c "$(curl -fsSL https://raw.github.com/joaomarcosth9/s-runner/main/install.sh)"
```
Or just:
```
cd /opt
sudo git clone https://github.com/joaomarcosth9/s-runner
sudo chmod +x s-runner/src/s.py
sudo chmod +x s-runner/src/diff-so-fancy/diff-so-fancy
sudo ln -s /opt/s-runner/src/s.py /usr/bin/s
```

## Uninstall
```
bash -c "$(curl -fsSL https://raw.github.com/joaomarcosth9/s-runner/main/uninstall.sh)"
```
Or just:
```
sudo rm -rf /opt/s-runner
sudo rm -f /usr/bin/s
```

## Notes
- You may need to change the first line of `src/s.py` to the path of your python interpreter. Just ensure that the `pip` command in your `$PATH` is related to the correct python interpreter.
