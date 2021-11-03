alpha_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "GRONSFELD"


def encrypt(text, key):
    encrypted_text = ""
    for i, j in enumerate(text):
        encrypted_text += alpha_eng[(alpha_eng.index(j) + int(key[i % len(key)])) % len(alpha_eng)]
    return encrypted_text


def decrypt(text, key):
    decrypted_text = ""
    for i, j in enumerate(text):
        decrypted_text += alpha_eng[(alpha_eng.index(j) - int(key[i % len(key)])) % len(alpha_eng)]
    return decrypted_text


print(encrypt('GRONSFELD', '2015'))  # шифрование
print(decrypt('IRPSUFFQF', '2015'))  # расшифровывание
