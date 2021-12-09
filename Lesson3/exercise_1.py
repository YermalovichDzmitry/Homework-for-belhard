def concat(*args: str, reversed=False) -> str:
    args = list(args)
    if reversed:
        args = [word for word in args[::-1]]
    concat_str = "".join(args)
    print(concat_str)
    return concat_str


concat("Hello", " ", "world")
