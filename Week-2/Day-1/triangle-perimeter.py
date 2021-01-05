def largestPerimeter(A):
    i = 0
    j = 1
    k = 2
    sum = 0
    while i < len(A) and j < len(A) and k < len(A):
        curr_sum = A[i] + A[j] + A[k]

        max1 = max(A[i], A[j], A[k])
        min1 = min(A[i], A[j], A[k])
        mid1 = mid(A[i], A[j], A[k])

        if A[i] < A[j] and A[i] < A[k]:
            i = max(i, j, k) + 1
        elif A[j] < A[i] and A[j] < A[k]:
            j = max(i, j, k) + 1
        elif A[k] < A[i] and A[k] < A[j]:
            k = max(i, j, k) + 1
        elif max1 <= min1 + mid1:
            return sum
        else:
            sum = max(curr_sum, sum)
            break
        
        sum = max(curr_sum, sum)

    return sum

def mid(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

print(largestPerimeter([3, 6, 2, 3]))
print(largestPerimeter([1, 2, 1]))
# print(largestPerimeter([3, 6, 2, 3]))