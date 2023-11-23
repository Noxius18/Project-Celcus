import pandas as pd
import os


direktoriAdmin = os.path.join("Data", "Member", "listAdmin.csv")
dataAdmin = pd.DataFrame(direktoriAdmin)

print(dataAdmin)

def loginAdmin():
    userMail = str(input("Input Username: "))
    userPass = str(input("Input Password: "))

    if(userMail in dataAdmin["Username"].values and userPass in dataAdmin["Password"].values):
        print("Selamat Datang")
    else:
        print("Password Salah, silahkan masuk lagi")

