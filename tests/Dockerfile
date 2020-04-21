FROM python:3.5

RUN pip install pytest

COPY ./ /pytest-extra-durations
RUN pip install -e /pytest-extra-durations
RUN pytest -v /pytest-extra-durations/tests
