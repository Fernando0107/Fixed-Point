# Python program to check fixed point in an array using linear search


def linearSearch(arr, n):
    it = 0

    for i in range(n):
        if arr[i] is i:
            return i, it
        it+=1
    # If no fixed point present then return -1
    return ("No fixed point for the given vector.")


# Driver program to check above functions
arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
n = len(arr)
print("Fixed Point is " + str(linearSearch(arr, n)))
