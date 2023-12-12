def message():

    n=input("enter a message:") #a statement prompting the user to enter a message

    for ch in n:
        print(ord(ch),end=" ") # this loop ensures that for each character it will give the unicode value



message()
