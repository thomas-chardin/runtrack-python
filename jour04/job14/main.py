def get_length(chaine):
    length = 0

    while True:
        try:
            element = chaine[length]
            length += 1
        except IndexError:
            break

    return length
def my_long_word(chiffre, phrase):
    length = get_length(phrase)
    word = ''
    word_list = []
    i=0
    while i < length:
        if phrase[i] != ' ' and phrase[i] != ',':
            word += phrase[i]
        else:
            if word != '':
                word_list += [word]
                word = ''
        i += 1
    if word != 0:
        word_list += [word]
        word = ''
    i = 0
    length = get_length(word_list)
    phrase_return = ""
    while i < length:
        if get_length(word_list[i]) >= chiffre:
            phrase_return += word_list[i] + ' '   
        i += 1
    return phrase_return
        
            
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

print(my_long_word(3, phrase))