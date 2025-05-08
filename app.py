from flask import Flask, request, redirect, render_template

app = Flask(__name__)

studenti = [
    {"id": 1, "nome": "Anna"},
    {"id": 2, "nome": "Marco"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aggiungi", methods=["POST"])
def aggiungi():
    nome = request.form["nome"]
    nuovo = {
        "id": len(studenti) + 1,
        "nome": nome
    }
    studenti.append(nuovo)
    return redirect("/studenti") 

@app.route("/studenti")
def elenco_studenti():
    return render_template("elenco.html", studenti=studenti)

if __name__ == "__main__":
    app.run(debug=True)
