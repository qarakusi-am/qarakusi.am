# Educational Videos made on Manim

## Contribution

### Setup

Before starting, make sure you have installed the following:
```
python3.8
python3-pip
python3-venv
manim
git # of course
```

// TODO: Add other modules that needs to be installed (e.g. latex related)

### Create the video

FOR LINUX, MACOS: 
```
PYTHONPATH=lib:objects python qarakusi.am.py 10107 --language armenian -pqh
```

FOR WINDOWS: 
```
$env:PYTHONPATH='lib;objects'; python qarakusi.am.py 10107 --language english -pql
```

### Fix scripts

Run the following to make a small fix in your manim:
```
python scripts/manim_fix.py
```

Run the following command on your svg file to make partial fixes (e.g. remove empty polynoms):
```
python scripts/svg_fixer.py path/to/my_svg_file.svg
```

### Golden rules

Never use tabs, instead use 4 spaces

Never push to the master. Push to another branch, than create a pull request.

Wait, until your change is reviewed by at least 1 other person. There will never be a super urgent change.

Explicit is better than implicit.
