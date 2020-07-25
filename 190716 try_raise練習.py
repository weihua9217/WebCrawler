try:
    A = int(input('請輸入整數:'))
    print('{0}為{1}'.format(A, '奇數' if A % 2 else '偶數'))
except ValueError:
    print('請輸入阿拉伯數字')
