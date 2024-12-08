text = input("Մուտքագրել տողը: ")

char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

odd_count = 0
odd_char = ""
half_palindrome = []

for char, count in char_count.items():
    if count % 2 != 0:
        odd_count += 1
        odd_char = char 
    half_palindrome.append(char * (count // 2))

if odd_count > 1:
    print("Չի կարող դառնալ պալինդրոմ")
else:
    left_half = "".join(half_palindrome)
    middle = odd_char 
    right_half = left_half[::-1]
    
    full_palindrome = left_half + middle + right_half
    print("Կարող է դառնալ պալինդրոմ։", full_palindrome)
