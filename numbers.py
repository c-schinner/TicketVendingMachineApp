def perfume_ticket():
    for n in range(1, 1000):
        yield f'P - {n}'


def medicine_ticket():
    for n in range(1, 1000):
        yield f'M - {n}'


def cosmetic_ticket():
    for n in range(1, 1000):
        yield f'C - {n}'


p = perfume_ticket()
m = medicine_ticket()
c = cosmetic_ticket()


def decorate_ticket(product):
    print("=" * 35)
    print("\n")
    print('Your ticket number is : ')

    if product == 'P':
        print(next(p))
    elif product == 'M':
        print(next(m))
    else:
        print(next(c))

    print('Please wait for your turn : ')
    print("\n")
    print("=" * 35)

