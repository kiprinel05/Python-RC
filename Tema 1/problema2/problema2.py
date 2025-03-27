def xor_operation(dividend, divisor):
    result = list(dividend)
    for i in range(len(divisor)):
        result[i] = '0' if result[i] == divisor[i] else '1'
    return ''.join(result)


def divide_message(message, generator):
    remainder = message[:len(generator)]
    steps = []

    while len(remainder) >= len(generator):
        if remainder[0] == '1':
            remainder = xor_operation(remainder, generator)
        else:
            remainder = remainder[1:]

        steps.append(remainder)

        message = message[1:]
        if len(message) > 0:
            remainder += message[0]

    remainder = remainder.lstrip('0')
    return remainder, steps


def crc_algorithm(message, generator):
    if not (all(bit in '01' for bit in message) and all(bit in '01' for bit in generator)):
        raise ValueError("Mes si pol trebuie sa fie binare")

    generator = generator.lstrip('0')

    if len(generator) == 0:
        raise ValueError("Pol gen nu poate fi 0 sau gol")

    if len(message) < len(generator):
        raise ValueError("Mes trebuie sa fie > gen")

    message_extended = message + '0' * (len(generator) - 1)
    remainder, steps = divide_message(message_extended, generator)
    return message_extended, remainder, steps


def main():
    message = input("Mesaj binar: ")
    generator = input("Pol gen: ")

    try:
        message_extended, remainder, steps = crc_algorithm(message, generator)

        print(f"Mesaj extins: {message_extended}")
        print("Rez XOR:")
        for step in steps:
            print(step)

        transmitted_message = message + remainder
        print(f"Mes transmis: {transmitted_message}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
