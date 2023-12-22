class Bateau:
    def __init__(self, nom, vitesse):
        self.nom = nom
        self.vitesse = vitesse
        self.distance_parcourue = 0

    def avancer(self):
        self.distance_parcourue += self.vitesse / 4  # Avance par seconde

class Bateau2x(Bateau):
    pass

class BateauSkiff(Bateau):
    pass

class Bateau2_(Bateau):
    pass

class Course:
    def __init__(self, type_bateau):
        self.type_bateau = type_bateau
        self.bateaux = []
        self.course_en_cours = False

    def ajout_bateau_ligne_depart(self, bateau):
        if type(bateau).__name__ == self.type_bateau:
            self.bateaux.append(bateau)
        else:
            print("Le bateau n'a pas pu être ajouté")

    def depart(self):
        self.course_en_cours = True

    def en_cours(self):
        return self.course_en_cours and any(b.distance_parcourue < 2000 for b in self.bateaux)

    def next_loop(self):
        for bateau in self.bateaux:
            bateau.avancer()
            if bateau.distance_parcourue >= 2000:
                self.course_en_cours = False

    def affiche_positions(self):
        return '\n'.join(f"{b.nom},{b.distance_parcourue}" for b in self.bateaux)

    def vainqueur(self):
        return max(self.bateaux, key=lambda b: b.distance_parcourue).nom

# Exemple d'utilisation
course_cadets = Course('Bateau2x')
bateau_1_2x = Bateau2x('mickey', 62)
bateau_2_2x = Bateau2x('minnie', 70)
bateau_3_skiff = BateauSkiff('picsou', 120)
course_cadets.ajout_bateau_ligne_depart(bateau_1_2x)
course_cadets.ajout_bateau_ligne_depart(bateau_2_2x)
course_cadets.ajout_bateau_ligne_depart(bateau_3_skiff)
course_cadets.depart()

while course_cadets.en_cours():
    course_cadets.next_loop()

print(course_cadets.affiche_positions())
print(course_cadets.vainqueur())
