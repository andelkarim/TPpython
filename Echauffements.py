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



def power_2(limit):
    powers_list = [0]  # Commencer par 0

    power = 2  # Commencer avec la première puissance de 2 (2^1 = 2)

    while power <= limit:
        powers_list.append(power)
        power *= 2

    return powers_list

# Exemple d'appel à la fonction avec limit = 10
result = power_2(10)
print(result)



def check_ip_format(ip):
    sections = ip.split('.')

    if len(sections) != 4:
        return False  

    for section in sections:
        if not section.isdigit() or not 0 <= int(section) <= 255:
            return False  # Si la section n'est pas un entier valide entre 0 et 255, ce n'est pas une adresse IPv4

    return True 

# Exemples d'appels à la fonction
print(check_ip_format('10.0.0.0'))  # True
print(check_ip_format('192.12.'))  # False






