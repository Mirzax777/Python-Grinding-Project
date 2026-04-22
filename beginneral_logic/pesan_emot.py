def main():
    message = input("Masukkan Pesan Anda Disini : ")
    words = message.split(' ')
    emojis = {
        ":)" : "😊",
        ":(" : "😢"
    }

    output = ""

    for word in words:
        output += emojis.get(word, word) + " "

    print(output)


if __name__ == '__main__':
    main()
