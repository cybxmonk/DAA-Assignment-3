class MergeSort:
    def merge(self, arr, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[left + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]

        i, j, k = 0, 0, left

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2

            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)

            self.merge(arr, left, mid, right)

    @staticmethod
    def print_array(arr):
        for i in arr:
            print(i, end=" ")
        print()

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    print("Original array:")
    MergeSort.print_array(arr)

    ms = MergeSort()
    ms.merge_sort(arr, 0, len(arr) - 1)

    print("\nSorted array:")
    MergeSort.print_array(arr)
