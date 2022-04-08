import operator
ops = {"*":operator.mul,
       '/':operator.truediv,
       '+':operator.add,
       '-':operator.sub}
input_string = str
muldiv_list = ['*', '/']
plusmin_list = ['+', '-']
last_dgt = int
pre_last_dgt = int

while input_string != "q":
    input_string = input()
    if input_string.isdigit() or input_string in muldiv_list or input_string in plusmin_list:
        if input_string.isdigit():
            pre_last_dgt=last_dgt
            last_dgt=input_string
            print(last_dgt)
    if input_string in muldiv_list or input_string in plusmin_list:
        last_dgt=ops[input_string](int(last_dgt),int(pre_last_dgt))
        print(last_dgt)
    else:
        digit_list = []
        atfirst_list = []
        delayed_list = []
        for symbol in input_string:
            if symbol.isdigit():
                digit_list.append(int(symbol))
            elif symbol in muldiv_list:
                atfirst_list.append(symbol)
            elif symbol in plusmin_list:
                delayed_list.append(symbol)
        digit_list.reverse()
        atfirst_list.extend(delayed_list)
        for op in atfirst_list:
            res=ops[op](digit_list[1],digit_list[0])
            digit_list[0]=res
            del digit_list[1]
            last_dgt=res
            print(res)
















