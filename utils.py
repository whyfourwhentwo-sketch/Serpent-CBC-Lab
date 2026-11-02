def pad(data : bytes) -> bytes:
    """
    Дополнение plain текста одинаковыми битами до длины, кратной 16-ти
    """
    n = 16 - len(data) % 16
    return data + bytes([n]) * n

def unpad(data: bytes) -> bytes:
    """
    Удаление добавленных при шифровании битов
    """
    return data[:-data[-1]]

def line() -> None:
    print('-' * 80)