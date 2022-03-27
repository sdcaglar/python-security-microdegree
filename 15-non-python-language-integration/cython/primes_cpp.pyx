# distutils: language=c++

from libcpp.vector cimport vector

def primes_cpp(unsigned int nb_primes):
    cdef int n, i
    cdef vector[int] p # C++ vector used like a Python list, but closer to a Python array type
    p.reserve(nb_primes) # allocate memory for 'nb_primes' elements

    n = 2
    while p.size() < nb_primes: # size() for vectors is similar to len()
        for i in p:
            if n % i == 0:
                break
        else:
            p.push_back(n) # push_back is similar to append()
        n += 1
    # Vectors are automatically converted to Python
    # list when converted to Python objects

    return p

