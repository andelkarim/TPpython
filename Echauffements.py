def produce_default_dict():
    default_dict = {'root': 'password'}
    return default_dict

# Exemple d'appel à la fonction
if __name__ == "__main__":
    my_default_dict = produce_default_dict()
    print(my_default_dict)  #autres opérations avec le dictionnaire ici


def salutation(nom, age):
    if age == '1':
        age_txt = "1 an"
    else:
        age_txt = f"{age} ans"

    message = f"Bonjour '{nom}', vous avez actuellement {age_txt}."
    return message

# Exemple d'appel à la fonction
resultat_1 = salutation('gael', '24')
print(resultat_1)  # Affiche le message pour 'gael' et 24 ans

resultat_2 = salutation('bébé', '0')
print(resultat_2)  # Affiche le message pour 'bébé' et 0 an






