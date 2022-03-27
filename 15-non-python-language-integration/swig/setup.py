from distutils.core import setup, Extension

name = "factorial" # Module name
version = "1.0" # Module version

# Extension name and source files required to compile
ext_modules = Extension(name = "_factorial", sources = ["factorial_python_interface.i", "factorial.c"])

setup(name = name, version = version, ext_modules = [ext_modules])
