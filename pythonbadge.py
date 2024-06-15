# Problem 1

answer = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
print(sum(answer))

# Problem 2

a, b = 0, 1
total = 0
while True:
    a, b = b, a + b
    if b >= 4000000:
        break
    if b % 2 == 0:
        total += b
print(total)

# Problem 3

n = 600851475143
i = 2

while i*i < n:
    while n % i == 0:
        n = n/i
    i = i+1

print(n)










