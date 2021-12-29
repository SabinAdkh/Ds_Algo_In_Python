def powerofDigit(base, exp):
    assert exp>=0 and int(exp) == exp, "The exponent must be positive integer only"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return int(base) * powerofDigit(base, exp-1)

print(powerofDigit(5, 2))