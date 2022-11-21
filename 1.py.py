def b3(n):
    if (n == 0):
        return
    a = n % 3
    n //= 3
    if (a < 0):
        n += 1
    b3(n)
    if (a < 0):
        print(a+(3* -1), end = "")
    else:
        print(a, end = "")
 
def convert(n): 
    if (n != 0):
        b3(n)
    else:
        print("0", end = "")
 
n=int(input())
convert(n)