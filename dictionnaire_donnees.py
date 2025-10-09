import pandas as pd

# Création du dictionnaire de données enrichi (Étape 1, BRUT)
data = [
    # ===== CLIENT =====
    ["CLIENT", "NumClient", "INT", "-", "PK", "Identifiant unique du client"],
    ["CLIENT", "Nom", "VARCHAR", "50", "-", "Nom du client"],
    ["CLIENT", "Prenom", "VARCHAR", "50", "-", "Prénom du client"],
    ["CLIENT", "Email", "VARCHAR", "100", "Unique", "Adresse email du client"],
    ["CLIENT", "Telephone", "VARCHAR", "15", "-", "Numéro de téléphone"],
    ["CLIENT", "Adresse", "VARCHAR", "150", "-", "Adresse postale du client"],
    ["CLIENT", "DateNaissance", "DATE", "-", "-", "Date de naissance du client"],
    ["CLIENT", "DateInscription", "DATE", "-", "-", "Date d’inscription du client"],

    # ===== VILLE =====
    ["VILLE", "NumVille", "INT", "-", "PK", "Identifiant unique de la ville"],
    ["VILLE", "NomVille", "VARCHAR", "80", "Unique", "Nom distinct de la ville (RG3)"],
    ["VILLE", "Pays", "VARCHAR", "50", "-", "Pays de la ville"],

    # ===== HOTEL =====
    ["HOTEL", "NumHotel", "INT", "-", "PK", "Identifiant unique de l’hôtel"],
    ["HOTEL", "NomHotel", "VARCHAR", "80", "-", "Nom de l’hôtel"],
    ["HOTEL", "Adresse", "VARCHAR", "120", "-", "Adresse de l’hôtel"],
    ["HOTEL", "NumVille", "INT", "-", "FK", "Hôtel lié à une ville (RG2)"],
    ["HOTEL", "Categorie", "VARCHAR", "20", "-", "Classement de l’hôtel (étoiles)"],
    ["HOTEL", "TelephoneHotel", "VARCHAR", "15", "-", "Numéro de téléphone de l’hôtel"],
    ["HOTEL", "EmailHotel", "VARCHAR", "100", "-", "Email de l’hôtel"],

    # ===== CIRCUIT =====
    ["CIRCUIT", "NumCircuit", "INT", "-", "PK", "Identifiant unique du circuit"],
    ["CIRCUIT", "NomCircuit", "VARCHAR", "80", "-", "Nom du circuit"],
    ["CIRCUIT", "Description", "VARCHAR", "255", "-", "Description du circuit"],
    ["CIRCUIT", "PrixIndicatif", "DECIMAL(8,2)", "-", "-", "Prix indicatif du circuit"],
    ["CIRCUIT", "DureeJours", "INT", "-", "-", "Durée totale en jours"],
    ["CIRCUIT", "Transport", "VARCHAR", "50", "-", "Mode/référence de transport (ex : vol AF415, car)"],

    # ===== ACCOMPAGNATEUR =====
    ["ACCOMPAGNATEUR", "NumAccompagnateur", "INT", "-", "PK", "Identifiant unique de l’accompagnateur"],
    ["ACCOMPAGNATEUR", "Nom", "VARCHAR", "50", "-", "Nom de l’accompagnateur"],
    ["ACCOMPAGNATEUR", "Prenom", "VARCHAR", "50", "-", "Prénom de l’accompagnateur"],
    ["ACCOMPAGNATEUR", "Email", "VARCHAR", "100", "-", "Email de l’accompagnateur"],

    # ===== VOYAGE =====
    ["VOYAGE", "NumVoyage", "INT", "-", "PK", "Identifiant unique du voyage"],
    ["VOYAGE", "NumCircuit", "INT", "-", "FK", "Voyage lié à un circuit"],
    ["VOYAGE", "NumAccompagnateur", "INT", "-", "FK", "Accompagnateur du voyage (RG4)"],
    ["VOYAGE", "DateDepart", "DATE", "-", "-", "Date de départ du voyage"],
    ["VOYAGE", "DateArrivee", "DATE", "-", "-", "Date d’arrivée du voyage"],
    ["VOYAGE", "VilleDepart", "INT", "-", "FK", "Ville de départ du voyage"],
    ["VOYAGE", "VilleArrivee", "INT", "-", "FK", "Ville d’arrivée du voyage"],
    ["VOYAGE", "PrixParPlace", "DECIMAL(8,2)", "-", "-", "Prix par place pour ce voyage"],
    ["VOYAGE", "CapacitePlaces", "INT", "-", "-", "Nombre total de places disponibles"],

    # ===== RESERVATION =====
    ["RESERVATION", "NumReservation", "INT", "-", "PK", "Identifiant unique de la réservation"],
    ["RESERVATION", "NumClient", "INT", "-", "FK", "Client ayant réservé"],
    ["RESERVATION", "NumVoyage", "INT", "-", "FK", "Voyage réservé"],
    ["RESERVATION", "PlacesReservees", "INT", "-", "-", "Nombre de places réservées"],
    ["RESERVATION", "Statut", "VARCHAR", "20", "-", "EnAttente / Definitive / Annulee"],
    ["RESERVATION", "MontantAcompte", "DECIMAL(8,2)", "-", "-", "Montant du premier versement (RG11)"],
    ["RESERVATION", "DateAcompte", "DATE", "-", "-", "Date du premier versement"],
    ["RESERVATION", "MontantSolde", "DECIMAL(8,2)", "-", "-", "Montant du solde (RG12)"],
    ["RESERVATION", "DateSolde", "DATE", "-", "-", "Date du paiement du solde"],
    ["RESERVATION", "DateReservation", "DATE", "-", "-", "Date de la réservation"],
    ["RESERVATION", "ModePaiement", "VARCHAR", "20", "-", "Moyen de paiement utilisé"],
    ["RESERVATION", "ReferencePaiement", "VARCHAR", "50", "-", "Référence de la transaction bancaire"],
]

# Création du DataFrame
df = pd.DataFrame(data, columns=["Entité", "Attribut", "Type", "Longueur", "Clé", "Description"])

# Sauvegarde en Excel
file_path = "C:/Users/idris/Dictionnaire_donnees_Complet.xlsx"
df.to_excel(file_path, index=False)

print(f" Fichier généré : {file_path}")

