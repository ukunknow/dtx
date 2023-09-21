def can_place_rooms(arr, n, k, mid):
    count = 1
    curr = arr[0]
    
    for i in range(1, n):
        if arr[i] - curr >= mid:
            count += 1
            curr = arr[i]
    
    return count >= k

def largest_minimum_distance(arr, n, k):
    arr.sort()
    
    low = 1
    high = arr[n-1] - arr[0]
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if can_place_rooms(arr, n, k, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return result

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(largest_minimum_distance(A, N, K))
