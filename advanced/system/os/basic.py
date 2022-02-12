import os
from datetime import datetime


# -> dir(module) -> all attributes and methods of module
# print(dir(os))

# -> current working directory
# print(os.getcwd())


# -> changing the working directory
# os.chdir('D:\Programming\Python\Python-Fundamentals')
# print(os.getcwd())


# -> list all directories
# directory = os.listdir()
# for d in directory:
#     print(d)


"""
creating directories
mkdir -> create single level (parent) dir only
makedirs -> create multilevel dirs

"""
# print(os.getcwd())
# os.mkdir("Demo1")
# os.makedirs("Demo2/App")

# os.rmdir("Demo1")
# os.removedirs("Demo2/App")


# -> Renaming
# os.rename("demo.txt", "demo.md")


# -> File Info
# st = os.stat('demo.txt')
# print(datetime.fromtimestamp(st.st_mtime))


# -> Traversing directory
# path = "D:\Programming\Python\Python-Fundamentals"
# for dirpath, dirname, filename in os.walk(path):
#     print("PATH   -> ", dirpath)
#     print("FOLDER -> ", dirname)
#     print("FILE   -> ", filename)
#     print()


# Environment Variables
# for env in os.environ:
#     print(env)

# print(os.environ.get('RPM'))

# os.path.join(os.environ.get("HOMEPATH"), 'text.txt')


# basename, dirname
path = "/prabhu/document.txt"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(os.path.exists(path))
print(os.path.isdir(path))
print(os.path.isfile(path))
print(os.path.splitext(path))
