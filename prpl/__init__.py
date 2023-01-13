from .prpl import *
from .prpl_progress import *
from .prpl_progress_simple import *

import os
import ctypes

""" code version """
__version__ = "0.1.1"

""" Enable escape sequence in cmd """
# WARNING
# When used in conjunction with a library that 
# provides console control, such as tqmd, 
# kernel settings may conflict, resulting in broken rendering.
if os.name == 'nt':
    ENABLE_PROCESSED_OUTPUT = 0x0001
    ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    MODE = ENABLE_PROCESSED_OUTPUT + ENABLE_WRAP_AT_EOL_OUTPUT + ENABLE_VIRTUAL_TERMINAL_PROCESSING

    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)
    kernel32.SetConsoleMode(handle, MODE)