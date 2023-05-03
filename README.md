# s-runner
I use this little program mostly for competitive programming, but it can be used for whatever you want.
I don't like to have the binaries of my programs in the same directory as the source codes (I often try to open those binaries with vim). So to avoid having to type `g++ -lm --std=c++17 foo.cpp -o /tmp/foo && /tmp/foo < /tmp/foo.in` every time, I've made this.

- [1. Usage](#usage)
- [2. Install](#install)
- [3. Uninstall](#uninstall)
- [4. Notes](#notes)

## Usage
Help:
```
usage: s [-h] [-c] [-f] [-i INPUTS [INPUTS ...]] [-p PROBLEM] [-std STDC++]
            path

s-runner by joaomarcosth9

positional arguments:
  path                  path to the source code file

options:
  -h, --help            show this help message and exit
  -c, --compile         just compile the file (default: False)
  -f, --fast            compile with less debugging flags (cpp only) (default:
                        False)
  -i INPUTS [INPUTS ...], --inputs INPUTS [INPUTS ...]
                        list of input files (default: None)
  -p PROBLEM, --problem PROBLEM
                        problem URL for automatic testing (codeforces and
                        atcoder) (default: None)
  -std STDC++, --stdc++ STDC++
                        C++ version (default: 20)
```
## Examples:
``` 
> s foo.cpp                         # Compile to /tmp/foo and run
> s foo.cpp -c                      # Just compile to /tmp/foo
> s foo.cpp -i foo.in               # Compile and run with /tmp/foo.in as input
> s foo.cpp -i foo.in bar.in        # Compile and run with /tmp/foo.in and /tmp/bar.in as input
```
### Online platforms testing
```
> s wm.cpp -p codeforces.com/problemset/problem/4/A    # Compile and run with CF testcases as input
> s vacation.cpp -p atcoder.jp/contests/dp/tasks/dp_c  # Compile and run with AtCoder testcases as input
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
## Uninstall
```
bash -c "$(curl -fsSL https://raw.github.com/joaomarcosth9/s-runner/main/uninstall.sh)"
```
## Notes
- You may need to change the first line of `src/s.py` to the path of your python interpreter. Just ensure that the `pip` command in your `$PATH` is related to the correct python interpreter.
