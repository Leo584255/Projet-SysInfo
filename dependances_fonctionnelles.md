CLIENT

PK : NumClient → {Nom, Prenom, Email, Telephone, Adresse, DateInscription}.

Candidat : Email → NumClient (unicité) ⇒ Email détermine le reste via NumClient.

VILLE

PK : NumVille → {NomVille, Pays}.

Candidat : NomVille → {NumVille, Pays} (unicité RG3).

HOTEL

PK : NumHotel → {NomHotel, Adresse, NumVille, Categorie, TelephoneHotel}.

Unicité RG2 : NumVille → NumHotel

CIRCUIT

PK : NumCircuit → {NomCircuit, Description, PrixIndicatif, DureeJours}.

ETAPE_CIRCUIT

PK composée : (NumCircuit, OrdreEtape) → {NumVille, NumHotel, NbNuits, TransportType, TransportRef}.

ACCOMPAGNATEUR

PK : NumAccompagnateur → {Nom, Prenom, Email}.

VOYAGE

PK : NumVoyage → {NumCircuit, NumAccompagnateur, DateDepart, DateArrivee, VilleDepart, VilleArrivee, DateLimiteVersement2, DateLimiteConfirmation, CapacitePlaces, PrixParPlace}.

RG8 (unicité locale) :

(DateDepart, NumCircuit, VilleDepart) → NumVoyage


RESERVATION

PK : NumReservation → {NumClient, NumVoyage, PlacesReservees, Statut, MontantAcompte, DateAcompte, MontantSolde, DateSolde, DateReservation, ModePaiement, ReferencePaiement}.
