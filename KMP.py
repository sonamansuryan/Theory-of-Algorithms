def lps(pattern):
    lps = [0] * len(pattern) 
    length = 0               
    i = 1                   
    while i < len(pattern):
        if pattern[i] == pattern[length]:  
            length += 1                    
            lps[i] = length               
            i += 1
        else:
            if length != 0:               
                length = lps[length - 1]   
            else:                         
                lps[i] = 0
                i += 1
    print(f"'{pattern}' նմուշի համար LPS զանգվածը: {lps}")  
    return lps

def knuth_morris_pratt(pattern, text):
    F = lps(pattern)         
    n = len(text)           
    m = len(pattern)        

    i = 0  
    j = 0
    matches = []
    while i < n:
        if text[i] == pattern[j]:
            if j == m - 1:  
                matches.append(i - j)
                j = F[j]  
                i += 1
            else:
                i += 1
                j += 1
        elif j > 0:
            j = F[j - 1]  
        else:
            i += 1

    return matches             

pattern = input("Նմուշը: ")
text = input("Տեքստը: ")
result = knuth_morris_pratt(pattern, text)
print(f"Նմուշը հայտնվում է հետևյալ ինդեքսներում՝ {result}")

