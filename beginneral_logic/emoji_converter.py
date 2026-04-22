def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😢"
    }

    output = ""

    for word in words:
        output += emojis.get(word, word) + " "

    return output


if __name__ == '__main__':
    message = input("Masukkan Pesan Anda Disini : ")
    result = emoji_converter(message)
    print(result)
