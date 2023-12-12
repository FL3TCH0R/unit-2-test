import math

def quadratic():
    a=int(input("Enter coefficient a:")) #prompting the user to enter all coefficients
    b=int(input("Enter coefficient b:"))
    c=int(input("Enter coeffcient c:"))

    discRoot=math.sqrt((b**2)-4*a*c)#this is the formula for the discriminant

    root1=(-b+discRoot)/(2*a) #this is to find the two possible solutions
    root2=(-b-discRoot)/(2*a)

    print("The roots are",root1,"and",root2) #the final statement

quadratic()
