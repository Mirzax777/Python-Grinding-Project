def calculate_price(good_credit, base_price=1000000):
    if good_credit:
        price = base_price * 0.1
    else:
        price = base_price * 0.2
    return price


if __name__ == '__main__':
    good_credit = False
    final_price = calculate_price(good_credit)
    print('price:', final_price)
