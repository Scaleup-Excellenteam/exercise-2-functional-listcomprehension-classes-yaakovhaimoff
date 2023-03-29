"""Yaakov Haimoff"""

def type_check(correct_type):
    def decorator(func):
        def wrapper(function_args):
            """This is the wrapper function to check if the argument is of the correct type"""
            if correct_type != type(function_args):
                raise TypeError("The argument did not received the correct argument which is {0} "
                                "for type {1}".format(function_args, correct_type))
            return func(function_args)

        return wrapper

    return decorator


@type_check(int)
def get_param(function_args):
    print("The function received the correct argument which is {0} "
          "for type {1}".format(function_args, type(function_args)))


try:
    print("example 1")
    num = 10
    get_param(num)

    print("example 2")
    string = "hello"
    get_param(string)

except TypeError as e:
    print(e)
