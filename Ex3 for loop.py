#write a program to calculate th sum of series up to n term, for example n=5 the seiries will become 2+22+222+2222+22222=24690
n = 5
sum=0
for i in range (1, n + 1):
    result= "2" *i
    sum += int(result)
print(sum)