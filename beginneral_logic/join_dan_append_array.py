def enumerate_join(my_list):
    hasil = []
    i = 1
    for word in my_list:
        hasil.append(str(i))
        hasil.append(word)
        i = i + 1
    final = ' '.join(hasil)
    return final


if __name__ == '__main__':
    my_list = ['batu', 'gunting', 'kertas', 'pistol', 'bom']
    print(enumerate_join(my_list))
