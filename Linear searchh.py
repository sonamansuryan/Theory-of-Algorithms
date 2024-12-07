text = input("Մուտքագրեք տեքստը: ")
pattern = input("Մուտքագրեք նախշը: ")

for i in range(len(text) - len(pattern) + 1):  
    match = True
    print(f"\nՔայլ {i + 1}: Տեքստի ինդեքս {i} - Ստուգում նախշը սկսած {text[i:i+len(pattern)]}")

    for j in range(len(pattern)):
        print(f"  Տառը տեքստից՝ {text[i + j]} և նախշից՝ {pattern[j]}")
        if text[i + j] != pattern[j]: 
            match = False
            print(f"  Գործընթացը կանգնեց՝ համընկնում չկա: {text[i + j]} != {pattern[j]}")
            break

    if match:
        print(f"  Նախշը գտնվեց ինդեքսում {i}")

        
