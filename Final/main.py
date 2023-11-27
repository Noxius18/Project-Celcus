from module import PanelAdmin, PanelMember, DataBuku, clear
from time import sleep as wait
from rich.console import Console
from rich.panel import Panel
from rich import box
from header import header

"""
Pastikan Library seperti rich dan pwinput sudah terinstall di device kalian
Untuk install library rich: pip install rich
Untuk install library pwinput: pip install pwinput
"""

def not_valid():
      console.print(f"[bold red]Opsi Tidak Valid")
      wait(1); clear()

console = Console()

PanelAdmin = PanelAdmin("dataAdmin")
PanelAdmin.cek_direktori()

PanelMember = PanelMember("dataMember")
PanelMember.cek_direktori()

DataBuku = DataBuku("dataBuku")
DataBuku.cek_direktori_buku()

clear()
while(True):
      console.print(header())
      if __name__ == '__main__':
            console.print(f"[bold white]Selamat Datang di Perpustakaan Celcus!")
            console.print(f"""[1]Panel Admin\n[2]Panel Member\n[3]Keluar""")

      
      opsi = int(input("> "))
      if(opsi == 1):
            clear()
            console.print(header())
            if(PanelAdmin.login_admin()):
                  while(True):
                        console.print(header())
                        menu_admin = Panel(
                              "\n".join([
                                    f"[[turquoise2]{1}[/turquoise2]] Input Buku",
                                    f"[[turquoise2]{2}[/turquoise2]] Pengembalian Buku",
                                    f"[[turquoise2]{3}[/turquoise2]] List Buku",
                                    f"[[turquoise2]{4}[/turquoise2]] Tambah Admin",
                                    f"[[turquoise2]{5}[/turquoise2]] Keluar"
                              ]),
                              title="[bold chartreuse3]Menu Admin",
                              expand=False,
                              box=box.ROUNDED
                        )
                        console.print(menu_admin)
                        opsiAdmin = int(input("> "))
                        if(opsiAdmin == 1):
                              clear()
                              console.print(header())
                              DataBuku.tambah_buku()
                        elif(opsiAdmin == 2):
                              clear()
                              # console.print(header())
                              DataBuku.balikin_buku()
                        elif(opsiAdmin == 3):
                              while(True):
                                    clear()
                                    console.print(header())
                                    DataBuku.lihat_buku()
                                    console.print("[1] Keluar")
                                    keluar1 = int(input("> "))
                                    if(keluar1 == 1): break
                              clear()
                        elif(opsiAdmin == 4):
                              clear()
                              console.print(header())
                              PanelAdmin.tambah_admin()
                        elif(opsiAdmin == 5):
                              clear()
                              break
                        else:
                              not_valid()
            else:
                  clear()

      elif(opsi == 2):
            clear()
            console.print(header())
            console.print(f"[PANEL MEMBER]", style="bold blue")
            console.print(f"[1] Login\n[2] Registrasi")
            opsi_panel_member = int(input("> "))

            if(opsi_panel_member == 1):
                  clear()
                  if(PanelMember.login_member()):
                        while(True):
                              clear()
                              console.print(header())
                              menu_member = Panel(
                                    "\n".join([
                                          f"[[turquoise2]{1}[/turquoise2]] List Buku",
                                          f"[[turquoise2]{2}[/turquoise2]] Pinjam Buku",
                                          f"[[turquoise2]{3}[/turquoise2]] Keluar"
                                    ]),
                                    title="[bold chartreuse3]Menu Member",
                                    expand=False,
                                    box=box.ROUNDED
                              )
                              console.print(menu_member)
                              opsi_member = int(input("> "))
                              if(opsi_member == 1):
                                    while(True):
                                          clear()
                                          console.print(header())
                                          DataBuku.lihat_buku()
                                          console.print("[1] Keluar")
                                          keluar2 = int(input("> "))
                                          if(keluar2 == 1): break
                                    clear()
                              elif(opsi_member == 2):
                                    clear()
                                    DataBuku.pinjam_buku()
                              elif(opsi_member == 3):
                                    clear()
                                    break
                              else:
                                    not_valid()
            elif(opsi_panel_member == 2):
                  clear()
                  PanelMember.tambah_member()
            else:
                  not_valid()
      elif(opsi == 3):
            console.print(f"Terima Kasih atas Kunjungannya", style="bold deep_sky_blue3")
            wait(2)
            clear()
            break
      else:
            not_valid()
            