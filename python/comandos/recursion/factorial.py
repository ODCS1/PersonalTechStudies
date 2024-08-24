# FIRST FORM
def factorial1(n, m=1):
    # base case
    if n == 0:
        return m
    
    m *= n

    # recursion case
    return factorial1(n-1, m)

# SECOND FORM
def factorial2(n):
    if n < 1:
        return 1
    
    return n * factorial2(n-1)


def main():
    n = 4
    n_factorial1 = factorial1(n)
    n_factorial2 = factorial2(n)
    print(n_factorial1)
    print(n_factorial2)

main()