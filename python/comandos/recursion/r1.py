
# # THE IDEIA OF THIS FUNCTION IS TO RETURN ALL THE EVEN VALUES IN THE PROPER VALUE PASSED
def recursion(n, arr=[]) -> list[int]:

    if n < 0:
        return arr

    if n % 2 == 0 and n > -1:
        arr.append(n)
    else:
        n += 1

    return recursion(n-2, arr)




def main():
    n = 10
    array = recursion(n)
    print(f"ALL VALUES OF THE ARRAY: {array}")

main()
