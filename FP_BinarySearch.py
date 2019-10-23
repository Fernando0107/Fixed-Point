# Main Function to find fixed index using binary search

def binarySearch(arr, low, high):
    if (high < low):
        return ("No fixed point.")

    # low + (high - low) / 2
    mid = int((low + high) / 2)
    midValue = arr[mid]

    if (mid == arr[mid]):
        return mid

    # Search left
    leftindex = min(mid - 1, midValue)
    left = binarySearch(arr, low, leftindex)

    if (left >= 0):
        return left

    # Search right
    rightindex = max(mid + 1, midValue)
    right = binarySearch(arr, rightindex, high)

    return right

# Driver code
if __name__ == '__main__':

    # input 1
    arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]

    n = len(arr)

    print("Fixed Point is", binarySearch(arr, 0, n - 1))

    # input 2
    arr1 = [-10, -1, 3, 3, 10, 30, 30, 50, 100]

    n1 = len(arr)

    print("Fixed Point is",binarySearch(arr1, 0, n1 - 1))


