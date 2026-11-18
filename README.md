# Task Manager v Pythonu

Jednoduchý konzolový správce pro tvorbu, zobrazení a mazání jednotlivých úkolů doplněný o testovací případy v samostatném dokumentu.



## Technologie

- Visual Studio Code 1.146.0
- Python 3.14.3



## Struktura projektu

- Task_Manager_Project
    - .task_source
        - verify.py
    - .gitignore
    - README.md
    - task_manager.py
    - test_cases.md



## Soubory

### task_manager.py
 
Zdrojový soubor se správcem úkolů. Na začátku souboru je v komentářích označených `#` uvedeno 5 názvů a popisů ukázkových úkolů pro ruční vložení přes volbu `1` hlavního menu.


#### Spuštění

1. Nainstalujte Visual Studio Code ze stránky [Visual Studio Code](https://code.visualstudio.com/) (nebo využijte jiný editor zdrojového kódu).

2. Nainstalujte Python ze stránky [Python](https://www.python.org/). Při instalaci vyberte možnost **Add Python to PATH**.

3. Ve Visual Studio Code otevřete terminál PowerShell a přejděte do stažené složky projektu. Cestu v následujícím příkladu nahraďte vlastní cestou:

   ```powershell
   cd "C:\cesta\k\Task_Manager_Project"
   python task_manager.py
   ```

   Pokud používáte spouštěč Pythonu pro Windows, můžete zadat `py task_manager.py`. Samotný editor není pro spuštění nutný; stačí Python a terminál.

4. V nabídce hlavního menu vyberte `1` pro přidání úkolu, `2` pro zobrazení úkolů, `3` pro odstranění úkolu nebo `4` pro ukončení programu. Každý vstup potvrďte stisknutím klávesy Enter. Pro přidání úkolu zadejte jeho název a popis; při odstranění úkolu zadejte číslo ze zobrazeného seznamu úkolů.

Úkoly se při běhu programu ukládají do `ukoly = []` jako slovníky obsahující název a popis. Po ukončení programu se zadané hodnoty neuchovávají.


#### Očekávaný výsledek

Po spuštění programu se zobrazí nabídka hlavního menu obsahující 4 volby výběru a oznámení `Vyberte možnost (1-4):`. Neplatná volba zobrazí upozornění a nabídku zopakuje.

Po zadání volby `1` program vyzve k vepsání názvu úkolu a po potvrzení klávesou Enter vyzve k zadání popisu úkolu. Prázdný název nebo popis vyvolá nové zadání obou údajů. Pouhé mezery se také považují za prázdný vstup.

V případě, že seznam úkolů již obsahuje nějaké položky, volba `2` je zobrazí vypsáním do terminálu. Pokud je seznam prázdný, program vypíše upozornění `Seznam úkolů je prázdný.`

Po uvedení volby `3` konzole v případě neprázdného seznamu vypíše všechny jeho očíslované položky a zobrazí výzvu `Zadejte číslo úkolu, který chcete odstranit:`. Při zadání čísla, které odpovídá některému z vypsaných úkolů, se položka vymaže a program vypíše oznámení o smazání vybraného úkolu. Při zadání celého čísla mimo rozsah seznamu program oznámí `Úkol s tímto číslem neexistuje.` Při nečíselném nebo prázdném vstupu, případně desetinném čísle, vypíše `Neplatný vstup. Zadejte celé číslo úkolu.` Jestliže v seznamu po zvolení této možnosti nejsou žádné položky, program vypíše `Seznam úkolů je prázdný.` Po odstranění se pořadová čísla při dalším výpisu přepočítají od 1.

Volba `4` způsobí ukončení programu s vypsáním oznámení `Konec programu.`. Úkoly jsou uložené pouze v paměti během běhu programu. Při dalším spuštění je seznam opět prázdný.



### test_cases.md

Dokument obsahující 17 testovacích případů pro jednotlivé funkce hlavního menu správce úkolů ze souboru `task_manager.py`. U všech těchto testovacích případů došlo k manuálnímu ověření vstupů, výstupů a stavu seznamu. 

Testovací případy pokrývají pozitivní, negativní i hraniční scénáře a jsou rozdělené podle funkcí `hlavni_menu`, `pridat_ukol`, `zobrazit_ukoly` a `odstranit_ukol`. Podrobnější popis způsobu provedení, samotné znění a hlavní součásti každého testovacího případu jsou k dispozici přímo v dokumentu `test_cases.md`. 


#### Jak se s dokumentem seznámit

- Otevřete [test_cases.md](test_cases.md) a seznamte se s prostředím, způsobem provedení a přehledem pokrytí jednotlivých funkcí.
- Projděte testovací případy včetně vstupních podmínek, kroků, očekávaných a skutečných výsledků.
- Pro zopakování testu spusťte [task_manager.py](task_manager.py), připravte uvedené úkoly a postupujte podle kroků vybraného TC. Každý případ začínejte novým spuštěním programu.
- Porovnejte chování programu s očekávaným výsledkem. Pole skutečného výsledku a stavu zachycují manuální testování ze dne 18. 11. 2026.

#### Očekávané výsledky

Všech 17 testovacích případů obsahuje popis, vstupní podmínky, postup, očekávaný a skutečný výsledek, stav a poznámky. Podle zaznamenaného manuálního ověření mají všechny případy stav `Pass`. Testy ověřují správu úkolů, návraty do hlavního menu, ošetření neplatných vstupů a hraniční situace, například prázdný seznam.

### .task_source/verify.py

Skript automatizovaně ověřuje stejných 17 testovacích případů TC01–TC17, které jsou popsány v `test_cases.md`. Kontroluje výstupy programu, výsledný seznam úkolů a návraty do menu. Skript nemění dokumentaci ani zapsané manuální výsledky.

Ze složky projektu jej lze spustit příkazem:

```powershell
python .task_source/verify.py
```

Při úspěšném ověření vypíše `17/17 automatizovaných kontrol: Pass.` Při nesouladu skončí chybou s popisem neúspěšné kontroly. Používá pouze standardní knihovnu Pythonu.
