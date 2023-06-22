def hello():
    print("hello")


def pack(socks, shoes, shirts):
    return [socks, shoes, shirts]


def eat_lunch(food):
    if len(food) == 0:
        print("my lunchbox is empty")
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"first I eat {food[0]}")
            else:
                print(f"Next I eat my {food[1]}")
    food = ["sandwich", "potato chips", "fruit", "yogurt"]
    return print(food)