# A function to draw tick marks dividing an inch for an English ruler.
def draw_interval(n):
    if n>0:
        draw_interval(n-1)
        print("-"*n)
        draw_interval(n-1)