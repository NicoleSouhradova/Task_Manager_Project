# Správce úkolů

ukoly = []

# Ukázkové úkoly pro ruční vložení přes volbu 1:
# 1. Název: Nakoupit potraviny
#    Popis: Koupit pečivo, mléko a zeleninu.
# 2. Název: Uklidit
#    Popis: Utřít prach, vyluxovat a vytřít.
# 3. Název: Vyprat prádlo
#    Popis: Prát zvlášť černé, barevné a jemné prádlo.
# 4. Název: Zalít květiny
#    Popis: Zalít bylinky a sukulenty.
# 5. Název: Zacvičit si
#    Popis: Udělat cviky na nohy, hýždě a břicho.


def hlavni_menu():
    volba = ""

    while volba != "4":
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
        else:
            print("Neplatná volba. Zadejte číslo od 1 do 4.")


def pridat_ukol():
    nazev = ""
    popis = ""

    while not (nazev and popis):
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()

        if not (nazev and popis):
            print("Název ani popis nesmí být prázdný. Zadejte oba údaje znovu.")

    ukoly.append({"nazev": nazev, "popis": popis})
    print(f"Úkol '{nazev}' byl přidán.")


def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return
    
    print("Seznam úkolů:")
    cislo = 1

    for ukol in ukoly:
        print(f"{cislo}. {ukol['nazev']} - {ukol['popis']}")
        cislo = cislo + 1


def odstranit_ukol():
    zobrazit_ukoly()

    if not ukoly:
        return
    
    try:
        cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
    except ValueError:
        print("Neplatný vstup. Zadejte celé číslo úkolu.")
        return
    
    if cislo >= 1 and cislo <= len(ukoly):
        index = cislo - 1
        vybrany_ukol = ukoly[index]
        nazev = vybrany_ukol["nazev"]
        del ukoly[index]
        print(f"Úkol '{nazev}' byl odstraněn.")
    else:
        print("Úkol s tímto číslem neexistuje.")


if __name__ == "__main__":
    hlavni_menu()
