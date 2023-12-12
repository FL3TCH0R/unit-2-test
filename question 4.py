def triangle(N):

    if N==1:
        return 1 #if N is equal to 1 the factorial will be 1
    else:
        return N + triangle(N-1)

print(triangle(5))

    
