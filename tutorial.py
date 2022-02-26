#tutorial.py
def say_hello(name=None):
    if name != "":
        print("Hello", name)
    else:
        print("Hello Stranger")


if __name__ == "__main__":
    say_hello(input("What's your name? "))