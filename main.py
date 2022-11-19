from art import logo


def caesar(user_text, shift_amount, cipher_direction):
    if cipher_direction == "decode":
        shift_amount *= -1
    caesar_text = ""
    for char in user_text:
        if char in alphabet:
            pos = alphabet.index(char)
            new_letter = alphabet[pos + shift_amount]
            caesar_text += new_letter
        else:
            caesar_text += char
    print(f"Here's the {cipher_direction}d result: {caesar_text}")


# find different solution than doubling alphabet to index out of range
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keep_going = True
while keep_going:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:  # 26 letters in alphabet
        shift %= 26  # shift = shift % 26
    caesar(text, shift, direction)
    want_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if want_continue == "no":
        keep_going = False
