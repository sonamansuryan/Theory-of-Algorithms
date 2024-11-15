def finite_automaton_matcher(text, delta, m):
    n = len(text)
    q = 0  

    for i in range(n):
        q = delta(q, text[i])
        
        if q == m:
            print(f"Նախշը գտնվում է {i - m + 1} ինդեքսում")                   
            q = 0  

def build_delta_function(pattern):
    m = len(pattern)
    def delta(q, char):
        if q < m and char == pattern[q]:
            return q + 1
        return 0
    return delta

text = input("Մուտքագրեք այն տեքստը, որում ցանկանում եք որոնել: ")
pattern = input("Մուտքագրեք այն նախշը, որը ցանկանում եք որոնել: ")
pattern_length = len(pattern)

delta_function = build_delta_function(pattern)
finite_automaton_matcher(text, delta_function, pattern_length)
