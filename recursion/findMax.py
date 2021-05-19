def findMaxNum(arr, n):  # M(n)
    if n == 1:  # O(1)
        return arr[0]  # O(1)
    return max(arr[n-1], findMaxNum(arr, n-1))  # M(n-1)

# big-O of recursive algorithm?
# recursive is assumed to take M(n)
# equation above equals M(n)=O(1)+M(n-1)
# equals O(n)
# recursive function that makes multiple calls is O(2^n)
