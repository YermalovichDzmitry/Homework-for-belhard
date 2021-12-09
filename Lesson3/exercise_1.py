def concat(*args, reversed=False):
    args = list(args)
    if reversed:
        args = [word for word in args[::-1]]
    concat_str = "".join(args)
    print(concat_str)
    return 0


concat("Hello", " ", "world", reversed=True)
