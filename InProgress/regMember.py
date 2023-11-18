import pandas as pd
import os

DataMember = pd.DataFrame(columns = ["Nama", "Email", "Password"])
dataDirektori = os.path.join("Data", "Member", "listMember.csv")

if(os.path.exists(dataDirektori)):
    DataMember = pd.read_csv(dataDirektori)
else:
    os.makedirs(os.path.dirname(dataDirektori), exist_ok = True)
    open(dataDirektori, 'w').close()

def tambahMember():
    global DataMember

    namaMember = str(input("Input Nama Anda     : "))
    emailMember = str(input("Input Email Anda   : "))
    passwordMember = str(input("Input Password  : "))

    DataMember = DataMember._append({
        "Nama": namaMember,
        "Email": emailMember,
        "Password": passwordMember
    }, ignore_index = True)

    DataMember.to_csv(dataDirektori, index = False)