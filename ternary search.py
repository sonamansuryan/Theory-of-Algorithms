def ternary_search(arr, target):
    left = 0
    right = len(arr) - 1
    print(f"Որոնվող արժեք՝ {target}")
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        print(f"\nՄիջին կետերը՝ arr[{mid1}] = {arr[mid1]}, arr[{mid2}] = {arr[mid2]}")
        
        if arr[mid1] == target:
            print(f"Արժեքը գտնվել է ինդեքս {mid1}-ում։")
            return mid1
        elif arr[mid2] == target:
            print(f"Արժեքը գտնվել է ինդեքս {mid2}-ում։")
            return mid2
        
        elif target < arr[mid1]:
            right = mid1 - 1
            print(f"Արժեքը փոքր է {arr[mid1]}-ից։ Շարժվում ենք ձախ։")
        
        elif target > arr[mid2]:
            left = mid2 + 1
            print(f"Արժեքը մեծ է {arr[mid2]}-ից։ Շարժվում ենք աջ։")
        
        else:
            left = mid1 + 1
            right = mid2 - 1
            print(f"Արժեքը գտնվում է {arr[mid1]}-ի և {arr[mid2]}-ի միջև։ Շարժվում ենք միջին հատվածում։")

    print("Արժեքը չգտնվեց։")
    return -1

text = input("Մուտքագրեք ցուցակ (թվերը պետք է լինեն ստորակետով առանձնացված): ")
target = int(input("Մուտքագրեք փնտրվող թիվը: "))

numbers = list(map(int, text.split(',')))
numbers.sort()  
print("\nԴասավորված ցուցակ՝", numbers)

ternary_search(numbers, target)
