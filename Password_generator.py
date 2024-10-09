import random
pass1=["a","b","c","d","e","f","g","h"
        "i","j","k","l","m","n","o","p"
        ,"q","r","s","t","u","v","w","x"
        ,"y","z","!","@","#","%","^","&","0"]
password=""
for x in range(16):
 password=password+random.choices(pass1)[0]
print("Your password is:\n",password) 
       