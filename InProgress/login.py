import pandas as pd
import platform
import os

platformUser = platform.system()

DataMember = pd.DataFrame(columns=["Nama", "Email", "Password"])

pathData = os.path.join("Data", "Member", "Member.csv")


"""
Berfungsi untuk Cek apakah Folder Data Tersedia
Jika tidak ada maka akan membuat Direktori untuk menyimpan List Member
User yang sudah dibuat dan menyimpannya
"""
if(os.path.exists(pathData)):
    DataMember = pd.read_csv(pathData)
else:
    os.makedirs(os.path.dirname(pathData), exist_ok = True)
    open(pathData, 'w').close()


def clearCLS():
    if(platformUser == "Linux"): os.system("clear")
    if(platformUser == "Windows"): os.system("cls")

def addMember():
    global DataMember
    
    namaMember = str(input("Input Nama: "))
    emailMember = str(input("Input Email: "))
    passwordMember = str(input("Input Password: "))

    DataMember = DataMember._append({
        "Nama": namaMember, 
        "Email": emailMember, 
        "Password": passwordMember}, ignore_index = True)
    
    DataMember.to_csv(pathData, index = False)


while(True):   
    print("1. Tambah Member")
    print("2. List Member")
    print("3. Keluar")
    case = int(input("Pilih Menu: "))

    clearCLS()

    if(case == 1):
        addMember()
        clearCLS()
    elif(case == 2):
        keluar = 0
        if(keluar != 1):
            subData = DataMember.filter(items=["Nama", "Email"])
            clearCLS()
            print(subData)
            print("\n1. Keluar")
            keluar = int(input("> "))
        clearCLS()
    else:
        break
        clearCLS()
