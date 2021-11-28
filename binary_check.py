def checking_binary_string(string):
    arrange=set(string)
    print(arrange)
    binary={'0','1'}
    if binary==arrange or arrange=={'0'} or arrange=={'1'}:
        print("String is binary")
    else:
        print("Strig is not a binary")
checking_binary_string("10101")
checking_binary_string("abcdi1010")