from flask import Flask, render_template, request, redirect
from supabase import create_client, Client
from datetime import datetime

app = Flask(__name__)

# 🔹 Remplace par tes infos Supabase
SUPABASE_URL = "VOTRE_SUPABASE_URL"
SUPABASE_KEY = "VOTRE_SUPABASE_API_KEY"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/')
def index():
    livraisons = supabase.table('livraisons').select('*').execute()
    return render_template('index.html', livraisons=livraisons.data)

@app.route('/ajouter', methods=['POST'])
def ajouter():
    nom_client = request.form['nom_client']
    produit = request.form['produit']
    supabase.table('livraisons').insert({
        'nom_client': nom_client,
        'produit': produit,
        'date_livraison': str(datetime.utcnow()),
        'status': 'En attente'
    }).execute()
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
