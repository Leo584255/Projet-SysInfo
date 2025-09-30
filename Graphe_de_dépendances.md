CLIENT

- NumClient → Nom, Prenom, Email, Telephone, Adresse, DateInscription

- Email → NumClient

VILLE

- NumVille → NomVille, Pays

- NomVille → NumVille, Pays

HOTEL

- NumHotel → NomHotel, Adresse, NumVille, Categorie, TelephoneHotel

- NumVille → NumHotel

CIRCUIT

- NumCircuit → NomCircuit, Description, PrixIndicatif, DureeJours

ETAPE_CIRCUIT

- (NumCircuit, OrdreEtape) → NumVille, NumHotel, NbNuits, TransportType, TransportRef

- (cohérence) : NumHotel → NumVille (si tu souhaites le figurer)

ACCOMPAGNATEUR

- NumAccompagnateur → Nom, Prenom, Email

VOYAGE

- NumVoyage → NumCircuit, NumAccompagnateur, DateDepart, DateArrivee, VilleDepart, VilleArrivee, DateLimiteVersement2, DateLimiteConfirmation, CapacitePlaces, PrixParPlace

- (DateDepart, NumCircuit, VilleDepart) → NumVoyage

- (DateArrivee, NumCircuit, VilleArrivee) → NumVoyage

RESERVATION

- NumReservation → NumClient, NumVoyage, PlacesReservees, Statut, MontantAcompte, DateAcompte, MontantSolde, DateSolde, DateReservation, ModePaiement, ReferencePaiement

- (NumClient, NumVoyage) → NumReservation
