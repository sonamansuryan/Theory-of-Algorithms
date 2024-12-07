def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    print("L: ", left)
    print("H: ",right)
    print(f"Որոնվող արժեք՝ {target}")

    while left <= right:
        mid = (left + right) // 2
        print(f"\n Միջին արժեքը՝ arr[{mid}] = {arr[mid]}")
        
        if arr[mid] == target:
            print(f"Արժեքը գտնվել է ինդեքս {mid}-ում։")
            return mid
        elif arr[mid] < target:
            print(f"Արժեքը մեծ է {arr[mid]}-ից։ Շարժվում ենք աջ։")
            left = mid + 1
        else:
            print(f"Արժեքը փոքր է {arr[mid]}-ից։ Շարժվում ենք ձախ։")
            right = mid - 1

    print("Արժեքը չգտնվեց։")
    return -1

text = input("Մուտքագրեք ցուցակ (թվերը պետք է լինեն ստորակետով առանձնացված): ")
target = int(input("Մուտքագրեք փնտրվող թիվը: "))

numbers = list(map(int, text.split(',')))
numbers.sort()  
print("\nԴասավորված ցուցակ՝", numbers)

binary_search(numbers, target)
