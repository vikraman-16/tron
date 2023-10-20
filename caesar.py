def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26 
            if char.islower():
                shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            result += shifted_char
        else:
            result += char
    
    return result


text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Original text: ", text)
print("Encrypted text: ", encrypted_text)

