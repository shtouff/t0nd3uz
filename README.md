# virtualenv

   $ python3 -mvenv /some/where
   $ source /some/where/bin/activate
   (virtualenv) $

# install deps

Activate the virtualenv, then:

    (virtualenv) $ pip install -r requirements.txt

# run the unit tests

    (virtualenv) $ pytest

# run the thing

```
(virtualenv) $ cat /tmp/mower.txt
5 5
1 2 N
LFLFLFLFF
3 3 E
FFRFFRFRRF

(virtualenv) $ python3 main.py /tmp/mower.txt
1 3 N
5 1 E
```

