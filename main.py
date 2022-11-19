def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    for letter in plain_text:
        pos = alphabet.index(letter)
        new_letter = alphabet[pos + shift_amount]
        encrypted_text += new_letter
    print(f"Here's the encoded result: {encrypted_text}")


def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        pos = alphabet.index(letter)
        new_letter = alphabet[pos - shift_amount]
        decrypted_text += new_letter
    print(f"Here's the decoded result: {decrypted_text}")


# find different solution than doubling alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)
