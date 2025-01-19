def notify(message, when):
    print(f"{message} in {when} minutes!")


def later2(func, first_arg):

    def inner(second_arg):
        func(first_arg, second_arg)
    
    return inner

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!