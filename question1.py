
def to_8bit(n):
    return format(n & 0xFF, '08b')

def from_8bit(binary):
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value

def calculate(a, b, operator):
    A = to_8bit(a)
    B = to_8bit(b)

    if operator == '+':
        result = a + b
        effective_b = b
    else:
        result = a - b
        effective_b = -b

    # 8-bit binary operands used for addition
    B_used = to_8bit(effective_b)
    binary_result = to_8bit(result)
    decimal_result = from_8bit(binary_result)

    print("\nExpression:", a, operator, "(" + str(b) + ")")
    print("Operand A:", A)
    print("Operand B:", B)
    
    if operator == '-':
        print("2's complement of B:", B_used)
    print("Binary result:", binary_result)
    print("Decimal result:", decimal_result)

    if result < -128 or result > 127:
        print("Overflow: YES")
    else:
        print("Overflow: NO")

# Given expressions
calculate(46, 29, '+')
calculate(-48, -23, '-')
