# #key = range , valve prime or not

# dict1 = {}


# def check_prime(l, u):
#     for number in range(l, u+1):
#         count = 0
#         for i in range(2, (number//2 + 1)):
#             if number % i == 0:
#                 count = count + 1
#                 break
        
#         if count == 0 and number != 1:
#              dict1[number] = 'yes its prime'
#         else:
#             dict1[number] = 'Not prime'


#     return dict1

# l = 10
# u = 30

# print(check_prime(l, u))





from cgitb import reset


def my_decorator(func1):
    def wrapper(*args, **kwargs):
        out_str = args[0].capitalize()
        return func1(out_str)
    return wrapper

@my_decorator
def check_func(inp):
    return inp

print(check_func("python"))        

