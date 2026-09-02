alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def encrypt(original_text, shift_amount):
    ciphertext = ""
    for letter in original_text:
        if letter not in alphabet:
            print("Invalid input. Please enter letters only.")
            return
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        ciphertext += alphabet[shifted_position]
    print(f"Here is the encoded result {ciphertext}")


def decrypt(original_text, shift_amount):
    plaintext = ""
    for letter in original_text:
        if letter not in alphabet:
            print("Invalid input. Please enter letters only.")
            return
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        plaintext += alphabet[shifted_position]
    print(f"Here is the decoded result {plaintext}")


should_continue = True

while should_continue:

    direction = input(f"Type ENCODE to encrypt, type DECODE to decrypt:\n").lower()

    if direction not in ["encode", "decode"]:
        print("Invalid input! Please type ENCODE or DECODE.")
        continue

    text = input(f"Type your message: \n").lower()

    shift = int(input("Type the shift number: \n"))

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)

    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")
