import heapq
stack1 = []
while True:
    try:
        str1 = input()
        if str1[:3] == 'pop':
            if stack1:
                stack1.pop()
        if str1[:3] == 'min' and stack1:
            print(stack1[-1])
        if str1[:4] == 'push':
            a = int(str1[5:])
            if stack1:
                if stack1[-1] > a:
                    stack1.append(a)
                else:
                    stack1.append(stack1[-1])
            else:stack1.append(a)
        # print(stack1)
    except EOFError:break