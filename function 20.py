global_var = 10

def change_value():
    global global_var
    global_var = 20

print("Before changing:", global_var)

change_value()

print("After changing:", global_var)
