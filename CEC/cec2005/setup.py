from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

extensions = [
    Extension('cec2008', ['cec2008.pyx', 'cec8_test_func.c'],
              include_dirs=[numpy.get_include()],
              extra_compile_args=['-std=c++11', '-w', '-O3', '-narch=native'],
              language='c'
              ),
]

setup(
    ext_modules=cythonize(extensions),
)
