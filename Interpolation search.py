def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    
    while low <= high and key >= arr[low] and key <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == key:
                return low
            return -1
        
        mid = low + ((key - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        print(f"Միջին կետը։ ինդեքս` {mid}, արժեքը` {arr[mid]}")
        
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

arr = list(map(int, input("Մուտքագրել թվերը դրանք ստորակետներով առանձնանցնելով։ ").split(",")))
key = int(input("Մուտքագրել որոնվող թիվը։ "))
sorted_arr = sorted(arr)
print("Դասավորված ցանկ։", sorted_arr)

result = interpolation_search(sorted_arr, key)
if result != -1:
    print(f"Որոնվող թիվը գտնվել է {result} ինդեքսում։")
else:
    print("Որոնվող թիվը չի գտնվել")
