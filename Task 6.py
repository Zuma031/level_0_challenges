def max( a, b ):
    if a > b:
        return a
    return b
def maxx( a, b, c, d ):
    return max( a, max( b, c ) )
print("max number is ",maxx(1, 22, 3, 2))