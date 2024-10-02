def caesar_cipher(text, shift):
    """Encrypts or decrypts a message using the Caesar cipher.

    Args:
        text: The text to be encrypted or decrypted.
        shift: The number of positions to shift the characters.

    Returns:
        The encrypted or decrypted message.
    """

    result = ""
    for char in text:
        if char.isalpha():
            # Calculate the shifted character code
            shifted_char = ord(char) + shift

            # Adjust for wrapping around the alphabet
            if char.isupper():
                if shifted_char > ord('Z'):
                    shifted_char -= 26
                elif shifted_char < ord('A'):
                    shifted_char += 26
            elif char.islower():
                if shifted_char > ord('z'):
                    shifted_char -= 26
                elif shifted_char < ord('a'):
                    shifted_char += 26

            # Convert the shifted character code back to a character
            result += chr(shifted_char)
        else:
            result += char
    return result

def main():
    while True:
        mode = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
        if mode not in ('e', 'd'):
            print("Invalid mode. Please enter 'e' or 'd'.")
            continue

        text = input("Enter your message: ")
        shift = int(input("Enter the shift amount (1-25): "))

        if shift < 1 or shift > 25:
            print("Invalid shift amount. Please enter a number between 1 and 25.")
            continue

        result = caesar_cipher(text, shift)
        print("Result:", result)

        again = input("Do you want to try again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
