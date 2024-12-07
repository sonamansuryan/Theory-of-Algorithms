import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  
    prev = 0
    
    print(f"Որոնվող արժեք՝ {target}")

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            print("Արժեքը չգտնվեց։")
            return -1

    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            print("Արժեքը չգտնվեց։")
            return -1

    if arr[prev] == target:
        print(f"Արժեքը գտնվել է ինդեքս {prev}-ում։")
        return prev

    print("Արժեքը չգտնվեց։")
    return -1

text = input("Մուտքագրեք ցուցակ (թվերը պետք է լինեն ստորակետով առանձնացված): ")
target = int(input("Մուտքագրեք փնտրվող թիվը: "))

numbers = list(map(int, text.split(',')))
numbers.sort()  

print("\nԴասավորված ցուցակ՝", numbers)

jump_search(numbers, target)
