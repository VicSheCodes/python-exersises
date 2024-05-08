

def high_and_low(lst):
    lst = [int(x) for x in lst.split(" ")]
    return f"{max(lst)} {min(lst)}"

if __name__ == "__main__":
    print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))