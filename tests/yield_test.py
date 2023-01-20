


def test(t_list):

    c_ = 0
    target_list_length = len(t_list)
    for a in t_list:
        data_per = c_/target_list_length
        print("\r"+str(a)+"   "+str(c_)+"    "+str(data_per), end="")
        c_+=1
        if c_!=target_list_length:
            yield a
        else:
            print("\r"+str(t_list[-1])+"   "+str(c_+1)+"    "+str(1), end="")



