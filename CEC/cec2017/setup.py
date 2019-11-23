import os

from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy as np

extra_compile_args=['-std=c++11', '-w', '-O3', '-march=native']
if os.getenv('DEBUG', None) is not None: extra_compile_args=['-std=c++11', '-g3', '-O0']

extensions = [
    Extension('cec2017', ['cec2017.pyx', 'cec17_test_func.cpp'],
              include_dirs=[np.get_include()],
              extra_compile_args=extra_compile_args,
              language='c++'
              ),
]

setup(
    ext_modules=cythonize(extensions),
)
