def caesar(user_text, shift_amount, direction_arg):
    if direction_arg == "decode":
        shift_amount *= -1
    caesar_text = ""
    for letter in user_text:
        pos = alphabet.index(letter)
        new_letter = alphabet[pos + shift_amount]
        caesar_text += new_letter
    print(f"Here's the {direction_arg}d result: {caesar_text}")


# find different solution than doubling alphabet to index out of range
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(text, shift, direction)
