def prefix_average1(S):
    """Rerurn list such that, for all j, A[j] equals average of S[0],....S[j]"""
    n = len(S)
    A = [0] * n
    for j in range(n):
        total = 0
        for i in range(j+1):
            total += S[i]
        A[j] = total /(j+1)
    print(A)
 
if __name__ == "__main__":
    prefix_average1([2,3,4,8,34,6,12,17])
