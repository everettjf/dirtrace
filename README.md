# dirtrace

`dirtrace` generates chromium's trace event format json file from directory content file size

![Xcode](/screen.png)

[中文说明](https://everettjf.github.io/2019/10/30/dirtrace/)

## Install

```
pip install dirtrace
```

## Usage

(1) run command

```
Usage: 
dirtrace -d <directory-path>
dirtrace -d <directory-path> -o <output-json-path>

This script generates chromium's trace event format json file from directory content file size.
Visit https://github.com/everettjf/DirTrace for more information.

Options:
  -h, --help         show this help message and exit
  -d DIR, --dir=DIR  which directory do you want to trace
  -o OUT, --out=OUT  output json path
```

(2) display

Open Chrome browser, and drag output json file into Chrome's `chrome://tracing/`

## Support

python 2.x && 3.x

---

*wish you enjoy :)*

