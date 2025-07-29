n, q = input().split()
n = int(n)

data = [chr(i) for i in range(65, 65 + n)]

cmp_cache = {}

def compare(x, y):
    if (x, y) in cmp_cache:
        return cmp_cache[(x, y)]
    if (y, x) in cmp_cache:
        return not cmp_cache[(y, x)]
    print(f"? {x} {y}", flush=True)
    res = input().strip() == '<'
    cmp_cache[(x, y)] = res
    cmp_cache[(y, x)] = not res
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

sorted_data = merge_sort(data)
print("! " + "".join(sorted_data), flush=True)