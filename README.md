# Experimental Python Bindings for NTL

---
[**HERE BE DRAGONS**](https://en.wikipedia.org/wiki/Here_be_dragons)

**ONLY meant for PROTOTYPING & EXPERIMENTAL purposes!**

**NOT FOR PRODUCTION, NOT FOR BETA, NOT FOR ALPHA, ONLY for DEVELOPMENT!**

**USE to EXPERIMENT, LEARN, and PROTOTYPE!**

[**HERE BE DRAGONS**](https://en.wikipedia.org/wiki/Here_be_dragons)

---

The code in this directory exposes a Python interface
for several NTL functions, and other C++ code using
NTL.

## Installation
For now, the `NTL` development header files must be available on the operating system
where `pyntl` is installed.

For Debian/Ubuntu systems `libntl-dev` can be installed:

```shell
sudo apt-get update
sudo apt-get install --yes libntl-dev
```

To install `pyntl` from its GitHub repository:

```shell
pip install git+https://github.com/initc3/pyntl.git
```

Check the installation:

```shell
python -c 'import ntl; print(ntl.version)'
```


# Development

## Modifying code
The provided `Dockerfile` installs the Python package in development/editable mode.
When working with docker-comopse, the source code under [src/ntl](./src/ntl) is
mounted in the containter.


## Building code
The rebuild the `.so` and `.cpp` files, from the root of the project, where `setup.py`
is located:


```shell
python setup.py build_ext --inplace
```

The same command can be used to rebuild the code if you
modify any of the Cython node. Note that you *must* rebuild the code
to observe any changes during execution.

# Writing Parallel Code
Take a look at NTL documentation and see which operations are already
parallelized. In general, it might be better to use these directly
whenever possible.

If you wish to write parallel code yourself, please take a look
at OpenMP documentation for Cython.

Here's a gist of what parallel code using OpenMP in Cython would look
like when using NTL

```
with nogil, parallel():
    ZZ_p::init(modulus)
    for i in prange(start, end, step):
        ...:
```

The operation above starts `n` threads (`n` is decided by OpenMP and
can be modified by using `openmp.set_num_threads` or modifying the
environment variable `OMP_NUM_THREADS`), calls
`ZZ_p::init()` for each thread, and then splits the
`for` loop into `n` chunks. Different chunking strategies
can be used but this has not been explored much and might not
particularly turn out to be useful since we have a largely even
distribution of work among threads.
