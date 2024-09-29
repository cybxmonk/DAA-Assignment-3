class Pair:
    def __init__(self, min_val=None, max_val=None):
        self.min = min_val
        self.max = max_val

def find_max_min(arr, low, high):
    result = Pair()
    
    if low == high:
        result.max = arr[low]
        result.min = arr[low]
        return result
    
    if high == low + 1:
        if arr[low] > arr[high]:
            result.max = arr[low]
            result.min = arr[high]
        else:
            result.max = arr[high]
            result.min = arr[low]
        return result

    mid = (low + high) // 2

    left = find_max_min(arr, low, mid)
    right = find_max_min(arr, mid + 1, high)

    result.min = min(left.min, right.min)
    result.max = max(left.max, right.max)

    return result

if __name__ == "__main__":
    arr = [3, 5, 1, 8, 7, 2, 6]

    result = find_max_min(arr, 0, len(arr) - 1)

    print("Minimum element:", result.min)
    print("Maximum element:", result.max)
