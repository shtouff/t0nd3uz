# run with Docker

Build:

    $ docker build . -t t0nd3uz

Then, run:

    $ docker run --rm --mount type=bind,source=$PWD/examples/mower.txt,target=/tmp/mower.txt t0nd3uz /tmp/mower.txt
    1 3 N
    5 1 E

# development

## virtualenv

    $ python3 -mvenv /some/where
    $ source /some/where/bin/activate
    (virtualenv)$

## install deps

Activate the virtualenv, then:

    (virtualenv)$ pip install -r requirements.txt -e .

## run the unit tests

    (virtualenv)$ pytest

## run the thing

    (virtualenv)$ cat examples/mower.txt
    5 5
    1 2 N
    LFLFLFLFF
    3 3 E
    FFRFFRFRRF

    (virtualenv)$ t0nd3uz examples/mower.txt
    1 3 N
    5 1 E
