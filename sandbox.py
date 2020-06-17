import random
print("Jello")
print("hello")

#generate random numbers until number generated > .99
tracker = True
counter = 0;

while tracker:
    number = random.random()
    counter += 1
    print(str(counter) + ": " + str(number))
    tracker = number < .99
