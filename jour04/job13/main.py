def get_length(liste):
    length = 0

    while True:
        try:
            element = liste[length]
            length += 1
        except IndexError:
            break

    return length

def tri_a_bulle(liste,length):
    count = 0
    i = 1
    while i < length:
        if liste[i] < liste[i-1]:
            liste[i], liste[i-1] = liste[i-1], liste[i]
            count += 1
        i += 1
    if count > 0:
        return 1
    else:
        return 0
        
    
def tri(liste):
    length = get_length(liste)
    finish_count = 1
    while finish_count != 0 :
        finish_count -= 1
        finish_count += tri_a_bulle(liste, length) 
    return liste 

L = [10,20,30,20,10,50,60,40,80,50,40]
print(L)

def is_not_in(element, liste):
    i = 0
    length = get_length(liste)
    while i < length:
        if liste[i] == element:
            return False
        i += 1
    return True 

def remove(liste):
    length = get_length(liste)
    liste_no_dupes = []
    i = 0
    while i < length:
        if is_not_in(liste[i], liste_no_dupes) == True:
            liste_no_dupes += [liste[i]]
        i += 1
    return liste_no_dupes

L_normal = remove(L)
print(L_normal)
    
            