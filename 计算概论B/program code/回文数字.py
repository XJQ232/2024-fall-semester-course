while True:
    try:
        str1 = input()
        str2 = str1[:]
        str1 = str1[::-1]
        print("YES" if str1 == str2 else "NO")
    except EOFError:
        break