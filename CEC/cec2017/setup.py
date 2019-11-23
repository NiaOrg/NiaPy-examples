from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

extensions = [
    Extension('cec2017', ['cec2017.pyx', 'cec17_test_func.cpp'],
              include_dirs=[numpy.get_include()],
              extra_compile_args=['-std=c++17', '-w', '-O3', '-march=native'],
              language='c++'
              ),
]

setup(
    ext_modules=cythonize(extensions),
)
