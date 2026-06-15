sequence = [
1,1,0,1,0,0,1,1,0,1,
1,0,1,0,0,1,1,0,1,0
]

ones = sequence.count(1)
zeros = sequence.count(0)

print("Randomness Test Results")
print("Ones :", ones)
print("Zeros:", zeros)

difference = abs(ones - zeros)

print("Difference:", difference)

if difference <= 2:
    print("Balanced distribution detected")
else:
    print("Weak randomness observed")