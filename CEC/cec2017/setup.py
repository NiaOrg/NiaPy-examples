import os

from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize

import numpy as np

compile_args=['-std=c++11', '-w', '-O3', '-march=native']
if os.getenv('DEBUG', None) is not None: compile_args=['-std=c++11', '-g3', '-O0']

extensions = [
    Extension('cec2017', ['cec2017.pyx', 'cec17_test_func.cpp'],
              extra_compile_args=compile_args,
              include_dirs=[np.get_include()],
              language='c++'
              ),
]

setup(
    ext_modules=cythonize(extensions),
)
