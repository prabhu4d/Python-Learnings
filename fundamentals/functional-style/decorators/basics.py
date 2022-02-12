"""
  decorator function is wrapper function and its add some additional functionality to the original function

"""


def decorator_fn(original_fn):
    def wrapper(*args, **kwargs):
        print("Running wrapper fn for {}".format(original_fn.__name__))
        original_fn(*args, **kwargs)

    return wrapper


@decorator_fn
def display():
    """
    this @ syntax is doing
    display = decorator_fn(display)
    """
    print("This is Original Function")


@decorator_fn
def display_info(name, age):
    print(f'display_info -> user bio ({name} {age})')


display()
display_info("Prabhu", 22)