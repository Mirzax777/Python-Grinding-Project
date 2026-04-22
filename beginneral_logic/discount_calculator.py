def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return f'The price should be a number'

    if not isinstance(discount, (int, float)):
        return f'The discount should be a number'

    if price <= 0:
        return f'The price should be greater than 0'

    if discount < 0 or discount > 100:
        return f'The discount should be between 0 and 100'

    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price


if __name__ == '__main__':
    print(apply_discount(100, 20))
    print(apply_discount(200, 50))
    print(apply_discount(50, 0))
    print(apply_discount(10, 100))
