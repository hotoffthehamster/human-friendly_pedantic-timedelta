# -*- coding: utf-8 -*-

"""
A setuptools based setup module.

See:
    https://packaging.python.org/en/latest/distributing.html
    https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils.
from setuptools import setup, find_packages
# Use open from codecs for consistent encoding.
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

requirements = [
    'Inflector',
]

setup(
    name='human-friendly_pedantic-timedelta',

    # Versions should comply with PEP440. For a discussion on single-
    # sourcing the version across setup.py and the project code, see
    #  https://packaging.python.org/en/latest/single_source_version.html
    version='0.0.1a1',

    description="Human-friendly timedelta formatter",
    long_description=long_description,

    # Project page.
    url='https://github.com/hotoffthehamster/human-friendly_pedantic-timedelta',

    # Author details.
    author='HotOffThe Hamster',
    author_email='hotoffthehamster+humanfriendlypedantictimedelta@gmail.com',

    # Choose your license.
    license='GPLv3',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # For whom the project is intended.
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # The License classification, which matches the "license" above.
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # The Python versions supported. All Modern Ones.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # Keywords for PyPI to display, and to use for search results.
    keywords='timedelta elapsed time duration human friendly string formatter',

    # Specify packages to install, either manually, or using find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # Alternatively, to distribute just a my_module.py, use py_modules:
    #   py_modules=["my_module"],

    # Run-time dependencies installed on `pip install`. To learn more
    # about "install_requires" vs pip's requirements files, see:
    #  https://packaging.python.org/en/latest/requirements.html
    install_requires=requirements,

    # Additional groups of dependencies (e.g. development dependencies).
    # Install these using the following syntax, e.g.,
    #   `pip install -e .[dev,test]`
    # FIXME: See also: requirements/*.pip
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # Data files to be installed. (<= Python 2.6 needs MANIFEST.in as well.)
    #  package_data={
    #      'sample': ['package_data.dat'],
    #  },

    # Although 'package_data' is the preferred approach, in some cases
    # you may need to place data files outside of your packages. See:
    #  http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #  data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #
    # [lb]: This installs to /usr/local/bin, e.g., if you don't sudo:
    #   Installing pedantic_timedelta script to /usr/local/bin
    #   error: [Errno 13] Permission denied: '/usr/local/bin/pedantic_timedelta'
    # Unless of course you're installing to a virtualenv.
    #
    #  entry_points={
    #      'console_scripts': [
    #          'pedantic_timedelta=pedantic_timedelta:main',
    #      ],
    #  },
)

