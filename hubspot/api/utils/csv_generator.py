from random import randint
import csv

EMAILS = [
    'Olivia@gmail.com',
    'Emma@gmail.com',
    'Charlotte@gmail.com',
    'Oleksandra@gmail.com',
    'Amelia@gmail.com'
]

PHONE_NUMBERS = [
    '380964848321',
    '0964848321',
    '380961232121',
    '0961232121'
]


def generate_data():
    with open('clients_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "email", "phone_number"])
        for i in range(1000):
            client_id = i + 1
            request_data = [
                client_id,
                EMAILS[randint(0, len(EMAILS) - 1)],
                PHONE_NUMBERS[randint(0, len(PHONE_NUMBERS) - 1)]
            ]
            writer.writerow(request_data)


if __name__ == '__main__':
    generate_data()
