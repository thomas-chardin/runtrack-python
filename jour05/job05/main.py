def chiffrement_cesar(message, chiffrement):
    messages = ""
    for n in message:
        if n.isalpha():
            if n.islower():
                messages += chr((ord(n) - ord('a') + chiffrement) % 26 + ord('a'))
            else:
                messages += chr((ord(n) - ord('A') + chiffrement) % 26 + ord('A'))
        else:
            messages += n
    return messages

# Exemple d'utilisation
message_original = "Je veux faire de la cyber..."
chiffrement = 3
messages = chiffrement_cesar(message_original, chiffrement)
print("Original:", message_original)
print("Chiffré:", messages)