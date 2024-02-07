def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    test_array = [5, 2, 4, 7, 1, 3, 2, 6]
    sorted_array = merge_sort(test_array)

    print("Original Array:", test_array)
    print("Sorted Array:", sorted_array)

#Original Array: [5, 2, 4, 7, 1, 3, 2, 6]
#Sorted Array: [1, 2, 2, 3, 4, 5, 6, 7]
