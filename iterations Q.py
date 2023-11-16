# assume that you have a message like "hello" , your messsage was encrypted to be like "khoor"
#write program code to decrepit the following message the folowing message to get the orainal one message=
#|rx#duh#juhdwh|

message= "|rx#duh#juhdwh"
x = 0
while(x<len(message)):
    new = ord(message[x])-3
    print(chr(new), end=" ")
    x+=1
   
   