# pyjacklib

Python bindings for `libjack` using [ctypes], which allow you to write JACK
client applications in Python.

The library provides a low-level, almost unaltered mapping of the `libjack`
[C API], plus a few additional convenience functions.

The source code repository contains a few [example scripts] to show its usage.

**Note:** **pyjacklib** *as a stand-alone project is in an early beta-stage and
the API may still change slightly before a 1.0 release. You have been warned!*


## Dependencies

To use the library, your system needs to have the following installed at
run-time:

* The [JACK] library
* A Python 3 implementation, which supports `ctypes`

To build and install the library you need:

* [setuptools]
* (optional) [pip]


## Building and Installing

You can download and install **pyjacklib** directly from PyPI using `pip`:

```con
pip install pyjacklib
```

Or you can download the latest source archive or clone the git repository
and run the following from inside the unpacked source directory resp. the root
of your checkout:

```con
python setup.py install
```

You can also build a wheel with:

```con
pip wheel .
```

... and install it using `pip install`.


## License

**pyjacklib** is licensed under the GNU Public License Version v2, or
any later version.

Please see the file [COPYING] for more information.


## Authors

Created by *Filipe Coelho (falkTX)* as part of [Cadence].

Turned into stand-alone project and enhanced by *Christopher Arndt*.


[C API]: https://jackaudio.org/api/
[Cadence]: https://github.com/falkTX/Cadence.git
[COPYING]: https://github.com/jackaudio/pyjacklib/blob/master/COPYING
[ctypes]: https://docs.python.org/3/library/ctypes.html
[example scripts]: https://github.com/jackaudio/pyjacklib/tree/master/examples
[JACK]: https://jackaudio.org/
[pip]: https://pypi.org/project/pip/
[setuptools]: https://pypi.org/project/setuptools/
