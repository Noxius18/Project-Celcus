import pandas as pd
import os
from rich.console import Console
import time
import platform

def clear():
    if(platform.system() == "Linux"): os.system("clear")
    if(platform.system() == "Windows"): os.system("cls")

def wait(int):
    return time.sleep(int)

console = Console()


"""Ini Percobaan Fungsi Login"""
class DataAdmin:
    def __init__(self, data_direktori) -> None:
        self.data = pd.DataFrame(columns=["username", "password"])
        self.data_direktori = os.path.join("Data", data_direktori + ".csv")
    
    def cek_direktori(self) -> None:
        """Untuk cek kondisi jika file csv tidak ada maka akan dibuat terlebih dahulu"""
        if(os.path.exists(self.data_direktori)):
            self.data = pd.read_csv(self.data_direktori)
        else:
            os.makedirs(os.path.dirname(self.data_direktori), exist_ok=True)
    
    def tambah_admin(self) -> None:
        userAdmin = str(input(("Input User Admin Baru: ")))
        passAdmin = str(input("Input Password Admin Baru: "))

        self.data = self.data._append({
            "username": userAdmin,
            "password": passAdmin
        }, ignore_index=True)

        self.data.to_csv(self.data_direktori, index=False)
    
    def login_admin(self) -> None: 
        login_user = str(input("Input Username: "))
        login_pass = str(input("Input Password: "))

        cek_data = self.data[(self.data["username"] == login_user) & (self.data["password"] == login_pass)]
        if(not cek_data.empty):
            print("Selamat Datang")
        else:
            console.print("[red]Kredensial Salah!, Silahkan Masuk kembali")
            wait(2)
            clear()


data_admin = DataAdmin("listAdmin")
data_admin.cek_direktori()

while(True):
    print(f"""
1.Login
2.REgister""")
    
    opsi = int(input("Opsi> "))

    if(opsi == 1):
        data_admin.login_admin()
    elif(opsi == 2):
        data_admin.tambah_admin()
    else:
        break
            
