from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

extensions = [
    Extension('cec2021', ['cec2021.pyx', 'cec21_test_func.cpp'],
              include_dirs=[numpy.get_include()],
              extra_compile_args=['-std=c++17'],
              language='c++'
              ),
]

with open('README.md', 'r') as fh:
    long_description = fh.read()
    
setup(
    description='NiaPy interface for the CEC 2021 competition',
    long_description=long_description,
    long_description_content_type='text/markdown',
    ext_modules=cythonize(extensions),
    extra_compile_args=['-w', '-O3', '-march=native'],
)
