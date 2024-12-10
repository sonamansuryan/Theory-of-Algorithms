text = input("Մուտքագրեք տեքստը: ")
pattern = input("Մուտքագրեք նախշը: ")

alphabet = set(text)

pat_len = len(pattern)
trans_func = [{} for i in range(pat_len + 1)]

for state in range(pat_len + 1):
    for char in alphabet:
        next_state = state
        while next_state > 0 and (next_state == pat_len or pattern[next_state] != char):
            next_state -= 1
        if next_state < pat_len and pattern[next_state] == char:
            next_state += 1
        trans_func[state][char] = next_state

state = 0
matches = []

for i, char in enumerate(text):
    state = trans_func[state].get(char, 0)
    if state == pat_len:
        matches.append(i - pat_len + 1)

if matches:
    print("Համընկումներ գտնվել են հետևյալ դիրքերում:", matches)
else:
    print("Համընկումներ չեն գտնվել։")
