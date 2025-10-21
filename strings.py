# String Operations 

# String reversal
ss = "Hello"
print("Reverse: ", ss[1::-1])
s = list(ss)
start, end = 0, len(s)-1
while start < end:
    temp = s[start]
    s[start] = s[end]
    s[end] = temp
    start += 1
    end -= 1
s = ''.join(s)
print("string: ", str(s))