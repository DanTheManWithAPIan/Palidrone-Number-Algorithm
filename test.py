def palidrome_number(num):
    new_num = ''
    num_list = [int(i) for i in str(num)]

    for number in range(len(num_list)):
        new_num += str(num_list.pop())

    if int(new_num) == num:
        return print(True)
    else:
        return print(False)


palidrome_number(343)
