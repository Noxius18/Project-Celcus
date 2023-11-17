import pandas as pd
import platform
import os

platformUser = platform.system()

DataMember = pd.DataFrame(columns=["Nama", "Email", "Password"])

if(os.path.exists("Data/dataTest.csv")):
    DataMember = pd.read_csv("Data/dataTest.csv")
else:
    os.mkdir("Data")
    if(platformUser == "Linux"):
        os.system("touch Data/dataTest.csv")
    # elif(platformUser == "Windows"):
    """Jangan Lupa di Windows tambahain Command buat bikin file"""

def addMember():
    global DataMember
    
    namaMember = str(input("Input Nama: "))
    emailMember = str(input("Input Email: "))
    passwordMember = str(input("Input Password: "))

    DataMember = DataMember._append({
        "Nama": namaMember, 
        "Email": emailMember, 
        "Password": passwordMember}, ignore_index = True)
    
    DataMember.to_csv("Data/dataTest.csv", index=False)

while(True):   
    print("1. Tambah Member")
    print("2. List Member")
    print("3. Keluar")
    case = int(input("Pilih Menu: "))

    os.system("clear")

    if(case == 1):
        addMember()
        os.system("clear")
    elif(case == 2):
        keluar = 0
        if(keluar != 1):
            subData = DataMember.filter(items=["Nama", "Email"])
            os.system("clear")
            print(subData)
            print("\n1. Keluar")
            keluar = int(input("> "))
        os.system("clear")
    else:
        break
        os.system("clear")
