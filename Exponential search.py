def binary_search(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2  
        print(f"Միջին կետ։ ինդեքսը՝ {mid}, արժեքը՝ {arr[mid]}")  
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
def exponential_search(arr, key):
    if arr[0] == key:
        return 0  
    
    i = 1
    while i < len(arr) and arr[i] < key:
        print(f"Բարելավված սահման՝ {i}, արժեքը՝ {arr[i]}")  
        i *= 2

    return binary_search(arr, i // 2, min(i, len(arr) - 1), key)

arr = list(map(int, input("Մուտքագրել թվերը դրանք ստորակետներով առանձնանցնելով։ ").split(",")))
key = int(input("Մուտքագրել որոնվող թիվը։ "))
sorted_arr = sorted(arr)
print("Դասավորված ցանկ։", sorted_arr)

result = exponential_search(sorted_arr, key)
if result != -1:
    print(f"Որոնվող թիվը գտնվել է {result} ինդեքսում։")
else:
    print("Որոնվող թիվը չի գտնվել")

