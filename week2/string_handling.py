s= " hello python!"
print(s.strip())
print(s.lower())
print(s.upper())
print(s[0:5])    
s2 = s.strip()
print(s2[0:5])  
words = s2.split()
print(words)
print(" ".join(words))
print(s2.replace("python", "World"))

'''strip() → trim spaces

lower()/upper() → letters change

s[a:b] → slicing

split() → break into list

join() → join list back to string

replace() → replace words'''