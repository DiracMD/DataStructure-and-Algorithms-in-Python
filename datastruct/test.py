n = input()
n1 = n.split()
n1.reverse()
for i in range(len(n1)):
    print(n1[i]+n[i-1])
    
