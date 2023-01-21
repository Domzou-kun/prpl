import sys


def list_for_loop_progress(target_list, checkpoint, title, symbol, symbol_c, c):

    """ yield progress setup """
    progress_counter = 0
    target_list_length = len(target_list)
    progress_color = f"\033[{c}m"
    color_end = "\033[0m"
    """ Return of an element by yield  """
    for alone_return_val in target_list:

        if (progress_counter % checkpoint) == 0:

            if symbol is None:
                sys.stdout.write("\033[2K\033[G" + title + f" {str(progress_counter + 1).rjust(len(str(target_list_length)))} / {target_list_length} datas ({str((progress_counter * 100) / target_list_length)[:4]}/100 %)")
                sys.stdout.flush()
            else:
                data_per = progress_counter / target_list_length
                sys.stdout.write("\033[2K\033[G" + title + " | " + progress_color + str(symbol * int(symbol_c * data_per)).ljust(symbol_c) + color_end + " | " + f"{str(data_per * 100)[:4]} / 100 % ")
                sys.stdout.flush()
            
        progress_counter += 1
        if progress_counter != target_list_length:
            yield alone_return_val
        else:
            if symbol is None:
                sys.stdout.write("\033[2K\033[G" + title + f" {str(target_list_length).rjust(len(str(target_list_length)))} / {target_list_length} datas ({str((target_list_length * 100) / target_list_length)[:4]}/100 %)\n")
                sys.stdout.flush()
                yield alone_return_val
            else:    
                data_per = 1
                sys.stdout.write("\033[2K\033[G" + title + " | " + progress_color + str(symbol * int(symbol_c * data_per)).ljust(symbol_c) + color_end + " | " + f"{str(data_per * 100)[:4]} / 100 % \n")
                sys.stdout.flush()
                yield alone_return_val
