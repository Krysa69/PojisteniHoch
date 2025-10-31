# Pojištění API – Flask + Swagger

Tento projekt je jednoduché REST API pro správu pojištěnců, pojistných smluv a pojistných událostí.  
API je napsané v Pythonu s použitím **Flask** a **Flasgger**, takže podporuje automaticky generovanou **Swagger/OpenAPI dokumentaci**.

---

## 📦 Funkce API

### Pojištěnci
- `GET /pojistenci` – Vrátí seznam všech pojištěnců.
- `POST /pojistenci` – Přidá nového pojištěnce.
- `DELETE /pojistenci/<id>` – Smaže pojištěnce podle ID.

### Smlouvy
- `GET /smlouvy` – Vrátí seznam všech smluv.
- `POST /smlouvy` – Přidá novou pojistnou smlouvu.

### Pojistné události
- `GET /udalosti` – Vrátí seznam všech pojistných událostí.
- `POST /udalosti` – Přidá novou pojistnou událost.

### Dokumentace
- `GET /api` – Vrací kompletní **OpenAPI/Swagger JSON** dokumentaci.
- Swagger UI: `/apidocs/` – interaktivní testování API.
- Markdown dokumentace: `dokumentacePojisteni.md` (ve stejném adresáři jako `main.py`).

---

## ⚙️ Instalace

1. Klonuj projekt nebo stáhni soubory:
```bash
git clone <url-projektu>
cd <adresar-projektu>
