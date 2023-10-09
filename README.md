# Educational Videos made on Manim

## Contribution

### Setup

Before starting, make sure you have installed the following:
```
python3.11
python3-pip
python3-venv
manim == v0.17.3
latex
git # of course
```

### Create the video

FOR LINUX, MACOS: 
```
PYTHONPATH=lib:objects python qarakusi.am.py 10107 --language armenian -pql
```

FOR WINDOWS: 
```
$env:PYTHONPATH='lib;objects'; python qarakusi.am.py 10107 --language english -pql
```

### Fix scripts

Run the following command on your svg file to make partial fixes (e.g. remove empty polynoms):
```
python scripts/svg_fixer.py path/to/my_svg_file.svg
```

### Golden rules

Never use tabs, instead use 4 spaces

Never push to the master. Push to another branch, than create a pull request.

Wait, until your change is reviewed by at least 1 other person. There will never be a super urgent change.

Explicit is better than implicit.

Add demo after creating new class.

Always delete useless branch after merging it to the master.

Always link the issue to the pull request.
