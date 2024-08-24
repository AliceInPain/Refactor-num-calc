
def add(z):
    result = []
    print("Adding x and y...")
    for index, (x, y) in enumerate(zip(z["x"], z["y"]), start=1):
        result.append((index, x + y))  # list of tuples (index1,result1)..
    for index, value in result:
        print(f"Result for x{index}, y{index}: {value}")


def multiply(z):
    result = []
    print("Multiplying x and y...")
    for index, (x, y) in enumerate(zip(z["x"], z["y"]), start=1):
        result.append((index, x*y))
    for index, value in result:
        print(f"Result for x{index}, y{index} is: {value}")


def divide(z):
    result = []
    print("Dividing x by y...")
    for index, (x, y) in enumerate(zip(z["x"], z["y"]), start=1):
        if y != 0:
            result.append((index, x/y))
        else:
            print("Not divisible by zero")
    for index, value in result:
        print(f"Result for x{index}, y{index} is: {value}")


def summ(numbers):
    result = []
    for index, list_ in enumerate(numbers, start=1):
        total = 0
        for num in list_:
            total = total + num
        result.append((index, total))
    for index, total in result:
        print(f"Total sum of list{index} is: {total}")


def main():

    z = {
        "x": [5, 7, 9,],
        "y": [10, 3, 4]
    }


    numbers = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10]
    ]

    add(z)
    multiply(z)
    divide(z)
    summ(numbers)


if __name__ == "__main__":
    main()
