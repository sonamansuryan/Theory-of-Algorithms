def search_pattern():
    text = input("Մուտքագրեք տեքստը: ")
    pattern = input("Մուտքագրեք որոնվող նախշը: ")

    n = len(text)
    m = len(pattern)
    found = False

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1

        if j == m:
            print(f"Նախշը գտնվել է {i} ինդեքսում:")
            found = True

    if not found:
        print("Տեքստում նախշը չի գտնվել:")

search_pattern()
        

    
