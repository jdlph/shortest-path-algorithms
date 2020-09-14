import os, sys

from distutils.core import setup, Extension

sfc_module = Extension(
    'SimpleDequeC', sources = ['module.c']
    )

setup(
    name = 'DequeC',
    version = '1.0',
    description = 'Python package with CSimpleDeque C extension',
    ext_modules = [sfc_module]
)