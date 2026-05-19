#Classe : Le catalogue IKEA (le plan du meuble).
#Objet : Le meuble que tu as monté dans ton salon (l'instance réelle).
#Attribut : La couleur du meuble, sa taille (ce qu'il est/a).
#Méthode : Ouvrir le tiroir, étendre la table (ce qu'il fait).

# 1. LA CLASSE (Le plan dans le catalogue IKEA)
class TableIKEA:
    
    # LE CONSTRUCTEUR (Le moment où on déballe le carton et on monte le meuble)
    def __init__(self, couleur_choisie, longueur_cm):
        # 2. LES ATTRIBUTS (Ce que la table EST/A)
        self.couleur = couleur_choisie
        self.longueur = longueur_cm
        self.est_allongee = False  # Par défaut, elle est pliée
        self.tiroir_ouvert = False # Par défaut, le tiroir est fermé

    # 3. LES MÉTHODES (Ce que la table peut FAIRE)
    def ouvrir_tiroir(self):
        if not self.tiroir_ouvert:
            self.tiroir_ouvert = True
            print("Le tiroir est maintenant ouvert.")
        else:
            print("Le tiroir est déjà ouvert !")

    def rallonger(self, ajout_cm):
        self.longueur += ajout_cm
        self.est_allongee = True
        print(f"La table a été rallongée. Nouvelle taille : {self.longueur} cm.")

# --- UTILISATION ---

# 4. L'OBJET (L'instance réelle dans TON salon)
# Ici, on crée une table spécifique : blanche, de 120cm
ma_table_salon = TableIKEA(couleur_choisie="Blanc", longueur_cm=120)

# On utilise une MÉTHODE
ma_table_salon.ouvrir_tiroir()

# On consulte un ATTRIBUT
print(f"Ma table est de couleur : {ma_table_salon.couleur}")

# On utilise une autre MÉTHODE pour modifier un ATTRIBUT
ma_table_salon.rallonger(40)
