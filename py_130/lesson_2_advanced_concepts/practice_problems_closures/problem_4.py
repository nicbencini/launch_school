
def printer(message):
    print(message)


def later(func, argument):

    def warning():
        func(argument)

    return warning

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!