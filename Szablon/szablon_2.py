def generate_banner(msg, style):
    print('-- start --')
    print(style(msg))
    print('-- end --')


def open_gate(msg):
    msg = 'opening the gate'
    return msg


def close_gate(msg):
    msg = 'closing the gate'
    return msg


def open_garage(msg):
    msg = 'opening the garage'
    return msg


def close_garage(msg):
    msg = 'closing the garage'
    return msg


def turn_on_aircondition(msg):
    msg = 'turning on the air condition'
    return msg


def turn_off_aircondition(msg):
    msg = 'turning off the air condition'
    return msg


def main():
    msg = 'wiadomość'
    czynnosc = input("Co chcesz zrobić? [OB]-otworzyć brame / [ZB]-zamknąć bramę / [OG] -otworzyć garaz / "
                     "[ZG]-zamknac garaz / [WK] - wlaczyc klimatyzacje / [ZK] - zatrzymac klimatyzacje")
    if czynnosc == 'OB':
        style = open_gate
    elif czynnosc == 'ZB':
        style = close_gate
    elif czynnosc == 'OG':
        style = open_garage
    elif czynnosc == 'ZG':
        style = close_garage
    elif czynnosc == 'WK':
        style = turn_on_aircondition
    elif czynnosc == 'ZK':
        style = turn_off_aircondition
    else:
        print("Blad")

    generate_banner(msg, style)


if __name__ == '__main__':
    main()
