# progress parallel for python
# copyright by Domzou

import sys

""" list progress """
def list_progress(target_list, args, args_key, func_sep, checkpoint, title, func, symbol, symbol_c, c) -> list:
    
    """ CSI console setup """
    csi_line = (func_sep + 1)*2
    title = "├─"+title
    """ moe mode """
    if symbol == "mew":
        symbol_moe = "~~(  =^･ω･^=)"
    """ setup argument target list """
    if args is not None:
        args[args_key] = args[args_key][func_sep]
        args_target_list = args[args_key]
    """ function running"""
    target_list_length = len(target_list)
    return_result_list = []
    progress_circle_bar = ["|", "\\", "-", "/", "|"]
    progress_circle_bar_counter = 0
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
            elif symbol == "mew":
                data_per = progress_counter / target_list_length
                console_msg = " " * (int(symbol_c * data_per)) + symbol_moe + " " * (int(symbol_c * (1-data_per)))
                if ((int(symbol_c * data_per)) + (int(symbol_c * (1 - data_per)))) != symbol_c:
                    console_msg = console_msg + " "
                sys.stdout.write(title + " | " + progress_color + console_msg + color_end + " | " + f"{str(data_per * 100)[:4]} / 100 % ")
            else:
                data_per = progress_counter / target_list_length
                sys.stdout.write(title + " | " + progress_color + str(symbol * int(symbol_c * data_per)).ljust(symbol_c) + color_end + " | " + f"{str(data_per * 100)[:4]} / 100 % ")

            sys.stdout.write(f"\033[1B\033[2K\033[G")
            sys.stdout.write(progress_circle_bar[progress_circle_bar_counter % 5])
            sys.stdout.write(f"\033[1A\033[G")
            
            progress_circle_bar_counter += 1
            sys.stdout.write(f"\033[{csi_line}A\033[G")
            sys.stdout.flush()
        progress_counter += 1
    
    """ thread complete message """
    sys.stdout.write(f"\033[{csi_line}B\033[2K")
    
    if symbol is None:
        sys.stdout.write(title + f"{str(progress_counter).rjust(len(str(target_list_length)))} / {target_list_length} datas")
    elif symbol == "mew":
        data_per = progress_counter / target_list_length
        console_msg = " " * (int(symbol_c * data_per)) + symbol_moe + " " * (int(symbol_c * (1 - data_per)))
        sys.stdout.write(title + " | " + progress_color + console_msg + color_end + " | " + f" 100 / 100 %")
    else:
        sys.stdout.write(title + " | " + progress_color + str(symbol * int(symbol_c * 1)).ljust(symbol_c) + color_end + " | " + f" 100 / 100 %")
    
    sys.stdout.write(f"\033[1B\033[2K\033[G")
    finish_msg = f"└──────────>> COMPLETE {func_sep + 1} thread"
    sys.stdout.write("│" + finish_msg.rjust((len(finish_msg) + (len(title) - 3))))
    sys.stdout.write(f"\033[{csi_line + 1}A\033[G")
    sys.stdout.flush()
    
    """ return result """
    return return_result_list