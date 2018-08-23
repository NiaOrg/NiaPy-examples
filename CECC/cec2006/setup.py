from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

extensions = [
    Extension('cec2006', ['cec2006.pyx', 'cec6_test_func.cpp'],
              include_dirs=[numpy.get_include()],
              language='c++'
              ),
]

setup(
    ext_modules=cythonize(extensions),
    extra_compile_args=['-w', '-g', '-O3'],
)
