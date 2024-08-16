import pyperclip
import time
import ctypes
from random import *


def lc_printf(o):
    print(lc_format(o))


# add dict support :p
def lc_format(o) -> str:
    if isinstance(o, str):
        return '"' + o + '"'
    elif isinstance(o, list):
        return "[" + ", ".join([lc_format(s) for s in o]) + "]"
    elif isinstance(o, int):
        return str(o)
    else:
        raise ValueError(f"Unsupported type {type(o)}")


def lc_copy(o):
    pyperclip.copy(lc_format(o))
    time.sleep(0.25)


def lc_copy_debug(o):
    text = lc_format(o)
    print(text)
    pyperclip.copy(text)
    time.sleep(0.25)
