# Day 1
# def hello():
#     print("hello")


# def pack(socks, shoes, shirts):
#     return [socks, shoes, shirts]


# def eat_lunch(food):
#     if len(food) == 0:
#         print("my lunchbox is empty")
#     else:
#         for i in range(len(food)):
#             if i == 0:
#                 print(f"first I eat {food[0]}")
#             else:
#                 print(f"Next I eat my {food[1]}")
#     food = ["sandwich", "potato chips", "fruit", "yogurt"]
#     return print(food)


# Day 2 - activity1

def arb_args(*args):
    for a in args:
        print(a)


def inner_func(x,y):
    def inner_1():
        return x + y
    def inner_2():
        return x - y 
    print(inner_1()+inner_2())

def lunch_lady(name, lunch="mac n cheese"):
    print(name, lunch)

def sum_n_product(x,y):
    return x+y, x*y

alias_arb_args = arb_args


#useful for INTERVIEWS

def arb_mean(*args):
    total = 0
    for a in args:
        total += a
    print(a/len(args))

def arb_longest_string(*args):
    long = 0
    longest = ""
    for a in args:
        if len(a) > long:
            long = len(a)
            longest = a
        return longest

# Day 2 activity 2 Key Word Aguments... KWARG

def name_args(**kwargs):
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])
name_args(a=10, b=20, c=30)

def name_args(**kwargs):
    return all(kwargs.values())
print(name_args(a=True, b=True, c=False))

