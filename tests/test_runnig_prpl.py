# "prpl" module testing program
# 
# The test code can be installed in developer mode by the following command. 
# >> python setup.py develop
# Uninstall command
# >> python setup.py develop -u
#
# The test program is controlled using if statements in the main function. 
# Please rewrite the if statement according to what you want to test.
# 
# Please check "docs\example_gif\"
# for a gif summary of the test program execution.

import time
import random

""" import prpl library """
from prpl import prpl

""" target calculation method """
def test_calc_func(i):
    return (i**i)**3

def timer_main():
    """ test list """
    t_list = list(range(0, 9564))

    """ prpl method """
    start = time.perf_counter()
    res = prpl(target_list=t_list, target_function=test_calc_func, gui_mode=True)
    end = time.perf_counter()
    print("[prpl]method progress time: "+"{:.2f}".format((end-start)))
    
    """ python "for" method """
    res = []
    start = time.perf_counter() #計測開始
    for i in t_list:
        res.append(test_calc_func(i))
    end = time.perf_counter() #計測終了
    print("[python standard \"for\"]method progress time: "+"{:.2f}".format((end-start)))
    print("\n")


""" target calculation method """
def test_2(i):
    return (i*4)

""" prpl mode test """
def mode_test():
    """ test list """
    t_list = list(range(0, 10000))
    random.shuffle(t_list)
    
    if False:
        """  standard mode """
        """ prpl_run_1.gif """
        print("standard mode")
        res = prpl(target_list=t_list, target_function=test_calc_func)
        time.sleep(2)
    if False:
        """ simple mode """
        """ prpl_run_2.gif """
        print("simple mode")
        res = prpl(target_list=t_list, target_function=test_calc_func, smpl=True)
        time.sleep(2)
    if True:
        """ change progress symbol """
        """ prpl_run_3.gif """
        print("change progress symbol")
        res = prpl(target_list=t_list, target_function=test_calc_func, symbol="#")
        time.sleep(2)
    if False:
        """ change progress symbol for simple mode """
        """ prpl_run_4.gif """
        res = prpl(target_list=t_list, target_function=test_calc_func, symbol="#", smpl=True)
        time.sleep(2)
    if False:
        """ change max thread """
        """ prpl_run_5.gif """
        print("change max thread")
        res = prpl(target_list=t_list, target_function=test_calc_func, list_sep=8)
        time.sleep(2)
    if True:
        """ change progress symbol color """
        """ prpl_run_6.gif """
        res = prpl(target_list=t_list, target_function=test_calc_func, symbol="#", color="green")
        time.sleep(2)
    if False:
        """ add timer """
        """ prpl_run_7.gif """
        res = prpl(target_list=t_list, target_function=test_calc_func, timer=True)
        time.sleep(2)
    if False:
        """ and more arguments... """
        """ prpl_run_8.gif """
        res = prpl(
            target_list=t_list,             # target List
            target_function=test_calc_func, # target Function
            list_sep=5,                     # number of list to split
            timer=True,                     # run timer
            smpl=True,                      # simple CUI
            symbol="$",                     # progress bar symbol
            symbol_c=65,                    # number of symbol
            checkpoint=25,                  # check interval
            title="testing prpl",           # thread title
            color="yellow"                  # color of progress bar
        )
        time.sleep(2)


    print("\n ==>> finish mode test <<== \n")



def target_function(target_var):
    calc_answer = (target_var**target_var)**2   # target formula
    return calc_answer

""" Sample code covered in the readme """
def readme_sample():
    import time
    import itertools
    import random

    boxes = list(itertools.chain.from_iterable([["|"]*50, ["\\"]*50, ["-"]*50, ["/"]*50, ["|"]*50]))
    
    calculation_result = []
    target_list = list(range(0, 10000))
    random.shuffle(target_list)

    print("\n conventional method start \n")
    conv_start = time.perf_counter()
    c = 0
    for target_var in target_list:
        b = boxes[c]
        print("\r"+"now calculation... "+b+" "*10, end="")
        c+=1
        if c==len(boxes):
            c = 0
        calc_answer = (target_var**target_var)**2   # formula
        calculation_result.append(calc_answer)
    conv_end = time.perf_counter()
    print("\n conventional method end \n")
    time.sleep(1.5)


    print("\n prpl method \n")
    prpl_start = time.perf_counter()
    target_list = list(range(0, 10000))
    calculation_result = prpl(target_function, target_list) # prpl
    prpl_end = time.perf_counter()

    print("[conventional methon]: {:.2f}sec".format(conv_end-conv_start))
    print("[prpl methon]: {:.2f}sec".format(prpl_end-prpl_start))


""" Other uses of prpl """
def and_more():
    import time

    if False:
        """ np.arrray is also available, but The type that returns as a result is the list type.  """
        import numpy as np
        test_np_array = np.array(list(range(0, 10000)))
        res = prpl(target_function, test_np_array)
        time.sleep(2)

    if False:
        """ Only one progress bar is available """
        test_list = list(range(0, 5000))
        res =  prpl(target_function, test_list, list_sep=1)
        time.sleep(2)



if __name__ == "__main__":
    if False:
        timer_main()
        """
        timer result
        ++++++++++++++++++++++++++++++++++  
        [prpl]method progress time: 15.83
        [for] method progress time: 31.04
        ++++++++++++++++++++++++++++++++++
        """
    if True:
        mode_test()

    if False:
        readme_sample()

    if False:
        and_more()
    

