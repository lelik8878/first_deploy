
def return_name(fn):
    def wrapper():
        our_name = input('What is your name?\n')
        print(f'Hi {our_name}')
        fn()
    return wrapper

def print_name():
    print('Hello world')


without_decorator = print_name

with_decorator = return_name(print_name)

without_decorator()

with_decorator()


