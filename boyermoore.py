def boyer_moore(pattern, text):
    m = len(pattern)
    n = len(text)
    
    bad_char = {}
    for i in range(m):
        value = m - i - 1
        if pattern[i] in bad_char:
            bad_char[pattern[i]] = min(bad_char[pattern[i]], value)

        else:
            bad_char[pattern[i]] = value

    bad_char[pattern[-1]] = m

    print(f"Սիմվոլի աղյուսակը՝ {bad_char}")

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:  
            print(f"Նմուշը գտնվել է` {i} ինդեքսում")
            i += m
        else: 
            shift = bad_char.get(text[i + j], m)
            i += max(1, shift)


pattern = input("Նմուշը: ")
text = input("Տեքստը: ")
boyer_moore(pattern, text)
    
    
