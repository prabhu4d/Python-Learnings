"""

"""


class Counter():
    static_public = "Public Counter"
    _static_protected = "Protected Counter"
    __static_private = "Private Counter"

    def __init__(self):
        self.__current = 0 # Private Member
        self._step = 1     # Protected Member

    def increment(self):
        self.__current += self._step

    def value(self):
        return self.__current

    def __set_zero(self):
        self.__current = 0

    def reset(self):
        self.__set_zero()

    def set_current(self, num):
        self.__current = num

    @property
    def static_private(self):
        return self.__static_private


counter = Counter()

# Assigning Value for Protected Member
counter._step = 5
print(counter._step)

# Calling Public method inorder to access private attriutes
counter.increment()
counter.increment()
counter.reset()
counter.set_current(100)

# but private variable can be access like this
# python mask like this around __variable
print(counter._Counter__current)


class Timer(Counter):
    static_public = "Public Timer"
    _static_protected = "Protected Timer"
    __static_private = "Private Timer"

    def __init__(self, time):
        Counter.__init__(self)
        self.time = time
    
    @property
    def static_private(self):
        return self.__static_private


timer = Timer(10)
timer._step = 100
timer.increment()
timer.increment()
print(f"Timer {timer.value()}")

print("---- Static ----")
print(counter.static_public)
print(counter._static_protected)
print(counter.static_private)
print(timer.static_public)
print(timer._static_protected)
print(timer.static_private)