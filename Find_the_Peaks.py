def findPeaks(mountain):
    peaks = []
    for i in range(1, len(mountain) - 1):
        if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
            peaks.append(i)
    return peaks

print(findPeaks([1, 4, 3, 8, 5]))
