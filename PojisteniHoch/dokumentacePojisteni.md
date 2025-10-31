# Dokumentace – Evidence pojistek a pojistných událostí

## 1. Účel aplikace
Cílem aplikace je vytvořit **webový systém pro správu pojištěnců, pojistných smluv a pojistných událostí**, který nahradí zastaralé a neefektivní vedení dat v Excelu.  
Systém umožní **centralizovanou správu dat, bezpečné uložení informací, snadné dohledávání a přehledné zobrazení** všech údajů o smlouvách a pojistných událostech.

Aplikace má být určena **pro interní potřebu pojišťovny nebo makléřské společnosti**, která spravuje klienty, jejich pojistky a řeší likvidaci pojistných událostí.

### Hlavní přínosy:
- Nahradí evidenci v Excelu přehledným webovým rozhraním.  
- Zjednoduší správu pojistných smluv, jejich limitů a připojených dokumentů.  
- Umožní rychle evidovat a řešit pojistné události.  
- Zajistí bezpečnost a ochranu osobních údajů dle GDPR.  

---

## 2. Hlavní funkce systému

### 2.1 Evidence pojištěnců
- Přidání nového pojištěnce (jméno, příjmení, datum narození, kontakt, e-mail).  
- Úprava a smazání pojištěnce s potvrzením.  
- Zobrazení seznamu pojištěnců s možností vyhledávání podle jména nebo ID.  
- Každý pojištěnec může mít více pojistek.  

### 2.2 Evidence pojistných smluv
- Vytváření a správa pojistných smluv.  
- Evidované údaje:
  - číslo smlouvy,  
  - typ pojištění (line of business – např. životní, majetková, úrazová),  
  - limity pojištění,  
  - pojistná částka,  
  - status smlouvy (aktivní, neaktivní, vypovězená),  
  - informace o platbě (zda byla zaplacena),  
  - datum platnosti od / do,  
  - vazba na pojištěnce (klienta) a správce smlouvy (makléře).  
- Možnost nahrát připojené dokumenty (PDF, DOCX).  
- Import dat z Excel tabulek.  

### 2.3 Evidence pojistných událostí
- Záznam pojistné události vázané na konkrétní pojistnou smlouvu.  
- Evidované údaje:
  - datum a čas události,  
  - popis škody a místo události,  
  - svědci, odhad škody, výše peněžní rezervy, částka plnění,  
  - číslo pojišťovny,  
  - připojené soubory (3–4 fotografie, dokumentace v PDF nebo DOCX),  
  - status události (otevřená, vyřízená, zamítnutá, v řešení).  
- Vyřizovatel má možnost měnit stav pojistné události.  

### 2.4 Vyhledávání a filtrování
- Vyhledávání pojištěnců podle jména, příjmení nebo ID.  
- Filtrování pojistek podle typu, klienta, platnosti, limitu nebo stavu.  
- Vyhledávání pojistných událostí podle stavu, data, pojištěnce nebo čísla pojistky.  

### 2.5 Autentizace a přístupová práva
- Přihlášení pomocí uživatelského jména a hesla.  
- Autorizace na základě přiřazené role.  
- Každá role má jiné oprávnění přístupu a úprav dat.  
- Ochrana dat dle GDPR (např. šifrování databáze).  

---

## 3. Uživatelské role

### 3.1 Správce systému
- Plný přístup ke všem datům a funkcím.  
- Správa uživatelů, jejich rolí a oprávnění.  
- Správa záloh databáze a údržba systému.  
- Možnost mazání nebo úprav všech záznamů.  

### 3.2 Makléř (správce pojistných smluv)
- Uzavírá nové pojistné smlouvy a eviduje limity pojištění.  
- Má přístup k informacím o klientech a jejich pojistkách.  
- Může přidávat a upravovat smlouvy, ale ne události.  

### 3.3 Likvidátor (vyřizovatel pojistných událostí)
- Řeší pojistné události a mění jejich stav.  
- Má přístup pouze k údajům o událostech, ne k osobním údajům klientů.  
- Vkládá dokumenty a odhady škody.  

### 3.4 Klient (pojištěnec)
- Přístup pouze ke svým údajům, pojistkám a událostem.  
- Může nahlásit novou pojistnou událost a přiložit dokumenty.  
- Nemůže upravovat údaje o jiných klientech.  

---

## 4. Požadavky na aplikaci

### 4.1 Funkční požadavky
- CRUD operace (vytvoření, čtení, úprava, mazání) pro pojištěnce, smlouvy a události.  
- Možnost importu/exportu dat (např. Excel, CSV, PDF).  
- Přehledné filtrování a vyhledávání dat.  
- Autentizace a autorizace uživatelů.  
- Možnost nahrát připojené soubory (fotografie, dokumenty).  
- Logování změn (volitelné – kdo upravil, kdy).  
- Zobrazení přehledů a statistik (např. počet pojistek, stav událostí).  
- Nastavení limitu velikosti souborů.  
- Možnost měnit velikost písma v rozhraní.  

### 4.2 Nefunkční požadavky
- Databáze musí být **šifrovaná** kvůli ochraně osobních údajů (GDPR).  
- Citlivá data (pojistné události, částky) vidí jen oprávněné osoby.  
- Systém musí fungovat bez potřeby dark mode.  
- Přístup k aplikaci pouze přes zabezpečené připojení (HTTPS).  
- Možnost omezení přístupu pro externí klienty pomocí **NDA** (smluv o mlčenlivosti).  
- Odezva aplikace do 3 sekund.  

---

## 5. Data a jejich evidence

### Evidované entity:
1. **Pojištěnec (Klient)**  
   - Osobní údaje (jméno, příjmení, datum narození, kontakt).  
   - Vazba na pojistky.  

2. **Pojistná smlouva**  
   - Číslo smlouvy.  
   - Typ pojištění (line of business).  
   - Limity pojištění.  
   - Pojistná částka, status, platnost, platba.  
   - Vazba na pojištěnce a makléře.  

3. **Pojistná událost**  
   - Datum, čas, popis škody, místo.  
   - Svědci, čísla pojišťoven, připojené soubory.  
   - Odhad škody, částka plnění, peněžní rezerva.  
   - Status události.  

4. **Soubory**  
   - 3–4 fotografie k jedné události.  
   - 1–2 dokumenty (PDF, DOCX).  

---

## 6. Technické požadavky (návrh backendu)
- **Backend technologie:** Node.js (Express) nebo Python (Flask/Django).  
- **Databáze:** MSSQL.  
- **Architektura:** REST API s oddělenou frontend částí.  
- **Autentizace:** JWT nebo session-based login.  
- **Ukládání souborů:** Serverové úložiště nebo cloud.  
- **Import Excel souborů:** pomocí knihovny (např. XLSX).  


