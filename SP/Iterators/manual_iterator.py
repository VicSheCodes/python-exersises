
def play_with_iterators():
    lst = [1, 2, 3, 4, 5, 6,]
    itr = iter(lst)
    try:
        for _ in range(len(lst)):
            print(next(itr))
    except StopIteration:
        print(f"\n Stop iteration when iterator is exausted. ")


if __name__ == "__main__":
    play_with_iterators()
