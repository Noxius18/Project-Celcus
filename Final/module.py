import pandas as pd
import os
import pwinput as pw
from time import sleep as wait
import platform
from rich.console import Console; from rich.table import Table; from rich import box

def clear():
    if(platform.system() == "Linux"): os.system("clear")
    if(platform.system() == "Windows"): os.system("cls")

console = Console()


class DataBuku:
    def __init__(self, data_direktori) -> None:
        self.dataBuku = pd.DataFrame(columns=["ID", "Judul", "Genre", "Jenis", "Author", "Status"])
        self.direktori_buku = os.path.join("Data", data_direktori + ".csv")
    
    def cek_direktori_buku(self) -> None:
        if(os.path.exists(self.direktori_buku)):
            self.dataBuku = pd.read_csv(self.direktori_buku)
        else:
            os.makedirs(os.path.dirname(self.direktori_buku), exist_ok=True)
    
    def tambah_buku(self) -> None:

        judulBuku = str(input("Judul Buku: "))
        authorBuku = str(input("Author Buku: "))
        genreBuku = str(input("Genre Buku: "))
        jenisBuku = str(input("Jenis Buku: "))
        idBuku = str(input("ID Buku: "))
        statusBuku = "Tersedia"

        self.dataBuku = self.dataBuku._append({
            "ID": idBuku,
            "Judul": judulBuku,
            "Genre": genreBuku,
            "Jenis": jenisBuku,
            "Author": authorBuku,
            "Status": statusBuku
        }, ignore_index=True)

        self.dataBuku.to_csv(self.direktori_buku, index=False)
    
    def pinjam_buku(self) -> None:
        print("Input ID Buku yang ingin dipinjam")
        userPinjam = str(input("> ")).upper()

        list_buku = self.dataBuku[self.dataBuku["ID"] == userPinjam].index
        
        if(not list_buku.empty):
            judul_buku = self.dataBuku.loc[self.dataBuku["ID"] == userPinjam, "Judul"].values[0]
            status_buku = self.dataBuku.loc[self.dataBuku["ID"] == userPinjam, "Status"].values[0]

            if(status_buku == "Sedang Dipinjam"): console.print(f"[yellow]Buku {judul_buku} sedang dipinjam")
            else:
                self.dataBuku.loc[list_buku, "Status"] = "Sedang Dipinjam"
                self.dataBuku.to_csv(self.direktori_buku, index=False)
                console.print(f"[green]Kamu telah meminjam buku {judul_buku}")
                console.print(f"[dodger_blue2]Jika sudah selesai membaca harap ke Meja Counter untuk dikembalikan")
        else:
            console.print("[red]Maaf, Buku Tidak Tersedia")
     
    def balikin_buku(self) -> None:
        print("Input ID Buku yang ingin Dikembalikan")
        userBalik = str(input("> ")).upper()

        list_buku = self.dataBuku[self.dataBuku["ID"] == userBalik].index
        judul_buku = self.dataBuku.loc[self.dataBuku["ID"] == userBalik, "Judul"].values[0]

        if(not list_buku.empty):
            self.dataBuku.loc[list_buku, "Status"] = "Tersedia"
            self.dataBuku.to_csv(self.direktori_buku, index=False)
            console.print(f'[green]Buku {judul_buku} telah dikembalikan')
    
    def lihat_buku(self) -> None:
        index_buku = self.dataBuku
        
        table = Table(title="List Buku", show_lines=True, box=box.ROUNDED)

        table.add_column("ID", justify="center")
        table.add_column("Judul Buku", justify="center")
        table.add_column("Genre", justify="center")
        table.add_column("Jenis Buku", justify="center")
        table.add_column("Author", justify="center")
        table.add_column("Status", justify="center")

        for row in index_buku.itertuples():
            warna_status = "red" if row.Status == "Sedang Dipinjam" else 'spring_green2'
            table.add_row(row.ID,
                          row.Judul, 
                          row.Genre,
                          row.Jenis,
                          row.Author, 
                          row.Status, style=warna_status)
           
        console.print(table)

class PanelAdmin:
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
        passAdmin = pw.pwinput(prompt="Input Password Admin Baru: ")

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
            console.print("[green]Login Berhasil!")
            wait(1); clear()
        else:
            console.print("[red]Kredensial Salah!, Silahkan Masuk kembali")
            wait(1); clear()
            
class PanelMember:
    def __init__(self, direktori_data) -> None:
        self.data = pd.DataFrame(columns=["Nama", "Email", "Password"])
        self.direktori_member = os.path.join("Data", direktori_data + ".csv")
    
    def cek_direktori(self) -> None:
        if(os.path.exists(self.direktori_member)):
            self.data = pd.read_csv(self.direktori_member)
        else:
            os.makedirs(os.path.dirname(self.direktori_member), exist_ok=True)
    
    def tambah_member(self) -> None:
        userNama = str(input("Nama Anda: "))
        userMail = str(input("Email Anda: "))
        userPass = pw.pwinput(prompt="Input Password: ")

        self.data = self.data._append({
            "Nama": userNama,
            "Email": userMail,
            "Password": userPass
        }, ignore_index=True)

        self.data.to_csv(self.direktori_member, index=False)
    
    def login_member(self) -> None:
        login_mail = str(input("Input Email: "))
        login_pass = pw.pwinput(prompt="Input Password: ")

        cek_data = self.data[(self.data["Email"] == login_mail) & (self.data["Password"] == login_pass)]

        if(cek_data.empty):
            clear()
            console.print(f"[yellow]Data tidak ditemukan, silahkan Register untuk Melanjutkan")
            wait(1)
            self.tambah_member()
        else:
            cek_nama = self.data.loc[self.data["Email"] == login_mail, "Nama"].values[0]
            if(not cek_data.empty):
                console.print(f"[green]Login Berhasil!")
                console.print(f"Selamat Datang [blue]{cek_nama}")
            else:
                clear()
                console.print(f"[red]Kredensial Salah, Silahkan login kembali")
                wait(1)
                self.login_member()