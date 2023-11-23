import pandas as pd
from tabulate import tabulate
import os

DataBuku = pd.DataFrame(columns = ["Judul", "Author", "Tahun", "Genre"])
direktoriBuku = os.path.join("Data", "listBuku", "listBuku.csv")

if(os.path.exist(direktoriBuku)):
    DataBuku = pd.read_csv(direktoriBuku)
else:
    os.makedirs(os.path.dirname(direktoriBuku))

def inputBuku():
    global DataBuku

    print(f"Judul Buku")
    judulBuku = str(input("> "))
    print(f"Author Buku")
    authorBuku = str(input("> "))
    print(f"Tahun Terbit Buku")
    tahunBuku = int(input("> "))
    print(f"Genre")
    genreBuku = str(input("> "))

    DataBuku = DataBuku._append({
        "Judul": judulBuku,
        "Author": authorBuku,
        "Tahun Terbit": tahunBuku,
        "Genre": genreBuku
    }, ignore_index = True)

    DataBuku.to_csv(direktoriBuku, index = False)



