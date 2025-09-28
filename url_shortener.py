import string
BASE62 = string.digits + string.ascii_letters
def encode(num):
    if num == 0:
        return BASE62[0]
    result = ''
    while num > 0:
        num, rem = divmod(num, 62)
        result = BASE62[rem] + result
    return result
def decode(s):
    num = 0
    for char in s:
        num = num * 62 + BASE62.index(char)
    return num
if __name__ == '__main__':
    number = int(input('Enter a number to encode: '))
    short = encode(number)
    print('Encoded:', short)
    print('Decoded:', decode(short))
