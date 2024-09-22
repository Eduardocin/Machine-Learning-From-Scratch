#Genarators

def return_n_values(n):
    num = 0
    while num < n:
        yield num
        num += 1


