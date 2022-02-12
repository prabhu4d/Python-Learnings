from quark import Quark

q = Quark()

q.flavor = "top"
q.flip()
print(q.flavor)