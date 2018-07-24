from setuptools import setup
from distutils.core import setup
from Cython.Build import cythonize

setup(name='QSP optimization',
      version='0.0',
      description='Optimization of quantum state preparation',
      url='https://github.com/alexandreday/https://github.com/alexandreday/Optimize_QSP',
      author='Alexandre Day',
      author_email='alexandre.day1@gmail.com',
      license='MIT',
      packages=['qsp_opt'],
      zip_safe=False,
      include_package_data=True,
      ext_modules = cythonize("qsp_opt/cythonUtils.pyx")
)
