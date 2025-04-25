def decor(f):
    def wrapper():
        f()
        print("@@@@@@@@@@@@@@")

    return wrapper


@decor
def msg():
    print("Hello")
    print("Hello")


# can be done this way
# m = decor(msg)
# m()

msg()
