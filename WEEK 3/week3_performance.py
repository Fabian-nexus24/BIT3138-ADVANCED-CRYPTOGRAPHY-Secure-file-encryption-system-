import time

start = time.time()

for _ in range(100000):

    text = "ADVANCED CRYPTOGRAPHY"

end = time.time()

execution_time = end - start

print("Execution Time:", execution_time, "seconds")