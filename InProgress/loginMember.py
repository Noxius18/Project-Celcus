from regMember import DataMember

def loginMember():
    userMail = str(input("Input Email: "))
    userPass = str(input("Input Password: "))

    if(userMail in DataMember["Email"].values and userPass in DataMember["Password"].values):
        print("Selamat Datang")
    else:
        print("Kredensial Salah, silahkan masuk lagi")