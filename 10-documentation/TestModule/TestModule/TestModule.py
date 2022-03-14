"""
Module TestModule
=================

.. _google: https://google.com

You can open the link of google_.

"""

class TestModule:
    """This is the TestModule class

    This class servers as a demo for the sphinx documentation

    """
    def __init__(self):
        """The class initialization.

        We dont need any arguments!
        """
        self.__name = "Demo"

    @property
    def name(self):
        """The name decorator

        It returns a dummy name
        """
        return self.__name



class  TextException(Exception):
    """Test Exception class

    .. _python.org: https://python.org

    This serves as an example for the Test Exception.

    You go learn python on python.org_
    """
    pass
