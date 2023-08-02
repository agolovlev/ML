def shift_letter(letter, shift):
    "Функция сдвигает символ letter на shift позиций"
    shifted = ((ord(letter) - 97) + shift) % 26 + 97
    return chr(shifted)

def caesar_cipher(string, shift):
    "Шифр цезаря"
    result = ''
    for i in string:
        if i.isalpha():
            result += shift_letter(i, shift)
        else:
            result += i
    return result



print(caesar_cipher('hello world!', 2))