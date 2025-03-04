#CHARACTER-ASCII CODE
val= input()
if(ord(val)>=65 and ord( val)<=90):
    print(" upper case alphabets")
elif(ord(val)>=97 and ord(val)<=122):
    print("lower alphabets")
    
elif(ord(val)>=48 and ord(val)<=57):
           print("Numbers")
else:
    print("special character")
#END
