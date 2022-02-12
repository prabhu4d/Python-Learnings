"""

"""


class decorator_class:
    def __init__(self, original_fn):
        self.original_fn = original_fn

    def __call__(self, *args, **kwargs):
        print("Running wrapper fn for {}".format(self.original_fn.__name__))
        return self.original_fn(*args, **kwargs)


@decorator_class
def display():
    """
    this @ syntax is doing
    display = decorator_fn(display)
    """
    print("This is Original Function")


@decorator_class
def display_info(name, age):
    print(f'display_info -> user bio ({name} {age})')


display()
display_info("Prabhu", 22)
