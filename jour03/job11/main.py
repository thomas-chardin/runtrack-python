def time_to_text(minutes):
    if type(minutes) == int :
        heures = minutes // 60
        minutes = minutes % 60
        print(f'{heures} heure(s) et {minutes} minutes')
    else :
        print("le type attendu est un nombre entier")
        
time_to_text(10)
time_to_text(100)
time_to_text(1000)