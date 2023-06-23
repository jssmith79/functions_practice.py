# # Day 1
# # def hello():
# #     print("hello")


# # def pack(socks, shoes, shirts):
# #     return [socks, shoes, shirts]


# # def eat_lunch(food):
# #     if len(food) == 0:
# #         print("my lunchbox is empty")
# #     else:
# #         for i in range(len(food)):
# #             if i == 0:
# #                 print(f"first I eat {food[0]}")
# #             else:
# #                 print(f"Next I eat my {food[1]}")
# #     food = ["sandwich", "potato chips", "fruit", "yogurt"]
# #     return print(food)


# # Day 2 - activity1

# def arb_args(*args):
#     for a in args:
#         print(a)


# def inner_func(x,y):
#     def inner_1():
#         return x + y
#     def inner_2():
#         return x - y 
#     print(inner_1()+inner_2())

# def lunch_lady(name, lunch="mac n cheese"):
#     print(name, lunch)

# def sum_n_product(x,y):
#     return x+y, x*y

# alias_arb_args = arb_args


# #useful for INTERVIEWS

# def arb_mean(*args):
#     total = 0
#     for a in args:
#         total += a
#     print(a/len(args))

# def arb_longest_string(*args):
#     long = 0
#     longest = ""
#     for a in args:
#         if len(a) > long:
#             long = len(a)
#             longest = a
#         return longest

# # Day 2 activity 2 Key Word Aguments... KWARG

# def name_args(**kwargs):
#     for kwarg in kwargs:
#         print(kwarg, kwargs[kwarg])
# name_args(a=10, b=20, c=30)

# def name_args(**kwargs):
#     return all(kwargs.values())
# print(name_args(a=True, b=True, c=False))

#DAY 2 AFTER CLASS FUNCTIONS

#find the max of 3 numbers
def max_num(a,b,c):
    lst = [a, b, c]
    return max(lst)

print(max_num(10,1000,2987))

#multiply 3 numbers in the function
def mult_list(x,y,z):
    lst = [x,y,z]
    return x*y*z

print(mult_list(2,10,11))

#function to reverse the string

def rev_string(my_string):
    return my_string[::-1]
print(rev_string("USA #1!"))

def num_within(number, start_range, end_range):
    return start_range <= number <= end_range
print(num_within(3,2,4))
print(num_within(10,5,10))
print(num_within(90,1,80))

# def pascal():