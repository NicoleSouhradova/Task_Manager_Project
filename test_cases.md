# Testovací případy pro Task Manager

Tento dokument obsahuje 17 testovacích případů (TC), které ověřují hotový soubor `task_manager.py`. Každý TC obsahuje název, popis, vstupní podmínky, kroky, očekávaný a skutečný výsledek, stav a poznámky.

## Prostředí a způsob provedení

- Pro spuštění programu `task_manager.py` je zapotřebí mít nainstalovaný Python 3.
- Každý TC je nezávislý. Před každým testem spusťte program znovu a připravte uvedené výchozí úkoly pomocí volby 1, ve stanoveném pořadí.
- Po proběhnutí každého testu program ukončete.
- Ukázkové úkoly jsou v komentářích na začátku dokumentu `task_manager.py`, automaticky se nenačítají při spuštění programu.
- Každý níže uvedený vstup potvrďte Enterem. `""` znamená pouze Enter; `"   "` znamená tři mezery a Enter. Uvozovky nezadávejte.

- Skutečné výsledky a stavy níže pocházejí z manuálního testování konzolové logiky dne 18. 11. 2026. Ověřeny byly ručně zadávané vstupy, návraty do menu, výstupy a výsledný stav seznamu.

## Přehled pokrytí

| Funkce | TC | Pokrytí |
| --- | --- | --- |
| `hlavni_menu` | TC01–TC07 | Všechny čtyři volby, návraty, chybný text, prázdný vstup a hranice rozsahu |
| `pridat_ukol` | TC08–TC11 | První i další úkol, prázdný název nebo popis a oprava vstupu |
| `zobrazit_ukoly` | TC12–TC13 | Více úkolů a prázdný seznam; jediný úkol také v TC02 |
| `odstranit_ukol` | TC14–TC17 | Prostřední úkol, prázdný seznam, neplatná čísla a text; jediný úkol také v TC03 |

## Funkce `hlavni_menu`

### TC01: Volba "1" - přidání úkolu

**Typ testu:**

Pozitivní

**Popis:**

Ověřit, že volba 1 spustí přidání a vrátí uživatele do hlavního menu.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu. 
- Program obsahuje prázdný seznam `ukoly = []`

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"1"` a potvrďte **Enterem**.
4. Zadejte `"Nakoupit potraviny"` a potvrďte **Enterem**.
5. Zadejte `"Koupit pečivo, mléko a zeleninu."` a potvrďte **Enterem**.
6. Zadejte `"4"` a potvrďte **Enterem**.
7. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje oznámení: `Úkol 'Nakoupit potraviny' byl přidán.` 
Pod oznámením o přidání se znovu zobrazí hlavní menu.
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen. 

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Kontroluje propojení hlavního menu a funkce pridat_ukol().

### TC02: Volba "2" - zobrazení úkolů

**Typ testu:**

Pozitivní

**Popis:**

Ověřit výstup volby 2 a následný návrat do hlavního menu.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu. 
- Před testem přidejte následující úkoly pomocí volby `1`. U každého zadejte název a popis; každý vstup potvrďte Enterem.

1. Název: `"Nakoupit potraviny"`; popis: `"Koupit pečivo, mléko a zeleninu."`.

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"2"` a potvrďte **Enterem**.
4. Zadejte `"4"` a potvrďte **Enterem**.
5. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje oznámení: `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.` 
Pod výpisem úkolů se znovu zobrazí hlavní menu.
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Kontroluje propojení hlavního menu a funkce zobrazit_ukoly().

### TC03: Volba "3" - odstranění úkolu

**Typ testu:**

Pozitivní

**Popis:**

Ověřit výstup volby 3 a návrat do hlavního menu.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu. 
- Před testem přidejte následující úkoly pomocí volby `1`. U každého zadejte název a popis; každý vstup potvrďte Enterem.

1. Název: `"Nakoupit potraviny"`; popis: `"Koupit pečivo, mléko a zeleninu."`.

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"3"` a potvrďte **Enterem**.
4. Zadejte `"1"` a potvrďte **Enterem**.
5. Zadejte `"4"` a potvrďte **Enterem**.
6. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje oznámení v tomto pořadí:

1. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`
2. `Úkol 'Nakoupit potraviny' byl odstraněn.`

Pod oznámením o vymazání úkolu se znovu zobrazí hlavní menu.
Konečným stavem před ukončením programu je prázdný seznam `ukoly = []`
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Kontroluje propojení hlavního menu a funkce odstranit_ukol().

### TC04: Nečíselná volba v hlavním menu

**Typ testu:**

Negativní

**Popis:**

Ověřit upozornění na neplatnou volbu a návrat do hlavního menu.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Program obsahuje prázdný seznam `ukoly = []`

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"abc"` a potvrďte **Enterem**.
4. Zadejte `"4"` a potvrďte **Enterem**.
5. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje upozornění: `Neplatná volba. Zadejte číslo od 1 do 4.` 
Pod upozorněním na neplatnou volbu se znovu zobrazí hlavní menu.
Konečným stavem před ukončením programu je prázdný seznam `ukoly = []`
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Nečíselný vstup nesmí ukončit program, ale vrátit uživatele do hlavního menu.

### TC05: Volby těsně mimo rozsah

**Typ testu:**

Negativní / hraniční

**Popis:**

Ověřit odmítnutí hraničních hodnot 0 a 5.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Program obsahuje prázdný seznam `ukoly = []`

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"0"` a potvrďte **Enterem**.
4. Zadejte `"5"` a potvrďte **Enterem**.
5. Zadejte `"4"` a potvrďte **Enterem**.
6. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje upozornění v tomto pořadí:

1. `Neplatná volba. Zadejte číslo od 1 do 4.`
2. `Neplatná volba. Zadejte číslo od 1 do 4.`

Konečným stavem před ukončením programu je prázdný seznam `ukoly = []`
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Dolní a horní neplatná hranice nabídky možností 1–4.

### TC06: Prázdná volba a mezery

**Typ testu:**

Negativní

**Popis:**

Ověřit prázdný vstup a vstup obsahující pouze mezery.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Program obsahuje prázdný seznam `ukoly = []`

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Nezadávejte žádný text a stiskněte pouze **Enter** (`""`).
4. Zadejte **3 mezery** a potvrďte **Enterem** (`"   "`).
5. Zadejte `"4"` a potvrďte **Enterem**.
6. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje upozornění v tomto pořadí:

1. `Neplatná volba. Zadejte číslo od 1 do 4.`
2. `Neplatná volba. Zadejte číslo od 1 do 4.`

Konečným stavem před ukončením programu je prázdný seznam `ukoly = []`
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Neplatný vstup nesmí ukončit program, ale vrátit uživatele do hlavního menu.

### TC07: Ukončení programu volbou "4"

**Typ testu:**

Pozitivní

**Popis:**

Ověřit ukončení programu bez dalších vstupů.

**Vstupní podmínky:**

Program zobrazuje hlavní menu.

**Kroky testu:**

1. Spusťte `task_manager.py`
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"4"` a potvrďte **Enterem**.
4. Porovnejte výstup a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje oznámení: `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Okamžité ukončení po spuštění programu nevyvolá chybu ani pád programu.

## Funkce `pridat_ukol`

### TC08: Přidání úkolu č. 1

**Typ testu:**

Pozitivní

**Popis:**

Ověřit vytvoření prvního záznamu v prázdném seznamu.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Program obsahuje prázdný seznam `ukoly = []`

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"1"` a potvrďte **Enterem**.
4. Zadejte `"Nakoupit potraviny"` a potvrďte **Enterem**.
5. Zadejte `"Koupit pečivo, mléko a zeleninu."` a potvrďte **Enterem**.
6. Zadejte `"2"` a potvrďte **Enterem**.
7. Zadejte `"4"` a potvrďte **Enterem**.
8. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje oznámení v tomto pořadí:

1. `Úkol 'Nakoupit potraviny' byl přidán.`
2. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`

Konečným stavem před ukončením programu je záznam `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.` v seznamu úkolů.
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

První úkol je při výpisu označen číslem 1.

### TC09: Přidání dalšího úkolu k již existujícímu úkolu č. 1

**Typ testu:**

Pozitivní

**Popis:**

Ověřit přidání na konec bez přepsání původního úkolu.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Před testem přidejte následující úkoly pomocí volby `1`. U každého zadejte název a popis; každý vstup potvrďte Enterem.

1. Název: `"Nakoupit potraviny"`; popis: `"Koupit pečivo, mléko a zeleninu."`.

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"1"` a potvrďte **Enterem**.
4. Zadejte `"Uklidit"` a potvrďte **Enterem**.
5. Zadejte `"Utřít prach, vyluxovat a vytřít."` a potvrďte **Enterem**.
6. Zadejte `"2"` a potvrďte **Enterem**.
7. Zadejte `"4"` a potvrďte **Enterem**.
8. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje oznámení v tomto pořadí:

1. `Úkol 'Uklidit' byl přidán.`
2. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`
3. `2. Uklidit - Utřít prach, vyluxovat a vytřít.`

Konečným stavem před ukončením programu jsou záznamy `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`; `2. Uklidit - Utřít prach, vyluxovat a vytřít.` v seznamu úkolů.
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Druhý úkol je při výpisu označen číslem 2 a je zachováno správné pořadí.

### TC10: Prázdný název a nové zadání

**Typ testu:**

Negativní

**Popis:**

Ověřit odmítnutí prázdného názvu a opakování názvu i popisu.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Program obsahuje prázdný seznam `ukoly = []`

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"1"` a potvrďte **Enterem**.
4. Nezadávejte žádný text a stiskněte pouze **Enter** (`""`).
5. Zadejte `"Tento popis neukládat."` a potvrďte **Enterem**.
6. Zadejte `"Nakoupit potraviny"` a potvrďte **Enterem**.
7. Zadejte `"Koupit pečivo, mléko a zeleninu."` a potvrďte **Enterem**.
8. Zadejte `"2"` a potvrďte **Enterem**.
9. Zadejte `"4"` a potvrďte **Enterem**.
10. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje upozornění/oznámení v tomto pořadí:

1. `Název ani popis nesmí být prázdný. Zadejte oba údaje znovu.`
2. `Úkol 'Nakoupit potraviny' byl přidán.`
3. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`

Při zadání prázdného názvu a krátkého popisu se po výpisu upozornění nezobrazuje opět hlavní menu, ale výzvy `Zadejte název úkolu:` a následně `Zadejte popis úkolu:` pro opravu vstupu.
Konečným stavem před ukončením programu je záznam `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.` v seznamu úkolů.
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Neplatný pokus nesmí vytvořit částečný úkol.

### TC11: Prázdný popis a nové zadání

**Typ testu:**

Negativní

**Popis:**

Ověřit odmítnutí prázdného popisu a opakování názvu i popisu.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Program obsahuje prázdný seznam `ukoly = []`

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"1"` a potvrďte **Enterem**.
4. Zadejte `"Tento název neukládat."` a potvrďte **Enterem**.
5. Nezadávejte žádný text a stiskněte pouze **Enter** (`""`).
6. Zadejte `"Nakoupit potraviny"` a potvrďte **Enterem**.
7. Zadejte `"Koupit pečivo, mléko a zeleninu."` a potvrďte **Enterem**.
8. Zadejte `"2"` a potvrďte **Enterem**.
9. Zadejte `"4"` a potvrďte **Enterem**.
10. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje upozornění/oznámení v tomto pořadí:

1. `Název ani popis nesmí být prázdný. Zadejte oba údaje znovu.`
2. `Úkol 'Nakoupit potraviny' byl přidán.`
3. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`

Při zadání krátkého názvu a prázdného popisu se po výpisu upozornění nezobrazuje opět hlavní menu, ale výzvy `Zadejte název úkolu:` a následně `Zadejte popis úkolu:` pro opravu vstupu.
Konečným stavem před ukončením programu je záznam `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.` v seznamu úkolů.
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Neplatný pokus nesmí vytvořit částečný úkol.

## Funkce `zobrazit_ukoly`

### TC12: Zobrazení několika úkolů najednou

**Typ testu:**

Pozitivní

**Popis:**

Ověřit zobrazení výpisu všech názvů, popisů a správného pořadí úkolů.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Před testem přidejte následující úkoly pomocí volby `1`. U každého zadejte název a popis; každý vstup potvrďte Enterem.

1. Název: `"Nakoupit potraviny"`; popis: `"Koupit pečivo, mléko a zeleninu."`.
2. Název: `"Uklidit"`; popis: `"Utřít prach, vyluxovat a vytřít."`.
3. Název: `"Vyprat prádlo"`; popis: `"Prát zvlášť černé, barevné a jemné prádlo."`.

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"2"` a potvrďte **Enterem**.
4. Zadejte `"4"` a potvrďte **Enterem**.
5. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje seznam úkolů v následujícím pořadí:

1. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`
2. `2. Uklidit - Utřít prach, vyluxovat a vytřít.`
3. `3. Vyprat prádlo - Prát zvlášť černé, barevné a jemné prádlo.`

Konečný stav před ukončením programu odpovídá výstupu z prvního bodu.
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shodný s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Výpis musí obsahovat všechny úkoly v pořadí, v jakém byly přidány.

### TC13: Zobrazení prázdného seznamu

**Typ testu:**

Hraniční

**Popis:**

Ověřit srozumitelné oznámení o prázdném seznamu místo chyby při absenci úkolů při zobrazování výpisu úkolů.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Program obsahuje prázdný seznam `ukoly = []`

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"2"` a potvrďte **Enterem**.
4. Zadejte `"4"` a potvrďte **Enterem**.
5. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje upozornění: `Seznam úkolů je prázdný.`
Konečným stavem před ukončením programu je prázdný seznam `ukoly = []`
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Prázdný seznam je podporovaný stav a nezpůsobuje pád programu. Funkce nemá vlastní vstup; neplatné volby testují TC04–TC06 v hlavním menu.

## Funkce `odstranit_ukol`

### TC14: Odstranění prostředního úkolu

**Typ testu:**

Pozitivní

**Popis:**

Ověřit odstranění pouze vybraného, prostředního záznamu a správné přečíslování úkolů.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Před testem přidejte následující úkoly pomocí volby `1`. U každého zadejte název a popis; každý vstup potvrďte Enterem.

1. Název: `"Nakoupit potraviny"`; popis: `"Koupit pečivo, mléko a zeleninu."`.
2. Název: `"Uklidit"`; popis: `"Utřít prach, vyluxovat a vytřít."`.
3. Název: `"Vyprat prádlo"`; popis: `"Prát zvlášť černé, barevné a jemné prádlo."`.

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"3"` a potvrďte **Enterem**.
4. Zadejte `"2"` a potvrďte **Enterem**.
5. Zadejte `"2"` a potvrďte **Enterem**.
6. Zadejte `"4"` a potvrďte **Enterem**.
7. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje úkoly / oznámení v následujícím pořadí:

1. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`
2. `2. Uklidit - Utřít prach, vyluxovat a vytřít.`
3. `3. Vyprat prádlo - Prát zvlášť černé, barevné a jemné prádlo.`
4. `Úkol 'Uklidit' byl odstraněn.`
5. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`
6. `2. Vyprat prádlo - Prát zvlášť černé, barevné a jemné prádlo.`

Konečným stavem před ukončením programu jsou záznamy `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`; `2. Vyprat prádlo - Prát zvlášť černé, barevné a jemné prádlo.` v seznamu úkolů.
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Úkoly na sousedních pozicích musí být zachovány a správně přečíslovány.

### TC15: Odstranění úkolu z prázdného seznamu

**Typ testu:**

Negativní

**Popis:**

Ověřit, že bez úkolů nelze zadávat číslo k odstranění.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Program obsahuje prázdný seznam `ukoly = []`

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"3"` a potvrďte **Enterem**.
4. Zadejte `"4"` a potvrďte **Enterem**.
5. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje upozornění: `Seznam úkolů je prázdný.`
Konečným stavem před ukončením programu je prázdný seznam `ukoly = []`
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Program oznámí prázdný seznam a rovnou vrátí menu.

### TC16: Nula, záporné číslo a číslo nad rozsahem při odstraňování

**Typ testu:**

Negativní / hraniční

**Popis:**

Ověřit odmítnutí čísel -1, 0 a 3 pro dva uložené úkoly při odstraňování úkolů.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Před testem přidejte následující úkoly pomocí volby `1`. U každého zadejte název a popis; každý vstup potvrďte Enterem.

1. Název: `"Nakoupit potraviny"`; popis: `"Koupit pečivo, mléko a zeleninu."`.
2. Název: `"Uklidit"`; popis: `"Utřít prach, vyluxovat a vytřít."`.

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"3"` a potvrďte **Enterem**.
4. Zadejte `"-1"` a potvrďte **Enterem**.
5. Zadejte `"3"` a potvrďte **Enterem**.
6. Zadejte `"0"` a potvrďte **Enterem**.
7. Zadejte `"3"` a potvrďte **Enterem**.
8. Zadejte `"3"` a potvrďte **Enterem**.
9. Zadejte `"2"` a potvrďte **Enterem**.
10. Zadejte `"4"` a potvrďte **Enterem**.
11. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje upozornění / úkoly v následujícím pořadí:

1. `Úkol s tímto číslem neexistuje.`
2. `Úkol s tímto číslem neexistuje.`
3. `Úkol s tímto číslem neexistuje.`
4. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`
5. `2. Uklidit - Utřít prach, vyluxovat a vytřít.`

Konečným stavem před ukončením programu jsou záznamy `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`; `2. Uklidit - Utřít prach, vyluxovat a vytřít.` v seznamu úkolů.
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Brání nechtěnému použití záporných indexů Pythonu. Po chybě se opakuje volba 3 z menu.

### TC17: Text, desetinné číslo a prázdný vstup při odstraňování

**Typ testu:**

Negativní

**Popis:**

Ověřit bezpečné zpracování desetinných čísel, prázdných vstupů včetně mezer a nečíselných vstupů při odstraňování úkolů.

**Vstupní podmínky:**

- Program zobrazuje hlavní menu.
- Před testem přidejte následující úkoly pomocí volby `1`. U každého zadejte název a popis; každý vstup potvrďte Enterem.

1. Název: `"Nakoupit potraviny"`; popis: `"Koupit pečivo, mléko a zeleninu."`.

**Kroky testu:**

1. Spusťte `task_manager.py` a připravte výchozí stav uvedený výše.
2. Ověřte obsah hlavního menu s volbami 1. Přidat nový úkol, 2. Zobrazit všechny úkoly, 3. Odstranit úkol a 4. Konec programu.
3. Zadejte `"3"` a potvrďte **Enterem**.
4. Zadejte `"abc"` a potvrďte **Enterem**.
5. Zadejte `"3"` a potvrďte **Enterem**.
6. Zadejte `"1.5"` a potvrďte **Enterem**.
7. Zadejte `"3"` a potvrďte **Enterem**.
8. Nezadávejte žádný text a stiskněte pouze **Enter** (`""`).
9. Zadejte `"3"` a potvrďte **Enterem**.
10. Zadejte **3 mezery** a potvrďte **Enterem** (`"   "`).
11. Zadejte `"2"` a potvrďte **Enterem**.
12. Zadejte `"4"` a potvrďte **Enterem**.
13. Porovnejte výstupy a výsledný stav s očekáváním níže.

**Očekávaný výsledek:**

Výstup obsahuje upozornění / úkoly v následujícím pořadí:

1. `Neplatný vstup. Zadejte celé číslo úkolu.`
2. `Neplatný vstup. Zadejte celé číslo úkolu.`
3. `Neplatný vstup. Zadejte celé číslo úkolu.`
4. `Neplatný vstup. Zadejte celé číslo úkolu.`
5. `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`

Konečným stavem před ukončením programu je záznam `1. Nakoupit potraviny - Koupit pečivo, mléko a zeleninu.`
Po závěrečné volbě 4 se vypíše `Konec programu.` a program je ukončen.

**Skutečný výsledek:**

Shoduje se s očekávaným výsledkem.

**Stav:**

Pass

**Poznámky:**

Každý pokus končí upozorněním na neplatný vstup a návratem do menu, žádný úkol se nesmaže.
