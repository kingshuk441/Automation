def merge(arr1, arr2):
    size_1 = len(arr1)
    size_2 = len(arr2)

    res = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if str.startswith(arr1[i], "_") and str.startswith(arr2[j], "_"):
            idx1 = arr1[i].rindex("_")
            idx2 = arr2[j].rindex("_")
            str1 = arr1[i]
            str2 = arr2[j]
            if len(arr1[i]) == 1:
                res.append(arr1[i])
                i += 1
                continue
            if len(arr2[j]) == 1:
                res.append(arr2[j])
                j += 1
                continue
            if len(arr1[i]) > idx1 + 1:
                str1 = str1[idx1 + 1:]
            if len(arr2[j]) > idx2 + 1:
                str2 = str2[idx2 + 1:]
            if isLower(str1, str2):
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        elif str.startswith(arr1[i], '_') or str.startswith(arr2[j], "_"):
            if str.startswith(arr1[i], '_'):
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        elif arr1[i] <= arr2[j]:
            res.append(arr2[j])
            j += 1
        else:
            res.append(arr1[i])
            i += 1

    res = res + arr1[i:] + arr2[j:]
    return res


def isLower(str1, str2):
    if str.lower(str1) <= str.lower(str2):
        return True
    return False


def mergeSort(arr, lo, hi):
    if lo == hi:
        return [arr[lo]]
    mid = int(hi + (lo - hi) / 2)
    left = mergeSort(arr, lo, mid)
    right = mergeSort(arr, mid + 1, hi)
    return merge(left, right)


def SortingColumn(arr):
    lo = 0
    hi = len(arr) - 1
    return mergeSort(arr, lo, hi)
