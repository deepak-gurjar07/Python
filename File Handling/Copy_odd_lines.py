f = open('abc.txt', 'r') 
f1 = open('abc1.txt', 'w') 
cont = f.readlines() 
type(cont)

for i in range(0, len(cont)): 
    if(i % 2 ! = 0): 
        f1.write(cont[i]) 
    else: 
        pass
    
f1.close()
f.close()
print("copying odd line successful")
