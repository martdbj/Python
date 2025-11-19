def decimal_a_binario(decimal):
    if decimal < 2:
        if decimal == 1:
            return "1"
        else:
            return "0"
    else:
        return decimal_a_binario(decimal // 2) + decimal_a_binario(decimal % 2)

print(decimal_a_binario(9))