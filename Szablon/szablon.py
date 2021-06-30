from cowpy import cow


def generate_banner(msg, style):
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --nn')


def dots_style(msg):
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg


def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)


def my_style(msg):
    result = ""
    for c in range(len(msg)):
        if c % 2 == 1:
            msg[c].upper()
            result += msg[c].upper()
        else:
            result += msg[c].lower()
    return '!!! ' + result + ' !!!'


def cow_style(msg):
    msg = cow.milk_random_cow(msg)
    return msg


def main():
    styles = (dots_style, admire_style, cow_style, my_style)
    msg = 'happy coding'
    [generate_banner(msg, style) for style in styles]


if __name__ == '__main__':
    main()
