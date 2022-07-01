# Educational Videos made on Manim

## Contribution

### Setup

Before starting, make sure you have installed the following:
```
python3.8
python3-pip
python3-venv
manim
make
git # of course
```

Please, use the python from virtual environment instead of the global python.
First, create the virtual environment by simply running `make` command in this directory.

Each time you open a terminal, run the following in this directory. (TODO: update for other OS, where this doesn't work)
```
. .venv/current/bin/activate
```

That's it :)

### Create the video

TODO (fix PYTHONPATH for other OS)
```
PYTHONPATH=lib:objects manim -pql problems/path/to/file.py
```

### Golden rules

Never use tabs, instead use 4 spaces
Always run `make lint` before commiting a change.
Never push to the master. Push to another branch, than create a pull request.
Wait, until your change is reviewed by at least 1 other person. There will never be a super urgent change.
Explicit is better than implicit.
