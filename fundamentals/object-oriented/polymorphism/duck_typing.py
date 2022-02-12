"""
If a bird walk like a duck or swim like a duck it is called duck

"""

class VSCode:
  def execute(self):
    print("Formatting")
    print("Debugging")
    print("Compiling")
    print("Running")

  
class PyCharm:
  def execute(self):
    print("Compiling")
    print("Running")


class Programmer:
  def code(self, ide):
    ide.execute()


prabhu = Programmer()
prabhu.code(VSCode())
prabhu.code(PyCharm())