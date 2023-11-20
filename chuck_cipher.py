from chuckcipher_logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def cipher(text, shift, direction):
    processed_text = ""
    for letter in text:
        curr_pos = alphabet.index(letter)
        if direction == 'encode':
            cipher_pos = curr_pos + shift
        elif direction == 'decode':
            cipher_pos = curr_pos - shift
        processed_text += alphabet[cipher_pos]
    return processed_text

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

final_text = cipher(text=text, shift=shift, direction=direction)

print(f"The result from your request is {final_text}")