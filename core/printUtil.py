def clear_print(st, clear_chars=10):
    print("\r" + " " * clear_chars + "\r", end="")
    print(st, end="")
