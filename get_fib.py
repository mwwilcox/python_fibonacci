from functools import lru_cache


@lru_cache
def getfib(number: int) -> int:
    if number <= 1:
        return number
    else:
        return getfib(number - 1) + getfib(number - 2)


def main():
    fibnum = int(input("Enter a number: "))
    # fibnum = 3
    print(getfib(fibnum))
    


if __name__ == "__main__":
    main()
