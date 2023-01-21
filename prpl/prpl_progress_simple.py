# progress parallel for python
# simple mode
# copyright by DomZou

import sys

""" list progress """
def list_progress_simple(target_list, args, args_key, func_sep, checkpoint, title, func, symbol, symbol_c, c)->list:
    
    """ console setup """
    csi_line = func_sep + 1
    """ setup argument target list """
    if args is not None:
        args[args_key] = args[args_key][func_sep]
        args_target_list = args[args_key]

    """ function running"""
    target_list_length = len(target_list)
    return_result_list = []
    progress_counter = 0
    progress_color = f"\033[{c}m"
    color_end = "\033[0m"
    while(progress_counter != target_list_length):
        
        if args is None:
            return_result_list.append(func(target_list[progress_counter]))
        else:   # If the argument exists.
            args[args_key] = args_target_list[progress_counter]
            return_result_list.append(func(**args))    

        if (progress_counter % checkpoint) == 0:
            sys.stdout.write(f"\033[{csi_line}B\033[2K")
            
            if symbol is None:
                sys.stdout.write(title + f"{str(progress_counter + 1).rjust(len(str(target_list_length)))} / {target_list_length} datas ({str((progress_counter * 100) / target_list_length)[:4]}/100 %)")
            else:
                data_per = progress_counter / target_list_length
                sys.stdout.write(title + " | " + progress_color + str(symbol * int(symbol_c * data_per)).ljust(symbol_c) + color_end + " | " + f"{str(data_per * 100)[:4]} / 100 % ")
                
            sys.stdout.write(f"\033[{csi_line}A\033[G")
            sys.stdout.flush()
        progress_counter += 1
    
    """ thread complete message """
    sys.stdout.write(f"\033[{csi_line}B\033[2K")

    if symbol is None:
        sys.stdout.write(title + f"{str(progress_counter).rjust(len(str(target_list_length)))} / {target_list_length} datas" + f" ==>> COMPLETE {func_sep + 1} thread")
    else:   # Using symbol
        sys.stdout.write(title + " | " + progress_color + str(symbol * int(symbol_c * 1)).ljust(symbol_c) + color_end + " | " + f" 100 / 100 %"f" ==>> COMPLETE {func_sep + 1} thread")
    
    sys.stdout.write(f"\033[{csi_line}A\033[G")
    sys.stdout.flush()
    
    
    """ return result """
    return return_result_list