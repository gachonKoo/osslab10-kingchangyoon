import sys
def get_divisors(number):
    divisors = [str(i) for i in range(1, number + 1) if number % i == 0]
    return divisors
if __name__ == "__main__":    
    if len(sys.argv) > 1:
        number = int(sys.argv[1])
        divisors = get_divisors(number)
        print(" ".join(divisors))
    else:
        print("Please provide a number as a command line argument.")
