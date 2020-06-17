import random
print("Jello")
print("hello")

#generate random numbers until number generated > .99
tracker = True


while tracker:
    number = random.random()
    tracker = number < .99
