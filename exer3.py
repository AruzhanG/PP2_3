def solve(numheads, numlegs):
    for x in range(numheads + 1):
        y = numheads - x
        if 2 * x + 4 * y == numlegs:
            return x,y

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
if result:
    chickens, rabbits = result
    print(f"Numbers of chicken: {chickens}")
    print(f"Numbers of chicken: {rabbits}")
else:
    print("No solition")