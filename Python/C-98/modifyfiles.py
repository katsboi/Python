def counter():
    test= open("test.txt")
    x = test.read()
    y = x.split()
    print(len(y)) 
counter()