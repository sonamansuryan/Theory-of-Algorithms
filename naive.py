def search_pattern():
    text = input("Տեքստը: ")
    pattern = input("Նմուշը: ")

    n = len(text)
    m = len(pattern)
    found = False

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            print(f"Նմուշը գտնվել է {i} ինդեքսում:")
            found = True

    if not found:
        print("Տեքստում նմուշը չի գտնվել:")

search_pattern()
        

    
