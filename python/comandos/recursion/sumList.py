def sumList(a) -> int:
    # base case
    if not a:
        return 0
    else:
        return a[0] + sumList(a[1:])


def main():
    arr = [1,2,3]
    sum_arr_elements = sumList(arr)
    print(sum_arr_elements)


main()