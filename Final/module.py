import pandas as pd
import polars as pl
import os
import pwinput as pw
import platform
from time import sleep as wait
from header import header
from rich.console import Console; from rich.table import Table; from rich import box, emoji

def clear():
    os.system("cls") if platform.system() == "Windows" else os.system("clear")

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
        console.print("[INPUT BUKU]", justify="left", style="bold chartreuse3")
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

        console.print(f"\nBuku Berhasil Ditambahkan!:white_check_mark:", style="bold green")
        wait(1)
        clear()
    
    def pinjam_buku(self) -> None:
        while(True):
            console.print(header())
            self.lihat_buku()
            console.print("Input [deep_sky_blue1]ID[/deep_sky_blue1] Buku yang ingin dipinjam | [1] Keluar")
            userPinjam = str(input("> ")).upper()

            list_buku = self.dataBuku[self.dataBuku["ID"] == userPinjam].index

            if(not list_buku.empty):
                judul_buku = self.dataBuku.loc[self.dataBuku["ID"] == userPinjam, "Judul"].values[0]
                status_buku = self.dataBuku.loc[self.dataBuku["ID"] == userPinjam, "Status"].values[0]

                if(status_buku == "Sedang Dipinjam"): 
                    console.print(f"\n[yellow]Buku [dodger_blue2]{judul_buku}[/dodger_blue2] sedang dipinjam")
                    wait(2)
                    clear()   
                else:
                    self.dataBuku.loc[list_buku, "Status"] = "Sedang Dipinjam"
                    self.dataBuku.to_csv(self.direktori_buku, index=False)
                    console.print(f"\nKamu telah meminjam buku [dodger_blue2]{judul_buku}[/dodger_blue2]:white_check_mark:", style="spring_green3")
                    console.print(f"Jika sudah selesai membaca harap ke Meja Counter untuk dikembalikan:twelve_o’clock:", style="orange_red1")
                    wait(4); clear()
                    break
            elif(userPinjam == "1"):
                clear()
                break
            else:
                console.print(f"\nMaaf, Buku Tidak Tersedia :exclamation_mark:", style="bold red")
                wait(2)
                clear()
                
     
    def balikin_buku(self) -> None:
        while(True):
            console.print(header())
            self.lihat_buku()
            console.print(f"Input [deep_sky_blue1]ID[/deep_sky_blue1] Buku yang ingin Dikembalikan | [1] Keluar")
            userBalik = str(input("> ")).upper()

            list_buku = self.dataBuku[self.dataBuku["ID"] == userBalik].index

            if(not list_buku.empty):
                judul_buku = self.dataBuku.loc[self.dataBuku["ID"] == userBalik, "Judul"].values[0]
                self.dataBuku.loc[list_buku, "Status"] = "Tersedia"
                self.dataBuku.to_csv(self.direktori_buku, index=False)

                console.print(f"\nBuku [dodger_blue2]{judul_buku}[/dodger_blue2] telah dikembalikan:white_check_mark:", style="bold green")
                wait(3); clear()
                break
            elif(userBalik == "1"):
                clear()
                break
            else:
                console.print(f"\nBuku Tidak Tersedia :exclamation_mark:", style="bold red")
                wait(2)
                clear()
    
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
        console.print("[TAMBAH ADMIN BARU]", style='bold green')
        userAdmin = str(input(("Input User Admin Baru: ")))
        passAdmin = pw.pwinput(prompt="Input Password Admin Baru: ")

        self.data = self.data._append({
            "username": userAdmin,
            "password": passAdmin
        }, ignore_index=True)

        self.data.to_csv(self.data_direktori, index=False)
        console.print("\n[bold green]Admin berhasil ditambah:white_check_mark:")
        wait(1); clear()
    
    def login_admin(self) -> bool: 
        console.print("[LOGIN ADMIN]", style="bold blue", justify="left")
        login_user = str(input("Input Username: "))
        login_pass = pw.pwinput(prompt="Input Password: ")

        cek_data = self.data[(self.data["username"] == login_user) & (self.data["password"] == login_pass)]
        if(not cek_data.empty):
            console.print("\nLogin Berhasil!:white_check_mark:", style='bold green')
            wait(1); clear()
            return True
        else:
            console.print("\nKredensial Salah!, Silahkan Masuk kembali:exclamation_mark:", style="bold red")
            wait(1); clear()
            return False
            
class PanelMember:
    def __init__(self, direktori_data) -> None:
        self.data = pl.DataFrame({"Nama": [], "Email": [], "Password": []})
        self.direktori_member = os.path.join("Data", direktori_data + ".csv")
    
    def cek_direktori(self) -> None:
        if(os.path.exists(self.direktori_member)):
            self.data = pl.read_csv(self.direktori_member)
        else:
            os.makedirs(os.path.dirname(self.direktori_member), exist_ok=True)
    
    def tambah_member(self) -> bool:
        console.print(header())
        console.print("[REGISTRASI MEMBER]", style="bold green", justify="left")
        userNama = str(input("Nama Anda: "))
        userMail = str(input("Email Anda: "))
        userPass = pw.pwinput(prompt="Input Password: ")
        console.print("\nRegistrasi Berhasil!:white_check_mark:", style="bold green")
        wait(1); clear()

        data_input_member = pl.DataFrame({
            "Nama": [userNama],
            "Email": [userMail],
            "Password": [userPass]
        })

        self.data = pl.concat([self.data, data_input_member], how="vertical_relaxed")

        self.data.write_csv(self.direktori_member)
        return True
    
    def login_member(self) -> bool:
        console.print(header())
        console.print("[LOGIN MEMBER]", style="bold blue", justify="left")
        login_mail = str(input("Input Email: "))
        login_pass = pw.pwinput(prompt="Input Password: ")

        cek_data = self.data.filter((self.data["Email"] == login_mail) & (self.data["Password"] == login_pass))
        cek_nama = self.data.filter(self.data["Email"] == login_mail)["Nama"].to_list()[0]
        if(len(cek_data) > 0):
            console.print(f"\n[bold green]Login Berhasil! :white_check_mark:")
            console.print(f"Selamat Datang [bold blue]{cek_nama}[bold blue]")
            wait(2)
            clear()
            return True
        else:
            console.print(f"\n[red]Kredensial Salah, Silahkan login kembali :exclamation_mark:")
            wait(1)
            clear()
            return False