name = "Ittesaf"
for a in name:
    print(a)
for b in range(50):
    print(b)

i = int(input("Enter a number = "))
sum = 0
for r in range(50, i-1):
    sum = sum + r
    print(sum)
string = input("Enter your name = ")
string2 = ''
for s in string:
    string2 = s + string2
print("orginal = ",string)
print("reverse = ",string2)

c = int(input("Enter a number = "))
for g in range(c, -100000000, c-1):
    print(g)

for x in range(100):
    if x == 50:
        print("Cgange the voice")
        break
    print(x)

for n in range(100):
    print(n)
else:
    print("finished")

print("Vowel finder")
sentence = input("Enter a sentence = ")
vowel = 'aeiouAEIOU'
vowel_count = 0
for char in sentence:
    if char in vowel:
        vowel_count = vowel_count + 1
print("Number of vowel = ",vowel_count)