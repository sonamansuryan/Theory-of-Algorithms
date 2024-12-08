text = input("Մուտքագրել տողը: ")

longest_palindrome = ""
for i in range(len(text)):
    for j in range(i + 1, len(text) + 1):
        substring = text[i:j]
        if substring == substring[::-1] and len(substring) > len(longest_palindrome):
            longest_palindrome = substring

print("Ամենաերկար պալինդրոմը։", longest_palindrome)
