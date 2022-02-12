import os

# RPM = os.getenv("RPM")
RPM = os.getcwd()

src = os.path.join(RPM, 'src')
shared = os.path.join(src, "shared")

auth = os.path.join(shared, "Authentication.py")
user = os.path.join(shared, "UserMethods.py")
app = os.path.join(src, "app.py")
appConfig = os.path.join(src, "appConfig.py")


for current_file in [app, appConfig, auth, user]:
    all_lines = None
    new_lines = []
    COMMENT = False
    comment_space = 0

    with open(current_file, "r") as file:
        all_lines = file.readlines()

    for i in all_lines:
        stripe_i = i.lstrip()
        total_len = len(i)
        strip_len = len(stripe_i)
        between_space = total_len - strip_len - comment_space
        if stripe_i[0:5] == "# CCC":
            COMMENT = not COMMENT
            comment_space = total_len - strip_len
        elif len(stripe_i) > 1 and COMMENT:
            if i.lstrip()[:2] != "# ":
                i = comment_space * " " + "# " + between_space * " " + stripe_i
            else:
                i = comment_space * " " + between_space * " " + stripe_i[2:]
        new_lines.append(i)

    with open(current_file, 'w') as wr_file:
        for line in new_lines:
            wr_file.writelines(line)
