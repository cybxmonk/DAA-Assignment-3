def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        last_merged = merged[-1]
        current_interval = intervals[i]

        if current_interval[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current_interval[1])
        else:
            merged.append(current_interval)

    return merged

if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result = merge(intervals)
    print("Merged intervals:", result)
