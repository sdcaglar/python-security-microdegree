## Section Topics

### 15.1 - SWIG with C

- 01 | Building blocks
    - Hashlib, json, ctypes, os, getpass modules of python
- 02 | Developing the script
    - Putting the parts together
- 03 | Conclusion
    - A database for authentication without any knowledge of the actual sensitive
      information.


#### SWIG (Simplified Wrapper and Interface Generator)

![SWIG](swig.png)

#### Process
Install SWIG (apt install swig)

Write desired C code and header

Write SWIG interface file
* The __%module__ directive provides the name of the module used in Python
* The __%{..%}__ block provides a place to put additional code, such as header
  files or declarations into the generated wrapper code
* The %include directive provides for additional files such as headers

Create Python files
* Option 1: Manually compile C code, configure Python and link shared library
* Option 2: Use distutils to create setup.py file and automatically create
  everything

Creates a Python wrapper around C declarations

Uses: Building scripting interface to C programs; provide C code to scripting
languages.

Process: Import SWIG; write C code; write interface file; generate Python files.

#### Commands used in chapters
```
cd swig
sudo apt install swig
python3 setup.py build_ext --inplace

python3
import factorial
print(factorial.get_modulus(5))
120
print(factorial.get_modulus(5, 2))
1
print(factorial.cvar.pi_var)
3.14
```

#### Summary

SWIG
  - Creates a Python wrapper around C declarations
Uses
  - Build scripting interface to C programs; provide C code to scripting languages
Process
  - Import SWIG; write C code; write interface file, generate Python files

### Helpful Resources

[Wrapping C/C++ for Python using SWIG)](https://www.geeksforgeeks.org/wrapping-cc-python-using-swig-set-1/?ref=gcse)