def prefix_average3(S):
    n = len(S)
    A = n * [0]
    total = 0
    for j in range(n):
        total +=S[j]
        A[j] = total/(j+1)
    print(A)

if __name__ =="__main__":
    prefix_average3([2,5,6,8,23,12,45])