n, k = map(int, input().split())
matrix1 = [[0]*n for i in range(n)]


def work(mat, number, size,index):
    if not number:
        return mat
    if number >= size*2 - 1:
        for i in range(size):
            mat[index][i+index] = mat[i+index][index] = 1
        if number == size*2 - 1:return mat
        return work(mat, number-size*2 + 1, size-1,index+1)
    else:
        if number % 2:
            number = (number+1)//2
            for i in range(number):
                mat[index][i+index]=mat[i+index][index]=1
            return mat
        else:
            number = (number+1)//2
            for i in range(number):
                mat[index][i+index]=mat[i+index][index]=1
            mat[1+index][1+index]=1
            return mat


if k > pow(n, 2):
    print('-1')
    exit()
else:
    output=work(matrix1, k, n,0)
    for i in range(n):
        print(*output[i])