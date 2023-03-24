# # Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird

if __name__ == '__main__':
    n = int(input("Ingresa un numero: ").strip())
    if n % 2 == 1:
        print("Weird")
    if n % 2 == 0 and n <= 5:
        print("Not weird")
    if n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")        
    if n % 2 == 0 and n > 20:
        print("Not Weird")