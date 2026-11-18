"""Doplňkové automatizované kontroly. Soubor test_cases.md se nemění."""
import contextlib
import copy
import io
from pathlib import Path
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import task_manager as tm

A = {"nazev": "Nakoupit potraviny", "popis": "Koupit pečivo, mléko a zeleninu."}
B = {"nazev": "Uklidit", "popis": "Utřít prach, vyluxovat a vytřít."}
C = {"nazev": "Vyprat prádlo", "popis": "Prát zvlášť černé, barevné a jemné prádlo."}
EMPTY = "Seznam úkolů je prázdný."
MENU = "Správce úkolů - Hlavní menu"
BAD_MENU = "Neplatná volba. Zadejte číslo od 1 do 4."
BAD_ADD = "Název ani popis nesmí být prázdný. Zadejte oba údaje znovu."
BAD_NUM = "Neplatný vstup. Zadejte celé číslo úkolu."
BAD_RANGE = "Úkol s tímto číslem neexistuje."
LINE_A = f"1. {A['nazev']} - {A['popis']}"
LINE_B = f"2. {B['nazev']} - {B['popis']}"
ADDED = f"Úkol '{A['nazev']}' byl přidán."
REMOVED = f"Úkol '{A['nazev']}' byl odstraněn."
cases = []


def case(group, name, kind, description, before, inputs, after, messages, menus, note):
    cases.append(dict(group=group, name=name, kind=kind, description=description,
                      before=before, inputs=inputs, after=after, messages=messages,
                      menus=menus, note=note))


# TC01: Volba "1" - přidání úkolu
case('hlavni_menu', 'Výběr přidání úkolu', 'Pozitivní', 'Ověřit, že volba 1 spustí přidání a vrátí uživatele do menu.', [], ['1', A['nazev'], A['popis'], '4'], [A], [ADDED], 2, 'Kontroluje propojení menu a funkce pridat_ukol.')
# TC02: Volba "2" - zobrazení úkolů
case('hlavni_menu', 'Výběr zobrazení úkolů', 'Pozitivní', 'Ověřit směrování volby 2 a následný návrat do menu.', [A], ['2', '4'], [A], [LINE_A], 2, 'Výpis nesmí změnit uložená data.')
# TC03: Volba "3" - odstranění úkolu
case('hlavni_menu', 'Výběr odstranění úkolu', 'Pozitivní', 'Ověřit směrování volby 3 a návrat do menu.', [A], ['3', '1', '4'], [], [LINE_A, REMOVED], 2, 'Seznam musí být vidět před zadáním čísla k odstranění.')
# TC04: Nečíselná volba v hlavním menu
case('hlavni_menu', 'Nečíselná volba a oprava', 'Negativní', 'Ověřit upozornění na text místo čísla a možnost nové volby.', [], ['abc', '4'], [], [BAD_MENU], 2, 'Chybná volba nesmí ukončit program.')
# TC05: Volby těsně mimo rozsah
case('hlavni_menu', 'Volby těsně mimo rozsah', 'Negativní / hraniční', 'Ověřit odmítnutí hodnot 0 a 5.', [], ['0', '5', '4'], [], [BAD_MENU, BAD_MENU], 3, 'Dolní a horní neplatná hranice nabídky 1–4.')
# TC06: Prázdná volba a mezery
case('hlavni_menu', 'Prázdná volba a mezery', 'Negativní', 'Ověřit prázdný vstup i vstup obsahující pouze mezery.', [], ['', '   ', '4'], [], [BAD_MENU, BAD_MENU], 3, 'Oba vstupy jsou neplatné, uživatel může pokračovat.')
# TC07: Ukončení programu volbou "4"
case('hlavni_menu', 'Ukončení volbou 4', 'Pozitivní', 'Ověřit ukončení programu bez další nabídky.', [], ['4'], [], ['Konec programu.'], 1, 'Horní platná hranice menu. Data se neukládají na disk.')
# TC08: Přidání úkolu č. 1
case('pridat_ukol', 'Přidání prvního úkolu', 'Pozitivní', 'Ověřit vytvoření prvního záznamu v prázdném seznamu.', [], ['1', A['nazev'], A['popis'], '2', '4'], [A], [ADDED, LINE_A], 3, 'První úkol má při zobrazení číslo 1.')
# TC09: Přidání dalšího úkolu k již existujícímu úkolu č. 1
case('pridat_ukol', 'Přidání dalšího úkolu', 'Pozitivní', 'Ověřit přidání na konec bez přepsání původního úkolu.', [A], ['1', B['nazev'], B['popis'], '2', '4'], [A, B], [f"Úkol '{B['nazev']}' byl přidán.", LINE_A, LINE_B], 3, 'Zachovává pořadí a oba popisy.')
# TC10: Prázdný název a nové zadání
case('pridat_ukol', 'Prázdný název a nové zadání', 'Negativní', 'Ověřit odmítnutí prázdného názvu a opakování názvu i popisu.', [], ['1', '', 'Tento popis neukládat.', A['nazev'], A['popis'], '2', '4'], [A], [BAD_ADD, ADDED, LINE_A], 3, 'Neplatný pokus nesmí vytvořit částečný úkol.')
# TC11: Prázdný popis a nové zadání
case('pridat_ukol', 'Prázdný popis a nové zadání', 'Negativní', 'Ověřit odmítnutí prázdného popisu a opakování obou údajů.', [], ['1', 'Tento název neukládat.', '', A['nazev'], A['popis'], '2', '4'], [A], [BAD_ADD, ADDED, LINE_A], 3, 'Nový název musí nahradit název z neplatného pokusu.')
# TC12: Zobrazení několika úkolů najednou
case('zobrazit_ukoly', 'Zobrazení několika úkolů', 'Pozitivní', 'Ověřit výpis všech názvů, popisů a správného pořadí.', [A, B, C], ['2', '4'], [A, B, C], [LINE_A, LINE_B, f"3. {C['nazev']} - {C['popis']}"], 2, 'Výpis musí obsahovat i poslední úkol a českou diakritiku.')
# TC13: Zobrazení prázdného seznamu
case('zobrazit_ukoly', 'Zobrazení prázdného seznamu', 'Hraniční', 'Ověřit srozumitelné oznámení místo chyby při absenci úkolů.', [], ['2', '4'], [], [EMPTY], 2, 'Funkce nemá vlastní vstup; chybné volby pokrývají testy menu. Prázdný seznam je podporovaný stav.')
# TC14: Odstranění prostředního úkolu
case('odstranit_ukol', 'Odstranění prostředního úkolu', 'Pozitivní', 'Ověřit odstranění pouze vybraného záznamu a přečíslování.', [A, B, C], ['3', '2', '2', '4'], [A, C], [LINE_A, LINE_B, f"Úkol '{B['nazev']}' byl odstraněn.", LINE_A, f"2. {C['nazev']} - {C['popis']}"], 3, 'Sousední úkoly musí zůstat zachovány.')
# TC15: Odstranění úkolu z prázdného seznamu
case('odstranit_ukol', 'Odstranění z prázdného seznamu', 'Negativní', 'Ověřit, že bez úkolů nelze zadávat číslo k odstranění.', [], ['3', '4'], [], [EMPTY], 2, 'Program oznámí prázdný seznam a rovnou vrátí menu.')
# TC16: Nula, záporné číslo a číslo nad rozsahem při odstraňování
case('odstranit_ukol', 'Nula, záporné číslo a číslo nad rozsahem', 'Negativní / hraniční', 'Ověřit odmítnutí čísel -1, 0 a 3 pro dva uložené úkoly.', [A, B], ['3', '-1', '3', '0', '3', '3', '2', '4'], [A, B], [BAD_RANGE, BAD_RANGE, BAD_RANGE, LINE_A, LINE_B], 5, 'Zamezuje nechtěnému použití záporných indexů Pythonu. Po chybě se opakuje volba 3 z menu.')
# TC17: Text, desetinné číslo a prázdný vstup při odstraňování
case('odstranit_ukol', 'Text, desetinné číslo a prázdný vstup', 'Negativní', 'Ověřit bezpečné zpracování necelých a nečíselných vstupů.', [A], ['3', 'abc', '3', '1.5', '3', '', '3', '   ', '2', '4'], [A], [BAD_NUM, BAD_NUM, BAD_NUM, BAD_NUM, LINE_A], 6, 'Každý pokus končí upozorněním a návratem do menu, žádný úkol se nesmaže.')



def verify(c):
    tm.ukoly[:] = copy.deepcopy(c['before'])
    output = io.StringIO()
    inputs = iter(c['inputs'])
    prompts = []

    def answer(prompt):
        prompts.append(prompt)
        return next(inputs)

    with patch('builtins.input', side_effect=answer), contextlib.redirect_stdout(output):
        tm.hlavni_menu()
    assert list(inputs) == [], 'Nevyužité vstupy'
    assert tm.ukoly == c['after'], 'Nesouhlasí konečný seznam'
    actual = output.getvalue()
    assert actual.count(MENU) == c['menus'], 'Nesouhlasí návraty do menu'
    assert actual.endswith('Konec programu.\n'), 'Chybí řádné ukončení'
    cursor = 0
    for message in c['messages']:
        pos = actual.find(message, cursor)
        assert pos >= 0, f'Chybí výstup: {message}'
        cursor = pos + len(message)
    if c['group'] == 'pridat_ukol':
        attempts = (len(c['inputs']) - (3 if '2' in c['inputs'][-2:-1] else 2)) // 2
        assert sum('Zadejte název' in p for p in prompts) == attempts
        assert sum('Zadejte popis' in p for p in prompts) == attempts
    if not c['before'] and c['inputs'][0] == '3':
        assert not any('který chcete odstranit' in p for p in prompts)
    return 'Pass'


if __name__ == "__main__":
    for number, scenario in enumerate(cases, start=1):
        verify(scenario)
        print(f"TC{number:02}: Pass")
    print(f"{len(cases)}/{len(cases)} automatizovaných kontrol: Pass.")
