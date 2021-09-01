string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
final = []

i = 0
count = 0
while i < len(string1):
    letter = string1[i]
    j = i
    while j < len(string2):
        if string1[j] == letter:
            final.insert(count, string2[j])
            count += 1
        j += 1
    i += 1
print(final)
