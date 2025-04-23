def quickCalc(value):
    value += (value - 1) * 2
    return value


x = int(input("Enter the amount of levels in your pyramid: "))
x = quickCalc(x)
print("This would require a", x, "by", x, "pyramid with", x*x, "blocks")

