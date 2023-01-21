# progress parallel for python
# Author: DomZou
# The license is MIT.

import os
import time
import shutil
from concurrent.futures import ProcessPoolExecutor
from itertools import chain
from inspect import signature

from .prpl_progress_simple import list_progress_simple
from .prpl_progress import list_progress
from .prpl_forl_loop_progress import list_for_loop_progress

def prpl(target_list: list = None, target_function = None, args: dict = None, list_sep: int = 5, checkpoint: int = 10, title: str = "", symbol: str = None, symbol_c: int = 50, smpl: bool = False, timer: bool = False, color: str = "white") -> list:
    
    """ progress color number """
    color_number = {
        "black": 30,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "blue": 34,
        "magenta": 35,
        "cyan": 36,
        "white": 37
    }
    if color in color_number.keys():
        c_num = color_number[color]
    else:
        c_num = 37  # white
    """ Thread progress title """
    if len(title) != 0:
        title = title+"  "
    else:
        if target_function is not None:
            title = target_function.__name__+"() "
        else:
            title = "State of progress"
    """ check symbol length """
    if (symbol != "mew") and (symbol is not None):
        if len(symbol) != 1:
            symbol = symbol[0]

    """ Using python's for loop statement alone """
    if target_function is None:
        return list_for_loop_progress(target_list = target_list, checkpoint = checkpoint, title = title, symbol = symbol, symbol_c = symbol_c, c = c_num)

    """ Terminal line size """
    terminal_line_size = shutil.get_terminal_size().lines
    print("\n"*terminal_line_size + f"\033[{terminal_line_size}A")  # scroll line
    """ List separate """
    target_list_length = len(target_list)
    sep_num = int(target_list_length/list_sep)
    sep_list = [ target_list[sep_:sep_ + sep_num] for sep_ in range(0, target_list_length, sep_num) ]   # split list along variable list_sep
    """ check variable list_sep """
    if len(sep_list) != list_sep:
        list_sep = len(sep_list)
    """ check arguments dict """
    if args is not None:
        target_function_arguments_list = list(signature(target_function).parameters.keys())
        target_new_argument_key = list(set(args.keys())^set(target_function_arguments_list))
        argument_key = target_new_argument_key[0]
        args[argument_key] = sep_list
    else:
        argument_key = None
    
    """ threading result form title """
    if smpl is False:
        print("┌──<< Threading Progress")
        print("│\033[3A")
    """ Start multi thread """
    if timer is True:
        _start = time.perf_counter()    # start thread timer
    thread_futures = []
    
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as pool:   # multi thread
        for index, arg_list in enumerate(sep_list):
            thread_title = title+f"in thread:{index+1} "
            if smpl is True:
                target_future = pool.submit(list_progress_simple, target_list = arg_list, args = args, args_key = argument_key, func_sep = index, checkpoint = checkpoint, title = thread_title, func = target_function, symbol = symbol, symbol_c = symbol_c, c = c_num)
            else:
                target_future = pool.submit(list_progress, target_list = arg_list, args = args, args_key = argument_key, func_sep = index, checkpoint = checkpoint, title = thread_title, func = target_function, symbol = symbol, symbol_c = symbol_c, c = c_num)
            thread_futures.append(target_future)
    
    """ return result list """
    future_result = [ fu_res.result() for fu_res in thread_futures ]
    _result = list(chain.from_iterable(future_result))
    if timer is True:
        _end = time.perf_counter()    # end thread timer

    """ COMPLETE message """
    if smpl is True:
        print(f"\033[{list_sep}B"+ "\n" + ">> Thread calculation is COMPLETE")
    else:   
        complete_msg = "└" + "─"*35 + ">> Thread calculation is COMPLETE\n"
        

        if timer is True:
            timer_msg = "├─Thread processing time: " + "{:.3f}".format((_end-_start)) + "\n"
            complete_msg = timer_msg + complete_msg
        print(f"\033[{(list_sep+1)*2}B" +  "│\n" + complete_msg)
    
    return _result



