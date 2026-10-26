
def ROR(binary, positions):
    print("\nROR (Rotate Right Without Carry)")
    print("Original:", binary)

    for i in range(positions):
        last_bit = binary[-1]
        binary = last_bit + binary[:-1]
        print("Step", i + 1, ":", binary)

    print("Final ROR result:", binary)


def RCR(binary, positions, carry=0):
    print("\nRCR (Rotate Right Through Carry)")
    print("Original:", binary)
    print("Initial carry:", carry)

    for i in range(positions):
        last_bit = int(binary[-1])
        binary = str(carry) + binary[:-1]
        carry = last_bit
        print("Step", i + 1, ":", binary,
              "Carry:", carry)

    print("Final RCR result:", binary)
    print("Final carry:", carry)


number = "11010101"

ROR(number, 3)
RCR(number, 3, 0)
