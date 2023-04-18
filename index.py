import os
from datetime import date
today = date.today()
d1 = today.strftime("%d-%m-%Y")

with open("combo.txt", "r") as combo:
    read = combo.readlines()
    for line in read:
        email = line.split(":")[0]
        services = email.split("@")[1]
        a = services.split(".")[0]
        if os.path.exists(f"./sorted/{a}"):
            with open(f"./sorted/{a}/output {d1}.txt", "a+") as f:
                    f.write(line)
        else:
            os.mkdir(f"./sorted/{a}")
            with open(f"./sorted/{a}/output {d1}.txt", "a+") as f:
                    f.write(line)
    print("done")

