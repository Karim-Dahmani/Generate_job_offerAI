# 📩 Auto-Candidature avec Lettre de Motivation Générée par IA

Ce projet permet de **générer automatiquement une lettre de motivation en français** grâce à Together AI et de l’envoyer directement par e-mail à un recruteur.

## ✨ Fonctionnalités
✅ Génération automatique de la **lettre de motivation** en français avec Together AI.  
✅ **Affichage de la lettre** pour validation et modification avant envoi.  
✅ **Envoi de la lettre uniquement dans l'email** (sans pièce jointe).  
✅ Possibilité d'extraire **les détails du poste depuis une URL** (LinkedIn, Indeed, etc.).  

---

## 🚀 Installation

### 1️⃣ **Cloner le projet**
```bash
git clone https://github.com/Karim-Dahmani/Generate_job_offerAI.git
cd Generate_job_offerAI
```

### 2️⃣ **Créer un environnement virtuel (optionnel mais recommandé)**
```bash
python -m venv venv
source venv/bin/activate  # Pour Mac/Linux
venv\Scripts\activate      # Pour Windows
```

### 3️⃣ **Installer les dépendances**
```bash
pip install -r requirements.txt
```

#### 📌 **Si `requirements.txt` n’existe pas, installez ces packages manuellement :**
```bash
pip install flask together requests beautifulsoup4 smtplib werkzeug
```

---

## 🔑 **Configuration**
Avant d’utiliser l’application, vous devez **ajouter vos identifiants** :

1. **Créer un compte Together AI** et récupérer votre clé API :  
   - 👉 [Inscription Together AI](https://together.ai/)
   - **Copiez votre clé API** et remplacez `"your_together_ai_api_key"` dans le fichier `app.py`.

2. **Configurer un email expéditeur Gmail** :
   - Activez les **mots de passe d'application** ici : [Google App Passwords](https://myaccount.google.com/apppasswords).
   - **Ajoutez votre email et mot de passe** dans `app.py` :
     ```python
     SENDER_EMAIL = "votre_email@gmail.com"
     SENDER_PASSWORD = "votre_mot_de_passe_app"
     ```

---

## 🏃 **Lancer l’Application**
Exécutez l’application Flask :
```bash
python app.py
```
Ouvrez votre navigateur et allez sur :
```
http://127.0.0.1:5000/
```

---

## 📌 **Utilisation**
1️⃣ **Remplissez les informations** :  
   - Nom de l’entreprise  
   - Email du recruteur  
   - Titre du poste  
   - Description du poste (ou lien de l’offre)

2️⃣ **Cliquez sur "Générer la lettre"**  
   - La lettre de motivation s'affiche pour validation.  

3️⃣ **Modifiez la lettre si nécessaire**, puis cliquez sur **"Envoyer la candidature"**.

4️⃣ 📩 **L’e-mail est envoyé avec la lettre de motivation dans le texte du mail**.

---

## 📂 **Structure du Projet**
```
auto-candidature/
│── templates/         # Dossiers des fichiers HTML (interface utilisateur)
│   ├── index.html     # Formulaire pour saisir les informations
│   ├── validate.html  # Page de validation de la lettre avant envoi
│── app.py             # Code principal de l'application
│── requirements.txt   # Liste des dépendances nécessaires
│── README.md          # Documentation du projet
```

---

## 🎯 **Améliorations Possibles**
✅ Ajouter un suivi des candidatures envoyées.  
✅ Intégrer un système de gestion des réponses des recruteurs.  
✅ Ajouter une interface plus intuitive avec Bootstrap.  

---

## 🤝 **Contributions**
Les contributions sont les bienvenues ! N’hésitez pas à **soumettre une Pull Request** ou à **ouvrir une issue** pour toute suggestion d’amélioration.

📬 **Contactez-moi** : [dahmanimohammedkarim@gmail.com]  
💼 **LinkedIn** : [Dahmani Mohammmed Karim](https://www.linkedin.com/in/mohammed-karim-dahmani-b532b41b2/)  

