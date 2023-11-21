#wite a function to count the contVowel(string)
message = input ("Enter a text:")
v= "aoeui"
counter = 0
def CountVowels(message,v):
    for chr1 in message:
         if (chr1 in v):
             counter+= 1
           
print(counter)    
