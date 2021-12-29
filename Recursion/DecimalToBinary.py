def DecimalToBinary(num):
    if num == 0:
        return 0
        return num % 2 + 10 * DecimalToBinary(num//2)


print(DecimalToBinary(324))
