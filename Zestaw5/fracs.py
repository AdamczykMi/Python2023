from math import gcd


def add_frac(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    common_denominator = den1 * den2
    new_num = num1 * den2 + num2 * den1
    return simplify_frac([new_num, common_denominator])


def sub_frac(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    common_denominator = den1 * den2
    new_num = num1 * den2 - num2 * den1
    return simplify_frac([new_num, common_denominator])


def mul_frac(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    new_num = num1 * num2
    new_den = den1 * den2
    return simplify_frac([new_num, new_den])


def div_frac(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    new_num = num1 * den2
    new_den = den1 * num2
    return simplify_frac([new_num, new_den])


def is_positive(frac):
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    num1, den1 = frac1
    num2, den2 = frac2
    diff = num1 * den2 - num2 * den1
    if diff > 0:
        return 1
    elif diff < 0:
        return -1
    else:
        return 0


def frac2float(frac):
    return frac[0] / frac[1]


def simplify_frac(frac):
    num, den = frac
    common = gcd(num, den)
    return [num // common, den // common]
