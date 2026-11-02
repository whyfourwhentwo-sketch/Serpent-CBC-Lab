from pyserpent import Serpent
import utils


def encrypt_mode():
    utils.line()
    text = input("Текст для шифрования: ")
    utils.line()

    key = Serpent.generate_key()
    cipher = Serpent(key)

    data = utils.pad(text.encode("utf-8"))
    ciphertext = cipher.encrypt(data)

    print("Скопируй оба значения:")
    print(f"Ключ:      {key.hex()}")
    print(f"Шифртекст: {ciphertext.hex()}")
    utils.line()

def decrypt_mode():
    utils.line()
    key = bytes.fromhex(input("Ключ (hex): ").strip())
    ciphertext = bytes.fromhex(input("Шифртекст (hex): ").strip())
    utils.line()
    cipher = Serpent(key)
    data = utils.unpad(cipher.decrypt(ciphertext))

    print(f"Исходный текст: {data.decode('utf-8')}")
    utils.line()

def main():

    utils.line()
    mode = 'a'
    

    while True:
        mode = input("Режим (e - зашифровать, d - расшифровать): ").strip().lower()
        

        if mode == "e":
            encrypt_mode()
            break
        elif mode == "d":
            decrypt_mode()
            break
        else:
            print("Нужно ввести e или d")


if __name__ == "__main__":
    main()