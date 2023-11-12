def averages(arr):
    # Check if arr is None or not a list
    if arr is None or not isinstance(arr, list):
        return []

    # Check if the array has at least two elements
    if len(arr) < 2:
        return []

    # Use list comprehension to calculate the average of each pair of consecutive numbers
    result = [(arr[i] + arr[i + 1]) / 2 for i in range(len(arr) - 1)]

    return result