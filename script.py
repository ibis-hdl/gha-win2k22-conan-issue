#! /usr/bin/env python3

import subprocess
import platform
import argparse
from pathlib import Path

# Neither 'multipledispatch' nor 'signature_dispatch' work on Github's Windows 2022 action runner, 
# always get the error e.g.: ModuleNotFoundError: No module named 'signature_dispatch'

class Foo:
    def __init__(self):
        python_ver=tuple(map(int, platform.python_version_tuple()))
        # match statements are a feature of Python 3.10
        assert python_ver > (3,10,0), f"Python > 3.10 required, got {platform.python_version()}"

    def hello(self):
        print(f"Hello Python v{platform.python_version()}")

if __name__ == '__main__':
    foo = Foo()
    foo.hello()

