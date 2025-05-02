def decor1(ff):
    def inner():
        print("☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️")
        # print(f().upper())
        return ff().upper()

    return inner


def decor2(f):
    def inner():
        # print(f)
        return print(f().split())

    return inner


@decor2
@decor1
def get_name():
    name = input("Enter Your Name")
    name = name + "   Welcome   " + "☀️☀️☀️☀️☀️☀️"

    return name


# x = decor2(decor1(get_name))


print(get_name())
