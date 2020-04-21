# pytest-extra-durations

Get more info about the speed of your test suite.

It works with pytest-xdist too.


### Installation

You can install "pytest-extra-durations" via `pip`:

```bash
pip install git+https://github.com/gabrieldemarmiesse/pytest-extra-durations.git
```

### Usage

This plugin provides three types of information.

#### The sum of all tests/setup/teardown durations

This can give you more info than the total time displayed by pytest because it's 
not influenced by the number of workers in pytest-dist, or the collection time.

Exemple:

```
============== Sum of all tests durations ===============
1.95s
```

This will be displayed all the time and can't be turned off unless you 
uninstall this plugin.


#### The sum of all the tests durations of a module

This will tell you how much time it took to execute all the tests in a given file.
The API is similar to the one of `--durations` in the Pytest CLI.

```bash
pytest --modules-durations=4 ./path/to/test/directory
```

gives:

```
=============== slowest 4 modules durations =============
1.17s tensorflow_addons/activations/tests/sparsemax_test.py
0.28s tensorflow_addons/activations/tests/gelu_test.py
0.10s tensorflow_addons/activations/tests/softshrink_test.py
0.09s tensorflow_addons/activations/tests/rrelu_test.py
```

#### The sum of all the tests durations of a test function

A test function can produce multiple tests, that can be executed on different workers 
too. This will sum the durations of all tests, setups and teardown produced by 
a single test function, and report the slower ones.

The API is similar to the one of `--durations` in the Pytest CLI.

```bash
pytest --functions-durations=4 ./path/to/test/directory
```

gives:

```
=============== slowest 4 modules durations =============
1.17s tensorflow_addons/activations/tests/sparsemax_test.py
0.28s tensorflow_addons/activations/tests/gelu_test.py
0.10s tensorflow_addons/activations/tests/softshrink_test.py
0.09s tensorflow_addons/activations/tests/rrelu_test.py
```


### TODO: 

* Integration with line_profiler
* Add tests (the ones present are dummy ones)
* Automatic upload to pypi with github actions
* Running the tests in github actions


### License


Distributed under the terms of the `MIT`_ license, "pytest-extra-durations" is free and open source software


