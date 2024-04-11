list = []

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        list.append("FizzBuzz")
    if i % 3 == 0:
        list.append("Buzz")
    if i % 5 == 0:
        list.append("Fizz")
    else:
        list.append(i)
    
print(list)
