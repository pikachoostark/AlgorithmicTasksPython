alpha_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alpha_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(text, alphabet=alpha_rus):
    encrypted_text = ""
    for letter in text.upper():
        if letter in alphabet:
            encrypted_text += alphabet[(alphabet.find(letter)+3) % (len(alphabet))]
        else:
            encrypted_text += letter
    return encrypted_text


def decrypt(text, alphabet=alpha_rus):
    decrypted_text = ""
    for letter in text.upper():
        if letter in alphabet:
            decrypted_text += alphabet[(alphabet.find(letter)-3) % (len(alphabet))]
        else:
            decrypted_text += letter
    return decrypted_text


test_text = "Съешь же ещё этих мягких французских булок, да выпей чаю."
print(encrypt(test_text))
print(decrypt(encrypt(test_text)))

cipher = "IOVNKXIGKYGX"
print(decrypt(decrypt(cipher, alpha_eng), alpha_eng))
