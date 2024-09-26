# Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits

#                    Answers
# VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV










S = str(input())
lower = []
upper = []
odd = []
even = []
L = [i for i in S]
L.sort()
for i in L:
    if ord(i) >= 97:
        lower = lower + [i]
    elif ord(i) <= 97 and ord(i) >= 65 :
        upper = upper + [i]
    elif ord(i) <= 65:
        if int(i) % 2 != 0:
            odd.append(str(i))
        else:
            even.append(str(i))
L = lower + upper + odd + even
S = "".join(L)
print(S)
