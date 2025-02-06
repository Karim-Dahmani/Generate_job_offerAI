import os
import re
import smtplib
import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from together import Together

app = Flask(__name__)

# ✅ Initialisation du client Together AI
client = Together(api_key="")

# ✅ Configuration email
SENDER_EMAIL = ""
SENDER_PASSWORD = ""

# ✅ Vérifier le format de l'email
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

# ✅ Extraire les détails de l'offre depuis une URL
def extract_job_details(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        job_title = soup.find("h1").text if soup.find("h1") else "Titre du poste non trouvé"
        job_description = soup.find("div", class_="job-description").text if soup.find("div", class_="job-description") else "Aucune description trouvée."

        return job_title, job_description.strip()
    except Exception as e:
        return "Erreur lors de la récupération des détails", str(e)

# ✅ Générer la lettre de motivation avec Together AI
def generate_cover_letter(company, job_title, job_description):
    try:
        prompt = f"""
        Rédige une lettre de motivation professionnelle en français pour une candidature au poste de {job_title} chez {company}. 
        La description du poste est la suivante :
        {job_description}
        
        La lettre doit être formelle, souligner les compétences pertinentes, exprimer la motivation du candidat et se terminer par un appel à l'action.
        """

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Erreur lors de la génération de la lettre : {e}"

# ✅ Envoyer l'email (lettre de motivation uniquement)
def send_cover_letter(to_email, company, job_title, cover_letter):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = to_email
    msg["Subject"] = f"Candidature pour {job_title} chez {company}"

    # ✅ Contenu de l'email : uniquement la lettre de motivation
    email_content = f"""

    {cover_letter}
    
    """

    msg.set_content(email_content)

    # ✅ Envoi de l'email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            return f"✅ Email envoyé avec succès à {to_email}"
    except smtplib.SMTPAuthenticationError:
        return "❌ Échec de l'authentification ! Vérifiez votre mot de passe d'application."
    except smtplib.SMTPConnectError:
        return "❌ Erreur de connexion ! Vérifiez votre connexion Internet."
    except Exception as e:
        return f"❌ Une erreur est survenue : {e}"

# ✅ Route principale (formulaire pour générer la lettre)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        company = request.form['company']
        to_email = request.form['to_email']
        job_title = request.form.get('job_title', '')
        job_description = request.form.get('job_description', '')

        job_url = request.form.get('job_url', '')
        if job_url:
            job_title, job_description = extract_job_details(job_url)

        if not is_valid_email(to_email):
            return "⚠️ Format d'email invalide. Veuillez réessayer."

        # ✅ Générer la lettre de motivation
        cover_letter = generate_cover_letter(company, job_title, job_description)

        return render_template('validate.html', company=company, job_title=job_title, cover_letter=cover_letter, to_email=to_email)

    return render_template('index.html')

# ✅ Route pour envoyer l'email après validation
@app.route('/send', methods=['POST'])
def send():
    to_email = request.form['to_email']
    company = request.form['company']
    job_title = request.form['job_title']
    cover_letter = request.form['cover_letter']

    response = send_cover_letter(to_email, company, job_title, cover_letter)
    return response

if __name__ == "__main__":
    app.run(debug=True)
