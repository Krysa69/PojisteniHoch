from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
import os

app = Flask(__name__)
swagger = Swagger(app)

# ===== "Databáze" v paměti =====
pojistenci = [
    {"id": 1, "jmeno": "Jan", "prijmeni": "Novák", "email": "jan.novak@email.cz"},
    {"id": 2, "jmeno": "Petr", "prijmeni": "Svoboda", "email": "petr@email.cz"}
]

smlouvy = [
    {"id": 1, "cislo": "SML001", "typ": "Životní", "castka": 150000, "pojistenec_id": 1},
    {"id": 2, "cislo": "SML002", "typ": "Úrazová", "castka": 80000, "pojistenec_id": 2}
]

udalosti = [
    {"id": 1, "popis": "Autonehoda", "castka": 50000, "smlouva_id": 2, "status": "otevřená"}
]

# ===== POJIŠTĚNCI =====
@app.route('/pojistenci', methods=['GET'])
def get_pojistenci():
    """Vrátí seznam pojištěnců
    ---
    responses:
      200:
        description: Vrací seznam všech pojištěnců
    """
    return jsonify(pojistenci)

@app.route('/pojistenci', methods=['POST'])
def add_pojistenec():
    """Přidá nového pojištěnce
    ---
    parameters:
      - name: id
        in: formData
        type: integer
      - name: jmeno
        in: formData
        type: string
      - name: prijmeni
        in: formData
        type: string
      - name: email
        in: formData
        type: string
    responses:
      200:
        description: Pojištěnec přidán
    """
    data = request.form
    novy = {
        "id": int(data["id"]),
        "jmeno": data["jmeno"],
        "prijmeni": data["prijmeni"],
        "email": data.get("email", "")
    }
    pojistenci.append(novy)
    return jsonify({"message": "Pojištěnec přidán", "data": novy})

@app.route('/pojistenci/<int:id>', methods=['DELETE'])
def delete_pojistenec(id):
    """Smaže pojištěnce podle ID
    ---
    parameters:
      - name: id
        in: path
        type: integer
    responses:
      200:
        description: Pojištěnec smazán
    """
    global pojistenci
    pojistenci = [p for p in pojistenci if p["id"] != id]
    return jsonify({"message": f"Pojištěnec s ID {id} smazán"})

# ===== SMLOUVY =====
@app.route('/smlouvy', methods=['GET'])
def get_smlouvy():
    """Vrátí seznam smluv
    ---
    responses:
      200:
        description: Vrací seznam všech smluv
    """
    return jsonify(smlouvy)

@app.route('/smlouvy', methods=['POST'])
def add_smlouva():
    """Přidá novou pojistnou smlouvu
    ---
    parameters:
      - name: id
        in: formData
        type: integer
      - name: cislo
        in: formData
        type: string
      - name: typ
        in: formData
        type: string
      - name: castka
        in: formData
        type: number
      - name: pojistenec_id
        in: formData
        type: integer
    responses:
      200:
        description: Smlouva přidána
    """
    data = request.form
    nova = {
        "id": int(data["id"]),
        "cislo": data["cislo"],
        "typ": data["typ"],
        "castka": float(data["castka"]),
        "pojistenec_id": int(data["pojistenec_id"])
    }
    smlouvy.append(nova)
    return jsonify({"message": "Smlouva přidána", "data": nova})

# ===== POJISTNÉ UDÁLOSTI =====
@app.route('/udalosti', methods=['GET'])
def get_udalosti():
    """Vrátí všechny pojistné události
    ---
    responses:
      200:
        description: Vrací všechny pojistné události
    """
    return jsonify(udalosti)

@app.route('/udalosti', methods=['POST'])
def add_udalost():
    """Přidá novou pojistnou událost
    ---
    parameters:
      - name: id
        in: formData
        type: integer
      - name: popis
        in: formData
        type: string
      - name: castka
        in: formData
        type: number
      - name: smlouva_id
        in: formData
        type: integer
      - name: status
        in: formData
        type: string
    responses:
      200:
        description: Událost přidána
    """
    data = request.form
    nova = {
        "id": int(data["id"]),
        "popis": data["popis"],
        "castka": float(data["castka"]),
        "smlouva_id": int(data["smlouva_id"]),
        "status": data.get("status", "otevřená")
    }
    udalosti.append(nova)
    return jsonify({"message": "Událost přidána", "data": nova})

# ===== OPENAPI / SWAGGER ENDPOINT =====
@app.route('/api', methods=['GET'])
def api_docs():
    """
    Vrátí kompletní OpenAPI / Swagger dokumentaci
    ---
    responses:
      200:
        description: Vrací Swagger JSON pro celé API
    """
    from flasgger import utils
    swag = utils.get_specs(app)
    return jsonify(swag)

if __name__ == '__main__':
    app.run(debug=True)
