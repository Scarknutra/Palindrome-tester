#task 1
name = input("Please type a word to check if a palindrome:")
rev = name[::-1]
name = name.replace(" ", "")
name = name.replace(".", "")
if name == rev:
    print ("Is a palindrome")
else:
    print ("is not a palindrome")
print (name)
#task 2
print("I will now check the text inside palindromic.txt for either palindromic rows or columns")
f = open('palindromic.txt')
table = []
for a in range(10):
    table.append([])
b = 0
c = 0
for line in f:
    temp = line.split(" ")
    line = "".join(temp)
    temp = line.split("\n")
    line = "".join(temp)
    if len(line) != 0:
        for c in range(0, len(line)):
            table[b].append(line[c])
        b = b + 1
        for d in range(len(line), int(2*len(line))):
            table[d].append(line[d-5])
length = len(line)
for i in range(0,10):
    for j in range(0,length//2):
        if table[i][j] != table[i][length - j -1]:
            flag = 1
        else:
            flag = 0
    if flag == 0:
        s = ""
        s = ''.join(table[i])
        if i >= 5:
            print(s + " is a palindrome starting at " "[" ,i - length, "]" + "[", j - 1,"]" "and is a column")
        else:
            print(s + " is a palindrom at " ' [', i, ']' + '[', j - 1,']' "and is a row in a table ")
#task 3 and 4
with open ('matrix.txt') as fin:
   lines = (line.split() for line in fin)
#unfinished

