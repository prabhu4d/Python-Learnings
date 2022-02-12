v = 100 # global scope

def value():
    v = 200   #local scope
    print(v)

value()
print(v)

##############################################################

f = 123  #global

def val():
    global f
    print(f)
    f = 321

val()
print(f)
