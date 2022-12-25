SNAFU_digits = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
digits_SNAFU = {-2: '=', -1: '-', 0: '0', 1: '1', 2: '2'}


def SNAFU_to_dec(SNAFU):
    acc, base = 0, 1
    for d in SNAFU[::-1]:
        acc += SNAFU_digits[d] * base
        base *= 5
    return acc


def dec_to_SNAFU(dec):
    acc = ''
    while dec > 0:
        r = dec % 5
        if r <= 2:
            dec //= 5
        else:
            r -= 5
            dec = (dec - r) // 5
        acc = digits_SNAFU[r] + acc
    return acc


with open('day25.txt', 'r') as file:
    line = file.readline().strip()
    acc = 0
    while line:
        acc += SNAFU_to_dec(line)
        line = file.readline().strip()

print(dec_to_SNAFU(acc))
