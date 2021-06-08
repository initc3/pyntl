#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from Cython.Build import cythonize

from setuptools import setup
from setuptools.extension import Extension

NAME = "ntl"
DESCRIPTION = "Experimental bindings to NTL, a C++ library for doing Number Theory."
REQUIRES_PYTHON = ">=3.7.0"
VERSION = None

# REQUIRED = ["gmpy2"]
REQUIRED = []

TESTS_REQUIRES = [
    "black",
    "flake8",
    "flake8-bugbear",
    "flake8-import-order",
    "pep8-naming",
    "pytest",
    "pytest-mock",
    "pytest-cov",
    "pytest-env",
    "pytest-xdist",
    "pytest-benchmark[histogram]",
]

DEV_REQUIRES = ["ipdb", "ipython"]

DOCS_REQUIRE = [
    "Sphinx",
    "sphinx-autobuild",
    "sphinx_rtd_theme",
    "sphinx_tabs",
    "doc8",
    "pydocstyle",
    "recommonmark",
]

EXTRAS = {
    "tests": TESTS_REQUIRES,
    "dev": DEV_REQUIRES + TESTS_REQUIRES + DOCS_REQUIRE,
    "docs": DOCS_REQUIRE,
}

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

if not VERSION:
    g = {}

    # TODO: consolidate how we do this
    with open(os.path.join(here, "src/ntl/__version__.py")) as f:
        exec(f.read(), g)
        VERSION = g["__version__"]


extra_compile_args = ["-std=c++11", "-O3", "-pthread", "-fopenmp", "-march=native"]
extra_link_args = [
    "-std=c++11",
    "-O3",
    "-pthread",
    "-fopenmp",
    "-lntl",
    "-lgmp",
    "-lm",
    "-march=native",
]

extensions = [
    Extension(
        name="ntl._ntl_helpers",
        sources=["src/ntl/ntl_helpers.pyx"],
        language="c++",
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
    )
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=REQUIRES_PYTHON,
    setup_requires=["Cython"],
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    ext_modules=cythonize(extensions),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    package_dir={"": "src"},
    packages=["ntl"],
)
