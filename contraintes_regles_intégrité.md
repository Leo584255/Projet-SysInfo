Entités (clés & unicité)

- CLIENT : PK = NumClient. Email unique. Nom, Prenom obligatoires (RG1 conserve l’historique des clients).

- VILLE : PK = NumVille. NomVille unique (RG3).

- HOTEL : PK = NumHotel. NumVille = FK vers VILLE et unique (1 hôtel par ville – RG2).

- CIRCUIT : PK = NumCircuit. (Catalogue, pas de dates).

- ETAPE_CIRCUIT : PK composée (NumCircuit, OrdreEtape). FKs : NumCircuit → CIRCUIT, NumVille → VILLE, NumHotel → HOTEL. NbNuits ≥ 1 (RG5). Au moins 2 étapes par circuit (RG6).

- ACCOMPAGNATEUR : PK = NumAccompagnateur.

- VOYAGE : PK = NumVoyage. FKs : NumCircuit, NumAccompagnateur, VilleDepart, VilleArrivee. Un seul accompagnateur par voyage (RG4).

- RESERVATION : PK = NumReservation. FKs : NumClient, NumVoyage. Règles statut/paiement issues RG10–RG14.

Relations (cardinalités & référentiel)

- VILLE—HOTEL : (1,1) côté HOTEL vers VILLE avec contrainte d’unicité HOTEL.NumVille (RG2).

- CIRCUIT—ETAPE_CIRCUIT : (1,N) avec N ≥ 2 (RG6).

- VOYAGE—CIRCUIT : (N,1). Dates et villes cohérentes avec les étapes : VilleDepart = ville de l’étape 1, VilleArrivee = ville de la dernière étape.

- VOYAGE—ACCOMPAGNATEUR : (N,1) mais exactement 1 par voyage (RG4).

- CLIENT—RESERVATION—VOYAGE : CLIENT (1,N) RESERVATION (N,1) VOYAGE.
