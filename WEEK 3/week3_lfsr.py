def lfsr(seed, taps, length):
    register = seed[:]
    sequence = []

    for _ in range(length):
        output_bit = register[-1]
        sequence.append(output_bit)

        feedback = 0
        for tap in taps:
            feedback ^= register[tap]

        register = [feedback] + register[:-1]

    return sequence


seed = [1, 0, 1, 1]
taps = [0, 3]

result = lfsr(seed, taps, 20)

print("LFSR Generated Sequence:")
print(result)