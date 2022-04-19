import argparse, operator, logging


def main(input_string=str):
    if i_string:
        input_string = i_string
        multiple(input_string)
        logging.info(f'Result= {last_digits[1]}')
        print(last_digits[1])
    else:
        while input_string != "q":
            input_string = input()
            if input_string.isdigit():
                if_digit(input_string)
            if input_string in muldiv_list:
                simple_ops(input_string)
            else:
                multiple(input_string)
            logging.info(f'Result= {last_digits[1]}')
            print(last_digits[1])
    return last_digits[1]


def if_digit(input_string):
    last_digits.pop(0)
    last_digits.append(input_string)


def simple_ops(input_string):
    last_digits[1] = ops[input_string](int(last_digits[1]), int(last_digits[0]))
    return last_digits[1]


def multiple(input_string):
    for symbol in str(input_string):
        if symbol.isdigit():
            digit_list.append(int(symbol))
        elif symbol in muldiv_list:
            atfirst_list.append(symbol)
    digit_list.reverse()
    for op in atfirst_list:
        if len(digit_list) > 1:
            res = ops[op](digit_list[1], digit_list[0])
            digit_list[0] = res
            digit_list.pop(1)
            last_digits[1] = digit_list[0]
    return last_digits[1]


if __name__ == '__main__':
    ops = {"*": operator.mul,
           '/': operator.truediv,
           '+': operator.add,
           '-': operator.sub}
    input_string = str
    muldiv_list = ['*', '/', '+', '-']
    last_digits = [0, 0]
    digit_list = []
    atfirst_list = []
    logging.basicConfig(filename='calc.log', level=logging.INFO)
    parser = argparse.ArgumentParser(description="Process")
    parser.add_argument("--i_string", type=str, help="input your string")
    args = parser.parse_args()
    i_string = args.i_string

    main()
