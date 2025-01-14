while True:
    try:
        n = input()
        len1 = len(n)
        dict1 = {}
        n_in = sorted(list(n))
        step = 2
        while True:
            if n[-1]=='0':
                print(f'{n} is not cyclic')
                break
            n1 = str(step * int(n))
            if len1 > len(n1):
                n1 = '0'*(len1-len(n1))+n1
            n1_out = sorted(list(n1[len(n1)-len1:]))
            if n1 == '9'*len(n1) or n1_out == n_in:
                print(f'{n} is cyclic')
                break
            if n1_out != n_in:
                # print(n1)
                # print(n1_out)
                # print(n_in)
                print(f'{n} is not cyclic')
                break
            else:
                step += 1

    except EOFError:
        break
