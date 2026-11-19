def demo():
    a = 10
    b = 20
    c = 30
    d = 40

print("Number of local variables: ",
      demo.__code__.co_nlocals)
