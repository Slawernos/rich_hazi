from abc import ABC, abstractmethod
from datetime import datetime

# Szoba abasztrakt osztály
class Szoba(ABC):
    def __init__(self, szobaszam:int, ar:int):
        self.szobaszam = szobaszam
        self.ar = ar
# Egyágyas Szoba osztály
class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 5000) 
        self.terasz="Tengerre néző!"
# Kétágyas szoba osztály
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000)  
        self.agy="Nagyon kenyelmes agy"

# Szálloda Osztály
class Szalloda:
    def __init__(self, nev:str):
        self.cim="1163. Budapest, Kisnagy utca 12. Magyarország"
        self.nev = nev
        self.szobak = []
    # Szoba(k) hozzaadasa a szallodaba
    def add_szoba(self,szobaszam:int, tipus:str):
        if tipus=="nagy":
            self.szobak.append(KetagyasSzoba(szobaszam))
        elif tipus=="kicsi":
            self.szobak.append(EgyagyasSzoba(szobaszam))           
        else:
            print("\n Szoba típus vagy szám nem megfelelő")
    # Szoba kereso metodus
    def find_szoba(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return szoba
        return None
    # Szoba listazo metodus
    def szobak_listazas(self):
        for szoba in self.szobak:
            print(f"A {szoba.szobaszam}. szoba ára: {szoba.ar} különlegessége: {szoba.terasz if isinstance(szoba,EgyagyasSzoba) else (szoba.agy if isinstance(szoba,KetagyasSzoba) else 'Nincs')}")

# Foglalas osztaly foglalas kezelesere
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"Foglalás: Szobaszam: {self.szoba.szobaszam}, Dátum: {self.datum.strftime('%Y-%m-%d')}"

# Foglalas kezelo osztaly
class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []
    # foglalas hozzaadasa , jovobeni datum es szobaletezes keresese
    def foglalas_hozzaadasa(self, szobaszam:int, datum:datetime):
        if datum < datetime.now():
            return "\n A foglalás dátuma a múltban van, ez nem érvényes!"
        szoba = self.szalloda.find_szoba(szobaszam)
        if szoba is None:
            return "\n Nincs ilyen szobaszám!"
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                return "\n Ez a szoba ezen a napon már foglalt!"
        self.foglalasok.append(Foglalas(szoba, datum))
        return f"\n Foglalás sikeres: Szoba {szobaszam}, Dátum: {datum.strftime('%Y-%m-%d')}"
    # foglalas lemondasa
    def foglalas_lemondasa(self, szobaszam:int, datum:datetime):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "Foglalás lemondva!"
        return "\n Nincs ilyen foglalás!"

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "\n Nincsenek foglalások."
        return "\n".join(str(foglalas) for foglalas in self.foglalasok)

szalloda = Szalloda("Grand Hotel Budapest")
szalloda.add_szoba(1,"nagy")
szalloda.add_szoba(2,"kicsi")
szalloda.add_szoba(3,"kicsi")


foglalas_kezelo = FoglalasKezelo(szalloda)

foglalas_kezelo.foglalas_hozzaadasa(1,datetime.strptime('2024-09-22',"%Y-%m-%d"))
foglalas_kezelo.foglalas_hozzaadasa(2,datetime.strptime('2025-02-22',"%Y-%m-%d"))
foglalas_kezelo.foglalas_hozzaadasa(1,datetime.strptime('2026-03-22',"%Y-%m-%d"))
foglalas_kezelo.foglalas_hozzaadasa(3,datetime.strptime('2024-04-22',"%Y-%m-%d"))
foglalas_kezelo.foglalas_hozzaadasa(1,datetime.strptime('2025-09-22',"%Y-%m-%d"))



print(f"Üdvözlöm a Trivéső hotelfoglaló alkalmazásban Ön a {szalloda.nev} felületén van most!")

def main_menu():
    while True:
        print("----------------------------Válaszzon az alábbi menüpontok közül!-------------------------------")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Szobák listázása")
        print("5. A Szálloda címe")
        print("6. Kilépés")
        valasztas = input("Válasszon egy opciót: ")

        if valasztas == '1':
            correct=0
            try:
                szobaszam = int(input("Adja meg a szobaszámot: "))
                correct=1
            except:
                print("\n Hibás szobaszám kérlek csak a listázott szobákból válassz!")
            try:
                if correct !=0:
                    datum = datetime.strptime(input("Adja meg a dátumot (YYYY-MM-DD): "), "%Y-%m-%d")
                    correct=2
            except:
                print("\n Hibás dátum próbáld újra!")
            if correct==2:
                print(foglalas_kezelo.foglalas_hozzaadasa(szobaszam, datum))
        elif valasztas == '2':
            szobaszam = int(input("Adja meg a szobaszámot, amelyikből le szeretné mondani a foglalást: "))
            datum = datetime.strptime(input("Adja meg a dátumot (YYYY-MM-DD): "), "%Y-%m-%d")
            print(foglalas_kezelo.foglalas_lemondasa(szobaszam, datum))
        elif valasztas == '3':
            print(foglalas_kezelo.foglalasok_listazasa())
        elif valasztas == '4':
            szalloda.szobak_listazas()
        elif valasztas == '5':
            print(f"\n A szálloda címe: {szalloda.cim}" )
        elif valasztas == '6':
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás, próbálja újra.")
        input("\n Üss egy entert az újraindításhoz")

main_menu()
