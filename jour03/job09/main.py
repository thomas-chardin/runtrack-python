def moyenne(note1, note2, note3):
    return ((note1 + note2 + note3) / 3)

note1, note2, note3 = input("Veuillez mettre les trois notes séparés par espace: ").split()
note1 = int(note1)
note2 = int(note2)
note3 = int(note3)
print(note1,note2,note3)
moyenne_etudiant = moyenne(note1,note2, note3)
print(moyenne_etudiant)

if 15.0 <= moyenne_etudiant <= 20.0:
    print("Très bon élève")
elif 11.0 <= moyenne_etudiant <= 14.99:
    print("Bon élève")
elif 8.0 <= moyenne_etudiant <= 10.99:
    print("Élève moyen")
elif 0.0 <= moyenne_etudiant <= 7.99:
    print("Élève devant faire des efforts")
else:
    print("les arguments rentrer ne sont pas des chiffres entier")