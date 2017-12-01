FROM python:3.6

ADD ./ /t0nd3uz-build/
WORKDIR /t0nd3uz-build

RUN python3 setup.py bdist_wheel && pip install dist/t0nd3uz*.whl && rm -rf /t0nd3uz-build

ENTRYPOINT ["/usr/local/bin/t0nd3uz"]

