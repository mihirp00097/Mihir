import math
n=int(input("enter a number."))
if 0 <= n < 10:
    print(f"square of {n}:{n**2}")
elif 10 <= n < 100:
        print(f"square root of {n}:{math.sqrt(n):.2f}")
elif 100 <= n < 1000:
            print(f"cube of {n}:{n**(1/3)}:.2f)")
else:
                print("please enter a number between 0 to 999.")